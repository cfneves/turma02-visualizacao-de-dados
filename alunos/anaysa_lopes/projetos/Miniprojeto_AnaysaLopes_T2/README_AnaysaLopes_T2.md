# Mini-Projeto Avaliativo: Análise Exploratória de Dados no Varejo
**Módulo 1 - Semana 07**  
**Aluna:** Anaysa Pereira Lopes  
**Turma:** T2 - Visualização de Dados e Business Intelligence

---

## 1. Descrição do Projeto
Este projeto consiste em uma Análise Exploratória de Dados (AED) aplicada a um conjunto de dados de varejo. O objetivo principal é transformar dados brutos em informações úteis, identificar padrões, tendências e insights que possam auxiliar na tomada de decisões estratégicas. O trabalho abrange desde a verificação da qualidade dos dados e sua limpeza até a geração de estatísticas descritivas e a exploração de padrões de agrupamento, culminando na preparação de uma base de dados purificada para análises mais avançadas ou para alimentar dashboards de Business Intelligence.

---

## 2. Estrutura do Projeto
A estrutura de diretórios do projeto foi organizada para facilitar a compreensão, a execução e a manutenção, seguindo as boas práticas de projetos de ciência de dados:

```text
Miniprojeto_AnaysaLopes_T2/
├── data/
│   ├── processed/
│   │   ├── .gitkeep                 <--- Garante a existência da pasta no repositório
│   │   └── base_varejo_limpa.csv    <--- Gerado automaticamente pelo script (oculto no Git)
│   └── raw/
│       ├── .gitkeep                 <--- Garante a existência da pasta no repositório
│       └── base_varejo.csv          <--- Deve ser inserido manualmente para teste (oculto no Git)
├── src/
│   └── miniprojeto_anaysa_lopes.py  <--- Script principal de automação
├── .gitignore                       <--- Bloqueio de segurança para os arquivos .csv
└── README_AnaysaLopes_T2.md         <--- Documentação do projeto
```

* **Miniprojeto_AnaysaLopes_T2/**: Diretório raiz do projeto.
* **data/**: Contém os dados utilizados no projeto.
* **raw/**: Armazena o conjunto de dados original (base_varejo.csv) sem modificações.
* **processed/**: Armazena o conjunto de dados após as etapas de limpeza e tratamento (base_varejo_limpa.csv).
* **src/**: Contém o código-fonte do projeto.
* **miniprojeto_anaysa_lopes.py**: O script principal em Python que realiza a AED.

---

## 3. Requisitos e Dependências

Para executar este projeto, você precisará ter o Python instalado, juntamente com as seguintes bibliotecas:

* **pandas**: Para manipulação e análise de dados.
* **matplotlib**: Para visualização de dados.

Você pode instalar essas dependências usando pip:

```bash
pip install pandas matplotlib
```

---

## 4. Como Executar o Projeto (Requisitos Técnicos Mínimos)

1. **Clone o repositório** (se aplicável, caso esteja no GitHub):

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd Miniprojeto_AnaysaLopes_T2
```

2. **Base de Dados:** Certifique-se de que o arquivo de dados brutos (`base_varejo.csv`) esteja na pasta `data/raw/`. Você pode obtê-lo no Kaggle.
3. Execute o script Python:
   * No VS Code: Abra o diretório principal do repositório no VS Code, navegue até a pasta projetos/Miniprojeto_AnaysaLopes_T2 e execute o arquivo src/miniprojeto_anaysa_lopes.py diretamente. O script imprimirá os resultados no terminal.
   * No Google Colab: Faça upload do arquivo miniprojeto_anaysa_lopes.py e reproduza a estrutura de pastas data/raw/base_varejo.csv no ambiente do Colab. Adapte o caminho do arquivo de dados, se necessário, e execute as células.
   * Via terminal: Navegue até a pasta raiz do mini-projeto e execute:

```bash
python src/miniprojeto_anaysa_lopes.py
```

O script gerará o arquivo `base_varejo_limpa.csv` na pasta `data/processed/` e exibirá os resultados da análise no console, incluindo gráficos.

---

## 5. Resultados, Insights Principais
Após a execução do script de Análise Exploratória de Dados, os seguintes insights e resultados analíticos foram consolidados:

* **Limpeza de Dados Eficaz:** A base de dados foi purificada com sucesso, resultando na remoção de todas as compras duplicadas de registros redundantes e na correção de falhas de dados na coluna de categoria de produtos (`PR_CAT`) por meio de substituição condicional pelo rótulo descritivo 'Sem Categoria'. Isso garante a integridade e a confiabilidade dos dados para análises futuras.
* **Perfil Familiar dos Clientes:** A análise descritiva abrangente da coluna Número de filhos do cliente (`CL_FHL`) revelou que a maioria dos clientes possui entre zero e um filho, conforme apontado pelas métricas estáveis de moda e média. Este dado sugere um público-alvo predominantemente composto por indivíduos ou famílias pequenas, direcionando ações de marketing específicas.
* **Engajamento por Gênero:** O agrupamento das transações por gênero isolou o volume de compras únicas por meio do método de contagem distinta (`nunique()`) na coluna `CO_ID`, identificando com precisão o grupo demográfico com maior engajamento comercial.
* **Evolução Temporal das Vendas:** A análise da evolução temporal do volume de itens vendidos por ano indicou quais períodos registraram picos de processamento operacional. Essa informação é crucial para entender sazonalidades, comportamentos históricos e planejar estoques futuros.
* **Segmentação de Mercado:** O cruzamento de segmento econômico por gênero, através de uma tabela dinâmica (`pivot_table()`), expôs visualmente a distribuição demográfica e revelou de forma exata onde se concentram as maiores forças e subcategorias de consumo.

---

## 6. Reflexão Teórica: ETL e Qualidade de Dados 
O processo de Análise Exploratória de Dados (AED) é intrinsecamente ligado aos conceitos de ETL (Extract, Transform, Load) e à importância da qualidade dos dados. No contexto deste mini-projeto, as etapas de ETL foram aplicadas da seguinte forma:

* **Extract (Extração):** A leitura do arquivo `base_varejo.csv` utilizando `pandas.read_csv()` representa a fase de extração. É fundamental que esta etapa seja robusta, capaz de lidar com diferentes formatos de arquivo e encodings, como demonstrado pelo uso de `sep=";"` e `encoding="utf-8-sig"` para sanar as distorções comuns geradas pelo Excel.
* **Transform (Transformação):** Esta é a fase mais extensa do projeto, englobando diversas operações para adequar os dados aos requisitos de análise. Inclui a padronização de strings (`.str.strip()`, `.str.upper()`), a conversão de tipos de dados (numéricos e datas com `pd.to_numeric()` e `pd.to_datetime()`), a remoção de colunas vazias e, crucialmente, o tratamento de valores ausentes e duplicadas. A imputação de nulos com a moda para variáveis categóricas e a mediana para variáveis numéricas (escolha justificada para evitar distorções por valores extremos), bem como a remoção de duplicatas, são exemplos diretos da fase de transformação, visando melhorar a qualidade e a consistência dos dados.
* **Load (Carregamento):** O salvamento do DataFrame limpo (`df_limpo`) para um novo arquivo CSV (`base_varejo_limpa.csv`) na pasta `data/processed` constitui a fase de carregamento. Este passo garante que os dados transformados e purificados estejam disponíveis para futuras análises ou para serem carregados em sistemas de Business Intelligence ou bancos de dados.

A **Qualidade dos Dados** é um pilar fundamental em qualquer projeto de análise. Dados de baixa qualidade podem levar a insights incorretos e decisões de negócio falhas. Neste projeto, a atenção à qualidade dos dados foi demonstrada através de:
* **Verificação Inicial:** A auditoria de valores nulos e duplicatas antes do tratamento é essencial para diagnosticar a saúde inicial dos dados.
* **Tratamento Sistemático:** A aplicação de técnicas de limpeza, como a remoção de duplicatas e a imputação de nulos, visa corrigir inconsistências e preencher lacunas, elevando a qualidade do conjunto de dados.
* **Padronização:** A padronização de strings e a conversão correta de tipos de dados garantem que as informações sejam interpretadas de forma consistente e precisa pelas ferramentas de análise.
* **Validação Pós-Limpeza:** A auditoria final, verificando a ausência de duplicatas e nulos residuais, confirma o sucesso das operações de limpeza e a alta qualidade dos dados resultantes. Compreender o que cada etapa de limpeza resolve, como enfatizado pelo professor, é crucial para garantir que as decisões de tratamento sejam tecnicamente justificadas e não apenas uma aplicação mecânica de funções.

Em suma, este mini-projeto não apenas demonstra a aplicação prática de técnicas de AED, mas também reforça a importância crítica de um processo ETL bem executado e da manutenção de alta qualidade dos dados para a obtenção de insights confiáveis e acionáveis.
