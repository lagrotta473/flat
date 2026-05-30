# Workflow: Tratamento de Erros

> O agente pratica a disciplina de qualidade que ajuda a documentar. Erros são tratados com rigor metodológico, não com tentativa e erro aleatória.

## Princípio

Todo erro — técnico ou de processo — é uma **não-conformidade interna** do agente. Aplicamos o ciclo PDCA/DMAIC e as ferramentas de causa-raiz que são a base da metodologia SGQ.

---

## Classificação de Erros

| Tipo | Exemplos |
|------|---------|
| **Erro técnico** | Falha ao ler arquivo, tool Python com bug, integração MCP fora do ar |
| **Erro de processo** | Mapeamento incorreto à cláusula ISO, consolidação sem rastreabilidade, commit sem aprovação |
| **Erro de interpretação** | Entendimento errado da intenção do usuário, generalização indevida |

---

## Passo a Passo

### Ciclo 1 — Identificação e Diagnóstico Rápido

1. Identificar o erro (sintoma observável).
2. Aplicar **5 Porquês** para encontrar a causa-raiz:
   - Por que aconteceu? → Resposta 1
   - Por que a Resposta 1 aconteceu? → Resposta 2
   - *(até 5 níveis ou até chegar à causa-raiz)*
3. Propor e testar uma correção baseada na causa-raiz.

### Ciclo 2 — Verificação

1. Verificar se a correção resolveu o problema.
2. Testar o cenário que originou o erro novamente.

### Ciclo 3 — Ação Preventiva

1. Perguntar: "O que podemos mudar para evitar que este erro ocorra novamente?"
2. Propor melhoria no workflow, skill ou tool correspondente.

### Limite de Ciclos

**Máximo de 3 ciclos.** Se não resolvido:
- Parar imediatamente.
- Consultar o usuário com diagnóstico estruturado:
  1. O que falhou (sintoma).
  2. Causa-raiz identificada até o momento.
  3. O que já foi tentado.
  4. Proposta de próximo passo (incluindo opção de escalar externamente).

---

## Registro

Todo erro passa por registro no `/context/error_log.md`, usando o formato de
registro definido naquele arquivo.

O registro é proposto ao usuário antes de ser commitado — segue a **Regra 4 (Aprovação Manual)**.

---

## Ishikawa — Categorias de Causa para Erros do Agente

Para erros complexos, aplicar o diagrama de Ishikawa com as seguintes categorias:

- **Método:** O workflow/skill estava mal definido?
- **Máquina:** Houve falha técnica (API, tool, integração)?
- **Material:** O dado de entrada estava incompleto ou ambíguo?
- **Mão-de-obra:** O agente aplicou o skill incorretamente?
- **Medição:** O critério de sucesso estava mal definido?
- **Ambiente:** Condição externa (rede, permissão, contexto) causou o problema?
