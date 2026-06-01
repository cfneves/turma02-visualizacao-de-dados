# PROJETO AVALIATIVO - VENDAS

Este projeto tem como objetivo realizar uma Análise Exploratória em uma base de dados varejo e retirar alguns insights dela.

## BASE DE DADOS

https://www.kaggle.com/datasets/namespaiva/base-varejo?resource=download


## ANÁLISE EXPLORATÓRIA


A base foi carregada utilizando pandas com separador ";" e encoding "latin1".


### INSPEÇÃO INICIAL


Foi feita uma análise com df.head() buscando:

- Colunas vazias
- Estrutura geral
- Possíveis problemas com os dados

Foi identificado que existiam colunas em branco geradas automaticamente.


### LIMPEZA DOS DADOS


Realizadas as etapas

- Remoção de colunas vazias
- Remoção de registros duplicados

### TRATAMENTO DE DATAS

Convertida a coluna de Data para Datetime:

## RESULTADOS

### ANÁLISE DESCRITIVA DA COLUNA FILHOS (CL_FHL)

- Média: 1.14 filhos
- Mínimo: 0
- Máximo: 4
- Mediana: 0

### ANÁLISE DE CLIENTES


COMPRAS POR GÊNERO:
- Feminino: 382.427
- Masculino: 351.020


COMPRAS POR SEGMENTO:
- Segmento B: 468.505
- Segmento C: 205.265
- Segmento A: 59.677


### ANÁLISE SOBRE PRODUTOS


COMPRAS POR CATEGORIA:

- Alimentos: 384.197
- Higiene: 137.702
- Limpeza: 128.632
- Bebidas: 38.264
- Pet: 28.553
- Acessórios: 12.871
- #N/D: 3.228

