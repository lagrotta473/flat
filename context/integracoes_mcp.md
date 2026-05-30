# Integrações MCP (Model Context Protocol)

> Status de cada integração: **Planejada**, **Configurada** ou **Ativa**.

## 1. GitHub — Versionamento da Metodologia

- **Status:** Ativa (este repositório).
- **Uso:** Versionar toda a `/knowledge_base`, `/workflows`, `/skills` e `/context`. Cada evolução metodológica gera um commit rastreável.
- **Regra:** O agente **propõe** o commit; o usuário **aprova** antes de executar.

## 2. Google Workspace (Docs / Drive / Sheets)

- **Status:** Planejada.
- **Uso previsto:**
  - Exportar documentos da knowledge_base para Google Docs (formato editável para clientes).
  - Organizar transcrições de reuniões no Drive.
  - Acompanhar indicadores de SGQ em Google Sheets.
- **Configuração necessária:** Credenciais OAuth + MCP server `google-workspace`.

## 3. Transcrição de Áudio → Texto

- **Status:** Planejada.
- **Uso previsto:** Processar gravações de reuniões com o professor, convertendo áudio em texto e salvando em `/references/reunioes/`.
- **Opções de implementação:** Whisper (local/API OpenAI), Google Speech-to-Text.
- **Configuração necessária:** Definir provider e chave de API.

## 4. Web Search

- **Status:** Disponível via ambiente Claude Code.
- **Uso:** Consultar textos normativos ISO 9001, benchmarks de SGQ, jurisprudência de qualidade em organismos públicos.
- **Regra:** Resultados de busca são sempre referenciados como fonte ao consolidar conhecimento.

## 5. Leitura de PDF

- **Status:** Disponível via ambiente Claude Code.
- **Uso:** Ler a norma ABNT NBR ISO 9001:2015, POPs, modelos de documentação.
- **Regra:** PDFs lidos são registrados em `/references/` com metadados de origem.

## 6. Base Vetorial / RAG

- **Status:** Planejada.
- **Uso previsto:** Busca semântica dentro de toda a `/knowledge_base` e `/references`. Responde perguntas como "o que já documentamos sobre gestão de riscos?".
- **Opções:** ChromaDB local, Pinecone, Weaviate.
- **Dependência:** Implementar após a knowledge_base ter volume suficiente (≥ 20 documentos).

---

## Checklist de Configuração

| Integração | Prioridade | Ação Necessária |
|------------|------------|-----------------|
| GitHub | Alta | ✅ Ativa |
| Web Search | Alta | ✅ Disponível |
| Leitura de PDF | Alta | ✅ Disponível |
| Google Workspace | Média | Configurar credenciais OAuth |
| Transcrição de Áudio | Média | Escolher provider e configurar API |
| Base Vetorial / RAG | Baixa | Aguardar volume de knowledge_base |
