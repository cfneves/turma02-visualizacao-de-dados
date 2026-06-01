# ==================================================
# MINI PROJETO AVALIATIVO - ANÁLISE EXPLORATÓRIA DE DADOS
# Autor: Lourenço Lemos
# ==================================================
# IMPORTAÇÃO DAS BIBLIOTECAS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("Bibliotecas importadas com sucesso!")
# ==========================================================
# CARREGAMENTO DOS DADOS
# ==========================================================

print("\n===== CARREGANDO BASE =====")

# IMPORTANTE:
# O arquivo utiliza ';' como separador

arquivo = "https://raw.githubusercontent.com/cfneves/turma-visualizacao-de-dados/master/modulo-01/base_do_projeto/Base%20Varejo.csv"

try:
    df = pd.read_csv(arquivo, sep=';') # dessa forma, o pandas entende que o separador é ';' e não a vírgula padrão
    print("Base carregada com sucesso!")
except Exception as erro:
    print(f"Erro ao carregar base: {erro}")

# ==========================================================
# ANÁLISE INICIAL
# ==========================================================

print("\n===== INFORMAÇÕES GERAIS =====")

print(f"Quantidade de linhas: {df.shape[0]}")
print(f"Quantidade de colunas: {df.shape[1]}")

print("\n===== COLUNAS =====")
print(df.columns.tolist())

print("\n===== TIPOS DE DADOS =====")
print(df.dtypes)

print("\n===== PRIMEIRAS LINHAS =====")
print(df.head())
# ==========================================================
# AJUSTE DE TIPOS DE DADOS
# ==========================================================

print("\n===== AJUSTANDO TIPOS =====")

# Convertendo colunas numéricas

colunas_numericas = ['CO_ID', 'CL_ID', 'CL_EC', 'CL_FHL', 'PR_ID']

for coluna in colunas_numericas:
    if coluna in df.columns:
        df[coluna] = pd.to_numeric(df[coluna], errors='coerce') # erros de conversão se tornam NaN

print(df.dtypes)
# ==========================================================
# IDENTIFICAÇÃO DE PROBLEMAS
# ==========================================================

# usa a soma para contar a quantidade de valores nulos por coluna
print("\n===== VALORES NULOS =====")
print(df.isnull().sum()) 

# ==========================================================
# REMOÇÃO DE COLUNAS VAZIAS
# ==========================================================

#IDENTIFICAMOS QUE EXISTEM QUATRO COLUNAS COMPLETAMENTE VAZIAS, NO FIM DA BASE DE DADOS, QUE PODEMOS REMOVER SEM PERDER INFORMAÇÕES RELEVANTES.

print("\n===== REMOÇÃO DE COLUNAS VAZIAS =====")

colunas_antes = df.shape[1]

df = df.iloc[:, :-4] # seleciona todas as linhas e todas as colunas, exceto as últimas 4

colunas_depois = df.shape[1]

print(f"Colunas removidas: {colunas_antes - colunas_depois}")

# ==========================================================
# ANÁLISE APÓS REMOÇÃO DE COLUNAS VAZIAS
# ==========================================================

print("\n===== INFORMAÇÕES GERAIS =====")

print(f"Quantidade de linhas: {df.shape[0]}")
print(f"Quantidade de colunas: {df.shape[1]}")

print("\n===== COLUNAS =====")
print(df.columns.tolist())

print("\n===== TIPOS DE DADOS =====")
print(df.dtypes)

print("\n===== PRIMEIRAS LINHAS =====")
print(df.head())

# ==========================================================
# AJUSTE DE TIPOS DE DADOS
# ==========================================================

print("\n===== AJUSTANDO TIPOS =====")

# Convertendo colunas numéricas

colunas_numericas = ['CO_ID', 'CL_ID', 'CL_EC', 'CL_FHL', 'PR_ID']

for coluna in colunas_numericas:
    if coluna in df.columns:
        df[coluna] = pd.to_numeric(df[coluna], errors='coerce') # erros de conversão se tornam NaN

print(df.dtypes)

# ==========================================================
# TRATAMENTO DE DATAS
# ==========================================================

print("\n===== TRATAMENTO DE DATAS =====")

# Conversão para datetime

# usando a função pd.to_datetime com errors='coerce' para transforma datas inválidas em NaT

df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')

# Contagem de datas inválidas

datas_invalidas = df['DATA'].isnull().sum()

print(f"Datas inválidas encontradas: {datas_invalidas}")

# ==========================================================
# TRATAMENTO DE INFORMAÇÕES VAZIAS NA BASE DE DADOS
# ==========================================================

print("\n===== TRATAMENTO DE INFORMAÇÕES VAZIAS =====")

# Começando pela coluna 'PR_CAT', que representa a categoria do produto. Essa informação é importante para análises futuras, como segmentação de vendas por categoria.
# Usando o método fillna para substituir categorias vazias. Nesse caso, substituímos por 'Sem Categoria'.

if 'PR_CAT' in df.columns:

    categorias_vazias_antes = df['PR_CAT'].isnull().sum()

    print(f"Categorias vazias antes: {categorias_vazias_antes}")

    df['PR_CAT'] = df['PR_CAT'].fillna('Sem Categoria')

    categorias_vazias_depois = df['PR_CAT'].isnull().sum()

    print(f"Categorias vazias depois: {categorias_vazias_depois}")

#Não farei substituição de valores vazios para as colunas CO_ID, CL_ID, PR_ID, PR_NOME, CL_GENERO, CL_EC e CL_SEG pois são identificadores únicos e não faz sentido criar um valor genérico para eles.

if 'CO_ID' in df.columns:

    co_id_vazios = df['CO_ID'].isnull().sum()

    print(f"Identificação da Compra vazios: {co_id_vazios}")

    df = df.dropna(subset=['CO_ID']) # removendo linhas com CO_ID vazio
    print(f"Linhas removidas com Identificação da Compra vazio: {co_id_vazios}")

if 'CL_ID' in df.columns:

    cl_id_vazios = df['CL_ID'].isnull().sum()

    print(f"Identificação do Cliente vazios: {cl_id_vazios}")

    df = df.dropna(subset=['CL_ID']) # removendo linhas com CL_ID vazio
    print(f"Linhas removidas com Identificação do Cliente vazio: {cl_id_vazios}")

if 'PR_ID' in df.columns:

    pr_id_vazios = df['PR_ID'].isnull().sum()

    print(f"Identificação do Produto vazios: {pr_id_vazios}")

    df = df.dropna(subset=['PR_ID']) # removendo linhas com PR_ID vazio
    print(f"Linhas removidas com Identificação do Produto vazio: {pr_id_vazios}")

if 'PR_NOME' in df.columns:

    pr_nome_vazios = df['PR_NOME'].isnull().sum()

    print(f"Nome do Produto vazios: {pr_nome_vazios}")

    df = df.dropna(subset=['PR_NOME']) # removendo linhas com PR_NOME vazio
    print(f"Linhas removidas com Nome do Produto vazio: {pr_nome_vazios}")

if 'CL_GENERO' in df.columns:

    cl_genero_vazios = df['CL_GENERO'].isnull().sum()

    print(f"Gênero do Cliente vazios: {cl_genero_vazios}")

    df = df.dropna(subset=['CL_GENERO']) # removendo linhas com CL_GENERO vazio
    print(f"Linhas removidas com Gênero do Cliente vazio: {cl_genero_vazios}")

if 'CL_EC' in df.columns:

    cl_ec_vazios = df['CL_EC'].isnull().sum()

    print(f"Estado Civil do Cliente vazios: {cl_ec_vazios}")

    df = df.dropna(subset=['CL_EC']) # removendo linhas com CL_EC vazio
    print(f"Linhas removidas com Estado Civil do Cliente vazio: {cl_ec_vazios}")

if 'CL_SEG' in df.columns:

    cl_seg_vazios = df['CL_SEG'].isnull().sum()

    print(f"Segmento do Cliente vazios: {cl_seg_vazios}")

    df = df.dropna(subset=['CL_SEG']) # removendo linhas com CL_SEG vazio
    print(f"Linhas removidas com Segmento do Cliente vazio: {cl_seg_vazios}")

# Para a coluna 'CL_FHL'
# Utilizando mediana para evitar distorções na distribuição dos dados, já que a quantidade de filhos pode variar bastante entre os clientes.

if 'CL_FHL' in df.columns:

    filhos_nulos_antes = df['CL_FHL'].isnull().sum()
    print(f"Filhos nulos antes: {filhos_nulos_antes}")

    mediana_filhos = df['CL_FHL'].median()
    df['CL_FHL'] = df['CL_FHL'].fillna(mediana_filhos)

    filhos_nulos_depois = df['CL_FHL'].isnull().sum()
    print(f"Filhos nulos depois: {filhos_nulos_depois}")

#A coluna de Datas já foi tratada anteriormente, removendo registros sem data válida, então não é necessário fazer mais nada nessa coluna.

# ==========================================================
# REMOÇÃO DE VALORES INVÁLIDOS
# ==========================================================

#Analisando a base de dados, foi possível perceber que temos válores inválidos "#N/D" em várias linhas, nas colunas PR_CAT e PR_NOME.
#Esses valores não são nulos, mas também não são válidos para as análises. Por isso, é importante fazer uma alteração nesses registros, para evidenciar que houve uma falha no processo de preenchimento dos dados.

print("\n===== AJUSTE DE VALORES INVÁLIDOS =====")

print("Valores inválidos em CATEGORIA antes do ajuste: ") 
print((df["PR_CAT"] == "#N/D").sum())

print("\nValores inválidos em NOME DO PRODUTO antes do ajuste: ") 
print((df["PR_NOME"] == "#N/D").sum())

# Substituindo os valores "#N/D" por NaN para facilitar a identificação e tratamento desses registros posteriormente.

df["PR_CAT"] = df["PR_CAT"].replace("#N/D", pd.NA)
df["PR_NOME"] = df["PR_NOME"].replace("#N/D", pd.NA)

# Agora, podemos substituir os valores nulos por um valor genérico, como "Sem Categoria" para a coluna PR_CAT e "Produto Não Informado" para a coluna PR_NOME.

df["PR_CAT"] = df["PR_CAT"].fillna("Sem Categoria")

df["PR_NOME"] = df["PR_NOME"].fillna("Produto Não Informado")

print()
print("Valores inválidos em CATEGORIA após o ajuste: ") 
print((df["PR_CAT"] == "#N/D").sum())

print("\nValores inválidos em NOME DO PRODUTO após o ajuste: ") 
print((df["PR_NOME"] == "#N/D").sum())

# ==========================================================
# REMOÇÃO DE DUPLICATAS
# ==========================================================

print("\n===== REMOÇÃO DE DUPLICATAS =====")

linhas_antes = df.shape[0]
print(f"Linhas antes de remover duplicatas: {linhas_antes}")
# Removendo duplicatas

df = df.drop_duplicates()

linhas_depois = df.shape[0]
print(f"Linhas depois de remover duplicatas: {linhas_depois}")
print(f"Duplicatas removidas: {linhas_antes - linhas_depois}")

# ==========================================================
# VALIDAÇÃO DO IDENTIFICADOR DE COMPRA (CO_ID)
# ==========================================================

print("\n===== VALIDAÇÃO DO IDENTIFICADOR DE COMPRA ====")

print(f"Total de registros: {len(df)}")
print(f"Compras únicas: {df['CO_ID'].nunique()}")

coid_duplicados = df['CO_ID'].duplicated().sum()

print(f"Compras duplicadas: {coid_duplicados}")

# ==========================================================
# ESTATÍSTICAS DESCRITIVAS
# ==========================================================

print("\n===== ESTATÍSTICAS DO NÚMERO DE FILHOS =====")

# Estatísticas da coluna número de filhos

coluna_filhos = df['CL_FHL']

print(f"Média: {coluna_filhos.mean():.2f}")
print(f"Mediana: {coluna_filhos.median()}")
print(f"Desvio padrão: {coluna_filhos.std():.2f}")
print(f"Moda: {coluna_filhos.mode()[0]}")
print(f"Máximo: {coluna_filhos.max()}")
print(f"Mínimo: {coluna_filhos.min()}")
print(f"Contagem: {coluna_filhos.count()}")

# ==========================================================
# AGRUPAMENTO 1 - GÊNERO
# ==========================================================

print("\n===== AGRUPAMENTO POR GÊNERO =====")

# agrupamento por gênero, contando a quantidade de compras (CO_ID) e ordenando do maior para o menor

agrupamento_genero = df.groupby('CL_GENERO')['CO_ID'].count().sort_values(ascending=False) 

print(agrupamento_genero)

# ==========================================================
# AGRUPAMENTO 2 - CATEGORIA
# ==========================================================

print("\n===== AGRUPAMENTO POR CATEGORIA =====")

# agrupamento por categoria, contando a quantidade de compras (CO_ID) e ordenando do maior para o menor

agrupamento_categoria = df.groupby('PR_CAT')['CO_ID'].count().sort_values(ascending=False)

print(agrupamento_categoria)

# ==========================================================
# PIVOT TABLE
# ==========================================================

print("\n===== PIVOT TABLE =====")

# tabela dinâmica que cruza gênero e categoria, contando a quantidade de compras (CO_ID) para cada combinação.

pivot = pd.pivot_table(
    df,
    values='CO_ID',
    index='CL_GENERO',
    columns='PR_CAT',
    aggfunc='count',
    fill_value=0
)

print(pivot)

# ==========================================================
# GRÁFICO DE BARRAS - TOP CATEGORIAS
# ==========================================================

top_categorias = (
    df.groupby('PR_CAT')['CO_ID']
      .count()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10, 5))

top_categorias.plot(kind='bar')

plt.title('Top 10 Categorias por Quantidade de Compras')
plt.xlabel('Categoria')
plt.ylabel('Quantidade de Compras')

plt.tight_layout()

plt.show()

# ==========================================================
# EXPORTAÇÃO DA BASE LIMPA
# ==========================================================

print("\n===== EXPORTANDO BASE LIMPA =====")

output = 'df_limpo.csv'

# Exporta CSV limpo

df.to_csv(output, index=False)

print(f"Arquivo exportado: {output}")

# ==========================================================
# CONCLUSÕES
# ==========================================================

print("\n===== CONCLUSÕES =====")

print("""
1. A análise identificou valores nulos e registros duplicados na base original.

2. Ao verificar o Identificador de Compra (CO_ID), verificamos que a base, apesar de ter mais de 800 mil linhas, registra 18471 compras únicas.

3. Através do agrupamento por gênero, foi possível identificar que a maioria dos clientes são mulheres.

4. O agrupamento por gênero permitiu identificar que as mulheres compram mais que os homens em todas as categorias.

5. O agrupamento por categoria mostrou que os alimentos são as categorias com maior volume de vendas, seguidos por produtos de higiene, e depois por produtos de limpeza.

6. Após a limpeza, a base ficou mais adequada para análises futuras e dashboards.
""")

# ==========================================================
# FIM DO PROJETO
# ==========================================================

print("\nProjeto finalizado com sucesso!")