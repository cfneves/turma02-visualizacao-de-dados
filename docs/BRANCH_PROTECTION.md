# Configuração de Branch Protection — Guia do Professor

Este documento descreve como configurar as regras de proteção de branch no GitHub para garantir que nenhum aluno consiga fazer push direto na `master` e que todos os PRs passem pela revisão obrigatória do professor.

> **Quem executa:** professor (@cfneves), uma única vez após o push desta estrutura.

---

## 1. Ativar Permissão de Escrita para GitHub Actions

Antes de tudo, os workflows precisam de permissão para comentar em PRs.

1. Acesse **Settings → Actions → General**
2. Em **Workflow permissions**, selecione:
   - `Read and write permissions`
3. Marque também:
   - `Allow GitHub Actions to create and approve pull requests`
4. Clique em **Save**

---

## 2. Configurar Branch Protection na `master`

1. Acesse **Settings → Branches**
2. Clique em **Add branch protection rule** (ou edite a regra existente)
3. Em **Branch name pattern**, digite: `master`

### Configurações obrigatórias

| Opção | Valor |
|-------|-------|
| Require a pull request before merging | ✅ Ativo |
| → Required number of approvals | `1` |
| → Dismiss stale reviews when new commits are pushed | ✅ Ativo |
| → Require review from Code Owners | ✅ Ativo |
| Require status checks to pass before merging | ✅ Ativo |
| → Require branches to be up to date before merging | ✅ Ativo |
| → Status check obrigatório | `Verificar escopo do PR` |
| Require conversation resolution before merging | ✅ Ativo |
| Do not allow bypassing the above settings | ✅ Ativo |
| Allow force pushes | ❌ Desativado |
| Allow deletions | ❌ Desativado |

> **Status check:** o nome `Verificar escopo do PR` corresponde ao campo `name` do job em `.github/workflows/pr-validator.yml`. Ele aparece na lista de checks disponíveis após o primeiro PR ser aberto.

### Como encontrar o status check na lista

O campo de busca por status checks só mostra opções que já executaram pelo menos uma vez. Para popular a lista:
1. Abra um PR de teste (pode ser um PR do próprio professor)
2. Aguarde o workflow executar
3. Volte em **Settings → Branches** e o check `Verificar escopo do PR` aparecerá

---

## 3. Remover Acesso Direto de Push dos Alunos

Se alunos foram adicionados como **collaborators** com acesso de escrita, remova-os:

1. Acesse **Settings → Collaborators and teams**
2. Para cada aluno, mude o papel de `Write` para `Read`
3. Ou remova o acesso completamente — alunos trabalham via **fork**, não como colaboradores

> **Dica:** com branch protection ativa e `Do not allow bypassing`, mesmo colaboradores com Write não conseguem fazer push direto na master.

---

## 4. Configurar o Registro de Alunos (students.json)

Para que o workflow de validação funcione, cada aluno precisa estar registrado:

1. Abra `.github/students.json`
2. Para cada aluno, preencha o campo `"github"` com o username exato do GitHub:
   ```json
   { "github": "username_do_aluno", "folder": "nome_da_pasta", "_nome": "Nome Completo" }
   ```
3. Faça commit e push diretamente na master (como professor):
   ```bash
   git add .github/students.json
   git commit -m "chore(github): cadastra username do aluno X"
   git push origin master
   ```

---

## 5. Fluxo Esperado Após a Configuração

```
Aluno faz fork → trabalha na fork → abre PR para master
       ↓
GitHub Actions executa pr-validator.yml
       ↓
┌─────────────────────────────────────────────┐
│ Aluno está em students.json?                │
│   NÃO → comentário de aviso + CI falha      │
│   SIM → verifica arquivos alterados         │
│          ↓                                  │
│   Arquivos todos em alunos/SeuNome/?        │
│     NÃO → comentário detalhado + CI falha   │
│     SIM → CI passa ✅                       │
└─────────────────────────────────────────────┘
       ↓
Professor recebe notificação para revisar
       ↓
Professor aprova → merge liberado
```

---

## 6. Adicionar Novo Aluno (checklist)

Quando um novo aluno entrar na turma:

- [ ] Criar pasta `alunos/NomeAluno/` com `README.md`
- [ ] Adicionar linha em `.github/CODEOWNERS`
- [ ] Adicionar entrada em `.github/students.json` com o github username
- [ ] Fazer commit dessas mudanças na master
- [ ] Instruir o aluno a fazer fork do repositório

---

## 7. Badges para o README

Após a primeira execução do workflow, adicione estes badges ao README:

```markdown
[![PR Validator](https://github.com/cfneves/turma-visualizacao-de-dados/actions/workflows/pr-validator.yml/badge.svg)](https://github.com/cfneves/turma-visualizacao-de-dados/actions/workflows/pr-validator.yml)
```

---

*Documento mantido pelo professor. Última atualização: 2026-05-12.*
