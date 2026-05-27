# Projeto de Estudos - Análise e Visualização de Dados

Este diretório reúne os notebooks, exercícios, bases e projetos desenvolvidos durante o curso de **Análise e Visualização de Dados**, dentro do módulo **Modelagem de Dados**.

O objetivo deste material é consolidar, de forma prática, os principais conceitos estudados até o momento: lógica de programação com Python, manipulação de dados com pandas, leitura e exportação de arquivos, análise exploratória, visualização de dados, NumPy, Git/GitHub e organização de projetos.

---

## Objetivos de Aprendizagem

- Praticar lógica de programação aplicada à análise de dados.
- Manipular bases tabulares com Python e pandas.
- Ler, tratar, transformar e exportar arquivos em diferentes formatos.
- Criar análises com filtros, agrupamentos, tabelas dinâmicas e métricas.
- Construir visualizações com matplotlib e seaborn.
- Utilizar NumPy para operações vetorizadas e cálculos eficientes.
- Organizar projetos com notebooks, bases, READMEs e arquivos de dependências.
- Versionar os estudos com Git e GitHub.

---

## Tecnologias e Ferramentas

### Linguagens

- Python
- SQL

### Bibliotecas Python

- pandas
- numpy
- matplotlib
- seaborn
- psycopg2
- kagglehub
- requests
- python-dateutil
- json
- datetime

### Ferramentas

- VS Code
- Jupyter Notebook
- Git
- GitHub
- PostgreSQL
- pgAdmin
- Kaggle

---

## Estrutura do Diretório

```text
samuel_bucco/
├── README.md
├── requirements.txt
├── .gitignore
├── semana_04/
│   ├── base_rh.ipynb
│   ├── aula_sexta_08_05_26.ipynb
│   ├── base_rh.py
│   ├── base_rh.csv
│   ├── base_rh_dia01.csv
│   ├── base_rh.json
│   ├── base_rh.xlsx
│   ├── base_rh_por_depto.xlsx
│   └── base_rh_deptos.xlsx
├── semana_05/
│   ├── notebooks/
│   │   ├── revisao_logica_python.ipynb
│   │   ├── aula_01_professor.ipynb
│   │   ├── aula_02.ipynb
│   │   ├── aula_03.ipynb
│   │   └── aula_12_05.ipynb
│   ├── exercicios/
│   │   ├── exercicio_pratico_dia_02.ipynb
│   │   └── gabarito_exercicio_dia02.ipynb
│   └── bases/
└── mini-projeto/
    ├── README.md
    ├── README_samuelBucco_AEVDT2.md
    ├── mini_projeto_01.ipynb
    └── data/
        ├── Base Varejo.csv
        └── Projeto III - Anlise Exploratria de Dados Utilizando o Python ou RStudio.pdf
```

---

## Conteúdos Estudados

### Python e Lógica de Programação

Foram revisados os fundamentos de Python com foco em aplicações para dados:

- variáveis e tipos de dados;
- operadores aritméticos e lógicos;
- entrada de dados com `input()`;
- estruturas condicionais com `if`, `elif` e `else`;
- estruturas de repetição;
- funções;
- manipulação de datas;
- leitura e escrita de arquivos;
- uso de notebooks como ambiente de estudo e experimentação.

Notebook relacionado:

- `semana_05/notebooks/revisao_logica_python.ipynb`

---

### Pandas e Manipulação de Dados

Durante as aulas foram praticadas operações essenciais para trabalhar com bases tabulares:

- criação e manipulação de DataFrames;
- leitura de arquivos CSV com separador, encoding e decimal configurados;
- inspeção inicial com `head()`, `tail()`, `shape`, `info()` e `describe()`;
- análise de valores nulos e valores únicos;
- seleção de colunas;
- filtros com condições simples e múltiplas;
- conversão de colunas de data com `pd.to_datetime()`;
- extração de ano, mês, dia, trimestre e semana com `.dt`;
- criação de colunas derivadas;
- uso de `groupby()` para agregações;
- uso de `reset_index()`, `rename()`, `sort_values()` e `query()`;
- uso de `merge()` para cruzar tabelas;
- criação de tabelas dinâmicas com `pivot_table()`;
- exportação para CSV, JSON e Excel.

Arquivos relacionados:

- `semana_04/base_rh.ipynb`
- `semana_04/aula_sexta_08_05_26.ipynb`
- `semana_05/notebooks/aula_01_professor.ipynb`
- `semana_05/notebooks/aula_02.ipynb`
- `semana_05/exercicios/exercicio_pratico_dia_02.ipynb`

---

### Base de RH

A base `base_rh` foi utilizada para praticar análise de dados em um contexto de Recursos Humanos.

Principais análises realizadas:

- contagem de funcionários por departamento;
- média, mínimo e máximo salarial por departamento;
- distribuição de funcionários por cargo;
- análise de admissões por ano;
- cálculo de tempo de casa;
- comparação de salário médio por departamento e gênero;
- criação de tabela de metas de headcount;
- verificação de departamentos que atingiram ou não a meta;
- geração de arquivos derivados em CSV, JSON e Excel.

Arquivos relacionados:

- `semana_04/base_rh.csv`
- `semana_04/base_rh.json`
- `semana_04/base_rh.xlsx`
- `semana_04/base_rh_por_depto.xlsx`
- `semana_04/base_rh_deptos.xlsx`

---

### Visualização de Dados

Foram criados gráficos para apoiar a leitura e interpretação das análises:

- histogramas;
- gráficos de barras;
- gráficos de barras horizontais;
- gráficos de linha;
- gráficos comparativos por categoria;
- visualizações de distribuição salarial;
- visualizações de admissões por ano;
- comparação de salário médio por gênero e departamento.

Bibliotecas utilizadas:

- matplotlib
- seaborn

Arquivos relacionados:

- `semana_05/notebooks/aula_01_professor.ipynb`
- `semana_05/notebooks/aula_02.ipynb`
- `semana_05/exercicios/gabarito_exercicio_dia02.ipynb`

---

### NumPy

A introdução ao NumPy foi feita a partir da própria base de RH, conectando arrays com operações comuns de análise de dados.

Conteúdos praticados:

- criação e extração de arrays a partir de DataFrames;
- comparação entre pandas Series e arrays NumPy;
- slicing em arrays unidimensionais e bidimensionais;
- operações vetorizadas;
- funções de agregação;
- uso do parâmetro `axis`;
- criação de histogramas com bins;
- broadcasting;
- classificação vetorizada com `np.where()` e `np.select()`.

Arquivo relacionado:

- `semana_05/notebooks/aula_03.ipynb`

---

## Mini-Projeto 01 - Análise Exploratória de Dados no Varejo

O mini-projeto aplica os conceitos estudados em uma base de varejo, passando por etapas de importação, diagnóstico, limpeza, tratamento, exploração e conclusão.

Base utilizada:

- `mini-projeto/data/Base Varejo.csv`

Etapas realizadas:

- download e organização da base de dados;
- carregamento da base com pandas;
- verificação de linhas, colunas e tipos de dados;
- identificação de valores nulos, duplicatas e inconsistências;
- remoção de colunas totalmente nulas;
- eliminação de duplicatas;
- conversão da coluna `DATA` para `datetime`;
- tratamento da categoria inconsistente `#N/D`;
- criação de coluna descritiva para estado civil;
- conversão de variáveis textuais para o tipo `category`;
- estatísticas descritivas da coluna `CL_FHL`;
- análises com `groupby()`;
- criação de tabela dinâmica com `pivot_table()`;
- registro dos principais insights encontrados.

Principais insights:

- a categoria `ALIMENTOS` concentra a maior parte dos registros de compra;
- as categorias `HIGIENE` e `LIMPEZA` também apresentam volume relevante;
- o público feminino possui maior quantidade total de registros de compra na base;
- a distribuição por categoria é parecida entre os gêneros;
- a coluna `CL_FHL` indica concentração de clientes com poucos ou nenhum filho;
- produtos sem categoria definida foram tratados como `SEM CATEGORIA`.

Arquivos relacionados:

- `mini-projeto/mini_projeto_01.ipynb`
- `mini-projeto/README.md`
- `mini-projeto/README_samuelBucco_AEVDT2.md`

---

## Git, GitHub e Organização do Projeto

Também foram praticados conceitos de organização e versionamento:

- criação e uso de `.gitignore`;
- controle de dependências com `requirements.txt`;
- uso de ambiente virtual `.venv`;
- commits;
- branches;
- merge;
- push e pull;
- Conventional Commits;
- organização de pastas por semana, aula, exercício e projeto.

---

## Como Configurar o Ambiente

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente no macOS/Linux:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Para atualizar o arquivo de dependências após instalar novas bibliotecas:

```bash
pip freeze > requirements.txt
```

O diretório `.venv/` é ignorado pelo Git por meio do arquivo `.gitignore`.

---

## Como Executar os Estudos

1. Abra a pasta `samuel_bucco` no VS Code.
2. Ative o ambiente virtual.
3. Instale as dependências com `pip install -r requirements.txt`.
4. Abra o notebook desejado.
5. Execute as células em ordem, de cima para baixo.

Para o mini-projeto, abra:

```text
mini-projeto/mini_projeto_01.ipynb
```

---

## Status Atual

Até o momento, este diretório contém exercícios e projetos cobrindo:

- fundamentos de Python;
- pandas para análise de dados;
- leitura e exportação de arquivos;
- tratamento de datas;
- agrupamentos e tabelas dinâmicas;
- visualização de dados;
- NumPy;
- análise exploratória com base real de varejo;
- organização de ambiente e versionamento.
