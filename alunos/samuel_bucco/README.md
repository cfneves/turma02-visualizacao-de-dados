# 📊 Projeto de Estudos em Data Science e Engenharia de Dados

Este repositório reúne os conteúdos, exercícios e projetos desenvolvidos durante meus estudos em Python, Análise de Dados, Git/GitHub e Banco de Dados.

O objetivo principal é consolidar conhecimentos práticos em:

* Python para análise de dados
* Manipulação de dados com Pandas
* Visualização de dados
* Git e GitHub
* PostgreSQL
* Estruturação de projetos
* Engenharia de dados básica
* Boas práticas de desenvolvimento

---

# 🚀 Tecnologias Utilizadas

Este projeto utiliza um ambiente virtual Python (`.venv`) para isolamento de dependências e melhor organização do desenvolvimento.

## Linguagens

* Python 3
* SQL

## Bibliotecas Python

* pandas
* numpy
* matplotlib
* seaborn
* psycopg2
* kagglehub
* python-dateutil
* re (biblioteca nativa do Python)
* datetime (biblioteca nativa do Python)
* json

## Ferramentas

* VS Code
* Git
* GitHub
* PostgreSQL
* pgAdmin
* Kaggle

---

# 📁 Estrutura do Projeto

```text
Análise de Dados/
│
├── Aulas/
│   ├── Módulo 01/
│   ├── Módulo 02/
│   ├── Módulo 03/
│   ├── Módulo 04/
│   └── ...
│
├── data/
│   ├── datasets
│   └── arquivos csv/json
│
├── .venv/
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📚 Conteúdos Estudados

## 🐍 Python

Durante os estudos foram abordados:

* Variáveis e tipos de dados
* Estruturas condicionais
* Estruturas de repetição
* Funções
* Orientação a Objetos
* Herança
* Encapsulamento
* Manipulação de datas
* Leitura e escrita de arquivos
* JSON

Exemplos desenvolvidos:

* Classe `Pessoa`
* Classe `Funcionario`
* Métodos getters e setters
* Herança utilizando `super()`

---

## 📊 Pandas e Análise de Dados

Além das análises básicas, também foram estudadas técnicas de agregação e transformação de dados utilizando tabelas dinâmicas e estruturas multidimensionais do pandas.

Principais operações trabalhadas:

* Criação e manipulação de DataFrames
* Limpeza de dados
* Filtros
* Máscaras booleanas
* `groupby()`
* `reset_index()`
* `rename()`
* `sort_values()`
* `dropna()`
* `apply()`
* `iterrows()`
* `value_counts()`
* `loc[]`
* `isin()`
* `stack()` e `unstack()`
* MultiIndex
* Operações vetorizadas
* Manipulação de datas com `.dt`
* Criação de colunas derivadas
* Exportação para JSON
* Construção de tabelas dinâmicas (pivot)

Exemplos realizados:

* Análise de admissões por ano
* Média salarial por departamento
* Tempo de casa dos colaboradores
* Distribuição de funcionários por departamento
* Filtros avançados utilizando múltiplas condições
* Identificação de lideranças por setor
* Construção de tabelas pivot com `unstack()`
* Geração de gráficos textuais
* Conversão de DataFrame para JSON
* Contagem e agregação de registros com `groupby()`

---

## 📈 Visualização de Dados

Bibliotecas estudadas:

* matplotlib
* seaborn

Tópicos praticados:

* Criação de gráficos
* Importação de datasets
* Ajustes de ambiente no VS Code
* Manipulação de datasets CSV

---

---

# 🧪 Ambiente Virtual Python

O projeto utiliza ambiente virtual para isolamento das dependências.

Estrutura utilizada:

```text
.venv/
```

Criação do ambiente virtual:

```bash
python -m venv .venv
```

Ativação no macOS/Linux:

```bash
source .venv/bin/activate
```

Geração do arquivo de dependências:

```bash
pip freeze > requirements.txt
```

O diretório `.venv/` é ignorado pelo Git através do arquivo `.gitignore`.

---

# 🌱 Git e GitHub

Conceitos praticados:

* Inicialização de repositórios
* Commit
* Push
* Pull
* Branches
* Merge
* `.gitignore`
* `requirements.txt`
* Versionamento de projetos
* Ambientes virtuais com `.venv`
* Conventional Commits
* Organização de dependências Python

Estratégias aprendidas:

* Organização de repositórios
* Fluxo com branches (`main` e `develop`)
* Integração entre VS Code e GitHub

---

# 📦 Ambientes Virtuais

Utilização de:

```bash
python -m venv .venv
```

Ativação do ambiente virtual:

## macOS/Linux

```bash
source .venv/bin/activate
```

Instalação das dependências:

```bash
pip install -r requirements.txt
```

---

# 📥 Datasets Utilizados

Datasets utilizados durante os estudos:

* Titanic
* Recursos Humanos (RH)
* Aviação civil
* Bases CSV e JSON
* Bases do Kaggle

---

# ▶️ Como Executar o Projeto

1. Clone o repositório

```bash
git clone <url-do-repositorio>
```

2. Acesse a pasta

```bash
cd nome-do-projeto
```

3. Crie e ative o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

4. Instale as dependências

```bash
pip install -r requirements.txt
```

5. Execute os scripts

```bash
python arquivo.py
```

---

# 🎯 Objetivo do Repositório

Este repositório tem finalidade educacional e serve como:

* material de apoio aos estudos
* registro da evolução técnica
* laboratório para testes e experimentos
* base para futuros projetos profissionais

---

# 📌 Próximos Passos

Planejamento futuro dos estudos:

* APIs
* Dashboards
* Machine Learning
* Power BI
* ETL
* Docker
* Deploy de aplicações
* Engenharia de Dados
* Cloud

---

# 👨‍💻 Autor

Samuel Bucco

Estudando Data Science, Engenharia de Dados e Desenvolvimento Python.
