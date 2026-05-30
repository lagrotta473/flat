# Skill: Análise de Gap ISO 9001

> Prompt reutilizável. Compara o estado atual de uma organização com os requisitos da ISO 9001:2015, identificando lacunas (gaps) por cláusula.

## Quando Usar

- Ao iniciar um projeto de implementação de SGQ numa nova organização.
- Ao preparar o diagnóstico inicial (pré-auditoria interna).
- Quando o professor ou o projeto apresentar a situação atual da vara.

---

## Contexto: O que é Gap Analysis em ISO 9001

Gap analysis (análise de lacunas) é o diagnóstico estruturado que responde:
> "Para cada requisito da norma, a organização já atende, atende parcialmente, ou não atende?"

O resultado orienta o **plano de implementação**: o que precisa ser criado, o que precisa ser formalizado, o que já existe mas não está documentado.

Escala de conformidade usada:
| Nível | Descrição |
|-------|-----------|
| **C** — Conforme | Requisito plenamente atendido com evidência objetiva |
| **CP** — Conforme Parcialmente | Requisito atendido em parte ou sem evidência suficiente |
| **NC** — Não Conforme | Requisito não atendido |
| **NA** — Não Aplicável | Requisito excluído do escopo com justificativa |

---

## Prompt de Análise de Gap

```
Você é um auditor sênior de ISO 9001:2015 especializado em organizações de serviço público.

Com base nas informações abaixo sobre a organização [NOME/TIPO], realize uma análise de gap
em relação aos requisitos da ISO 9001:2015.

Para cada cláusula (4 a 10), avalie o nível de conformidade (C / CP / NC / NA) e justifique
em 1-2 frases com base nas informações fornecidas. Onde houver lacuna (CP ou NC), indique:
- O que está faltando (evidência, processo, documento, responsável).
- Esforço estimado para fechar o gap: Alto / Médio / Baixo.

Apresente o resultado em tabela:

| Cláusula | Título | Nível | Justificativa | O que falta | Esforço |
|----------|--------|-------|--------------|-------------|---------|

Ao final, identifique os 3 gaps prioritários (maior impacto + menor esforço = quick wins).

Informações sobre a organização:
[INSERIR: estrutura, processos, documentação existente, contexto da reunião/diagnóstico]
```

---

## Saída Esperada

Tabela de gap analysis + lista de 3 quick wins priorizados. Apresentar ao usuário para validação antes de usar como insumo para planejamento da knowledge_base.

## Critério de Qualidade

- [ ] Toda avaliação CP ou NC tem justificativa baseada em evidência (ou ausência dela).
- [ ] Quick wins são acionáveis — dizem o que *fazer*, não apenas o que *falta*.
- [ ] Gaps de cláusula 5 (Liderança) são sinalizados com atenção especial — são os mais difíceis de fechar em setor público.
- [ ] O resultado é apresentado em linguagem acessível ao gestor, não apenas ao auditor.
