# Mini-Projeto — Visualização de Dados
**Aluno:** Luiz Fernando de Jesus Silva Homem

## Como Rodar o Projeto

O projeto foi desenvolvido em um Jupyter Notebook (`.ipynb`).

1. Abra o arquivo **`anlise_varejo.ipynb`** localizado nesta mesma pasta.
2. Clique em **"Run All"** (Executar Tudo) no topo do arquivo ou execute célula por célula pressionando `Shift + Enter`.

## Sprints do Projeto

### Sprint 1: Importação de Bibliotecas e Diagnóstico Inicial

* **Setup do Ambiente:**
  * `pandas`: Manipulação principal do DataFrame.
  * `re`: Biblioteca de expressões regulares reservada para limpezas textuais.

* **Primeira Impressão:**
  * Leitura do arquivo bruto `Base Varejo.csv` ajustando os parâmetros especiais.
  * O shape inicial da base revelou **830.000 linhas e 14 colunas**.
  * **Primeiro problema detectado:** Identificação de 4 colunas fantasmas no final do arquivo (`Unnamed: 10` até `13`) cheias de nulos, do início ao fim.

---

### Sprint 2: Mapeamento dos Problemas (Qualidade dos Dados)

Avaliando a base, listei os 5 problemas críticos que precisavam de correção antes de qualquer análise:

1. **Colunas Vazias:** `Unnamed: 10` a `13` com 100% de linhas nulas (precisam ser removidas).
2. **Nulos Ocultos:** O termo `#N/D` aparecendo **3.650 vezes** como texto nas colunas `PR_CAT` e `PR_NOME`, mascarando a falta de informação.
3. **Tipagem Errada:** A coluna `DATA` veio como texto (`str`), impedindo qualquer filtro cronológico.
4. **Linhas Clonadas:** **96.553 duplicatas** exatas na base, o que irá atrapalhar qualquer tipo de análise.
5. **Textos Mal Formatados:** Textos misturando maiúsculas e minúsculas de forma inconsistente (ex: `REFRIGERANTE LIMaO`).

---

### Sprint 3: Execução da Limpeza e Exportação.

* **Estratégia com `numpy`:**
  * Importei o `numpy` (`import numpy as np`) para usar o `np.nan`. Isso serviu para transformar o texto `#N/D` em nulo real na memória, permitindo que o `.fillna()` fizesse o tratamento correto para `"NÃO INFORMADO"`.

* **Limpeza no Código:**
  * **Drop das Colunas:** Passei o `.drop()` nas colunas `Unnamed` usando uma única variável (`df_limpar`) para manter o código sequencial e limpo.
  * **Conversão da Linha do Tempo:** Usei o `pd.to_datetime()` com o formato brasileiro (`%d/%m/%Y`) e travei com `errors='coerce'` para converter a coluna `DATA` para `datetime64[us]`.
  * **Extermínio de Duplicatas:** Rodei o `.drop_duplicates()` e emendei direto o `.reset_index(drop=True)` para reajustar o índice das linhas e não deixar buracos na memória.
  * **Automação do Texto (Caixa Alta):** Em vez de tratar coluna por coluna, usei a cabeça: joguei as colunas `CL_GENERO`, `CL_SEG`, `PR_CAT` e `PR_NOME` em uma lista e passei um laço `for` aplicando `.str.upper()`. Matou o problema do "LIMaO" na hora.

* **Check-out dos Dados (A Camada Prata):**
  * Salvei o progresso final direto em um novo arquivo físico: `Base_Varejo_Limpa.csv`.
  * Travei com `index=False` para não criar coluna de índice inútil, `sep=';'` para manter o padrão e `encoding='cp1252'` para blindar a acentuação. 
  * **Resultado final:** Base limpa, higienizada e consolidada com exatamente **733.447 linhas**.

### Sprint 4: Estatistica Descritiva e Padrões de Agrupamento

  * **Análise de Variaveis Quantitativas (perfil Familiar):**
    * Isolei a coluna `CL_FHL` (Número de Filhos) para extrair os dados estatísticos, para uma melhor compreensão da base.
    * O resultado apresentou uma **Contagem de 733.447 registros**, com mínimo de **0** e máxima de **4** filhos.
    * **Métricas de Tendência Central:** A **Média** fixou-se em **1.15**, enquanto a **Mediana** e a **Moda** fixaram-se em **0**, uma forte indicação de que os clientes não possuem filhos. O **Desvio Padrão** apresentou um resultado de **1.42** que indica uma distribuição normal.

  * **Exploração de Padrões com `groupby`():**
    * Apliquei agrupamentos cruzando colunas categóricas e volumetria de identificadores para responder a perguntas operacionais.
    * **Segmentação por Genêro:** O público femino (`F`) liderou o volume de compras com **`382.427` compras**, enquanto o público masculino (`M`) com **351.020 compras.**
    * **Volumetria por categoria:** A categoria **ALIMENTOS** liderou como maior volume de compras, acumulando **384.197 itens vendidos** (mais do que a soma de todas as outras categorias juntas). As categorias HIGIENE e LIMPEZA apresentaram **137.702** e **128.632** compras, respectivamente. Sendo esses o top 3 de volume de compras.

### Sprint 5: Relatório Final (ETL e Qualidade dos Dados)

* **Minhas considerações do processo de ETL:**
  * Fazer esse mini-projeto me mostrou que não da para confiar em algumas informações apresentadas pela leitura rasa do (df.info), lá no df.info() ele disse que 830.000 non-null, mas na verdade haviam 3650 #N/D na base. Ao ignorar essa etapa os valores estatísticos seriam bem diferentes dos que eu apresentei. Além de colunas fantasmas que estavam ali no meio, 100% vazias sem nenhuma utilidade. 


### Sprint 5: Conclusão e o que aprendi sobre ETL (Qualidade dos Dados)

* **O que achei do processo de ETL:**
  Fazer esse mini-projeto me mostrou na prática que não dá para confiar em base de dados bruta. Se eu jogasse os dados direto num gráfico ou relatório sem antes fazer o tratamento que fiz nas primeiras sprints, os números iam dar totalmente errados por causa daquelas quase 100 mil linhas duplicadas e das colunas fantasmas que estavam ali no meio atrapalhando tudo. É aquilo: se entra dado ruim, o resultado final sai ruim. 

  Mudar a coluna de DATA para o formato certo de data e colocar todos os textos em letras maiúsculas não é só para deixar o arquivo bonito. É isso que garante que o código não vai quebrar e que o `groupby` da Sprint 4 funcione de verdade, trazendo os números certos de compras por gênero e por categoria para o dono do negócio tomar as decisões certas com dados de confiança.