# Workflow: Ingestão de Nova Fonte

> Sub-workflow do processo de destilação. Foca exclusivamente na etapa de receber e arquivar corretamente uma nova fonte de conhecimento.

## Gatilho

O usuário fornece um material bruto para ser adicionado ao sistema.

---

## Tipos de Fonte Aceitos

| Tipo | Onde salvar | Nomenclatura |
|------|------------|--------------|
| Transcrição de reunião com professor | `/references/reunioes/` | `AAAA-MM-DD_reuniao_tema.md` |
| Documento normativo (ISO, ABNT) | `/references/normas/` | `AAAA-MM-DD_norma_titulo.md` |
| Material do professor (slides, apostilas) | `/references/material_professor/` | `AAAA-MM-DD_material_titulo.md` |
| Reflexão pessoal do usuário | `/references/reflexoes/` | `AAAA-MM-DD_reflexao_tema.md` |
| Artigo ou referência externa | `/references/literatura/` | `AAAA-MM-DD_artigo_titulo.md` |

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

Após aprovação, criar o arquivo em `/references/` com o seguinte cabeçalho:

```markdown
# [Título Descritivo]

**Tipo:** reuniao | reflexao | norma | material | artigo  
**Data:** AAAA-MM-DD  
**Fonte original:** [descrição — sem dados sigilosos]  
**Anonimizado:** Sim | Não aplicável  
**Processado para knowledge_base:** Não

---

[Conteúdo da fonte]
```

### 5. Confirmar e Prosseguir

- Confirmar ao usuário que o arquivo foi criado.
- Perguntar se deseja prosseguir imediatamente para a destilação (Workflow de Destilação de Conhecimento) ou se será processado depois.
