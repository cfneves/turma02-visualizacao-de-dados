# %%
# Importando as bibliotecas essenciais
import pandas as pd
print("Pandas carregado com sucesso!")

# %%
# ====================================================================
# 1. CARREGAMENTO DOS DADOS E REGRA DO IDENTIFICADOR (SEPARADOR)
# ====================================================================

from pathlib import Path

caminho_arquivo = (
    Path(__file__).parent /
    "../../../base_do_projeto/Base Varejo.csv"
).resolve()

# Lendo os dados e validando a regra de separação dos registros (sep=';')
df = pd.read_csv(caminho_arquivo, sep=';')

print("--- Primeiras 5 linhas da Base ---")
print(df.head()) # ou print(df.head())

# %%
# ====================================================================
# 2. IDENTIFICAÇÃO DE PROBLEMAS (Tipos, Nulos e Duplicados)
# ====================================================================

print("\n--- Informações Gerais (Tipos de Dados e Nulos) ---")
df.info()

print("\n--- Contagem de Valores Nulos por Coluna ---")
print(df.isnull().sum())

print("\n--- Verificação de Linhas Duplicadas ---")
print(f"Total de registros duplicados: {df.duplicated().sum()}")

# %%
# ====================================================================
# 3. TRATAMENTO E LIMPEZA DE DADOS
# ====================================================================

# 3.1 Removendo registros duplicados
df = df.drop_duplicates()

# 3.2 Remove colunas completamente vazias
df = df.drop(columns=['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'])

print("\n--- Estrutura após Limpeza ---")
print(df.info())

# 3.3 Tratando valores nulos (Tratar nulos preenchendo com "Sem Categoria")
# Preenchendo as colunas de Produtos e Categorias que possam estar vazias
if 'PR_CAT' in df.columns:
    df['PR_CAT'] = df['PR_CAT'].fillna('Sem Categoria')
if 'PR_NOME' in df.columns:
    df['PR_NOME'] = df['PR_NOME'].fillna('Sem Nome')

# 3.4 Tratando Identificador de Compra
# Remove compras sem ID
df = df.dropna(subset=['CO_ID']) 
# Transforma ID em texto para não somar IDs por engano
df['CO_ID'] = df['CO_ID'].astype(str)

# 3.5 Convertendo datas
df['DATA'] = pd.to_datetime(
    df['DATA'],
    format='%d/%m/%Y',
    errors='coerce'
)

print("\n--- Verificação de Datas Inválidas ---")
print(f"Datas inválidas encontradas: {df['DATA'].isnull().sum()}")

# %%
# ====================================================================
# 4. ESTATÍSTICAS BÁSICAS (Foco no Número de Filhos - CL_FHL)
# ====================================================================

# Estatísticas descritivas da quantidade de filhos
print("\n--- Estatísticas Descritivas: Número de Filhos (CL_FHL) ---")
print(f"Contagem: {df['CL_FHL'].count()}")
print(f"Média: {df['CL_FHL'].mean():.2f}")
print(f"Mediana: {df['CL_FHL'].median()}")
print(f"Moda: {df['CL_FHL'].mode()[0]}")
print(f"Desvio Padrão: {df['CL_FHL'].std():.2f}")
print(f"Mínimo: {df['CL_FHL'].min()}")
print(f"Máximo: {df['CL_FHL'].max()}")

print("\n--- Contagem de Clientes por Quantidade de Filhos ---")
# Conta clientes por quantidade de filhos
contagem_filhos = df['CL_FHL'].value_counts().sort_index()
print(contagem_filhos)


# %%
# ====================================================================
# 5. PADRÕES DE AGRUPAMENTO
# ====================================================================

# Quais categorias vendem mais? -> Compras por categoria de produto
print("\n--- Produtos Vendidos por Categoria ---")
vendas_categoria = df.groupby('PR_CAT')['PR_ID'].count().sort_values(ascending=False)
print(vendas_categoria)

# Quem compra mais? -> Compras por gênero e segmento
print("\n--- Compras por Gênero e Segmento ---")
# Conta compras únicas para evitar duplicidade
vendas_perfil = df.groupby(['CL_GENERO', 'CL_SEG'])['CO_ID'].nunique().reset_index()
vendas_perfil = vendas_perfil.sort_values(by='CO_ID', ascending=False)
vendas_perfil.columns = ['Gênero', 'Segmento', 'Qtd_Compras_Unicas']
print(vendas_perfil)

# Como variam as vendas ao longo do tempo? -> Compras ao longo do tempo
# Cria coluna ano/mês
df['ANO_MES'] = df['DATA'].dt.to_period('M')

print("\n--- Compras ao Longo do Tempo ---")
vendas_tempo = df.groupby('ANO_MES')['CO_ID'].nunique()
print(vendas_tempo)

# %%
# ====================================================================
# 6. CONCLUSÕES
# ====================================================================

print("\n--- PRINCIPAIS INSIGHTS ---")

print("• A categoria ALIMENTOS apresentou o maior número de vendas, com 384.197 registros.")
print("• O segmento B concentrou a maior quantidade de compras (5.946 compras).")
print("• Clientes do gênero feminino do segmento B foram os que mais compraram (5.946 compras).")
print("• A maioria dos clientes não possui filhos, pois a mediana e a moda da variável CL_FHL foram iguais a 0.")
print("• A quantidade média de filhos por cliente foi de aproximadamente 1,15, variando entre 0 e 4 filhos.")
print("• Foram identificados 96.553 registros duplicados e quatro colunas totalmente vazias, que foram removidas durante a etapa de limpeza dos dados.")
