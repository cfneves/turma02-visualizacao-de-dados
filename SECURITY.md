# Política de Segurança

## Escopo

Este repositório contém materiais educacionais, exercícios de programação e portfólios de alunos. Não há sistemas em produção, APIs públicas ou infraestrutura de servidores associada a este repositório.

## O que reportar

Mesmo sendo um repositório educacional, existem situações que merecem atenção imediata:

- **Dados sensíveis acidentalmente commitados** — senhas, tokens de API, chaves privadas ou dados pessoais reais (CPF, e-mail, telefone) expostos em algum arquivo
- **Credenciais expostas** em notebooks Jupyter ou scripts `.py`
- **Dados de terceiros** publicados sem consentimento

## Como reportar

**Não abra uma Issue pública para problemas de segurança.**

Entre em contato diretamente com o professor:

- **GitHub:** [@cfneves](https://github.com/cfneves)
- **E-mail:** disponível no perfil GitHub

Descreva o problema com o máximo de detalhes: arquivo afetado, tipo de dado exposto e como foi identificado.

## Boas Práticas para Alunos

Para evitar exposição acidental de dados:

```python
# ERRADO — nunca commit credenciais
API_KEY = "sk-abc123xyz..."

# CORRETO — use variáveis de ambiente
import os
API_KEY = os.getenv("API_KEY")
```

- Nunca adicione arquivos `.env` ao repositório — o `.gitignore` já os exclui
- Não use dados pessoais reais em datasets de exercício — anonimize ou use dados fictícios
- Revise o diff antes de cada `git push`

## Versões Suportadas

| Recurso | Suporte |
|---------|---------|
| Materiais de aula | Atualizados durante o curso |
| Exercícios com gabarito | Mantidos durante o Módulo 1 |
| Portfólios dos alunos | Responsabilidade de cada aluno |
