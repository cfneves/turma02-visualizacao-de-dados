# Guia de Contribuição

Bem-vindo! Este guia explica como enviar seus trabalhos corretamente e manter o repositório organizado.

---

## Índice

1. [Configuração inicial](#1-configuração-inicial)
2. [Criando sua pasta de aluno](#2-criando-sua-pasta-de-aluno)
3. [Fluxo de entrega](#3-fluxo-de-entrega)
4. [Convenção de commits](#4-convenção-de-commits)
5. [Abrindo um Pull Request](#5-abrindo-um-pull-request)
6. [Verificação automática de PRs](#6-verificação-automática-de-prs)
7. [Resolvendo conflitos](#7-resolvendo-conflitos)
8. [Boas práticas em notebooks](#8-boas-práticas-em-notebooks)

---

## 1. Configuração Inicial

Faça isso **uma única vez** no início do curso.

**Passo 1 — Faça um Fork do repositório:**

Clique no botão **Fork** no canto superior direito da página do repositório no GitHub. Isso cria uma cópia pessoal na sua conta.

**Passo 2 — Clone o seu fork e configure o upstream:**

```bash
# Clone o SEU fork (substitua SEU_USUARIO pelo seu username):
git clone https://github.com/SEU_USUARIO/turma-visualizacao-de-dados.git
cd turma-visualizacao-de-dados

# Adicione o repositório original como "upstream":
git remote add upstream https://github.com/cfneves/turma-visualizacao-de-dados.git

# Confirme os remotes configurados:
git remote -v
# origin    https://github.com/SEU_USUARIO/turma-visualizacao-de-dados.git (fetch)
# origin    https://github.com/SEU_USUARIO/turma-visualizacao-de-dados.git (push)
# upstream  https://github.com/cfneves/turma-visualizacao-de-dados.git (fetch)
# upstream  https://github.com/cfneves/turma-visualizacao-de-dados.git (push)
```

> **Por que fork?** O repositório principal está protegido — nenhum aluno pode fazer push direto. O fluxo correto é: trabalhe na sua fork → abra um PR → o professor revisa e merge.

---

## 2. Criando sua Pasta de Aluno

Crie **uma única vez** sua pasta dentro de `alunos/`:

```
alunos/
└── nome-sobrenome/         ← minúsculas, sem espaços, use _
    ├── README.md           ← seu portfólio (use o template!)
    ├── exercicios/         ← uma pasta por exercício
    │   ├── exercicio_01/
    │   └── exercicio_02/
    └── projetos/           ← seus projetos autorais
        └── projeto_01/
```

**Copie o template de portfólio:**

```bash
cp alunos/TEMPLATE_README.md alunos/seu-nome/README.md
```

Edite o `README.md` com suas informações reais — esse arquivo é o seu cartão de visitas.

---

## 3. Fluxo de Entrega

Para **cada entrega** (exercício ou projeto), siga este fluxo:

```bash
# Passo 1: Sincronize sua fork com o repositório principal
git fetch upstream
git checkout master
git merge upstream/master
git push origin master          # mantém sua fork atualizada

# Passo 2: Crie uma branch para esta entrega
git checkout -b feat/exercicio-01-seu-nome

# Passo 3: Adicione seus arquivos SOMENTE dentro da sua pasta
# ⚠️  Nunca modifique arquivos fora de alunos/seu-nome/

# Passo 4: Commit
git add alunos/seu-nome/
git commit -m "feat(alunos): adiciona exercício 01 - Seu Nome"

# Passo 5: Envie a branch para o SEU fork
git push origin feat/exercicio-01-seu-nome

# Passo 6: Abra o Pull Request no GitHub
# (o terminal exibe o link direto após o push)
# Base: cfneves/turma-visualizacao-de-dados → master
# Compare: SEU_USUARIO/turma-visualizacao-de-dados → feat/exercicio-01-seu-nome
```

---

## 4. Convenção de Commits

Use o padrão **Conventional Commits**:

```
tipo(escopo): descrição curta em português
```

| Tipo | Quando usar |
|------|-------------|
| `feat` | Nova entrega, exercício ou projeto |
| `fix` | Correção de algo já enviado |
| `docs` | Atualização de README ou documentação |
| `data` | Adição ou atualização de dataset |
| `style` | Formatação, sem mudança de lógica |

**Exemplos:**

```bash
git commit -m "feat(alunos): adiciona exercício 02 - Ana Paula"
git commit -m "fix(alunos): corrige gráfico do exercício 01 - João Silva"
git commit -m "docs(alunos): atualiza portfólio com projeto final - Maria"
git commit -m "data: adiciona dataset vendas_2024.csv"
```

---

## 5. Abrindo um Pull Request

1. Após o `git push`, o terminal exibe um link direto — clique nele, ou acesse o repositório no GitHub
2. Clique em **"Compare & pull request"** (aparece automaticamente após o push)
3. Verifique que a base é `cfneves/turma-visualizacao-de-dados` → **`master`**
4. Preencha o template do PR (título + checklist)
5. Clique em **"Create pull request"**

**Título sugerido:**

```
feat(alunos): adiciona [exercício/projeto] - Seu Nome
```

---

## 6. Verificação Automática de PRs

Ao abrir um PR, dois workflows são disparados automaticamente:

| Workflow | O que faz |
|----------|-----------|
| **🔒 Validador de Escopo** | Verifica se todos os arquivos alterados estão dentro de `alunos/SeuNome/`. Se arquivos fora da sua pasta forem detectados, o PR é bloqueado com um comentário explicativo. |
| **👋 Boas-vindas** | No seu primeiro PR, você recebe uma mensagem com checklist rápido. |

**O que fazer se o validador reprovar seu PR:**

1. Leia o comentário automático — ele lista os arquivos com problema
2. Corrija sua branch removendo alterações fora da sua pasta
3. Faça um novo push — o workflow re-executa automaticamente

**Para que a validação funcione**, seu GitHub username precisa estar cadastrado em `.github/students.json`. Se for seu primeiro PR no repositório, avise o professor para que ele faça o cadastro.

---

## 7. Resolvendo Conflitos

Conflitos acontecem quando outro aluno enviou arquivos enquanto você trabalhava na sua branch. É normal — não é erro seu.

```bash
# 1. Traga as atualizações do repositório
git checkout master
git pull origin master

# 2. Volte para a branch da sua entrega
git checkout feat/seu-exercicio

# 3. Aplique as mudanças do master na sua branch
git rebase master
```

Se aparecer um conflito num arquivo de outro aluno (ex: `alunos/maria_helena/README.md`):

```bash
# Abra o arquivo conflitado e remova os marcadores:
# <<<<<<< HEAD
# (versão do master — MANTENHA ESTA)
# =======
# (versão da sua branch — REMOVA ESTA PARTE)
# >>>>>>> sua-branch

# Após resolver:
git add alunos/nome-do-colega/README.md
git rebase --continue

# Atualize a branch remota
git push origin feat/seu-exercicio --force-with-lease
```

**Regra de ouro:** em conflito com arquivo de outro aluno, **sempre mantenha a versão do `master`** (a versão do repositório original).

---

## 8. Boas Práticas em Notebooks

- Reinicie o kernel e execute todas as células (`Kernel > Restart & Run All`) antes de commitar
- Sem erros de execução — células com erro **bloqueiam o PR**
- Adicione um título (`# Exercício 01 — Nome`) na primeira célula
- Documente o que cada seção faz com células Markdown
- Dados sensíveis (senhas, tokens) nunca no notebook — use variáveis de ambiente

---

Dúvidas? Abra uma **[Issue](https://github.com/cfneves/turma-visualizacao-de-dados/issues)** com `[dúvida]` no título.
