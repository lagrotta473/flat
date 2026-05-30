# Skill: Extração de Aprendizados

> Prompt reutilizável. Aplicado após a ingestão de uma nova fonte para identificar os aprendizados relevantes para SGQ.

## Quando Usar

Sempre que um novo arquivo for adicionado a `/references/` e precisar ser processado para a knowledge_base.

---

## Prompt de Extração

```
Você é um especialista em Sistemas de Gestão da Qualidade (SGQ) com profundo conhecimento da ISO 9001:2015.

Leia o seguinte material de referência e extraia TODOS os aprendizados relevantes para a construção de uma metodologia de SGQ.

Para cada aprendizado, estruture da seguinte forma:

**Aprendizado [N]:**
- **Enunciado:** [Declaração clara e concisa do aprendizado, em linguagem de metodologia]
- **Contexto:** [Em que situação ou exemplo esse aprendizado surgiu no texto]
- **Implicação prática:** [O que um praticante de SGQ deve fazer diferente ou melhor por causa desse aprendizado]
- **Cláusula ISO provável:** [Sua melhor estimativa da cláusula ISO 9001 mais relevante]

Critérios de relevância — inclua aprendizados sobre:
- Processos de implementação de SGQ
- Armadilhas comuns e como evitá-las
- Boas práticas de documentação
- Gestão de não-conformidades e ações corretivas
- Indicadores de desempenho de qualidade
- Engajamento de liderança e partes interessadas
- Gestão de riscos e oportunidades
- Auditoria interna e externa
- Qualquer insight prático sobre como SGQ funciona na realidade

Ignore: informações administrativas sem relevância metodológica, dados pessoais, números de processo.

Material:
[INSERIR CONTEÚDO DO ARQUIVO DE REFERÊNCIA]
```

---

## Saída Esperada

Lista numerada de aprendizados, cada um com os 4 campos preenchidos. Apresentar ao usuário para validação antes de prosseguir para o mapeamento ISO.

## Critério de Qualidade da Extração

- [ ] Nenhum aprendizado relevante foi omitido.
- [ ] Enunciados são independentes do contexto (fazem sentido lidos isoladamente).
- [ ] Implicações práticas são acionáveis (dizem o que *fazer*, não apenas o que *saber*).
- [ ] Cláusula ISO é plausível (será confirmada na skill de mapeamento).
