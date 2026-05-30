# Skill: Mapeamento à ISO 9001

> Prompt reutilizável. Mapeia aprendizados extraídos às cláusulas corretas da ISO 9001:2015.

## Quando Usar

Após a extração e validação de aprendizados pelo usuário, antes da consolidação na knowledge_base.

---

## Referência Rápida: Estrutura da ISO 9001:2015

| Cláusula | Título | Subcláusulas principais |
|----------|--------|------------------------|
| **4** | Contexto da organização | 4.1 Entendendo a org.; 4.2 Partes interessadas; 4.3 Escopo; 4.4 SGQ e seus processos |
| **5** | Liderança | 5.1 Liderança e comprometimento; 5.2 Política da qualidade; 5.3 Funções, responsabilidades |
| **6** | Planejamento | 6.1 Riscos e oportunidades; 6.2 Objetivos da qualidade; 6.3 Planejamento de mudanças |
| **7** | Apoio | 7.1 Recursos; 7.2 Competência; 7.3 Conscientização; 7.4 Comunicação; 7.5 Informação documentada |
| **8** | Operação | 8.1 Planejamento operacional; 8.2 Requisitos p/ produtos/serviços; 8.4 Controle de externos; 8.5 Produção/serviço; 8.7 Saídas não conformes |
| **9** | Avaliação de desempenho | 9.1 Monitoramento; 9.2 Auditoria interna; 9.3 Análise crítica pela direção |
| **10** | Melhoria | 10.1 Generalidades; 10.2 Não-conformidade e ação corretiva; 10.3 Melhoria contínua |

---

## Prompt de Mapeamento

```
Você é um especialista em ISO 9001:2015.

Para cada aprendizado abaixo, identifique:
1. A cláusula principal (ex.: 6.1)
2. O título da cláusula
3. Uma justificativa breve (1-2 frases) do porquê esse mapeamento é correto

Se um aprendizado se aplicar a múltiplas cláusulas, liste todas em ordem de relevância.

Aprendizados para mapear:
[INSERIR LISTA DE APRENDIZADOS]
```

---

## Casos Especiais de Mapeamento

- **Aprendizados transversais** (afetam múltiplas cláusulas): mapear à cláusula *principal* e mencionar as secundárias com nota `(também: X.Y)`.
- **Aprendizados sobre cultura/comportamento:** normalmente mapeiam à cláusula 5 (Liderança) ou 7.3 (Conscientização).
- **Aprendizados sobre documentação:** normalmente mapeiam à cláusula 7.5 (Informação documentada).
- **Aprendizados sobre auditoria:** normalmente mapeiam à cláusula 9.2 (Auditoria interna).

## Critério de Qualidade do Mapeamento

- [ ] Cada aprendizado tem ao menos uma cláusula mapeada.
- [ ] A justificativa de mapeamento é específica (não genérica).
- [ ] Mapeamentos ambíguos são explicitados e confirmados com o usuário.
