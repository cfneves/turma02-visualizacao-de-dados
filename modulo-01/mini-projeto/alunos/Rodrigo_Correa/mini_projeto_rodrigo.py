# -*- coding: utf-8 -*-
# Mini projeto avaliativo - Rodrigo Correa
# Exportado a partir do notebook para reproducao local.

# ------------------------------------------------------------------------------
# # Importação dos Dados

import pandas as pd
url = "https://raw.githubusercontent.com/cfneves/turma-visualizacao-de-dados/refs/heads/master/modulo-01/base_do_projeto/Base%20Varejo.csv"

df_original = pd.read_csv(url, sep=';')
df = df_original.copy()

df.head()

df.info()

df.describe()

# ------------------------------------------------------------------------------
# # Limpeza e Tratamento dos Dados

df = df.drop(columns=['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'])
df.head()

# ------------------------------------------------------------------------------
# ## Duplicatas

num_duplicatas = df.duplicated().sum()
print(f'Número de linhas duplicadas no dataset: {num_duplicatas}')

df_limpo = df.drop_duplicates().copy()
num_duplicatas_apos = df_limpo.duplicated().sum()
print(f'Número de linhas duplicadas no dataset: {num_duplicatas_apos}')

# ------------------------------------------------------------------------------
# ## Correção dos Tipos de Dados

colunas_inteiras = ['CO_ID', 'CL_ID', 'CL_EC', 'CL_FHL', 'PR_ID']
for col in colunas_inteiras:
    df_limpo[col] = pd.to_numeric(df_limpo[col], errors='coerce').astype('Int64')

colunas_categoricas = ['CL_GENERO', 'CL_SEG', 'PR_CAT', 'PR_NOME']
for col in colunas_categoricas:
    df_limpo[col] = df_limpo[col].astype('string').str.strip().str.upper()

for col in ['CL_GENERO', 'CL_SEG', 'PR_CAT', 'PR_NOME']:
    df_limpo[col] = df_limpo[col].astype('category')

df_limpo['DATA'] = pd.to_datetime(df_limpo['DATA'],format='%d/%m/%Y',errors='coerce')

print(df_limpo.isna().sum())

df_limpo.info()

# ------------------------------------------------------------------------------
# # Estatística Descritiva

coluna_filhos = 'CL_FHL'

media = df_limpo[coluna_filhos].mean()
mediana = df_limpo[coluna_filhos].median()
desvio_padrao = df_limpo[coluna_filhos].std()
moda = df_limpo[coluna_filhos].mode()[0]
maximo = df_limpo[coluna_filhos].max()
minimo = df_limpo[coluna_filhos].min()
contagem = df_limpo[coluna_filhos].count()

print(f'Estatísticas Descritivas para a coluna {coluna_filhos}:')
print(f'Média: {media:.2f}')
print(f'Mediana: {mediana:.2f}')
print(f'Desvio Padrão: {desvio_padrao:.2f}')
print(f'Moda: {moda}')
print(f'Máximo: {maximo}')
print(f'Mínimo: {minimo}')
print(f'Contagem: {contagem}')

display(df_limpo[coluna_filhos].describe())

# Quantidade de Compras por Genero de Cliente
compras_por_genero_pivot_total = pd.pivot_table(
    df_limpo,
    index='CL_GENERO',
    values='PR_ID',
    aggfunc='count')

compras_por_genero_pivot_total = compras_por_genero_pivot_total.rename(columns={'PR_ID': 'Total de Compras'})

display(compras_por_genero_pivot_total.sort_values(by='Total de Compras', ascending=False))

genero_mais_compras_total = compras_por_genero_pivot_total.idxmax()['Total de Compras']
max_compras_total = compras_por_genero_pivot_total.max()['Total de Compras']

print(f"\nO gênero com o maior número de compras é '{genero_mais_compras_total}' com {max_compras_total} compras.")

# Quantidade de Compras por Segmento de Cliente
compras_por_segmento = pd.pivot_table(
    df_limpo,
    index='CL_SEG',
    values='PR_ID',
    aggfunc='count'
)

compras_por_segmento = compras_por_segmento.rename(columns={'PR_ID': 'Total de Compras'})

display(compras_por_segmento.sort_values(by='Total de Compras', ascending=False))

segmento_mais_compras = compras_por_segmento.idxmax()['Total de Compras']
max_compras_segmento = compras_por_segmento.max()['Total de Compras']

print(f"\nO segmento de cliente com o maior número de compras é '{segmento_mais_compras}' com {max_compras_segmento} compras.")

# Quantidade de Compras por Categoria de Produto
compras_por_categoria = df_limpo.groupby('PR_CAT')['PR_ID'].count().reset_index()
compras_por_categoria = compras_por_categoria.rename(columns={'PR_ID': 'Total de Compras'})

display(compras_por_categoria.sort_values(by='Total de Compras', ascending=False).head(10))

# Quantidade de Compras por Número de Filhos
compras_por_filhos = df_limpo.groupby('CL_FHL')['PR_ID'].count().reset_index()
compras_por_filhos = compras_por_filhos.rename(columns={'PR_ID': 'Total de Compras'})

display(compras_por_filhos.sort_values(by='Total de Compras', ascending=False))

# ------------------------------------------------------------------------------
# # Conclusões e Insights
#
# Com base nas análises exploratórias realizadas até o momento, podemos extrair os seguintes insights principais e observar alguns pontos a serem considerados:
#
# ### Insights Obtidos:
#
# 1.  **Perfil de Clientes:**
# *   Clientes do gênero feminino ('F') realizam a maior quantidade de compras (382.427) em comparação com o gênero masculino ('M') (351.020).
# *   Clientes da classe 'B' são os mais ativos em termos de número total de compras (468.505), seguido pela classe 'C' e depois 'A'.
# *   Clientes sem filhos ('CL_FHL' = 0) são os que mais realizam compras, e o volume de compras tende a diminuir à medida que o número de filhos aumenta.
#
# 2.  **Categorias de Produtos:**
# *   A categoria de produtos 'ALIMENTOS' é de longe a mais vendida, com um número expressivo de 384.197 compras, destacando sua importância no mix de produtos. 'HIGIENE' e 'LIMPEZA' também são categorias fortes.
#
# ### Problemas Remanescentes e Pontos de Atenção:
#
# 1.  As análises focaram na quantidade de compras. Seria importante incluir o valor de cada compra para entender o faturamento gerado por gênero, segmento, categoria, etc.
# 2.  As colunas 'Unnamed: 10' a 'Unnamed: 13' foram descartadas por estarem vazias. É fundamental verificar se esses campos foram realmente irrelevantes ou se representavam dados ausentes que deveriam ter sido tratados de outra forma na coleta original.
