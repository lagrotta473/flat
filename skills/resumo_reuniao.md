# Skill: Resumo de Reunião

> Prompt reutilizável. Produz um resumo executivo de uma reunião antes da extração de aprendizados.

## Quando Usar

Opcionalmente, antes da extração de aprendizados, para ter uma visão geral da reunião e identificar os temas principais.

---

## Prompt de Resumo

```
Você é um especialista em SGQ e facilitador de reuniões técnicas.

Leia a transcrição abaixo e produza um resumo executivo estruturado com:

## Resumo da Reunião

**Data:** [extrair do contexto ou deixar em branco]
**Participantes:** [listar funções, sem nomes — anonimizado]
**Duração aproximada:** [se inferível]

### Tema Central
[1-2 frases descrevendo o assunto principal discutido]

### Tópicos Abordados
1. [Tópico 1]
2. [Tópico 2]
3. [...]

### Decisões Tomadas
- [Decisão 1]
- [Decisão 2]

### Ações Definidas
| Ação | Responsável (função) | Prazo |
|------|---------------------|-------|
| ... | ... | ... |

### Principais Aprendizados Metodológicos (visão geral)
[3-5 bullet points dos insights mais relevantes para SGQ — detalhamento vem na extração de aprendizados]

### Próxima Reunião
[Data e pauta, se mencionados]

Transcrição:
[INSERIR TRANSCRIÇÃO]
```

---

## Saída Esperada

Documento formatado em Markdown, pronto para ser salvo como cabeçalho do arquivo de referência ou como documento separado em `/references/reunioes/`.

## Critério de Qualidade

- [ ] Todos os tópicos principais estão capturados.
- [ ] Nenhum nome real de pessoa aparece (apenas funções).
- [ ] Decisões e ações são distinguidas claramente.
- [ ] O resumo pode ser lido independentemente da transcrição.
