# Mini Projeto - Análise Exploratória de Dados Varejo

## Descrição

Projeto desenvolvido para a disciplina de Visualização de Dados e Business Intelligence.

O objetivo deste mini-projeto é realizar uma Análise Exploratória de Dados (AED) utilizando Python e Pandas, aplicando técnicas de limpeza, tratamento, organização e exploração de dados em uma base de varejo.

O projeto busca transformar dados brutos em informações úteis para análise operacional e geração de insights.

---

## Objetivos do Projeto

* Importar e explorar uma base de dados CSV
* Identificar problemas de qualidade dos dados
* Tratar valores nulos e inconsistências
* Ajustar tipos de dados
* Gerar estatísticas descritivas
* Realizar agrupamentos e análises exploratórias
* Produzir insights a partir dos dados

---

## Tecnologias Utilizadas

* Python 3
* Pandas
* VSCode
* Git
* GitHub

---

## Estrutura do Projeto

* `projeto_stefano_laurito.py`

  * Script principal contendo toda a análise exploratória.

* `base_varejo.csv`

  * Base de dados utilizada no projeto.

* `README_stefano_laurito_T2.md`

  * Documentação do projeto.

---

## Importação da Base

A leitura e extração estruturada dos dados foram realizadas utilizando a biblioteca Pandas através do método read_csv().

A base foi importada utilizando o separador ;, permitindo a correta interpretação das colunas do arquivo CSV.

Exemplo utilizado:

df = pd.read_csv("base_varejo.csv", sep=";")

O arquivo CSV foi carregado corretamente sem necessidade de ajuste manual de encoding.

---

## Problemas Identificados na Base

Durante a análise exploratória foram encontrados alguns problemas na estrutura dos dados:

* Colunas totalmente vazias (`Unnamed: 10`, `Unnamed: 11`, `Unnamed: 12` e `Unnamed: 13`)
* Registros duplicados
* Coluna `DATA` carregada inicialmente como texto (`str`)
* Categoria inválida `#N/D` na coluna `PR_CAT`

---

## Tratamentos Realizados

As seguintes etapas de limpeza e tratamento foram aplicadas:

* Remoção de colunas totalmente vazias
* Remoção de registros duplicados
* Conversão da coluna `DATA` de string para o tipo `datetime`
* Verificação de valores nulos
* Verificação da estrutura da base
* Validação da integridade da coluna `CO_ID` como identificador de compra

---

## Estatísticas Descritivas

Foram calculadas estatísticas descritivas para a coluna `CL_FHL` (número de filhos do cliente):

* Média
* Mediana
* Moda
* Desvio padrão
* Valor máximo
* Valor mínimo
* Contagem de registros

---

## Agrupamentos Realizados

Foram realizados agrupamentos utilizando `groupby()` para análise dos dados:

### Quantidade de compras por gênero

Análise da distribuição de compras entre clientes do gênero masculino e feminino.

### Quantidade de vendas por categoria

Análise das categorias de produtos com maior volume de vendas.

### Quantidade de compras por gênero e categoria

Análise combinada entre gênero dos clientes e categorias de produtos, permitindo identificar padrões de consumo mais específicos.

---

## Principais Insights

1. A categoria `ALIMENTOS` apresentou o maior volume de vendas da base, demonstrando forte relevância no varejo analisado.

2. Clientes do gênero feminino realizaram mais compras em comparação ao gênero masculino.

3. A maior parte dos clientes não possui filhos, considerando que a mediana e a moda da coluna `CL_FHL` foram iguais a 0.

4. Foram identificados mais de 96 mil registros duplicados, indicando possíveis inconsistências no processo de exportação ou integração dos dados.

5. A presença da categoria `#N/D` sugere falhas de categorização em parte dos produtos cadastrados.

6. Apesar das inconsistências encontradas, a base apresentou boa integridade geral, sem valores nulos nas principais colunas analíticas.


---

## Reflexão Teórica — ETL e Qualidade de Dados

Durante o desenvolvimento deste projeto foi possível compreender a importância do processo de ETL (Extract, Transform and Load) na análise de dados.

A etapa de extração ocorreu na importação da base CSV utilizando a biblioteca Pandas. Em seguida, foram realizadas transformações importantes para melhorar a qualidade da base, como remoção de colunas vazias, eliminação de registros duplicados e conversão de tipos de dados.

A qualidade dos dados possui impacto direto na confiabilidade das análises. Problemas como colunas inconsistentes, registros duplicados e categorias inválidas podem gerar interpretações incorretas e comprometer decisões de negócio.

A Análise Exploratória de Dados permitiu identificar padrões de consumo, verificar inconsistências e gerar informações úteis a partir de dados brutos, demonstrando a importância do tratamento adequado dos dados antes da construção de dashboards ou análises mais avançadas.

---

## Como Executar

1. Abrir o projeto no VSCode
2. Navegar até a pasta do projeto
3. Executar o arquivo Python:

```bash
python projeto_stefano_laurito.py
```

---

## Autor

Stéfano Laurito
