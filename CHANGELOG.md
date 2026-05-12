# Changelog

Registro de atualizações dos materiais, estrutura e documentação do repositório.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

---

## [Não publicado]

### Em andamento
- Materiais da Semana 06 — Limpeza e Transformação de Dados
- Exercícios Módulo 04 complementares

---

## [1.5.0] — 2026-05-12

### Adicionado
- `.github/CODEOWNERS` — professor controla todo o repositório; cada aluno co-owner da sua pasta
- `.github/students.json` — registro de alunos mapeando GitHub username → pasta em `alunos/`
- `.github/workflows/pr-validator.yml` — workflow que valida escopo de PRs: bloqueia alterações fora da pasta do aluno
- `.github/workflows/welcome.yml` — mensagem de boas-vindas automática para primeiros contribuidores
- `docs/BRANCH_PROTECTION.md` — guia passo a passo para configurar branch protection no GitHub

### Melhorado
- `CONTRIBUTING.md` — seção 1 migrada para fluxo fork + upstream; nova seção 6 documenta verificação automática de PRs
- `PULL_REQUEST_TEMPLATE.md` — adicionada menção ao validador automático no checklist

### Corrigido
- Removidos `aulas/semana_04/Exercicio_final.ipynb` e `aulas/semana_04/base_rh.csv` (arquivos adicionados indevidamente por aluno fora da pasta pessoal)

---

## [1.4.0] — 2026-05-12

### Adicionado
- `LICENSE` — licença MIT
- `CODE_OF_CONDUCT.md` — Contributor Covenant v2.1 em PT-BR
- `SECURITY.md` — política de segurança e boas práticas para alunos
- `CHANGELOG.md` — este arquivo
- `.github/ISSUE_TEMPLATE/config.yml` — configuração dos templates de issue

### Melhorado
- `README.md` — reescrita completa: badges profissionais, tabela comparativa de modelo pedagógico, seção "Para Educadores", layout visual aprimorado, CTA limpo
- Estrutura do repositório documentada com subpastas `html/`, `bases/` e `notebooks/`
- Seção "Stack e Competências" expandida com terceira coluna de competências
- Headings renomeados para terminologia técnica (`Diretrizes`, `Suporte`)

### Corrigido
- Badge de contagem de alunos atualizado para 31
- Jakson Luis adicionado à tabela de portfólios
- Jakson Luis (`jaksonmoraes`) adicionado como colaborador

---

## [1.3.0] — 2026-05-08

### Adicionado
- `aulas/semana_05/notebooks/` — notebooks de desafios Pandas e NumPy
- `exercicios/04. Exercicios/calculadora.py` — desafio calculadora interativa
- `exercicios/04. Exercicios/gabarito_calculadora.py`
- `exercicios/04. Exercicios/cadastro_produtos_gabarito.py`

---

## [1.2.0] — 2026-05-05

### Adicionado
- `aulas/semana_04/` — estrutura completa com `html/`, `bases/` e `notebooks/`
- Datasets de aula: `base_rh.csv`, `base_rh.xlsx`, `base_rh.json`, formatos variados

### Melhorado
- `exercicios/README.md` — documentação completa dos 10 exercícios com tabela de status

---

## [1.1.0] — 2026-04-28

### Adicionado
- `aulas/semana_03/html/` — slides Python fundamentos e guias de colaboração
- `exercicios/01.sintaxe/` — 3 exercícios de print, input e comentários
- `exercicios/02.variaveis/` — 6 arquivos sobre tipos primitivos
- `exercicios/03.Estruturas/` — condicionais e loops

---

## [1.0.0] — 2026-04-21

### Adicionado
- Estrutura inicial do repositório
- `README.md` — documentação base
- `CONTRIBUTING.md` — guia de contribuição completo com fluxo, commits e resolução de conflitos
- `PULL_REQUEST_TEMPLATE.md` — template de PR com checklist
- `.github/ISSUE_TEMPLATE/duvida.md` — template de dúvida
- `.github/ISSUE_TEMPLATE/problema_pr.md` — template de problema em PR
- `.gitignore` — Python, Jupyter, datasets comprimidos, credenciais
- `aulas/semana_02/html/` — slides de Git e GitHub
- `alunos/TEMPLATE_README.md` — modelo de portfólio para alunos
- Pastas iniciais dos 30 alunos colaboradores
- `datasets/README.md` — diretrizes para datasets compartilhados
- `projetos/README.md` — galeria de projetos finais
