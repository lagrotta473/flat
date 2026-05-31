"""
Busca semântica na knowledge_base usando Gemini Embeddings + ChromaDB.

Uso:
    python tools/buscar_na_base.py "controle de saídas não conformes"
    python tools/buscar_na_base.py "como tratar erros recorrentes" --clausula 10
    python tools/buscar_na_base.py --reindexar   (rebuilda o índice)

Pré-requisitos:
    1. GEMINI_API_KEY configurado no .env (aistudio.google.com → gratuito)
    2. KB com 20+ documentos para justificar busca semântica
    3. pip install google-generativeai chromadb python-dotenv

Ativar quando: knowledge_base tiver 20+ documentos consolidados.
Referência: https://ai.google.dev/gemini-api/docs/embeddings
"""

import argparse
import json
import os
import sys
from pathlib import Path


MODELO_EMBEDDING = "models/text-embedding-004"
CHROMA_COLLECTION = "sgq_knowledge_base"


def _carregar_env():
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(env_path)
        except ImportError:
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, _, val = line.partition("=")
                        os.environ.setdefault(key.strip(), val.strip())


def _verificar_dependencias():
    faltando = []
    try:
        import google.generativeai
    except ImportError:
        faltando.append("google-generativeai")
    try:
        import chromadb
    except ImportError:
        faltando.append("chromadb")
    if faltando:
        print(
            f"Erro: dependências não instaladas: {', '.join(faltando)}\n"
            f"Execute: pip install {' '.join(faltando)}",
            file=sys.stderr,
        )
        sys.exit(1)


def _gerar_embedding(texto: str) -> list[float]:
    """Gera embedding via Gemini text-embedding-004."""
    import google.generativeai as genai

    resultado = genai.embed_content(
        model=MODELO_EMBEDDING,
        content=texto,
        task_type="retrieval_document",
    )
    return resultado["embedding"]


def _gerar_embedding_query(texto: str) -> list[float]:
    """Gera embedding de consulta (task_type diferente para melhor retrieval)."""
    import google.generativeai as genai

    resultado = genai.embed_content(
        model=MODELO_EMBEDDING,
        content=texto,
        task_type="retrieval_query",
    )
    return resultado["embedding"]


def _obter_client_chroma():
    import chromadb

    chroma_path = os.environ.get("CHROMA_DB_PATH", "./data/chroma")
    Path(chroma_path).mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=chroma_path)


def _listar_documentos_kb(clausula: int | None = None) -> list[Path]:
    """Lista todos os .md consolidados da knowledge_base."""
    repo_root = Path(__file__).parent.parent
    kb_root = repo_root / "knowledge_base"

    padrão = f"clausula_{clausula}_*/**/*.md" if clausula else "**/*.md"
    docs = [
        p for p in kb_root.glob(padrão)
        if p.name != ".gitkeep" and "_modelos" not in str(p)
    ]
    return sorted(docs)


def reindexar(clausula: int | None = None):
    """Indexa (ou re-indexa) os documentos da KB no ChromaDB."""
    import google.generativeai as genai

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Erro: GEMINI_API_KEY não configurado no .env", file=sys.stderr)
        sys.exit(1)

    genai.configure(api_key=api_key)
    client = _obter_client_chroma()

    # Recria a collection para re-indexação limpa
    try:
        client.delete_collection(CHROMA_COLLECTION)
    except Exception:
        pass
    collection = client.create_collection(CHROMA_COLLECTION)

    docs = _listar_documentos_kb(clausula)
    if not docs:
        print("Nenhum documento encontrado na knowledge_base.")
        return

    print(f"Indexando {len(docs)} documentos...")
    for i, doc_path in enumerate(docs, 1):
        texto = doc_path.read_text(encoding="utf-8")
        if len(texto.strip()) < 50:
            continue  # Pula arquivos quase vazios

        # Metadados para filtros futuros
        partes = doc_path.parts
        clausula_num = next(
            (p.split("_")[1] for p in partes if p.startswith("clausula_")),
            "transversal",
        )
        metadados = {
            "clausula": clausula_num,
            "arquivo": str(doc_path.relative_to(Path(__file__).parent.parent)),
            "tipo": "overview" if doc_path.name == "_overview.md" else "aprendizado",
        }

        embedding = _gerar_embedding(texto[:8000])  # Limite de tokens do modelo
        collection.add(
            ids=[str(doc_path)],
            embeddings=[embedding],
            documents=[texto[:2000]],  # Preview para exibição
            metadatas=[metadados],
        )
        print(f"  [{i}/{len(docs)}] {doc_path.name}")

    print(f"\n✓ Índice criado com {collection.count()} documentos.")


def buscar(query: str, n_resultados: int = 3, clausula: int | None = None):
    """Busca documentos relevantes para a query."""
    import google.generativeai as genai

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Erro: GEMINI_API_KEY não configurado no .env", file=sys.stderr)
        sys.exit(1)

    genai.configure(api_key=api_key)
    client = _obter_client_chroma()

    try:
        collection = client.get_collection(CHROMA_COLLECTION)
    except Exception:
        print(
            "Índice não encontrado. Execute primeiro:\n"
            "  python tools/buscar_na_base.py --reindexar",
            file=sys.stderr,
        )
        sys.exit(1)

    where = {"clausula": str(clausula)} if clausula else None
    embedding_query = _gerar_embedding_query(query)

    resultados = collection.query(
        query_embeddings=[embedding_query],
        n_results=min(n_resultados, collection.count()),
        where=where,
        include=["documents", "metadatas", "distances"],
    )

    print(f'\nResultados para: "{query}"\n{"─" * 50}')
    for i, (doc, meta, dist) in enumerate(
        zip(
            resultados["documents"][0],
            resultados["metadatas"][0],
            resultados["distances"][0],
        ),
        1,
    ):
        relevancia = round((1 - dist) * 100, 1)
        print(f"\n[{i}] {meta['arquivo']}  (relevância: {relevancia}%)")
        print(f"    Cláusula: {meta['clausula']} · Tipo: {meta['tipo']}")
        print(f"    Preview: {doc[:200].strip()}...")

    return resultados


def main():
    parser = argparse.ArgumentParser(
        description="Busca semântica na knowledge_base usando Gemini Embeddings."
    )
    parser.add_argument("query", nargs="?", help="Texto da busca")
    parser.add_argument(
        "--reindexar",
        action="store_true",
        help="Re-indexa todos os documentos da KB (necessário após adicionar novos docs)",
    )
    parser.add_argument(
        "--clausula",
        type=int,
        default=None,
        help="Filtrar por número de cláusula ISO (ex: --clausula 8)",
    )
    parser.add_argument(
        "--resultados",
        type=int,
        default=3,
        help="Número de resultados a retornar (padrão: 3)",
    )
    args = parser.parse_args()

    _carregar_env()
    _verificar_dependencias()

    if args.reindexar:
        reindexar(args.clausula)
    elif args.query:
        buscar(args.query, args.resultados, args.clausula)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
