# Análise Exploratória de Dados no Varejo (AED)

## Sobre o projeto

Neste projeto realizei uma Análise Exploratória de Dados (AED) utilizando Python, Pandas e Matplotlib com o objetivo de transformar dados brutos de transações de um supermercado em informações úteis para apoiar a tomada de decisão.

O trabalho envolveu desde a limpeza e preparação dos dados até a geração de indicadores, análises visuais e insights de negócio.

---

## Tecnologias utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

---

## Etapas do projeto

### 1. Limpeza e preparação dos dados

Antes de qualquer análise, foi necessário tratar a base de dados para garantir a qualidade das informações.

As principais atividades realizadas foram:

* Identificação e remoção de registros duplicados;
* Tratamento de valores ausentes;
* Conversão de tipos de dados;
* Padronização de colunas;
* Conversão de datas para o formato `datetime`;
* Validação da consistência dos dados.

Durante essa etapa, um dos desafios encontrados foi a presença de valores ausentes representados pela string `#N/D`, que não eram identificados automaticamente como nulos pelo Pandas. Isso exigiu uma investigação adicional para garantir a confiabilidade das análises.

---

## Principais descobertas

### Perfil dos clientes

A maior parte das transações foi realizada por clientes sem filhos, representando a parcela mais significativa do volume de compras da base analisada.

Esse resultado sugere que o público predominante da rede possui perfil familiar reduzido, o que pode influenciar estratégias de marketing e mix de produtos.

---

### Segmentação de clientes

A análise por segmento mostrou que o Segmento B é o principal responsável pelo volume de vendas da empresa.

Também foi identificado um comportamento interessante na Classe C, onde o volume de compras realizado por mulheres supera significativamente o dos homens, diferentemente do observado nos demais segmentos.

---

### Produtos e categorias

A categoria de Alimentos lidera com folga em quantidade de vendas, confirmando seu papel central no negócio.

Por outro lado, ao analisar a representatividade financeira dos produtos, categorias de nicho relacionadas ao mercado PET e infantil apresentaram destaque, indicando oportunidades para estratégias de venda cruzada e aumento de ticket médio.

---

### Sazonalidade das vendas

A análise temporal revelou comportamentos importantes ao longo do ano.

Os meses de janeiro e maio apresentaram os maiores volumes de transações, enquanto novembro registrou uma queda significativa na atividade comercial.

Esse padrão pode servir como apoio para planejamento de campanhas promocionais, ações de marketing e gestão de estoque.

---

## Visualização dos dados

Para facilitar a interpretação dos resultados, foram desenvolvidos gráficos e dashboards utilizando Matplotlib.

As visualizações foram construídas priorizando clareza e comunicação dos indicadores, utilizando percentuais de representatividade e comparações visuais que facilitam a análise por parte dos gestores.

---

## Aprendizados

Além do uso de ferramentas de análise de dados, este projeto reforçou a importância da etapa de preparação dos dados.

Grande parte do trabalho de um analista está relacionada à qualidade da informação. Pequenos problemas na base podem gerar conclusões equivocadas e impactar diretamente a tomada de decisão.

O projeto também permitiu aprofundar conhecimentos em:

* Limpeza de dados;
* Manipulação de DataFrames;
* Agrupamentos com `groupby`;
* Tabelas dinâmicas com `pivot_table`;
* Junções com `merge`;
* Visualização de dados com Matplotlib;
* Geração de insights de negócio.

---

## Conclusão

A análise demonstrou como dados operacionais podem ser transformados em informações estratégicas capazes de apoiar decisões comerciais, de marketing e de gestão.

Mais do que produzir gráficos, o objetivo foi entender o comportamento dos clientes, identificar padrões de consumo e encontrar oportunidades de melhoria para o negócio.

---

Projeto desenvolvido no módulo de Visualização de Dados e Business Intelligence do programa SCTECH + SENAI.
