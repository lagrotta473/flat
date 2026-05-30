# Setup do VPS — Agente Destilador SGQ

> Guia de configuração para rodar o agente via SSH num servidor Linux. Execute os passos em ordem; cada etapa tem um critério de verificação.

---

## Pré-requisitos no VPS

| Requisito | Versão mínima | Verificar com |
|-----------|--------------|---------------|
| Ubuntu/Debian | 22.04+ | `lsb_release -a` |
| Node.js | 18+ | `node --version` |
| npm | 9+ | `npm --version` |
| Git | 2.x | `git --version` |
| Python | 3.10+ | `python3 --version` |

---

## Passo 1 — Instalar o Claude Code CLI

```bash
npm install -g @anthropic-ai/claude-code
claude --version          # deve retornar a versão instalada
```

---

## Passo 2 — Configurar a chave de API

```bash
# Adicionar ao ~/.bashrc ou ~/.zshrc para persistir entre sessões
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
source ~/.bashrc

# Verificar
echo $ANTHROPIC_API_KEY   # deve exibir a chave
```

> A chave fica **apenas no servidor**, nunca commitada no repositório.
> Coloque `*.env` e qualquer arquivo com `API_KEY` no `.gitignore` se criar um.

---

## Passo 3 — Clonar e configurar o repositório

```bash
# Configurar identidade do Git (uma vez)
git config --global user.name  "Seu Nome"
git config --global user.email "andrelagrotta@gmail.com"

# Clonar o projeto
git clone https://github.com/lagrotta473/flat.git ~/sgq-agent
cd ~/sgq-agent

# Verificar que está na branch correta
git branch      # deve mostrar a branch de trabalho ativa
git log --oneline -5
```

---

## Passo 4 — Verificar que o CLAUDE.md é carregado automaticamente

```bash
cd ~/sgq-agent
claude          # inicia o agente
# O agente deve reconhecer o contexto do projeto SGQ automaticamente
# (CLAUDE.md em maiúsculo = carregamento automático pelo Claude Code)
```

**Teste rápido:** na primeira sessão, peça ao agente "qual é o seu propósito?" — ele deve responder referenciando destilação de conhecimento SGQ.

---

## Passo 5 — Configurar o .gitignore

```bash
cat > ~/sgq-agent/.gitignore << 'EOF'
# Credenciais e ambiente
.env
*.env
.env.local
secrets.*

# Cache e temporários
__pycache__/
*.pyc
*.pyo
.DS_Store
.idea/
.vscode/

# Logs temporários
*.log
EOF

git add .gitignore
git commit -m "chore: adiciona .gitignore"
```

---

## Passo 6 — Manter a sessão ativa via tmux (recomendado)

SSH cai? A sessão do agente morre junto. Use `tmux` para sessões persistentes:

```bash
# Instalar tmux (se não tiver)
sudo apt install tmux -y

# Criar uma sessão nomeada para o agente
tmux new-session -s sgq

# Dentro da sessão tmux:
cd ~/sgq-agent && claude

# Desconectar sem matar: Ctrl+B, depois D
# Reconectar mais tarde:
tmux attach -t sgq
```

---

## Passo 7 — Alias de conveniência (opcional)

Adicionar ao `~/.bashrc` para entrar direto no agente:

```bash
echo 'alias sgq="cd ~/sgq-agent && tmux attach -t sgq 2>/dev/null || tmux new-session -s sgq claude"' >> ~/.bashrc
source ~/.bashrc

# Uso: só digitar "sgq" no terminal
```

---

## Checklist de Verificação Final

Antes de usar no projeto real, confirmar todos os itens:

- [ ] `claude --version` retorna versão sem erro
- [ ] `echo $ANTHROPIC_API_KEY` retorna a chave (não vazio)
- [ ] `git log --oneline -3` mostra os commits do projeto
- [ ] `claude` abre o agente e ele reconhece o contexto SGQ
- [ ] `.gitignore` criado e commitado
- [ ] `tmux` instalado e sessão `sgq` funcionando
- [ ] Testar um ciclo completo: pedir ao agente para criar um arquivo de rascunho em `/references/reunioes/` e depois deletar — só para confirmar que leitura/escrita funcionam

---

## Solução de Problemas Comuns

| Problema | Causa provável | Solução |
|----------|---------------|---------|
| `claude: command not found` | npm não está no PATH | `export PATH="$PATH:$(npm bin -g)"` |
| `AuthenticationError` | Chave de API inválida ou não exportada | Verificar `echo $ANTHROPIC_API_KEY` |
| `CLAUDE.md não carregado` | Arquivo em minúsculo ou errado | Confirmar que o arquivo se chama `CLAUDE.md` (maiúsculo) |
| Git push falha | SSH key não configurada | Usar HTTPS com token ou configurar SSH key do GitHub |
| Sessão SSH cai | Timeout do servidor | Usar tmux (Passo 6) |

---

*Criado em: 2026-05-30 | Para uso no projeto: Agente Destilador de Conhecimento SGQ*
