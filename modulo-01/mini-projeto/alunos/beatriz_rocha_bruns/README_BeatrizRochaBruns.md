# Mini-Projeto: Análise Exploratória de Dados (AED) - Varejo 🛒

**Autor(a):** Beatriz Rocha Bruns
**Curso:** Visualização de Dados e Business Intelligence [T2]  
**Módulo:** 1 - Semana 07

---

## 📌 Contextualização do Projeto

Este projeto tem como objetivo realizar uma **Análise Exploratória de Dados (AED)** aplicada a uma base real de varejo. A base contém informações detalhadas sobre compras, incluindo dados de clientes, produtos, categorias e datas. 

O intuito principal é aplicar os conhecimentos adquiridos em sala de aula para transformar dados brutos em informações úteis, preparando a base para análises mais avançadas ou para a construção de dashboards no futuro.

---

## 🛠️ Ferramentas Utilizadas

* **Linguagem:** Python
* **Ambiente:** Jupyter Notebook / VS Code
* **Bibliotecas Principais:** `pandas` e `datetime`
* **Controle de Versão:** Git e GitHub

---

## 📋 Etapas Realizadas (Metodologia)

De acordo com os requisitos e critérios de avaliação do projeto, as seguintes tarefas foram executadas no script principal:

1. **Leitura e Organização dos Dados:** * Importação do arquivo `.csv` mapeando corretamente o separador de ponto-e-vírgula (`;`).
2. **Identificação de Inconsistências:** * Verificação dos tipos de dados, contagem de valores nulos e busca por registros duplicados.
3. **Limpeza e Tratamento:**
   * Remoção de linhas duplicadas.
   * Preenchimento de valores nulos nas dimensões físicas e de produto, adotando o padrão **"Sem Categoria"**.
   * Remoção de registros onde o Identificador de Compra (`CO_ID`) era nulo e padronização dessa coluna.
   * Conversão assertiva da string de `DATA` para o formato de data utilizando o módulo `datetime`.
4. **Estatísticas Descritivas:**
   * Geração de estatísticas básicas, com foco especial na coluna de *Número de Filhos dos Clientes* (`CL_FHL`).
5. **Agrupamentos e Padrões (Insights Básicos):**
   * Aplicação de funções do Pandas para responder a perguntas operacionais de negócio, utilizando pelo menos duas combinações de agrupamento (ex: Categorias mais vendidas, Perfil de clientes e Volume de vendas ao longo do tempo).

---

## 🚀 Como executar este projeto

1. Clone o repositório principal da turma.
2. Certifique-se de ter o Python e a biblioteca Pandas instalados em seu ambiente.
3. Abra o arquivo `.py` com o nome do projeto.
4. Execute as células sequencialmente. *Nota: O script utiliza um caminho relativo ('../../../base_do_projeto/Base Varejo.csv') para poupar espaço de armazenamento local, acessando diretamente a base geral da turma.*

---

## 🧠 Reflexão Teórica sobre ETL e Qualidade dos Dados

O processo de ETL (Extract, Transform and Load) é uma etapa fundamental em projetos de Business Intelligence e Análise de Dados. Durante este mini-projeto, foi possível aplicar conceitos práticos de extração dos dados a partir de um arquivo CSV, transformação por meio da identificação e correção de inconsistências e, por fim, preparação da base para futuras análises e visualizações.

A qualidade dos dados impacta diretamente na confiabilidade das informações geradas. Registros duplicados, valores ausentes, categorias inconsistentes e tipos de dados incorretos podem comprometer análises e levar a interpretações equivocadas. Por esse motivo, foram realizadas etapas de limpeza, tratamento de valores nulos, remoção de duplicidades e conversão adequada da coluna de datas.

A experiência demonstrou que uma base de dados bem estruturada é essencial para produzir indicadores confiáveis, apoiar a tomada de decisões e servir como fonte para dashboards e análises mais avançadas.

---

## 📊 Principais Insights Obtidos

* A categoria **ALIMENTOS** apresentou o maior volume de vendas, com 384.197 registros, destacando-se em relação às demais categorias.

* O segmento **B** concentrou a maior quantidade de compras únicas, sendo o principal perfil de clientes analisado.

* Clientes do gênero feminino do segmento **B** registraram a maior quantidade de compras únicas (5.946), seguidos pelos clientes masculinos do mesmo segmento (5.897).

* A análise da quantidade de filhos dos clientes mostrou média de aproximadamente **1,15 filho por cliente**, porém a mediana foi **0**, indicando que grande parte dos clientes não possui filhos.

* Durante a etapa de preparação dos dados foram identificados e removidos 96.553 registros duplicados e quatro colunas totalmente vazias, contribuindo para a melhoria da qualidade da base analisada.
