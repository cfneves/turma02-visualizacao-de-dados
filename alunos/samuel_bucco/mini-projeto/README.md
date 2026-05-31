# Mini-Projeto 01 - Analise Exploratoria de Dados no Varejo

Este projeto foi desenvolvido como parte do curso de Analise e Visualizacao de Dados, no Modulo 1 - Modelagem de Dados.

O objetivo e realizar uma Analise Exploratoria de Dados (AED) utilizando uma base de varejo, aplicando etapas de carregamento, verificacao, limpeza, tratamento e exploracao dos dados com Python e pandas.

## Base de Dados

A base utilizada é o arquivo `Base Varejo.csv`, localizado na pasta `modulo-01/base_do_projeto/Base Varejo.csv`.

Ela contem registros de compras com informacoes como:

- data da compra;
- identificacao do cliente;
- genero;
- estado civil;
- quantidade de filhos;
- segmento do cliente;
- identificacao do produto;
- categoria do produto;
- nome do produto.

## Etapas Realizadas

No notebook `mini_projeto_01.ipynb`, foram realizadas as seguintes etapas:

- carregamento da base com pandas;
- verificacao de quantidade de linhas, colunas e tipos de dados;
- identificacao de valores nulos, duplicatas e inconsistencias;
- remocao de colunas totalmente nulas;
- eliminacao de duplicatas;
- conversao da coluna `DATA` para o tipo datetime;
- tratamento da categoria inconsistente `#N/D`;
- criacao de coluna descritiva para estado civil;
- conversao de variaveis textuais para o tipo category;
- estatisticas descritivas da coluna `CL_FHL`;
- agrupamentos com `groupby`;
- analise com `pivot_table`;
- conclusoes com os principais insights encontrados.

## Principais Insights

- A categoria `ALIMENTOS` concentra a maior parte dos registros de compra.
- As categorias `HIGIENE` e `LIMPEZA` tambem aparecem com volume relevante.
- O publico feminino possui maior quantidade total de registros de compra na base.
- Apesar da diferenca em volume, a distribuicao por categoria e parecida entre os generos.
- A coluna `CL_FHL` indica concentracao de clientes com poucos ou nenhum filho.
- A base possui produtos sem categoria definida, tratados como `SEM CATEGORIA`.

## Tecnologias Utilizadas

- Python
- pandas
- Jupyter Notebook
- VS Code

## Arquivos do Projeto

```text
mini-projeto/
├── README.md
├── README_samuelBucco_AEVDT2.md
├── mini_projeto_01.ipynb
└── data/
    ├── Base Varejo.csv
    └── Projeto III - Anlise Exploratria de Dados Utilizando o Python ou RStudio.pdf
```

