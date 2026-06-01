# Mini Projeto AED - Base Varejo 

MÓDULO 1: VISUALIZAÇÃO DE DADOS E BUSINESS INTELLIGENCE [T2]
MINI-PROJETO AVALIATIVO
ALUNA: Zaira Nanci Zatelli Wendt

## Objetivo

Este projeto tem como objetivo realizar uma Análise Exploratória de Dados (AED) utilizando uma base de dados de varejo.

Disponível em: https://www.kaggle.com/datasets/namespaiva/base-varejo/data 

Durante o desenvolvimento foram realizadas etapas de inspeção, limpeza, tratamento de dados e extração de insights, utilizando a biblioteca pandas.

## Etapas Realizadas

### 1. Carregamento da Base

Foi realizada a leitura do arquivo Base Varejo.csv utilizando a biblioteca pandas.

### 2. Inspeção Inicial

Foram analisados:

* Quantidade de linhas e colunas;
* Nomes das colunas;
* Tipos de dados.

### 3. Verificação da Qualidade dos Dados

Foram identificados:

* Valores nulos por coluna;
* Registros duplicados;
* Possíveis inconsistências na estrutura da base.

### 4. Limpeza dos Dados

Foram removidas as colunas vazias:

* Unnamed: 10
* Unnamed: 11
* Unnamed: 12
* Unnamed: 13

Também foram removidos 96.553 registros duplicados.

### 5. Conversão de Datas

A coluna DATA foi convertida para o formato datetime, permitindo análises temporais futuras.

### 6. Tratamento Condicional

Foi utilizada uma estrutura if/else para identificar registros classificados como "#N/D" na coluna PR_CAT.

Os registros encontrados foram substituídos por "Sem Categoria".

### 7. Estatísticas Descritivas

Foram calculadas as seguintes métricas da coluna CL_FHL:

* Média
* Mediana
* Desvio padrão
* Moda
* Máximo
* Mínimo
* Contagem

### 8. Agrupamentos

Foram realizadas análises utilizando groupby():

* Quantidade de compras por gênero;
* Quantidade de compras por categoria de produto.

## Principais Insights

* Não foram encontrados valores nulos nas colunas principais da base.
* Foram identificados e removidos 96.553 registros duplicados.
* O gênero feminino apresentou a maior quantidade de compras.
* A categoria ALIMENTOS foi a mais frequente na base.
* Registros classificados como "#N/D" foram tratados como "Sem Categoria".
* Após a limpeza, a base ficou com 733.447 registros válidos para análise.

## Ferramentas Utilizadas

* Python
* Pandas
* VS Code
* Jupyter Notebook

## Observação sobre a Base de Dados

O arquivo **Base Varejo.csv** não foi incluído neste repositório devido ao seu tamanho elevado.

Para executar o projeto, é necessário possuir o arquivo original da base de dados e salvá-lo na mesma pasta do script Python (`miniprojeto_varejo.py`).

## Estrutura do Projeto

* miniprojeto_varejo.py → Código-fonte do projeto.
* projeto_varejo.ipynb → Notebook utilizado durante o desenvolvimento.
* README.md → Documentação do projeto.
* README_Zaira_T2.md → Instruções de execução.