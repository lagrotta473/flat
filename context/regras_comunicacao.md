# Regras de Comunicação e Convenções

## Tom de Voz

- **Didático + técnico:** O agente explica o *porquê* das decisões metodológicas, não apenas o *o quê*.
- **Vocabulário correto de SGQ:** usa os termos da norma com precisão — não-conformidade, ação corretiva, evidência objetiva, parte interessada, contexto da organização, etc.
- **Sem jargão desnecessário:** quando um termo técnico é introduzido pela primeira vez numa sessão, o agente o define brevemente.
- **Encorajador:** o usuário está aprendendo; o agente reforça o raciocínio correto e explica gentilmente os pontos a revisar.

## Idioma

- **Português do Brasil**, sempre — em todas as respostas, commits, nomes de arquivo e documentação.
- Termos da norma ISO podem aparecer em inglês quando a tradução for ambígua, com a versão em português entre parênteses.

## Estrutura das Respostas

Para tarefas complexas, o agente organiza a resposta em:
1. **O que entendi** — confirma a intenção antes de agir.
2. **O que farei** — lista os passos propostos.
3. **Aguardando aprovação** — para ações externas (commits, criação de arquivo).

Para respostas curtas (perguntas factuais, definições), resposta direta sem estrutura formal.

## Nomenclatura de Arquivos

Padrão obrigatório: `AAAA-MM-DD_tipo_tema.md`

| Campo | Valores possíveis |
|-------|-------------------|
| `AAAA-MM-DD` | Data de criação no formato ISO 8601 |
| `tipo` | `reuniao`, `reflexao`, `norma`, `modelo`, `aprendizado`, `errata` |
| `tema` | Descrição curta em kebab-case (sem acentos) |

**Exemplos:**
- `2026-05-30_reuniao_gestao-de-riscos.md`
- `2026-06-15_reflexao_analise-critica-lideranca.md`
- `2026-07-01_modelo_politica-da-qualidade.md`

## Organização da Knowledge Base

Documentos da `/knowledge_base` seguem a numeração das cláusulas ISO 9001:

| Pasta/Arquivo | Cláusula |
|---------------|----------|
| `clausula_4_contexto_organizacional/` | 4 — Contexto da organização |
| `clausula_5_lideranca/` | 5 — Liderança |
| `clausula_6_planejamento/` | 6 — Planejamento |
| `clausula_7_suporte/` | 7 — Apoio |
| `clausula_8_operacao/` | 8 — Operação |
| `clausula_9_avaliacao_desempenho/` | 9 — Avaliação de desempenho |
| `clausula_10_melhoria/` | 10 — Melhoria |

## Versionamento de Documentos

Cada documento da knowledge_base possui um rodapé de metadados:

```markdown
---
Versão: v0.1
Data: AAAA-MM-DD
Fonte: [tipo de fonte — data]
Cláusula ISO: X.Y
Aprovado por: [usuário — data]
```

Progressão de versões:
- `v0.x` — rascunho, ainda não aprovado pelo usuário.
- `v1.0` — primeira versão aprovada e consolidada.
- `vX.Y` — revisões posteriores aprovadas.
