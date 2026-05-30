# Workflow: Destilação de Conhecimento

> Processo central do agente. Executado sempre que uma nova fonte de conhecimento chega.

## Gatilho

O usuário compartilha uma nova fonte:
- Transcrição de reunião com o professor.
- Documento (PDF, Docs, artigo).
- Anotação ou reflexão pessoal.
- Trecho de norma ou literatura técnica.

---

## Passo 1 — Ingestão da Fonte

1. Receber o material do usuário.
2. Identificar o tipo: `reuniao` | `reflexao` | `norma` | `modelo` | `aprendizado`.
3. Verificar se já existe um arquivo equivalente em `/references/`. Se sim, confirmar com o usuário se é um arquivo novo ou uma atualização.
4. **Propor** a criação do arquivo em `/references/` com nomenclatura correta: `AAAA-MM-DD_tipo_tema.md`.
5. Aguardar aprovação do usuário antes de criar o arquivo.

---

## Passo 2 — Extração de Aprendizados

Aplicar a **Skill de Extração de Aprendizados** (`/skills/extracao_de_aprendizados.md`):

1. Ler o arquivo de referência na íntegra.
2. Identificar todos os aprendizados relevantes para SGQ/ISO 9001.
3. Para cada aprendizado, formatar:
   ```
   **Aprendizado:** [Enunciado claro e conciso]
   **Contexto:** [Em que situação esse aprendizado surgiu]
   **Implicação prática:** [O que muda na metodologia ou na prática]
   ```
4. Apresentar a lista ao usuário para validação antes de prosseguir.

---

## Passo 3 — Mapeamento às Cláusulas ISO

Aplicar a **Skill de Mapeamento ISO** (`/skills/mapeamento_iso.md`):

1. Para cada aprendizado validado, identificar a(s) cláusula(s) da ISO 9001 correspondente(s).
2. Apresentar o mapeamento ao usuário:
   ```
   Aprendizado X → Cláusula 6.1 (Ações para abordar riscos e oportunidades)
   ```
3. Aguardar confirmação ou ajuste do mapeamento.

---

## Passo 4 — Consolidação na Knowledge Base

1. Verificar se já existe conteúdo relacionado no arquivo da cláusula correspondente em `/knowledge_base/`.
2. Se **não existe**: propor a criação de novo conteúdo no arquivo da cláusula.
3. Se **existe**: comparar com o conteúdo atual:
   - **Complementar:** propor adição sem conflito.
   - **Refinar/Contradizer:** sinalizar o conflito explicitamente, apresentar versão antiga vs. nova, propor atualização com justificativa.
4. Aguardar aprovação do usuário antes de qualquer edição.

---

## Passo 5 — Versionamento

1. Após aprovação do usuário, criar/editar o arquivo na knowledge_base.
2. Atualizar o rodapé de metadados com nova versão e data.
3. Propor commit no GitHub com mensagem descritiva:
   ```
   feat(knowledge_base): adiciona aprendizado sobre [tema] à cláusula [X.Y]
   
   Fonte: [tipo de fonte — data]
   ```
4. Aguardar aprovação do usuário antes de executar o commit.

---

## Critérios de Qualidade

- [ ] Todo aprendizado tem fonte rastreável.
- [ ] Nenhum dado sensível foi incluído (verificação de anonimização).
- [ ] O mapeamento à cláusula ISO foi confirmado pelo usuário.
- [ ] O arquivo de referência original não foi modificado.
- [ ] O commit tem mensagem descritiva e referência à fonte.
