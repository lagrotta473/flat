# Workflow: Ingestão de Nova Fonte

> Sub-workflow do processo de destilação. Foca exclusivamente na etapa de receber e arquivar corretamente uma nova fonte de conhecimento.

## Gatilho

O usuário fornece um material bruto para ser adicionado ao sistema.

---

## Tipos de Fonte Aceitos

Os tipos de fonte, suas pastas de destino e a nomenclatura estão definidos em
`/context/convencoes.md` (seção "Estrutura de Pastas" → `/references/`).

---

## Protocolo de Ingestão

### 1. Receber e Identificar

- Perguntar ao usuário (se não estiver claro): qual o tipo e a data da fonte?
- Confirmar o tema principal para compor o nome do arquivo.

### 2. Anonimizar

Antes de salvar, verificar e anonimizar:
- Nomes de pessoas → substituir por função ("Servidor A", "Juiz responsável", "Professor")
- Nome da vara/órgão → substituir por "Organização X" (a menos que seja dado público irrelevante para confidencialidade)
- Dados de processos judiciais → remover completamente

### 3. Propor e Aguardar Aprovação

Apresentar ao usuário:
- Nome de arquivo proposto.
- Conteúdo anonimizado para revisão.
- Localização na estrutura de pastas.

### 4. Criar o Arquivo

Após aprovação, criar o arquivo em `/references/` usando o **Template A —
Cabeçalho de arquivo de referência** definido em `/context/convencoes.md`.

### 5. Confirmar e Prosseguir

- Confirmar ao usuário que o arquivo foi criado.
- Perguntar se deseja prosseguir imediatamente para a destilação (Workflow de Destilação de Conhecimento) ou se será processado depois.
