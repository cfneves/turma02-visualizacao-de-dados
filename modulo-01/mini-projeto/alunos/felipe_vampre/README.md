![Logos](./images/logos.png)
<br>

## 💻 Curso Datascience - Visualização de Dados e Business Intelligence. 
Mini Projeto Avaliativo - Módulo 1 - Semana 07

<br>
<br>

## 🏪 AED (Análise Exploratória de Dados): "Base 'Varejo'" 
Utilizando a base 'Varejo' que contém registros reais de compras
(https://www.kaggle.com/datasets/namespaiva/base-varejo/data)

<br>

### 🎯 Propósito

> O desafio propõe entregar um script em Python ou Jupyter Notebook que realize uma Análise Exploratória da base Varejo seguindo etapas claras, documentadas e reproduzíveis. Etapas obrigatórias: 
  
<br>

1. Usar pandas; outras bibliotecas são opcionais (NumPy, Matplotlib, Seaborn).
2. Carregar a base Varejo.csv com pandas e mostrar: número de registros, colunas e tipos de dados.
3. Verificar e reportar ao menos dois problemas básicos: valores nulos por coluna, duplicatas e possíveis inconsistências (ex.: datas inválidas ou categorias vazias).
4. Fazer as três etapas de limpeza mínima necessária: remover ou imputar nulos (explique a escolha), eliminar duplicatas relevantes e ajustar tipos de dados (ex.: converter coluna DATA para datetime).
5. Gerar estatísticas descritivas básicas para coluna de número de filhos do cliente (média; mediana; desvio padrão; moda; máximo; mínimo; e contagem).
6. Explorar padrões de agrupamento com pelo menos dois agrupamentos (por exemplo: gênero com mais vendas, compras), usando groupby() ou pivot_table().
7. Produzir um pequeno bloco de conclusões (3–6 tópicos) com os principais insights obtidos e possíveis problemas remanescentes na base.

<br>

### ✅ Requisitos das tarefas

> Sprints das tarefas necessários para conclusão do mini projeto.

<br>

- **Sprint 1 (Importação dos dados):** Realização da importação dos dados na plataforma Kaggle para a IDE VsCode ou Colab, onde o script  será executado.
- **Sprint 2 (Transformação de Strings, Integer e Float e Datetime):** Desenvolvimento das funções de limpeza de texto, inteiros e decimais usando métodos e expressões regulares.
- **Sprint 3 (Limpeza de Nulos e Duplicatas):** Aplicação das condicionais e funções  para identificação e substituição de valores vazios e de str para valores de data tipo datetime, na tabela de varejo. 
- **Sprint 4 (Estatística Descritiva):** Aplicação das funções estatísticas para coletar parâmetros da coluna de Número de filhos do cliente.
- **Sprint 5 (Relatório e Documentação):** Construção dos contadores do relatório final exibido no terminal, finalização do README.md com a reflexão teórica e submissão do link no AVA.
- **Sprint 6 (Versionamento):** Envio dos arquivos (script + README.md + df_limpo), via Git para o repositório da turma no GitHub.


### 📖 Documentação e Insights

 Para uma análise profunda sobre tudo que foi realizado no script, consulte a seção no final deste arquivo:

> **[📊 Visualizações e Resultados](#-visualizações-e-resultados)** 

<br>

### 🚀 Como Começar (Instalação)

> #### Pré-requisitos

* **Python:** Versão 3.12.3 ou superior.
* **Ambiente virtual .venv:** Criação do ambinte virtual e instalação das dependências.

<br>

> #### Instalação e Configuração

<br>

1. **Clone o repositório e acesse a pasta:**
```bash

git clone https://github.com/lf-vampre/sctec-datascience-mini-projeto-1-1
cd sctec-datascience-mini-projeto-1-1

```

<br>

2. **Crie e ative o ambiente virtual (venv):**
```bash

python3 -m venv .venv # ou então: python -m venv .venv

```

* Ativação (Linux/WSL/MacOS):
```bash

source .venv/bin/activate

```

* Ativação (Windows - PowerShell):
```bash

.\.venv\Scripts\Activate.ps1

```

<br>

3. **Instale as dependências:**
```bash

pip install -r requirements.txt

```

<br>

### 💻 Uso Básico

> Abra o arquivo "miniprojeto_felipevampre.ipynb" no vscode, selecione o kernel do python do ambiente .venv e rode todas as células ou uma a uma para acompanhar o pipeline de dados


<br>

### 📊 Visualizações e Resultados

> Abaixo está a descrição resumida das etapas realizadas no código:

<br>

Todo o pipeline de ETL e AED contou com verificações minusciosas para validar a integridade dos dados e integridade das regras de negócio. Após foram gerados alguns insights e gráficos com o cruzamento dos dados.

---

### Durante a transformação dos dados foram encontradas algumas inconsistências e foram necessários fazer ajustes a estrutura geral da base:

---

Existiam 4 colunas sem dado algum, provavelmente o arquivo csv continha mais separadores (;) ao final de cada linha, o que fez o interpretador carregar como colunas extras. Solução: Estas colunas foram removidas

---

Os nomes das colunas não eram legíveis, então todas as colunas foram renomeadas para fácil compreensão. Novos nomes: 'Data', 'Nota_Fiscal', 'Num_Cliente', 'Sexo', 'Estado_Civil', 'Num_Filhos', 'Classe_Economica', 'Cod_Produto', 'Cat_Produto', 'Nome_Produto'

---

Existiam 96.553 linhas "duplicadas". Antes de excluir qualquer linha, foi feita uma análise precisa para determinar se estas linhas eram erros, inconsistência, ou estrutura real da base de dados. 

Após profunda análise envolvendo a frequência que cada produto aparecia nas notas, verificação de dados estatísticos sobre as quantidades encontradas, análise detalhada de nota fiscal de exemplo e o impacto da remoção da duplicatas (que representa 11,6% da base), foi concluido que os registros repetidos são uma representação implícita de quantidade vendida de cada produto e não erro de duplicação. 

O que reforça esta tese é a ausência de uma coluna de quantidade, sendo assim, para cada produto vendido repetido é lançada uma nova linha na base. Desta forma os registros foram mantidos na base.

---

Foram corrigidos os tipos de dados. A coluna "Data" foi transformada em "datetime", as colunas categóricas transformadas em "category" e a coluna "Num_Filhos" transformada em "int8" resultando em uma otimização da base e economia de 94,19% de memória.

---

Foram verificadas inconsistência nos dados nas colunas "Sexo", "Estado_Civil", "Classe_Economica" e "Cat_Produto". Econtrada apenas nesta última coluna.

---

Na coluna "Cat_Produto" foi encontrada uma categoria "#N/D". Antes de tratar este dado foi feita uma investigação para encontrar quantos e quais produtos estavam ligados a essa categoria. 

Foi encontrado somente um produto de Cod_Produto=107. Após esta descoberta a investigação continuou para sabermos se o produto 107 aparecia em mais de uma categoria além da "#N/D" e se existia outro produto com o mesmo nome. 

Depois foi medido o impacto na inconsistência deste dado que afetavam 3650 linhas, 3228 notas distintas e 956 clientes distintos. 

Com a finalização da investigação conluiu-se que não existia informação alternativa para recuperar ou reclassificar o produto 107, então tanto a categoria como o produto nomeados com "#N/D" foram renomeados para "Não Identificado".

---

A análise de inconsistência seguiu na base de dados e foram verificados as seguintes questões: 

1. Existe o mesmo produto em multiplas categorias? 

2. Existe o mesmo Cod_Produto em multiplos produtos (Nome_Produto)? 

3. Existem produtos associados a mais de um Código? 

Somente nesse último item a resposta foi positiva, necessitando de aprofundamento na investigação.

---

Quanto a resposta anterior de que existiam produtos (Nome_Produto) com mais de um Cod_Produto, foram encontrados 108 produtos com 2 códigos e 1 produto com 4 códigos. 

Na investigação, descobriu-se que estes produtos representavam 92.4% de todos os produtos (quase toda a base). 

-> 92.4% dos produtos tem 2 códigos (quase toda a base)

-> Se fosse um erro cadastral ou problema de qualidade dos dados, esperaríamos valores menores como 5% / 10% / 15%. Se isso está ocorrendo em praticamente toda a base, não parece uma anomalia e sim uma característica do modelo de dados. 

-> A verificação anterior mostrou que o contrário não é verdadeiro, não existe Cod_Produto associado a mais de um produto, isso é mais importante para consistência cadastral. 

-> Os resultados sugerem que as ocorrências podem estar relacionadas a mudanças de codificação ou à existência de diferentes SKUs compartilhando uma mesma descrição comercial, e não necessariamente a erros cadastrais.

-> Isso sugere que a base de dados está estruturada da seguinte forma:
```
Nome_Produto (Arroz)
    ├── Cod_Produto 101 (Ex: Arroz Branco)
    └── Cod_Produto 102 (Ex: Arroz Integral)
```

-> Conclusão Final: Não é uma inconsistência.

---

Ainda na investigação de inconsistências foram cruzados os dados da Dimensão do Produto (combinação única de código, nome e categoria) vs Cod_Produto com as seguintes conclusões:

-> 229 combinações únicas de (Cod_Produto, Nome_Produto, Cat_Produto)

-> Cada Cod_Produto aparece associado a exatamente um único nome e uma única categoria

-> Em outras palavras: </br>
       * Não existem SKUs ambíguos. </br>
       * Um SKU nunca aponta para dois produtos diferentes. </br>
       * Um SKU nunca muda de categoria. </br>

-> Isso demonstra que "Cod_Produto" é provavelmente a "Primary Key" dessa base de dados (valores exclusivos (sem duplicatas) e não nulos (NOT NULL))

---

### Engenharia de Features e carga (Load) da base limpa:

---

Foram criadas 3 novas features temporais (colunas) extraindo-se o dia, o mês e o dia da semana da coluna "Data".

Colunas atualizadas da base:
['Data', 'Nota_Fiscal', 'Num_Cliente', 'Sexo', 'Estado_Civil', 'Num_Filhos', 'Classe_Economica', 'Cod_Produto', 'Cat_Produto', 'Nome_Produto', 'Dia', 'Mes', 'Dia_Semana']

---

A base da dados limpa e enriquecida das novas features foi salva do DataFrame "df_limpo" para o arquivo "Base_Varejo_limpo.csv"

---

### Engenharia de Features, carga (Load) da base limpa e Validação de regra de negócio:

---

Conforme solicitado no brief do mini projeto, foram extraidas as estatísticas da coluna "Num_Filhos", conclusão:

A mediana é o valor central, como nas estatísticas temos 50% exibido como "0" e também podemos ver na distribuição que mais de 50% dos valores está no "0", concluímos que a media é "0". Em relação as outras estatísticas, temos uma média de 1.14 filhos por cliente, desvio padrão de 1.41, moda igual a 0, variando entre o mínimo de 0 e máximo de 4, considerando 830 mil registros.

---

Outro critério do brief do mini projeto era validar a regra do identificaodr de número de compra (NF). Então foi verificado se existia alguma Nota_Fiscal atribuida a mais de um cliente e se existia alguma Nota_Fiscal com mais de uma data. Ambas as respostas foram negativas, validando a integridade dos registros.

---

### AED - Análise e insights:

---

Na primeira análise foi agrupado todas as notas fiscais únicas por cliente e depois separado em 3 grandes grupos. Observando a estatística desse agrupamento, verificou-se que o cliente com menor número de notas tinha 7 e com maior número de notas tinha 34, sendo a média 18.47. Então os grupos foram divididos entre 7 a 17 (Ocasional), 18 a 26 (Recorrente) e 27+ (Frequente).

Após foi criado o gráfico com as informações descobrindo que a grade maioria dos clientes se encontram na faixa "Recorrente".

---

Na segunda análise foram extraídas o volume de vendas (produtos) por classe econômica e exibido em um gráfico de pizza. Nesta informação podemos notar que a grande parte das vendas vem de clientes da classe B com 63.9%, ficando a classe C em segundo com 28% e a classe A com 8.2%.

---

Na terceira, quarta e quinta análises o foco foi nas sazonalidades (Utilizando as novas features criadas):

1. Por dia da semana -> Com picos de vendas na seguinte ordem: Quarta, Sexta, Domingo, Segunda, Quinta, Terça e Sábado

2. Por mês -> A análise foi plotada em um gráfico de linhas, podendo ver a variação ao longo do ano, sendo o maior volume de vendas no mês de Janeiro (1) e o menor no mês de Novembro (11)

3. Por perído do mês -> Através da coluna "Dia", extraida com dt.day da coluna "Data", foram criados 3 grupos das seguintes faixas "Dias 01 a 10", "Dias 11 a 20" e "Dias 21 a 31". Após contar a quantidade de itens vendidos por período, foi criado um gráfico de barras para interpretação e a maioria das vendas aconteceram na primeira faixa do início do mês.

---

Na sexta e última análise o objetivo era medir a volume de vendas por categoria de produtos. O resultado foi colocado em um gráfico de barras horizontais e ordenados da categoria com mais vendas para a que continha menos vendas. A ordem ficou: Alimentos, Higiene, Limpeza, Bebidas, Pet, Acessorios e Não Identificado.

---

<br>

### 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python (Pandas, Matplotlib).
* **Base de Dados:** csv.
* **Ambiente:** VS Code / WSL / venv
* **Orquestração:** Lógica celular em Jupyter Notebook.

---

<br>

### 🛠️ Histórico de Commits (git log --oneline)

c948b85 (HEAD -> main, origin/main) Criação do arquivo requirements.txt e do README_FelipeVampre_TurmaV2.md

b06d04c Atualizado o arquivo README.md

62e0c50 Finalizado o arquivo de código 'miniprojeto_felipevampre.ipynb'.

f57de1d Projeto será entregue em .ipynb ao invés de .py, migrando o código para o arquivo miniprojeto_felipevampre.ipynb

4f3ca1b Esboço inicial do main.py com pré requisitos e primeiras funções.

6a606f2 Primeiro Commit: Arquivo README.md e main.py.

