"""
Converte transcrições exportadas do Microsoft Teams para o formato do projeto.

Uso:
    python tools/converter_teams_transcript.py <arquivo_teams> [--tema TEMA] [--data AAAA-MM-DD]

Exemplos:
    python tools/converter_teams_transcript.py reuniao.vtt --tema "juiz-cacimbinhas"
    python tools/converter_teams_transcript.py transcript.docx --tema "professor-iso9001"

Formatos de entrada suportados:
    .vtt  — WebVTT (Teams exporta neste formato via "Download transcript")
    .docx — Word (Teams exporta via "Open in Word" depois de baixar)

Saída:
    references/reunioes/AAAA-MM-DD_reuniao_<tema>.md  com Template A de metadados

Como exportar do Teams:
    1. Após a reunião, abra o chat da reunião no Teams
    2. Clique nos três pontos "..." ao lado da gravação/transcrição
    3. Selecione "Baixar" ou "Download transcript"
    4. Salve o arquivo .vtt ou .docx
    5. Execute este script

Dependências (instalar via pip):
    pip install python-docx  (necessário apenas para arquivos .docx)
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path


# ── Mapeamento de nomes para funções (anonimização) ──────────────────────────
# Adicione aqui os nomes reais que devem ser substituídos.
# Este mapa é mantido fora do Git — edite localmente conforme necessário.
# Formato: "Nome Real": "Função no SGQ"
MAPA_ANONIMIZACAO: dict[str, str] = {
    # Exemplos (substitua pelos nomes reais da vara):
    # "João da Silva":   "Juiz Titular",
    # "Maria Oliveira":  "Servidora A",
    # "Carlos Souza":    "Estagiário B",
}


def _anonimizar(texto: str) -> str:
    """Substitui nomes reais por funções conforme MAPA_ANONIMIZACAO."""
    for nome, funcao in MAPA_ANONIMIZACAO.items():
        texto = texto.replace(nome, funcao)
    return texto


def _parse_vtt(conteudo: str) -> list[dict]:
    """Parseia arquivo WebVTT do Teams. Retorna lista de {speaker, text}."""
    linhas = conteudo.splitlines()
    segmentos = []
    speaker_atual = ""
    texto_atual = []

    for linha in linhas:
        linha = linha.strip()
        # Linha de tempo: 00:01:23.456 --> 00:01:25.789
        if "-->" in linha:
            continue
        # Linha com falante: "Nome: " ou "<v Nome>"
        match_v = re.match(r"<v\s+(.+?)>(.+)", linha)
        match_colon = re.match(r"^(.+?):\s+(.+)", linha)

        if match_v:
            speaker_atual = match_v.group(1).strip()
            texto_atual.append(match_v.group(2).strip())
        elif match_colon and not re.match(r"^\d", linha):
            speaker_atual = match_colon.group(1).strip()
            texto_atual.append(match_colon.group(2).strip())
        elif linha and linha not in ("WEBVTT", "NOTE"):
            # Remove tags de formatação VTT
            linha_limpa = re.sub(r"<[^>]+>", "", linha)
            if linha_limpa:
                texto_atual.append(linha_limpa)
        elif not linha and texto_atual:
            # Linha em branco = fim do segmento
            texto = " ".join(texto_atual).strip()
            if texto:
                segmentos.append({"speaker": speaker_atual, "text": texto})
            texto_atual = []

    if texto_atual:
        texto = " ".join(texto_atual).strip()
        if texto:
            segmentos.append({"speaker": speaker_atual, "text": texto})

    return segmentos


def _parse_docx(caminho: Path) -> list[dict]:
    """Parseia arquivo .docx de transcrição do Teams."""
    try:
        from docx import Document
    except ImportError:
        print(
            "Erro: python-docx não instalado.\n"
            "Execute: pip install python-docx",
            file=sys.stderr,
        )
        sys.exit(1)

    doc = Document(str(caminho))
    segmentos = []
    speaker_atual = ""

    for para in doc.paragraphs:
        texto = para.text.strip()
        if not texto:
            continue
        # Teams docx geralmente tem padrão "Nome\nTexto falado"
        match = re.match(r"^(.+?)\s{2,}(.+)", texto)
        if match:
            speaker_atual = match.group(1).strip()
            segmentos.append({"speaker": speaker_atual, "text": match.group(2).strip()})
        else:
            segmentos.append({"speaker": speaker_atual, "text": texto})

    return segmentos


def _segmentos_para_markdown(segmentos: list[dict]) -> str:
    """Converte segmentos em Markdown legível, agrupando falas consecutivas do mesmo speaker."""
    linhas = []
    speaker_anterior = None

    for seg in segmentos:
        speaker = _anonimizar(seg["speaker"])
        texto = _anonimizar(seg["text"])

        if speaker != speaker_anterior:
            if linhas:
                linhas.append("")
            linhas.append(f"**{speaker or 'Participante'}:** {texto}")
            speaker_anterior = speaker
        else:
            linhas.append(texto)

    return "\n".join(linhas)


def converter(caminho_entrada: Path, tema: str, data_str: str) -> Path:
    """Converte arquivo Teams para referência Markdown do projeto."""
    ext = caminho_entrada.suffix.lower()

    if ext == ".vtt":
        conteudo = caminho_entrada.read_text(encoding="utf-8", errors="replace")
        segmentos = _parse_vtt(conteudo)
    elif ext in (".docx", ".doc"):
        segmentos = _parse_docx(caminho_entrada)
    else:
        raise ValueError(f"Formato '{ext}' não suportado. Use .vtt ou .docx")

    if not segmentos:
        raise RuntimeError("Nenhum conteúdo de fala encontrado no arquivo.")

    texto_md = _segmentos_para_markdown(segmentos)

    repo_root = Path(__file__).parent.parent
    destino_dir = repo_root / "references" / "reunioes"
    destino_dir.mkdir(parents=True, exist_ok=True)

    nome_arquivo = f"{data_str}_reuniao_{tema}.md"
    destino = destino_dir / nome_arquivo

    conteudo_final = f"""# Reunião: {tema.replace("-", " ").title()}

**Tipo:** reuniao
**Data:** {data_str}
**Fonte original:** Transcrição Microsoft Teams — {caminho_entrada.name}
**Anonimizado:** {'Sim (parcial — revisar)' if MAPA_ANONIMIZACAO else 'Não (MAPA_ANONIMIZACAO vazio — revisar antes de usar)'}
**Processado para knowledge_base:** Não

---

## Transcrição

{texto_md}

---

*Transcrição exportada do Microsoft Teams e convertida pelo tools/converter_teams_transcript.py.*
*Revise o conteúdo, anonimize nomes sensíveis e aprove antes de usar na knowledge_base.*
*Para adicionar mapeamentos de anonimização, edite MAPA_ANONIMIZACAO no topo do script.*
"""

    destino.write_text(conteudo_final, encoding="utf-8")
    return destino


def main():
    parser = argparse.ArgumentParser(
        description="Converte transcrição do Microsoft Teams para Markdown do projeto SGQ."
    )
    parser.add_argument("arquivo", type=Path, help="Arquivo .vtt ou .docx exportado do Teams")
    parser.add_argument(
        "--tema",
        default="reuniao",
        help="Slug do tema (ex: juiz-cacimbinhas, professor-iso9001). Padrão: reuniao",
    )
    parser.add_argument(
        "--data",
        default=date.today().isoformat(),
        help="Data no formato AAAA-MM-DD. Padrão: hoje",
    )
    args = parser.parse_args()

    if not args.arquivo.exists():
        print(f"Erro: arquivo não encontrado: {args.arquivo}", file=sys.stderr)
        sys.exit(1)

    destino = converter(args.arquivo, args.tema, args.data)
    print(f"✓ Transcrição convertida: {destino}")

    if not MAPA_ANONIMIZACAO:
        print(
            "\n⚠  MAPA_ANONIMIZACAO está vazio — nenhuma anonimização foi aplicada.\n"
            "  Edite MAPA_ANONIMIZACAO no topo de tools/converter_teams_transcript.py\n"
            "  com os nomes reais antes de usar o arquivo na knowledge_base."
        )
    print(f"\n  Próximo passo: revise {destino} e execute o workflow de ingestão.")


if __name__ == "__main__":
    main()
