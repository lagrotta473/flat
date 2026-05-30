# Tools — Scripts Python

> Scripts de automação que executam ações concretas dentro dos workflows. Criados apenas quando um processo manual se torna repetitivo o suficiente para justificar automação.

## Princípio

Ferramentas só são criadas quando:
1. Um processo manual é executado repetidamente (≥ 3 vezes).
2. O usuário aprova a criação da tool.
3. O workflow correspondente documenta onde/como a tool é chamada.

## Tools Planejadas

| Tool | Propósito | Status |
|------|-----------|--------|
| `transcrever_audio.py` | Converter áudio de reunião em texto | Planejado |
| `exportar_para_docx.py` | Exportar Markdown da knowledge_base para Word | Planejado |
| `buscar_na_base.py` | Busca semântica na knowledge_base (RAG) | Planejado |
| `validar_rastreabilidade.py` | Verificar que todos os docs têm metadados completos | Planejado |

## Tools Ativas

*Nenhuma tool implementada ainda.*

## Padrão de Desenvolvimento de Tools

```python
#!/usr/bin/env python3
"""
Tool: nome_da_tool.py
Propósito: [descrição em uma frase]
Workflow: [qual workflow utiliza esta tool]
Criado em: AAAA-MM-DD
"""

import argparse

def main():
    # implementação
    pass

if __name__ == "__main__":
    main()
```
