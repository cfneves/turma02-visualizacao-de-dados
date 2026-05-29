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