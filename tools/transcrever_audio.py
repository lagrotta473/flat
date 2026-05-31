"""
Transcreve um arquivo de áudio usando Google Cloud Speech-to-Text (pt-BR).

Uso:
    python tools/transcrever_audio.py <caminho_do_audio> [--tema TEMA] [--data AAAA-MM-DD]

Exemplos:
    python tools/transcrever_audio.py reuniao.wav --tema "juiz-cacimbinhas"
    python tools/transcrever_audio.py gravacao.flac --tema "professor-metodologia" --data 2026-06-07

Saída:
    references/reunioes/AAAA-MM-DD_reuniao_<tema>.md  com Template A de metadados

Formatos de entrada suportados diretamente: FLAC, WAV, OGG/Opus
Para MP3, M4A, MP4: instale ffmpeg e o script converte automaticamente.

Dependências (instalar via pip):
    pip install google-cloud-speech python-dotenv
"""

import argparse
import os
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path


def _carregar_env():
    """Carrega variáveis de ambiente do .env se existir."""
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(env_path)
        except ImportError:
            # dotenv não instalado — lê manualmente
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, _, val = line.partition("=")
                        os.environ.setdefault(key.strip(), val.strip())


def _converter_para_flac(caminho_entrada: Path) -> Path:
    """Converte áudio para FLAC via ffmpeg (necessário para MP3/M4A)."""
    saida = Path(tempfile.mktemp(suffix=".flac"))
    resultado = subprocess.run(
        ["ffmpeg", "-y", "-i", str(caminho_entrada), str(saida)],
        capture_output=True,
        text=True,
    )
    if resultado.returncode != 0:
        raise RuntimeError(
            f"Falha ao converter com ffmpeg:\n{resultado.stderr}"
        )
    return saida


def _detectar_encoding(caminho: Path):
    """Detecta o RecognitionConfig correto baseado na extensão."""
    from google.cloud import speech

    ext = caminho.suffix.lower()
    if ext in (".flac",):
        return speech.RecognitionConfig.AudioEncoding.FLAC, 0  # 0 = auto-detect rate
    elif ext in (".wav",):
        return speech.RecognitionConfig.AudioEncoding.LINEAR16, 0
    elif ext in (".ogg", ".opus"):
        return speech.RecognitionConfig.AudioEncoding.OGG_OPUS, 0
    else:
        raise ValueError(
            f"Formato '{ext}' não suportado diretamente. "
            "Converta para FLAC/WAV ou instale ffmpeg."
        )


def transcrever(caminho_audio: Path) -> str:
    """Envia o áudio para Google Speech-to-Text e retorna o texto."""
    from google.cloud import speech

    client = speech.SpeechClient()

    # Converte se necessário
    ext = caminho_audio.suffix.lower()
    arquivo_temp = None
    if ext in (".mp3", ".m4a", ".mp4", ".aac"):
        print(f"  Convertendo {ext} → FLAC via ffmpeg...")
        caminho_audio = _converter_para_flac(caminho_audio)
        arquivo_temp = caminho_audio
        ext = ".flac"

    encoding, sample_rate = _detectar_encoding(caminho_audio)

    audio_bytes = caminho_audio.read_bytes()
    audio = speech.RecognitionAudio(content=audio_bytes)

    config = speech.RecognitionConfig(
        encoding=encoding,
        sample_rate_hertz=sample_rate if sample_rate else None,
        language_code="pt-BR",
        model="latest_long",
        enable_automatic_punctuation=True,
        enable_word_time_offsets=False,
    )

    tamanho_mb = len(audio_bytes) / 1_048_576
    print(f"  Tamanho do áudio: {tamanho_mb:.1f} MB")

    if tamanho_mb > 10:
        # Áudios grandes: long_running_recognize
        print("  Áudio longo — usando reconhecimento assíncrono (pode levar alguns minutos)...")
        operation = client.long_running_recognize(config=config, audio=audio)
        print("  Aguardando conclusão...")
        response = operation.result(timeout=600)
    else:
        # Áudios curtos: recognize síncrono
        print("  Transcrevendo...")
        response = client.recognize(config=config, audio=audio)

    if arquivo_temp:
        arquivo_temp.unlink(missing_ok=True)

    partes = [
        result.alternatives[0].transcript
        for result in response.results
        if result.alternatives
    ]

    if not partes:
        raise RuntimeError("Transcrição retornou vazia. Verifique o áudio e as credenciais.")

    return "\n\n".join(partes)


def salvar_referencia(texto: str, tema: str, data_str: str, caminho_original: Path) -> Path:
    """Cria o arquivo de referência com Template A de metadados."""
    repo_root = Path(__file__).parent.parent
    destino_dir = repo_root / "references" / "reunioes"
    destino_dir.mkdir(parents=True, exist_ok=True)

    nome_arquivo = f"{data_str}_reuniao_{tema}.md"
    destino = destino_dir / nome_arquivo

    conteudo = f"""# Reunião: {tema.replace("-", " ").title()}

**Tipo:** reuniao
**Data:** {data_str}
**Fonte original:** Gravação de áudio — {caminho_original.name}
**Anonimizado:** Não (pendente — revisar antes de consolidar na knowledge_base)
**Processado para knowledge_base:** Não

---

## Transcrição

{texto}

---

*Transcrição gerada automaticamente via Google Cloud Speech-to-Text (pt-BR).*
*Revise o conteúdo, anonimize nomes sensíveis e aprove antes de usar na knowledge_base.*
"""

    destino.write_text(conteudo, encoding="utf-8")
    return destino


def main():
    parser = argparse.ArgumentParser(
        description="Transcreve áudio de reunião para Markdown usando Google Speech-to-Text."
    )
    parser.add_argument("audio", type=Path, help="Caminho para o arquivo de áudio")
    parser.add_argument(
        "--tema",
        default="reuniao",
        help="Slug do tema (ex: juiz-cacimbinhas, professor-metodologia). Padrão: reuniao",
    )
    parser.add_argument(
        "--data",
        default=date.today().isoformat(),
        help="Data no formato AAAA-MM-DD. Padrão: hoje",
    )
    args = parser.parse_args()

    if not args.audio.exists():
        print(f"Erro: arquivo não encontrado: {args.audio}", file=sys.stderr)
        sys.exit(1)

    _carregar_env()

    credentials_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not credentials_path or not Path(credentials_path).exists():
        print(
            "Erro: GOOGLE_APPLICATION_CREDENTIALS não configurado ou arquivo JSON não encontrado.\n"
            "Configure em .env apontando para config/google-service-account.json",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Transcrevendo: {args.audio}")
    texto = transcrever(args.audio)

    destino = salvar_referencia(texto, args.tema, args.data, args.audio)
    print(f"\n✓ Transcrição salva em: {destino}")
    print(f"  Próximo passo: revise o arquivo, anonimize nomes e execute o workflow de ingestão.")


if __name__ == "__main__":
    main()
