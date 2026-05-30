# Workflow: Consulta à Knowledge Base

> Processo para responder perguntas sobre a metodologia SGQ usando o conhecimento já consolidado.

## Gatilho

O usuário faz uma pergunta sobre SGQ, ISO 9001, ou sobre como proceder numa situação específica do projeto.

Exemplos:
- "O que já documentamos sobre gestão de riscos?"
- "Como a norma define ação corretiva vs. correção?"
- "Qual o requisito da cláusula 9.2 para auditoria interna?"
- "O que aprendemos com o professor sobre esse tema?"

---

## Passo 1 — Classificar a pergunta

| Tipo | Onde buscar |
|------|-------------|
| Conceito normativo (o que a norma diz) | `knowledge_base/clausula_X/_overview.md` |
| Aprendizado do projeto (o que foi destilado) | `knowledge_base/clausula_X/AAAA-MM-DD_aprendizado_*.md` |
| Modelo ou template | `knowledge_base/clausula_X/_modelos/` |
| Fonte bruta (o que o professor disse exatamente) | `references/reunioes/` |

---

## Passo 2 — Buscar e responder

1. Ler o(s) arquivo(s) relevante(s) da knowledge_base.
2. Responder com:
   - O que a norma exige (se pergunta normativa).
   - O que já foi destilado e consolidado (se pergunta sobre aprendizado).
   - Indicação da fonte (cláusula, arquivo de origem).
3. Se a resposta **não estiver** na knowledge_base ainda:
   - Informar claramente: "Ainda não consolidamos esse ponto."
   - Oferecer resposta baseada em conhecimento geral de ISO 9001.
   - Propor criar um aprendizado pendente para ser consolidado na próxima sessão.

---

## Passo 3 — Sinalizar lacunas

Se a pergunta revelou que um tema importante **ainda não está documentado**, registrar como **item de backlog**:

```
**Backlog de conhecimento:**
- Tema: [descrição]
- Cláusula ISO: [X.Y]
- Fonte provável: [reunião com professor / pesquisa / norma]
- Prioridade: Alta / Média / Baixa
```

Propor ao usuário incluir esse item no próximo ciclo de destilação.

---

## Critério de Qualidade

- [ ] Toda resposta cita a cláusula ISO correspondente.
- [ ] Distingue claramente entre "a norma diz" e "aprendemos com o projeto".
- [ ] Lacunas são sinalizadas — nunca inventar conteúdo que não está na base.
- [ ] Backlog é proposto quando relevante (não silenciado).
