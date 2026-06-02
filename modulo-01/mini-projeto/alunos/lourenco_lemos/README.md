<<<<<<< HEAD
Mini-Projeto Avaliativo - Módulo 1 - Vizualização de dados e Business Objects

1 - CONTEXTUALIZAÇÃO

Será desenvolvida uma Análise Exploratória de Dados(AED) aplicada ao varejo, para entender como transformar dados brutos em informações úteis.

Nesse projeto serão colocadas em práticas tarefas comuns no trabalho de analista de dados: identificação de problemas nos dados, tratativa desses
problemas com a biblioteca pandas e a geração de estatísticas simples e agrupamentos, para responder perguntas e levantar insights.

O objetivo educacional final desse projeto é preparar os alunos desse curso para realizar análises mais avançadas e preparar dados para a elaboração de dashboard: realizar limpeza de dados, extrair dados estatísticos e comunicar insights de forma objetiva.

=======
# Mini Projeto Avaliativo – Análise Exploratória de Dados (AED)

## Autor

Lourenço Lemos

## Objetivo do Projeto

Este projeto tem como objetivo realizar uma Análise Exploratória de Dados (AED) utilizando Python e Pandas sobre uma base de dados de varejo.

Foram aplicadas técnicas de limpeza, tratamento e análise dos dados para identificar problemas de qualidade e extrair informações relevantes para apoio à tomada de decisão.

---

## Tecnologias Utilizadas

* Python 3
* Pandas
* NumPy
* Matplotlib
* VS Code

---

## Estrutura do Projeto

```text
lourenco_lemos/
│
├── notebook/
│   └── projeto_varejo.ipynb
│   └── df_limpo.csv
│
├── python/
│   └── projeto_varejo.py
│
├── README.md
└── requirements.txt
```

---

## Etapas Desenvolvidas

### 1. Importação dos Dados

A base de dados foi carregada utilizando a biblioteca Pandas diretamente do repositório disponibilizado pela disciplina.

### 2. Análise Inicial

Foram identificados:

* Quantidade de registros;
* Quantidade de colunas;
* Tipos de dados;
* Valores nulos;
* Registros duplicados;
* Inconsistências nos dados.

### 3. Limpeza dos Dados

Foram realizadas as seguintes etapas:

* Remoção de colunas vazias;
* Tratamento de valores "#N/D";
* Preenchimento de categorias vazias com "Sem Categoria";
* Tratamento de valores nulos;
* Conversão da coluna DATA para datetime;
* Remoção de registros duplicados.

### 4. Estatísticas Descritivas

Foi realizada análise da coluna CL_FHL (Número de Filhos do Cliente), calculando:

* Média;
* Mediana;
* Moda;
* Desvio padrão;
* Valor mínimo;
* Valor máximo;
* Contagem.

### 5. Agrupamentos

Foram realizadas análises utilizando:

* groupby();
* pivot_table().

Os agrupamentos permitiram identificar padrões de comportamento dos clientes e categorias de produtos.

### 6. Visualização

Foi gerado gráfico de barras para auxiliar na interpretação dos resultados encontrados.

---

## Principais Insights

1. A análise identificou valores nulos e registros duplicados na base original.

2. Ao verificar o Identificador de Compra (CO_ID), verificamos que a base, apesar de ter mais de 800 mil linhas, registra 18471 compras únicas.

3. Através do agrupamento por gênero, foi possível identificar que a maioria dos clientes são mulheres.

4. O agrupamento por gênero permitiu identificar que as mulheres compram mais que os homens em todas as categorias.

5. O agrupamento por categoria mostrou que os alimentos são as categorias com maior volume de vendas, seguidos por produtos de higiene, e depois por produtos de limpeza.

6. Após a limpeza, a base ficou mais adequada para análises futuras e dashboards.

---

## Reflexão Teórica – ETL e Qualidade de Dados

O processo de ETL (Extract, Transform and Load) é fundamental para garantir que os dados utilizados em análises sejam confiáveis e consistentes.

Durante o desenvolvimento deste projeto foi possível observar problemas comuns encontrados em bases reais, como registros duplicados e dados preenchidos incorretamente.

A etapa de transformação e limpeza dos dados mostrou-se essencial para melhorar a qualidade das informações e evitar interpretações incorretas durante a análise.

A qualidade dos dados impacta diretamente a tomada de decisão, tornando indispensável a realização de verificações e tratamentos antes da construção de relatórios e dashboards.

---

## Como Executar o Projeto

1. Clone o repositório:

```bash
git clone <https://github.com/cfneves/turma-visualizacao-de-dados/tree/master/modulo-01/mini-projeto/alunos/lourenco_lemos>
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o notebook no VS Code ou Jupyter Notebook.

---

## Conclusão

O projeto permitiu aplicar conceitos de análise exploratória de dados, limpeza, tratamento de inconsistências e geração de estatísticas descritivas utilizando as bibliotecas pandas, numpy e matplotlib, consolidando conhecimentos fundamentais para projetos de Business Intelligence e Visualização de Dados.


>>>>>>> 5434d13a7d362b774198afbefdceeabe998d3087
