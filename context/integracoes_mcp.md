# Integrações MCP (Model Context Protocol)

> Status: **Ativa** | **Configurada** (aguarda chaves) | **Futura** (aguarda gatilho) | **Disponível** (sem configuração)

---

## 1. GitHub — Versionamento

- **Status:** Ativa.
- **Uso:** Versionar `/knowledge_base`, `/workflows`, `/skills`, `/context`, `/web`. Cada evolução gera commit rastreável.
- **Regra:** Agente propõe; usuário aprova antes de executar.

---

## 2. Google Drive — Exportar documentos para professor/cliente

- **Status:** Configurada (aguarda `GOOGLE_CLIENT_ID` e `GOOGLE_CLIENT_SECRET` no `.env`).
- **MCP server:** `@modelcontextprotocol/server-gdrive` (configurado em `.claude/settings.json`)
- **Uso:**
  - Upload de PDFs/DOCX da metodologia para compartilhar com professor e vara
  - Organizar pasta por projeto (Cacimbinhas, futura Clínica)
- **Credenciais:** `console.cloud.google.com` → Projeto → Drive API → OAuth 2.0 → Desktop app
- **Ativar:** colocar `GOOGLE_CLIENT_ID` e `GOOGLE_CLIENT_SECRET` no `.env` e reiniciar Claude Code

---

## 3. Transcrição de Áudio — Google Cloud Speech-to-Text

- **Status:** Configurada (aguarda `GOOGLE_APPLICATION_CREDENTIALS` no `.env`).
- **Tool:** `tools/transcrever_audio.py`
- **Uso:** Processar gravações de reuniões (WAV, FLAC, OGG) → salvar transcrição em `references/reunioes/`
- **Idioma:** `pt-BR`, modelo `latest_long`
- **Credencial:** mesmo service account JSON do Drive → `config/google-service-account.json`
- **Custo:** gratuito até 60 min/mês; ~R$ 0,09/hora adicional

### Atalho: Reuniões via Microsoft Teams

O professor usa Teams. Se ele (ou você) ativar a **transcrição automática durante a chamada**:
1. Ao final, exporte o arquivo `.vtt` pelo chat da reunião
2. Execute: `python tools/converter_teams_transcript.py reuniao.vtt --tema "juiz-cacimbinhas"`
3. O arquivo já vai direto para `references/reunioes/` — **sem gastar minutos de API**

Tool: `tools/converter_teams_transcript.py` — zero custo, zero API key.

---

## 4. Web Search

- **Status:** Disponível via Claude Code (ferramenta `WebSearch` embutida).
- **Uso:** Consultar normas ISO 9001, resoluções CNJ, benchmarks SGQ em órgãos públicos.
- **Upgrade opcional:** Brave Search MCP para pesquisa programática por tools Python
  - Configurado em `.claude/settings.json` (aguarda `BRAVE_API_KEY` no `.env`)
  - Chave: `brave.com/search/api` → gratuito 2000 queries/mês

---

## 5. Leitura de PDF

- **Status:** Disponível via Claude Code (ferramenta `Read` nativa).
- **Uso:** Ler ABNT NBR ISO 9001:2015, POPs, documentos da vara.
- **Regra:** PDFs lidos são registrados em `references/normas/` ou `references/material_professor/`.

---

## 6. RAG / Busca Semântica — Gemini Embeddings + ChromaDB

- **Status:** Futura (ativar quando KB ≥ 20 documentos).
- **Tool:** `tools/buscar_na_base.py`
- **Tecnologia:** `text-embedding-004` (Gemini) para vetores + ChromaDB local para armazenamento
- **Referência:** `https://ai.google.dev/gemini-api/docs/embeddings`
- **Credencial:** `GEMINI_API_KEY` em `.env` → `aistudio.google.com` → gratuito (1500 req/dia)
- **Como ativar:**
  1. Colocar `GEMINI_API_KEY` no `.env`
  2. `pip install google-generativeai chromadb`
  3. `python tools/buscar_na_base.py --reindexar`
  4. `python tools/buscar_na_base.py "controle de saídas não conformes"`

---

## Checklist de Ativação

| Integração | Status | Ação para ativar |
|------------|--------|-----------------|
| GitHub | ✅ Ativa | — |
| Web Search (Claude Code) | ✅ Disponível | — |
| Leitura de PDF | ✅ Disponível | — |
| Teams Transcript | ✅ Pronta | `pip install python-docx` + exportar `.vtt` do Teams |
| Exportar DOCX | ✅ Pronta | `pip install python-docx` |
| Google Drive MCP | ⏳ Aguarda chaves | `GOOGLE_CLIENT_ID` + `GOOGLE_CLIENT_SECRET` no `.env` |
| Speech-to-Text | ⏳ Aguarda chaves | `GOOGLE_APPLICATION_CREDENTIALS` no `.env` (service account JSON) |
| Brave Search MCP | ⏳ Aguarda chaves | `BRAVE_API_KEY` no `.env` |
| RAG (Gemini + ChromaDB) | 🔜 KB < 20 docs | `GEMINI_API_KEY` no `.env` + reindexar |

→ Template de todas as chaves com instruções: `.env.template`
