# Mini Projeto AED - Base Varejo

# Objetivo
 
# Este projeto tem o objetivo de realizar uma Análise Exploratória de Dados, identificando problemas na qualidade dos dados, realizar limpeza e extrair insights.

# Importação das Bibliotecas

# Importar pandas 
# Biblioteca utilizada para análise e manipulação de dados. 

import pandas as pd
print("Biblioteca pandas importada com sucesso!")

# Carregamento da Base de Dados
 
# Etapa para realizar a leitura do arquivo CSV utilizando pandas.
 
# Utilizado separador ";" porque a base está estruturada nesse formato.

# Carregando o arquivo CSV

df = pd.read_csv("Base Varejo.csv", sep=";")

# Visualização inicial da Base
# 
# Nesta etapa serão exibidas as primeiras linhas do dataset, ajudando a compreender a estrutura dos dados.
# 
# Aqui também podemos ver, colunas, valores e estrutura da tabela.

df.head()

# Informações gerais da Base
 
# Nesta etapa serão analisados: números de registros, número de colunas e tipos de dados.

# Exibe informações gerais da base
# Quantidade de linhas e colunas

print(f"Número de linhas: {df.shape[0]}")
print(f"Número de colunas: {df.shape[1]}") 

print()

# Identifica nomes das colunas

print("Colunas disponíveis")
print(df.columns)

print()

# Mostra tipos dos dados

print("Tipos de dados")
print(df.dtypes)

# Identificação de colunas inválidas
 
# Durante a análise, identifiquei colunas chamadas "Unnamed", que estavam vazias.
 
# Essa colunas não tem valor analítico para o projeto, elas serão removidas antes das próximas etapas de limpeza e transformação dos dados.

# Exibe o nome de todas as colunas da base

print(" - - - - - - COLUNAS DA BASE - - - - - - ")
print(df.columns)                                   # .columns - Exibe o nome de todas as colunas da base

print()

# Verifica quantos valores nulos existem em cada coluna

print(" - - - - - - VALORES NULOS - - - - - - ")
print(df.isnull().sum())                            # .isnull() - Verifica valores nulos em cada coluna 
                                                    # .sum()    - Soma quantos valores nulos existem em cada coluna

# Remoção de colunas inválidas
 
# As colunas "Unnamed" foram removidas da base, elas estavam vazias e sem contribuição para a análise de dados.

# Remove colunas com nome de "Unnamed""Base Varejo.csv"

df = df.loc[:, ~df.columns.str.contains("Unnamed")]         # df.loc                  - Seleciona partes da tabela
                                                            # :                       - Significa todas as linhas
                                                            # df.columns              - Pega os nomes das colunas
                                                            # str.contains("Unnamed") - Verifica quais colunas possuem Unnamed no nome
                                                            # ~ - Significa negação   - Seleciona todas EXCETO as que possuem "Unnamed"
print("Colunas após limpeza: ")

print(df.columns)

# Conversão e validação da coluna DATA
 
# A coluna DATA estava em formato de str (texto). Para análises temporais corretas, nesta etapa ela será convertida para o tipo datetime.
 
# Após a conversão, será realizada validação para identificar possíveis datas inválidas ou valores ausentes.

# Conversão da coluna DATA para datetime

df["DATA"] = pd.to_datetime(
   df["DATA"],                   # df["DATA"] - Seleciona a coluna que será convertida
   format="%d/%m/%Y",            # format     - Informa que as datas estão no formato dia/mês/ano
   errors="coerce"               # errors      - Informa que, caso haja alguma data que não possa ser convertida, ela deve ser transformada em NaT (Not a Time), ou seja, um valor nulo específico para datas
)

print("Conversão realizada com sucesso")

print()
print("Primeiras linhas da coluna DATA:")
print(df["DATA"].head())

print()
print("Tipos de dados após conversão:")
print(df["DATA"].dtype)

print()
print("Valores nulos na coluna DATA após conversão:")
print(df["DATA"].isnull().sum())

# Resultado da validação
 
# A conversão da coluna DATA foi realizada com sucesso para o formate datetime.
 
# A verificação retornou 0 datas inválidas, indicando que todos os registros da coluna DATA estavam em formate válido e puderam ser convertidos corretamente.


# Verificando a qualidade dos dados
 
# Nesta etapa será verificado possíveis problemas na base, como valores nulos, duplicatas, colunas vazias e inconsistências em datas.
 
# ### Valores nulos
 
# Nesta etapa serão analisado os valores nulos para identificar possíveis problemas de preenchimento.
 
# ### Duplicatas
 
# Etapa para verificar a existência de linhas duplicadas na base de dados.


print(" - - - - - - VERIFICAÇÃO DA QUALIDADE DOS DADOS - - - - - ")

print("\nValores nulos por coluna: ")                   # \n            - Pula uma linha antes do texto.
print(df.isnull().sum())                                # .isnull()     - Verifica quais células estão vazias 
                                                        # .sum()        - Soma quantos valores vazios tem em cada coluna
print("\nQuantidade de linhas duplicadas: ")            
print(df.duplicated().sum())                            # .duplicated() - Verifica linhas repetidas
                                                        # .sum()        - Soma quantas linhas repetidas existem

# Resultado da verificação da qualidade dos dados
 
# Não foram encontrados valores nulos nas colunas principais da base, indicando que os campos estão totalmente preenchidos.
 
# Foram identificados 96.553 linhas duplicadas, com a etapa de limpeza, os registros duplicados serão removidos antes das análises exploratórias e estatísticas.
 


# Remoção de duplicatas

# Nesta etapa serão removidas linhas duplicadas da base de dados, evitando assim, comtagens repetidas e possíveis erros nos resultados da análise.

# Conta duplicatas antes da limpeza
duplicatas_antes = df.duplicated().sum()                        # .duplicated().sum() - Conta quantas linhas duplicadas existem antes de removê-las

# Remova linhas duplicadas
df = df.drop_duplicates()                                       # .drop_duplicates()  - Remove linhas duplicadas da base de dados

# Conta duplicatas após limpeza
duplicatas_depois = df.duplicated().sum()

print("Duplicatas antes da limpeza:", duplicatas_antes)

print()

print("Duplicatas depois da limpeza:", duplicatas_depois)

print()

print(f"Quantidade de linhas após limpeza: {df.shape[0]}")

# Resultado da limpeza
 
# Foram identificadas 96.553 registros duplicados na base de dados.
 
# Esses registros foram removido e após a limpeza, a base não apresentou mais registros duplicados, aumentando a confiabilidade das análises nas etapas seguintes.

# Tratamento de Categorias e Valores não informados (if/else)

# Durante a análise da base foi criada uma regra condicional utilizando if/else para verificar a existência de categorias sem classificação.

# Caso fossem encontrados registros como "#N/D", esse valores seriam substituídos por "Sem Categoria", tornando a informação mais clara para futuras análises.


# Verifica se existe a categoria "#N/D" na coluna "PR_CAT"

if "#N/D" in df["PR_CAT"].values:                                           # Verifica se existe a categoria "#N/D" na coluna "PR_CAT". .values - Pega os valores da coluna como um array e verifica se "#N/D" está presente nesse array

    # Substitui todos os registros "#N/D" por "Sem Categoria"
    df["PR_CAT"] = df["PR_CAT"].replace("#N/D", "Sem Categoria")            # Troca os valores "#N/D" por "Sem Categoria" na coluna "PR_CAT". .replace() - Substitui um valor por outro em uma série ou coluna. O primeiro argumento é o valor a ser substituído e o segundo é o valor que irá substituir.

    # Exibe mensagem informando que a substituição foi realizada
    print("Registro '#N/D' substituídos por 'Sem Categoria' com sucesso!")

else:

    # Exibe mensagem caso não existam registros "#N/D"
    print("Não foram encontrados registros '#N/D' na coluna 'PR_CAT'. Nenhuma substituição necessária.")

# Resulatdo do tratamento

# Aplicado estrutura condicional utilizando if/else para verificar a existência de registros classificados como "#N/D" na coluna PR_CAT.

# Os registros encontrados foram substituídos por "Sem categoria". Essa abordagem permite manter os registros na base sem perder informações de compra.


# Estatísticas descritivas

# Nesta etapa será calculado as estatísticas da coluna CL_FHL, considerando o padrão dos valores encontrados na base.

print(" - - - - - - ESTATÍSTICAS DA COLUNA CL_FHL - - - - - - ")

print()

# Calcula e xibe a média, mediana, desvio padrão, moda, máximo, mínimo e contagem de valores da coluna "CL_FHL"
print(f"Média: {df['CL_FHL'].mean():.2f}")

print()

print(f"Mediana: {df['CL_FHL'].median()}")

print()

print(f"Desvio Padrão: {df['CL_FHL'].std():.2f}")

print()

print(f"Moda: {df['CL_FHL'].mode()[0]}")

print()

print(f"Máximo: {df['CL_FHL'].max()}")

print()

print(f"Mínimo: {df['CL_FHL'].min()}")

print()

print(f"Contagem: {df['CL_FHL'].count()}")


# Resultado das Estatísticas descritivas

# A análise da coluna CL_FHL mostrou que:

# A média de filhos por cliente é de 1,15. 

# A maior parte dos clientes possui 0 filhos, conforme indicado pela mediana e pela moda.

# Foram encontrados clientes com até 4 filhos.

# Esses resultados indicam que a maior concentração de clientes não possui filhos, embora existam grupos menores com um ou mais filhos.

# Agrupamento por gênero
 
# Nesta etapa será anlisada a quantidade de compras realizadas por cada gênero do cliente.

# O objetivo é identificar qual grupo possui maior participação nas compras registradas na base.

# Agrupa os dados por gênero e conta a quantidade de compras.

compras_por_genero = df.groupby("CL_GENERO")["CO_ID"].count()   # .groupby("CL_GENERO") - Agrupa os dados pela coluna CL_GENERO
                                                                # ["CO_ID"]        - Seleciona a coluna CO_ID para contar as compras

print("Quantidade de compras por gênero: ")

print(compras_por_genero)


# Resultado da Análise
 
# Foi identificado que o gênero feminino apresentou a maior quantidade de compras na base analisada. Representando 432.576 compras, enquanto o gênero masculino representou 397.424 compras.
 
# Apesar da diferença não ser muito grande, os clientes do gênero feminino representam a maior participação nas compras registradas na base analisada.

# Quantidade de compras por categoria
 
# Nesta etapa será analisada a quantidade de compras por categoria de produto.

# O objetivo é identificar quais categorias aparecem com maior frequência na base.

# Agrupa por categoria de produto e conta a quantidade de compras.

compras_por_categoria = (
    df.groupby("PR_CAT")["CO_ID"]       # groupby("PR_CAT") - Agrupa os dados pela coluna PR_CAT (categoria de produto)
    .count()                            # .count()          - Conta quantas compras existem em cada categoria
    .sort_values(ascending=False)       # .sort_values()    - Ordena os resultados do maior para o menor
)

print("Quantidade de compras por categoria de produto: ")

print()

print(compras_por_categoria)

# Resultado da análise
# 
# Foi observado que a categoria "Alimentos" apresentou o maior volume de compras, com 434.767 registros. 
# 
# Em seguida aparecem as categorias "Higiene" e "Limpeza", com 155.574 e 145.754 registros, respectivamente.
# 
# As categorias "Acessórios" e "PET" apresentam menor participação comparadas às principais categorias.
# 
# Nesta etapa também foi identificada a categoria "Sem categoria", representando registros que originalmente estavam classificados como "#N/D" e foram tratados durante a etapa tratamento de categorias e valores não informados.


# Conclusões e Insights
# 
# 1. A base apresentou boa qualidade em relação aos valores nulos, não sendo encontrados campos vazios nas colunas principais após a limpeza inicial.
# 
# 2. Foram identificados 96.553 registros duplicados, que foram removidos para evitar distorções nas análises e garantir maior confiabilidade dos resultados.
# 
# 3. O gênero feminino apresentou a maior quantidade de compras registradas na base, com 432.576 transações, indicando uma participação ligeiramente superior em relação ao gênero masculino.
# 
# 4. A categoria ALIMENTOS foi a mais frequente na base, representando o maior volume de compras entre todas as categorias analisadas.
# 
# 5. Também foi identificada a categoria "Sem Categoria", representando registros que originalmente estavam classificados como "#N/D" e foram tratados durante a etapa de limpeza dos dados.
# 
# 6. A análise exploratória permitiu compreender melhor a estrutura da base, identificar problemas de qualidade dos dados e gerar informações úteis para futuras análises de negócio.