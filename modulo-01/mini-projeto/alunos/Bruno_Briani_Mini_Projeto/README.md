# MiniProjeto: Tratamento e Análise de Dados para Dashboard de Vendas

Este repositório contém o projeto prático de análise exploratória e tratamento de dados desenvolvido para o curso de **Visualização de Dados**. O objetivo principal do script é carregar, limpar, estruturar e analisar uma base de dados de vendas no varejo para posterior alimentação de um dashboard gerencial.

---

## 📌 Objetivo do Projeto

O foco deste projeto é o pipeline de **Engenharia e Análise Exploratória de Dados (EDA)**, garantindo que inconsistências comuns em sistemas de vendas (como valores nulos mascarados, delimitadores incorretos e tipos de dados incompatíveis) sejam corrigidos antes da etapa de visualização final.

A análise concentra-se em:
- **Categorias de Produtos:** Identificação dos segmentos mais rentáveis e volumosos.
- **Perfil do Cliente:** Entendimento das características demográficas e de consumo dos compradores.
- **Higienização de Dados:** Tratamento rigoroso de strings vazias, ausências de dados (`#N/D`) e separadores de arquivos.

---

## 📊 Base de Dados

- **Origem:** Kaggle
- **Dataset:** [Base Varejo - Comportamento de Compras](https://www.kaggle.com/datasets/namespaiva/base-varejo)
- **Características:** Dados estruturados contendo informações de transações comerciais, segmentação de produtos, preços e dados demográficos de clientes.

---

## 🛠️ Tecnologias e Dependências

O projeto foi totalmente desenvolvido em **Python 3**, utilizando as seguintes bibliotecas para manipulação e visualização:

- [Pandas](https://pandas.pydata.org/) — Para leitura, indexação e tratamento das matrizes de dados e strings nulas.
- [NumPy](https://numpy.org/) — Para computação numérica e suporte a operações vetoriais.
- [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/) — Para a geração dos gráficos estatísticos e estilização visual das distribuições.

---

## 📁 Estrutura de Etapas do Código

O script principal está dividido de forma modular seguindo boas práticas de Data Science:

1. **Etapa 1: Carga e Identificação de Nulos:** Leitura do arquivo `.csv` tratando especificidades de separadores (`;`) e convertendo marcadores de texto como `#N/D` ou `ND` em nulos reais (`NaN`) nativos do Pandas.
2. **Etapa 2: Limpeza e Tipagem:** *(Espaço para descrever a remoção de duplicadas ou conversão de tipos como datas/valores se houver no seu código).*
3. **Etapa 3: Análise Exploratória:** Agrupamentos estatísticos por categorias de produtos e clientes.
4. **Etapa 4: Visualização dos Resultados:** Exportação dos gráficos gerados para suporte ao Dashboard.

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o Repositório
Navegue até a pasta do seu usuário dentro do repositório da turma:
```bash
git clone [https://github.com/brunobriani-hub/turma-visualizacao-de-dados.git](https://github.com/brunobriani-hub/turma-visualizacao-de-dados.git)
cd turma-visualizacao-de-dados/alunos/Bruno_Briani


Aluno: Bruno Briani de Paula
Turma: Visualização de Dados e Bussines Inteligence - 2026
Professor: Cláudio Neves
Data: 01/06/2026

