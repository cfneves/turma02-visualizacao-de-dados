#SPRINT 1 -IMPORTANDO OS DADOS E AS BIBLIOTECAS E REALIZANDO A ANÁLISE EXPLORATÓRIA DOS DADOS

#IMPORTANDO AS BIBLIOTECAS
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#IMPORTANDO OS DADOS
print('Carregando os dados...')
df = pd.read_csv('Base_varejo.csv', encoding='utf-8-sig', sep=';')
print('Dados carregados com sucesso!')
print()


#- ANÁLISE EXPLORATÓRIA DOS DADOS

#EXIBINDO AS PRIMEIRAS 5 LINHAS DO DATAFRAME
print('Exibindo as 5 primeiras linhas do dataframe:')
print()
print(df.head(5))
print()

#EXIBINDO AS ÚLTIMAS 5 LINHAS DO DATAFRAME
print('Exibindo as 5 últimas linhas do dataframe:')
print()
print(df.tail(5))
print()

#Visualizando as colunas e o número de linhas e colunas do dataframe
print('Visualizando as colunas e o número de linhas e colunas do dataframe:')
print()
print('Colunas:', df.columns.tolist())
print('Número de linhas:', df.shape[0])
print('Número de colunas:', df.shape[1])
print()

#Visualizando informações gerais sobre o dataframe
print('Visualizando informações gerais sobre o dataframe:')
print()
print(df.info())
print('Colunas e tipos de dados:')
print(df.info())
print()

#Visualizando estatísticas descritivas do dataframe
print('Visualizando estatísticas descritivas do dataframe:')
print()
print(df.describe().round(1))
print()

#Tipos de dados de cada coluna
print('Tipos de dados de cada coluna:')
print()
print(df.dtypes)
print()

#Renomear as colunas para nomes mais simples
#Utilizando o método rename() para renomear as colunas, passando um dicionário com os nomes antigos como chaves e os novos nomes como valores. O parâmetro inplace=True é usado para modificar o DataFrame original.
print("Renomeando todas as colunas do dataset para nomes mais simples...")
df.rename(columns={
    'DATA': 'data_compra', 'CO_ID': 'codigo_id', 'CL_ID': 'cliente_id', 'CL_GENERO': 'cliente_genero', 'CL_EC': 'estado_civil_cliente', 'CL_FHL': 'qtd_filhos_clientes', 'CL_SEG': 'classe_economica_cliente',
    'PR_ID': 'produto_id', 'PR_CAT': 'produto_categoria', 'PR_NOME': 'nome_produto', 'unnamed_10': 'coluna_10', 'unnamed_11': 'coluna_11', 'unnamed_12': 'coluna_12', 'unnamed_13': 'coluna_13'
}, inplace=True)
print("Colunas renomeadas com sucesso:", df.columns.tolist())
print()


#Verificando as informaçlões gerais do dataframe após renomear as colunas
print("Analisando as informações gerais do dataframe após renomear as colunas:")
print()
print(df.info())
print()

#Verificando as colunas
print("Verificando as colunas do dataframe:")
print()
print(df.columns)
print()




#SPRINT 2 - TRANSFORMAÇÃO E TIPO DE DADOS 

#Criando uma cópia do dataframe original para manter os dados originais intactos durante as transformações
df_sujo = df.copy()

#Se precisar garantir que o indicador seja numérico, podemos usar o método pd.to_numeric() para converter a coluna.
print("Convertendo a coluna 'codigo_id' para o tipo numérico...")
df['codigo_id'] = pd.to_numeric(df['codigo_id'], errors='coerce')
print("Coluna 'codigo_id' convertida para o tipo numérico com sucesso!")
print()


#  Transformando a coluna 'data_compra' para o tipo datetime
print("Transformando a coluna 'data_compra' para o tipo datetime...")
df['data_compra'] = pd.to_datetime(
    df['data_compra'], 
    format='%d-%m-%Y',
    errors='coerce')
print("Coluna 'data_compra' transformada com sucesso!")
print()

# Extraindo mês e ano para habilitar análises temporais
print("Extraindo mês e ano da coluna 'data_compra'...")
df['MES'] = df['data_compra'].dt.month
df['ANO'] = df['data_compra'].dt.year
print("Colunas 'MES' e 'ANO' adicionadas com sucesso!")
print()


# Verificando os tipos de dados após a transformação
print("Verificando os tipos de dados após a transformação:")
print()
print(df.dtypes)
print()


#Análise de valores ausentes (NaN)

#NaN por coluna
print("Análise de valores ausentes (NaN) por coluna:")

#Contagem de NaN por coluna usando o método isnull() para identificar os valores ausentes e sum() para contar a quantidade de NaN em cada coluna. O resultado é armazenado na variável nan_coluna.
nan_coluna = df.isnull().sum()
print()
print("Contagem de NaN por coluna:")
print(nan_coluna.to_string())

#NaN por linha E total de células ausentes
print("Análise de valores ausentes (NaN) por linha e total de células ausentes:")
print()
print(f'Total de células ausentes: {df.isnull().sum().sum()}')
print(f'Total de linhas com pelo menos um NaN: {df.isnull().any(axis=1).sum()}')
print()


# Percentual de NaN por coluna (só mostra colunas com NaN)

#Para calcular o percentual de NaN por coluna, dividimos a contagem de NaN em cada coluna pelo número total de linhas do DataFrame e multiplicamos por 100 para obter o percentual. O resultado é arredondado para uma casa decimal usando round(1). Em seguida, filtramos apenas as colunas que possuem algum NaN (percentual maior que 0) e ordenamos os resultados em ordem decrescente para facilitar a visualização.
print("Percentual de NaN por coluna (apenas colunas com NaN):")
nan_percentual = (nan_coluna / len(df) * 100).round(1)
nan_filtrado = nan_percentual[nan_percentual > 0].sort_values(ascending=False)
print()  
print("=== Percentual de valores ausentes ===")
for coluna, pct in nan_filtrado.items():
    barras = '█' * int(pct / 2)
    print(f"  {coluna:<25} {pct:5.1f}%  {barras}")

print()

#Gráfico de barras: % de ausentes por coluna
print('Gerando gráfico de barras: % de ausentes por coluna')
nan_percentual = df.isnull().mean() * 100
nan_percentual = nan_percentual[nan_percentual > 0].sort_values(ascending=False)
print()
#Criando un gráfico para visualizar melhor o percentual de valores ausentes por coluna.
plt.figure(figsize=(10, 6))
plt.bar(nan_percentual.index, nan_percentual.values, color='salmon',edgecolor='white')
plt.title('Percentual de Valores Ausentes por Coluna')
plt.xlabel('Colunas')
plt.ylabel('Percentual de NaN (%)')
plt.tight_layout()  
plt.show()
print()


# implementou a lógica para substituir '#N/D' por 'Sem Categoria' na coluna 'produto_categoria'

print("Substituindo valores '#N/D' na coluna 'produto_categoria' por 'Sem Categoria'...")
df_sujo['produto_categoria'] = df_sujo['produto_categoria'].replace('#N/D', 'Sem Categoria')
df_sujo['produto_categoria'] = df_sujo['produto_categoria'].fillna('Sem Categoria')
print("Coluna 'produto_categoria' atualizada com sucesso.")



#Limpeza de colunas que contém NaN usando dropna().
print("Iniciando limpeza de colunas com NaN usando dropna...")
colunas_com_nan = df_sujo.columns[df_sujo.isnull().any()].tolist()
print(f"Colunas com pelo menos um NaN: {len(colunas_com_nan)}")
print(colunas_com_nan)
print(f"Número de colunas antes da limpeza: {df_sujo.shape[1]}")
df_sujo = df_sujo.dropna(axis=1, how="any")
print(f"Número de colunas após dropna: {df_sujo.shape[1]}")
print("Observação: removi colunas inteiras com valores faltantes para evitar análises sobre variáveis incompletas.")


#Removendo as duplicatas do dataframe
print("Removendo duplicatas do dataframe...")
duplicatas = df_sujo.duplicated().sum()
print(f"Número de linhas duplicadas encontradas: {duplicatas}")
df_sujo = df_sujo.drop_duplicates()
print(f"Número de linhas após remoção de duplicatas: {df_sujo.shape[0]}")
print("Observação: removi linhas duplicadas para garantir a integridade dos dados e evitar análises distorcidas.")
print()



#SPRINT 4 - ANÁLISE DESCRITIVA DA COLUNA DE NÚMERO DE FILHOS DO CLIENTE.

#Criando um novo dataframe limpo para manter o dataframe original intacto
df_limpo = df_sujo.copy()

#Gerar estatísticas descritivas básicas para coluna de número de filhos do cliente (média; mediana; desvio padrão; moda; máximo; mínimo; e contagem).
print("Gerando estatísticas descritivas para a coluna 'qtd_filhos_clientes':")
media = df_limpo['qtd_filhos_clientes'].mean()
mediana = df_limpo['qtd_filhos_clientes'].median()
desvio_padrao = df_limpo['qtd_filhos_clientes'].std()
moda = df_limpo['qtd_filhos_clientes'].mode()[0]
maximo = df_limpo['qtd_filhos_clientes'].max()
minimo = df_limpo['qtd_filhos_clientes'].min()
contagem = df_limpo['qtd_filhos_clientes'].count()
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Moda: {moda}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Contagem: {contagem}")
print()


#SPRINT 5 - AGRUPAMENTO DE DADOS E VISUALIZAÇÃO

#Criando um groupby para contar a quantidade de compras por categoria de produto
print("Criando um groupby para contar a quantidade de compras por categoria de produto...")
groupby_categoria = df_limpo.groupby('produto_categoria').size().reset_index(name='quantidade_compras')
print("Groupby criado com sucesso! Exibindo as primeiras linhas do resultado:")
print(groupby_categoria.head())

#Criando um groupy by com duas colunas para contar a quantidade de compras por categoria de produto e gênero do cliente
print("Criando um groupby para contar a quantidade de compras por categoria de produto e gênero do cliente...")
groupby_categoria_genero = df_limpo.groupby(['produto_categoria', 'cliente_genero']).size().reset_index(name='quantidade_compras')
print("Groupby criado com sucesso! Exibindo as primeiras linhas do resultado:")
print(groupby_categoria_genero.head())


#SPRINT 6 - GRÁFICOS E VISUALIZAÇÕES

#Criando um gráfico de barras para visualizar a quantidade de compras por categoria de produto
print("Criando um gráfico de barras para visualizar a quantidade de compras por categoria de produto...")
plt.figure(figsize=(10, 6))
plt.bar(groupby_categoria['produto_categoria'], groupby_categoria['quantidade_compras'], color='skyblue', edgecolor='black')
plt.title('Quantidade de Compras por Categoria de Produto')
plt.xlabel('Categoria de Produto')
plt.ylabel('Quantidade de Compras')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print()


#Criando um gráfico para mostrar qual genero de cliente compra mais em cada categoria de produto
print("Criando um gráfico de barras para visualizar a quantidade de compras por categoria de produto e gênero do cliente...")
plt.figure(figsize=(12, 8)) 
for genero in groupby_categoria_genero['cliente_genero'].unique():
    subset = groupby_categoria_genero[groupby_categoria_genero['cliente_genero'] == genero]
    plt.bar(subset['produto_categoria'], subset['quantidade_compras'], label=genero, edgecolor='black')
plt.title('Quantidade de Compras por Categoria de Produto e Gênero do Cliente')
plt.xlabel('Categoria de Produto')
plt.ylabel('Quantidade de Compras')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print()

# Exportando o dataframe transformado para CSV
print('Gerando arquivo de saída CSV com o dataframe transformado...')
df.to_csv('Base_varejo_transformado.csv', index=False, encoding='utf-8-sig')
print('Arquivo CSV gerado: Base_varejo_transformado.csv')
print()

#SPRINT 7 - RELATÓRIO FINAL DO TERMINAL
print('Construindo o relatório final do terminal...')
print()
print('=== RELATÓRIO FINAL ===')
print(f'Total de linhas no dataset original: {len(df)}')
print(f'Total de colunas no dataset original: {df.shape[1]}')
print(f'Total de linhas após limpeza: {len(df_limpo)}')
print(f'Total de colunas após limpeza: {df_limpo.shape[1]}')
print(f'Linhas duplicadas removidas: {duplicatas}')
print(f'Colunas com valores ausentes removidas: {len(colunas_com_nan)}')
print(f'Total de valores ausentes originais: {int(df.isnull().sum().sum())}')
print(f'Linhas com pelo menos um valor ausente no original: {int(df.isnull().any(axis=1).sum())}')
print(f'Categorias únicas em produto_categoria após limpeza: {df_limpo["produto_categoria"].nunique()}')
print(f'Quantidade de registros com categoria "Sem Categoria": {df_limpo["produto_categoria"].value_counts().get("Sem Categoria", 0)}')
print(f'Total de compras contabilizadas no groupby de categoria: {int(groupby_categoria["quantidade_compras"].sum())}')
if not groupby_categoria.empty:
    top_categoria = groupby_categoria.sort_values('quantidade_compras', ascending=False).iloc[0]
    print(f'Categoria com maior número de compras: {top_categoria['produto_categoria']} ({top_categoria['quantidade_compras']} compras)')
else:
    print('Não há categorias disponíveis para relatório de compras.')

compras_por_genero = groupby_categoria_genero.groupby('cliente_genero')['quantidade_compras'].sum().sort_values(ascending=False)
if not compras_por_genero.empty:
    genero_top = compras_por_genero.index[0]
    qtd_top = compras_por_genero.iloc[0]
    print(f'Gênero com maior volume de compras por categoria: {genero_top} ({qtd_top} compras)')
else:
    print('Não há dados de gênero disponíveis para relatório de compras.')
print('=== FIM DO RELATÓRIO ===')

