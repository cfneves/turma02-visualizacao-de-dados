# README.md

# Mini Projeto Avaliativo – Análise Exploratória de Dados (AED)

## Autor

Leo Gobel

## Turma

T2 – Visualização de Dados e Business Intelligence

## Objetivo do Projeto

O objetivo deste projeto foi realizar uma Análise Exploratória de Dados (AED) utilizando a base de varejo disponibilizada para a atividade avaliativa. Foram aplicadas técnicas de limpeza, tratamento e análise dos dados utilizando a biblioteca Pandas, com o propósito de transformar dados brutos em informações úteis para tomada de decisão.

Foram exibidos:

* Quantidade de registros
* Quantidade de colunas
* Nomes das colunas
* Tipos de dados

### 2. Verificação da Qualidade dos Dados

Foram analisados:

* Valores nulos por coluna
* Registros duplicados
* Categorias vazias
* Categorias com valor "#N/D"

### 3. Limpeza dos Dados

As seguintes ações foram realizadas:

* Remoção de colunas totalmente vazias
* Tratamento de categorias nulas utilizando `fillna()`
* Remoção de registros duplicados
* Conversão da coluna DATA para formato datetime utilizando `pd.to_datetime()`

### 4. Estatística Descritiva

Foi realizada uma análise estatística da coluna referente ao número de filhos dos clientes, contemplando:

* Média
* Mediana
* Moda
* Desvio padrão
* Valor mínimo
* Valor máximo
* Contagem

### 5. Agrupamentos e Padrões

Foram utilizados os métodos:

* `groupby()`
* `pivot_table()`

Para identificar padrões de comportamento dos clientes e categorias de produtos.

## Reflexão Sobre ETL

O processo de ETL (Extract, Transform and Load) é fundamental em projetos de dados.

A etapa de Extração consiste na obtenção dos dados a partir da fonte original. Neste projeto, a extração foi realizada por meio da leitura do arquivo CSV.

A etapa de Transformação envolve a limpeza e preparação dos dados para análise. Foram removidas colunas sem utilidade, tratados registros duplicados e ajustados os tipos de dados para garantir consistência nas análises.

Por fim, a etapa de Carga representa a disponibilização dos dados tratados para análises, relatórios ou dashboards. Embora este projeto não tenha utilizado banco de dados, a base final ficou preparada para alimentar ferramentas de Business Intelligence.

## Reflexão Sobre Qualidade dos Dados

A qualidade dos dados influencia diretamente a confiabilidade dos resultados obtidos.

Durante a análise foram identificados problemas como registros duplicados, colunas completamente vazias e categorias inconsistentes. Caso esses problemas não fossem tratados, poderiam gerar interpretações incorretas e comprometer a tomada de decisão.

Por esse motivo, a etapa de limpeza e validação dos dados é indispensável em qualquer projeto de análise de dados.

## Principais Insights Obtidos

1. Foram identificados 96.553 registros duplicados, representando aproximadamente 11,63% da base original.

2. Quatro colunas apresentavam 100% dos valores nulos e foram removidas da análise.

3. A categoria ALIMENTOS foi a mais representativa da base, registrando 384.197 compras.

4. Clientes do gênero feminino realizaram mais compras do que clientes do gênero masculino.

5. A maior parte dos clientes possui poucos ou nenhum filho, conforme demonstrado pela mediana e moda iguais a zero.

6. A existência da categoria "#N/D" indica possíveis inconsistências cadastrais que podem ser tratadas em futuras etapas de qualidade de dados.

## Conclusão

O projeto permitiu aplicar conceitos fundamentais de análise exploratória de dados, tratamento de informações e identificação de padrões utilizando Python e Pandas.

Além de atender aos requisitos técnicos propostos, a atividade demonstrou a importância da qualidade dos dados e da utilização de técnicas de limpeza para gerar informações confiáveis e relevantes para o negócio.
