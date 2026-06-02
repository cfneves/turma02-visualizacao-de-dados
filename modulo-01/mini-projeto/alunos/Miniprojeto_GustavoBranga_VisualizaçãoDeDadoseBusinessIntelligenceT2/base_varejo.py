import pandas as pd            # pandas = biblioteca de analise de dados
import numpy as np             # numpy = biblioteca de numeros 
import re                      # expressão regular (limpar texto)
from datetime import datetime    # para eu trabalhar com dadas 

#confirmar que as importações funcionaram

print(' pandas versão:', pd.__version__)
print(' numpy versão:', np.__version__)
print(' Bibliotecas com sucesso!')

# pd.read_csv = ler arquivo em csv
# caminho = onde esta o arquivo csv.

CAMINHO = r"C:\Users\gusta\OneDrive\Área de Trabalho\aula1\turma-visualizacao-de-dados\modulo-01\base_do_projeto\Base Varejo.csv"

df = pd.read_csv(
  CAMINHO,
  sep=';',      # separador que esta no csv
  encoding='cp1252', #enconding do windows, para ler acentos
  decimal=','  #separador decimal
)

print('---Dados carregados com sucesso---')
print(f' total de linhas : {df.shape[0]}')  # 0 = numero de linhas
print(f' total de colunas : {df.shape[1]}') # 1 = numero de colunas

# Apresentando as informações gerais do arquivo

print(' ----INFORMACOES GERAIS---- ')
print(f'Registros : {df.shape[0]}')
print(f'Colunas : {df.shape[1]}')
print()
print(' ----TIPOS DE DADOS---- ')
print(df.dtypes)
print()
print(' ----PRIMEIRAS LINHAS---- ')
print(df.head())

print('Colunas dataset:') 
print(df.columns.tolist()) # Para ver os nomes das colunas e se estão corretos

df.head(5)

#Convertendo colunas para numeros
# errors = 'coerce' transforma texto invalido em NaN
df['CO_ID'] = pd.to_numeric(df['CO_ID'], errors='coerce')
df['CL_ID'] = pd.to_numeric(df['CL_ID'], errors='coerce')
df['CL_EC'] = pd.to_numeric(df['CO_ID'], errors='coerce')
df['CL_FHL'] = pd.to_numeric(df['CL_FHL'], errors='coerce')
df['PR_ID'] = pd.to_numeric(df['PR_ID'], errors='coerce')
# Print para verificar se teve a mudança de numeros.
print(df[['CO_ID', 'CL_ID', 'CL_EC', 'CL_FHL', 'PR_ID']].dtypes) 

# Verificar se o ID e unico
total = len(df)
unico1 = df['CL_ID'].nunique()
unico2 = df['CO_ID'].nunique()
unico3 = df['PR_ID'].nunique()
duplicados = total - unico1 - unico2 - unico3
print(f'Total de registros : {total}')
print(f'IDs unicos : {unico1 + unico2 + unico3}')
print(f'IDs duplicados : {duplicados}')
# Separar registros duplicados para analise
mask_dup = df.duplicated(subset=['CL_ID', 'CO_ID', 'PR_ID'], keep=False)
df_dup = df[mask_dup]
print(df_dup.head())

# Utilizado para verificar os nulos
nulos = df.isnull().sum()
pct = (nulos / len(df) * 100).round(2)
relatorio = pd.DataFrame({'Nulos': nulos, 'Pct (%)': pct})
relatorio = relatorio[relatorio['Nulos'] > 0].sort_values('Pct (%)', ascending=False)
print(relatorio)

#Para verificar a quantidade de linhas vazias
print(df.isna().sum())

# Remover colunas completamente vazias
# Justificativa: colunas com 100% de nulos não carregam
# Sem informações uteis e apenas poluem a base de dados.
df = df.drop(columns=['Unnamed: 10', 'Unnamed: 11',
                       'Unnamed: 12', 'Unnamed: 13'])

print(f'Colunas após limpeza: {df.columns.tolist()}')

# CL_FHL (nº de filhos) não possui nulos — nenhuma imputação necessária.
print(f'Nulos em CL_FHL: {df["CL_FHL"].isnull().sum()}')

# Verificar duplicatas exatas
qtd_antes = len(df)
df = df.drop_duplicates()
qtd_depois = len(df)
print(f'Duplicatas removidas: {qtd_antes - qtd_depois}')

# Salvando o DataFrame limpo
df.to_csv('base_varejo_lipo.csv', index=False, encoding='cp1252')
print('Arquivo base_varejo_lipo.csv salvo com sucesso.')

col = df['CL_FHL']
print(col.describe().round(2))
print(f'Moda: {col.mode()[0]}')

#Agrupando vendas por genero
vendas_genero = df.groupby('CL_GENERO')['CO_ID'].agg(
    qtd_compras='count'
).reset_index()
vendas_genero.columns = ['Genero', 'Qtd_Compras']
 
print()
print('=== COMPRAS POR GÊNERO ===')
print(vendas_genero.to_string(index=False))

#  Compras por categoria de produto
vendas_cat = df.groupby('PR_CAT')['CO_ID'].agg(
    qtd_compras='count'
).sort_values('qtd_compras', ascending=False).reset_index()
vendas_cat.columns = ['Categoria', 'Qtd_Compras']
 
print()
print('=== COMPRAS POR CATEGORIA ===')
print(vendas_cat.to_string(index=False))

# Conclusões

print('---------CONCLUSÕES DA ANÁLISE---------')
print('1. VOLUME: A base contém 830.000 registros com 10 colunas, depois de remover 4 que estavam vazias.')
print('2. QUALIDADE: Nenhum nulo nas colunas principais.')
print('3. GÊNERO: Clientes do sexo Feminino (F) realizam mais.')
print('4. CATEGORIAS: ALIMENTOS lidera com 434.767 compras.')
print('5. FILHOS: Média de 1,15 filhos por cliente. A moda é 0.')
print('6. PROBLEMA REMANESCENTE: A base não possui coluna de valor de compras.')