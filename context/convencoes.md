# Convenções do Projeto

> **Fonte única de verdade** para nomenclatura, estrutura de pastas, templates de metadados e versionamento. Todos os demais arquivos referenciam este — nunca redefinem.

---

## 1. Nomenclatura de Arquivos

Padrão obrigatório: `AAAA-MM-DD_tipo_tema.md`

| Campo | Valores possíveis |
|-------|-------------------|
| `AAAA-MM-DD` | Data de criação no formato ISO 8601 |
| `tipo` | `reuniao`, `reflexao`, `norma`, `material`, `artigo`, `aprendizado`, `modelo`, `errata` |
| `tema` | Descrição curta em kebab-case, **sem acentos** |

**Exemplos:**
- `2026-05-30_reuniao_gestao-de-riscos.md`
- `2026-06-15_reflexao_analise-critica-lideranca.md`
- `2026-07-01_modelo_politica-da-qualidade.md`

---

## 2. Estrutura de Pastas

### `/references/` — material bruto (somente leitura)

| Tipo de fonte | Pasta | Nomenclatura |
|---------------|-------|--------------|
| Transcrição de reunião com professor | `references/reunioes/` | `AAAA-MM-DD_reuniao_tema.md` |
| Documento normativo (ISO, ABNT) | `references/normas/` | `AAAA-MM-DD_norma_titulo.md` |
| Material do professor (slides, apostilas) | `references/material_professor/` | `AAAA-MM-DD_material_titulo.md` |
| Reflexão pessoal do usuário | `references/reflexoes/` | `AAAA-MM-DD_reflexao_tema.md` |
| Artigo ou referência externa | `references/literatura/` | `AAAA-MM-DD_artigo_titulo.md` |

### `/knowledge_base/` — metodologia destilada (por cláusula ISO 9001)

| Pasta | Cláusula |
|-------|----------|
| `clausula_4_contexto_organizacional/` | 4 — Contexto da organização |
| `clausula_5_lideranca/` | 5 — Liderança |
| `clausula_6_planejamento/` | 6 — Planejamento |
| `clausula_7_suporte/` | 7 — Apoio |
| `clausula_8_operacao/` | 8 — Operação |
| `clausula_9_avaliacao_desempenho/` | 9 — Avaliação de desempenho |
| `clausula_10_melhoria/` | 10 — Melhoria |

Cada pasta de cláusula contém:
- `_overview.md` — visão geral da cláusula, requisitos e intenção normativa.
- Documentos de aprendizado: `AAAA-MM-DD_aprendizado_tema.md`.
- `_modelos/` — templates práticos (Política da Qualidade, formulários, etc.).

---

## 3. Templates de Metadados

Há **dois** templates distintos, um para cada tipo de documento. Não os misture.

### Template A — Cabeçalho de arquivo de referência

Usado no topo de toda fonte bruta salva em `/references/`:

```markdown
# [Título Descritivo]

**Tipo:** reuniao | reflexao | norma | material | artigo
**Data:** AAAA-MM-DD
**Fonte original:** [descrição — sem dados sigilosos]
**Anonimizado:** Sim | Não aplicável
**Processado para knowledge_base:** Não | Sim (data: AAAA-MM-DD)

---

[Conteúdo da fonte]
```

### Template B — Rodapé de documento consolidado

Usado no final de todo documento da `/knowledge_base/`:

```markdown
---
Versão: v0.1
Data: AAAA-MM-DD
Fonte: [tipo de fonte — data]
Cláusula ISO: X.Y
Aprovado por: [usuário — data]
```

---

## 4. Versionamento de Documentos

Progressão de versões no Template B:

- `v0.x` — rascunho, ainda não aprovado pelo usuário.
- `v1.0` — primeira versão aprovada e consolidada.
- `vX.Y` — revisões posteriores aprovadas.

O histórico completo de cada documento é preservado no Git.
