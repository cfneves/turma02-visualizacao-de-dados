#!/usr/bin/env python
# coding: utf-8

# # ============================================
# # DESAFIO MINI PROJETO - ANÁLISE EXPLORATÓRIA DE DADOS (AED)
# # Base de Dados: Varejo.csv
# # Aluno: Isaac Trenard
# # Turma: Visualização de Dados e Business Intelligence [T2]
# # SCTEC / SESI / SENAI 
# # ============================================

# # ============================================
# # SPRINT 1 - Importação dos dados
# # ============================================
# # 1.1. (Importação dos dados): Realização da importação dos dados na plataforma Kaggle 
# # para a IDE VsCode, onde o script será executado.

# # Importando base de dados e bibliotecas necessárias.

# In[189]:


import pandas as pd 
import re 
import matplotlib.pyplot as plt 
print("Ferramentas de trabalho importadas com sucesso!")


# # Lendo o arquivo CSV e armazenando em um DataFrame.

# In[191]:


base_Varejo = r'C:\Users\miran\OneDrive\Desktop\turma-visualizacao-de-dados\alunos\Isaac_Trenard\MiniProjeto_Isaac_Trenard_TURMA_Visualização_de_Dados_2\Base_Varejo.csv'

df_Varejo = pd.read_csv(base_Varejo, encoding='utf-8', sep=';')
print("Arquivo CSV lido e armazenado em um DataFrame com sucesso!")


# # ============================================
# # 1.2 Mostrar o número de registros, colunas e tipos de dados.
# # ============================================

# In[192]:


print(f'Número de linhas: {df_Varejo.shape[0]}')
print(f'Número de colunas: {df_Varejo.shape[1]}')
print(f'\nColunas e tipos de dados: \n{df_Varejo.dtypes}')


# # ============================================
# # 1.2  Verificar e reportar ao menos dois problemas básicos:
# # Valores nulos por coluna, duplicatas e possíveis inconsistências.
# # (ex.: datas inválidas ou categorias vazias).
# # ============================================

# In[193]:


print("\n--- Primeiras 5 linhas do DataFrame ---")
df_Varejo.head()


# In[194]:


print("\n--- Últimas 5 linhas do DataFrame ---")
df_Varejo.tail()


# # 1.3 Informações essenciais sobre o DataFrame

# In[195]:


print("\n--- Informações gerais do DataFrame ---")
df_Varejo.info()


# Problema 1: Os nomes de colunas não são intuitivos (siglas e abreviações) o que dificultam a compreensão imediata dos dados o que gerará no futuro  consultas na documentação externa para entender o que cada coluna representa.

# In[197]:


# Solução do Problema 1: Renomeação das colunas para nomes funcionais

df_Varejo = df_Varejo.rename(columns={
    'DATA': 'data',
    'CO_ID': 'id_compra',
    'CL_ID': 'id_cliente',
    'CL_GENERO': 'genero',
    'CL_EC': 'estado_civil',
    'CL_FHL': 'num_filhos',
    'CL_SEG': 'segmento',
    'PR_ID': 'id_produto',
    'PR_CAT': 'categoria',
    'PR_NOME': 'produto'
})
df_Varejo.columns = [col.title() for col in df_Varejo.columns]
print("Colunas renomeadas com sucesso!")
print(df_Varejo.columns.tolist())


# # ============================================
# # SPRINT 2 - Transformação de Strings, Integer, Float e Datetime
# # ============================================
# # Desenvolvimento das funções de limpeza de texto, inteiros e decimais usando métodos e expressões regulares.

# # Problema 2: Foi reconhecido que a coluna 'DATA' está como str o que distorce nossa análise.
# 

# In[202]:


# SOLUÇÃO DO PROBLEMA 2: Converter coluna DATA para datetime

df_Varejo['Data'] = pd.to_datetime(
    df_Varejo['Data'],
    format="%d/%m/%Y",
    errors="coerce"
)
print(f'Coluna DATA convertida para: {df_Varejo["Data"].dtype}')


# # ============================================
# # 2.1 Pesquisa de possíveis valores nulos por coluna.
# # ============================================

# In[203]:


print(f'\n--- Análise dos valores nulos em cada coluna ---\n')

df_com_nulos = pd.DataFrame({
    'Nulos': df_Varejo.isnull().sum(),
    'Tipo': df_Varejo.dtypes 
})
print(df_com_nulos)
print(f'\nTotal de valores nulos no DataFrame: {df_Varejo.isnull().sum().sum()}')

# Visualização das colunas com problemas (Unnamed)
print("\n--- Visualização das colunas Unnamed (totalmente vazias) ---")
print(df_Varejo[['Unnamed: 10', 'Unnamed: 11','Unnamed: 12', 'Unnamed: 13']].head(5))   


# # ============================================
# # 2.2 Análise de linhas duplicadas
# # ============================================

# In[205]:


df_com_duplicados = df_Varejo.duplicated()

# Ver linhas duplicadas
linhas_duplicadas = df_Varejo[df_com_duplicados].head()
print("\n--- Exemplo de linhas duplicadas (primeiras 5) ---")
print(linhas_duplicadas[['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13']])
print(f'\nTotal de registros duplicados encontrados: {df_com_duplicados.sum()}')


# # ============================================
# # SPRINT 3 - Limpeza de Nulos e Duplicatas.
# # ============================================
# # Aplicação das condicionais e funções para identificação e substituição de valores vazios e de str para valores de data tipo datetime.

# # Problema 3: Foram encontrados 3.320.000 nulos distribuídos igualmente em 4 colunas denominadas 'Unnamed' dentro do DataFrame. Ou seja, todas as linhas dessas colunas estão vazias. Também foram detectadas 96.553 linhas duplicadas.

# In[206]:


print("\n--- Problema 3: Colunas Unnamed totalmente vazias e linhas duplicadas ---")

# SOLUÇÃO 3: Remover colunas Unnamed (10,11,12,13) pois não representam nada na base

print("\n--- Removendo colunas Unnamed (totalmente vazias) ---")
df_Varejo = df_Varejo.drop(columns=['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'])
print(f"Colunas Unnamed removidas. Total de colunas agora: {df_Varejo.shape[1]}")

# Remover linhas duplicadas
print("\n--- Removendo linhas duplicadas ---")
df_Varejo = df_Varejo.drop_duplicates()
print(f"Linhas duplicadas removidas. Total de linhas agora: {df_Varejo.shape[0]}")


# # ============================================
# # Conferência da limpeza realizada
# # ============================================

# In[207]:


print("\n--- CONFERÊNCIA DA LIMPEZA ---")

# Verificar se ainda existem duplicados
df_com_duplicados = df_Varejo.duplicated()
print(f'Total de registros duplicados após limpeza: {df_com_duplicados.sum()}')

# Verificar total de colunas após limpeza
print(f'Total de colunas após limpeza: {df_Varejo.shape[1]}')

# Verificar total de linhas após limpeza
print(f'Total de linhas após limpeza: {df_Varejo.shape[0]}')


# # ============================================
# # 2.3 Inconsistências (ex.: datas inválidas ou categorias vazias)
# # ============================================

# In[208]:


print('\n--- Verificação de inconsistências remanescentes ---')

# Verificar se há datas inválidas (NaT) após conversão
datas_invalidas = df_Varejo['Data'].isnull().sum()
print(f'Datas inválidas (NaT) na coluna DATA: {datas_invalidas}')

# Verificar categorias vazias em colunas de texto

colunas_texto = df_Varejo.select_dtypes(include=['object','str']).columns
for col in colunas_texto:
    vazios = df_Varejo[col].isnull().sum()
    print(f'Valores vazios em {col}: {vazios}')


# Sprint 4 (Estatística Descritiva): Aplicação das funções estatísticas para coletar parâmetros da coluna de Número de filhos do cliente.
# 
# Gerar estatísticas descritivas básicas para coluna de número de filhos do cliente (média; mediana; desvio padrão; moda; máximo; mínimo; e contagem).

# In[211]:


print('ESTATÍSTICAS DESCRITIVAS')
print('Coluna: Número de Filhos')

print(df_Varejo['Num_Filhos'].describe().round(2))

# Calcular a moda da coluna Num_filhos
moda = df_Varejo['Num_Filhos'].mode()
print(f'A Moda na coluna Num_Filhos: {moda[0]} filhos')


# Explorar padrões de agrupamento com pelo menos dois agrupamentos (por exemplo: gênero com mais vendas, compras), usando groupby() ou pivot_table().

# In[212]:


print(df_Varejo.groupby('Genero')['Categoria'].value_counts())


# Bloco de conclusoes:

# 1. Qualidade dos dados após limpeza
# Após a remoção de 4 colunas totalmente vazias (Unnamed) e 96.553 linhas duplicadas, a base foi reduzida de 830.000 para 733.447 registros válidos. Não há mais valores nulos nas colunas essenciais, e a coluna Data foi convertida para datetime, permitindo análises temporais futuras.
# 
# 2. Perfil dos clientes em relação a filhos
# A análise da coluna Num_Filhos mostra que 50% dos clientes não têm filhos (mediana = 0), e a média é de 1,15 filhos por cliente. O valor mais frequente (moda) é 0 filhos, indicando que a maioria dos clientes não tem filhos. Apenas 25% dos clientes têm 2 ou mais filhos.
# 
# 3. Comportamento de compra por gênero e categoria
# As categorias ALIMENTOS e HIGIENE são as mais compradas tanto por homens quanto por mulheres. Mulheres (F) lideram as compras em todas as categorias, com destaque para ALIMENTOS (200.274 compras) e HIGIENE (71.721 compras). Homens (M) também concentram suas compras em ALIMENTOS (183.923) e HIGIENE (65.981).
# 
# 4. Problema remanescente: categoria #N/D
# Foi identificada uma categoria com nome #N/D (provavelmente "Não Disponível"), representando 1.692 compras de mulheres e 1.536 de homens. Esse valor é pequeno, mas precisa ser tratado. A sugestão é renomear #N/D para Outros ou investigar quais produtos estão sem categoria definida para possível fusão com categorias existentes.

# In[213]:


# ============================================
# SPRINT 5 - RELATÓRIO FINAL
# ============================================

print("\n" + "="*70)
print("RELATÓRIO FINAL - ANÁLISE DE DADOS DE VAREJO")
print("="*70)

print("\n📊 RESUMO GERAL:")
print(f"   - Total de clientes analisados: {df_Varejo.shape[0]:,}")
print(f"   - Total de colunas na base limpa: {df_Varejo.shape[1]}")
print(f"   - Período dos dados: {df_Varejo['Data'].min().date()} a {df_Varejo['Data'].max().date()}")

print("\n👨‍👩‍👧 PERFIL DOS CLIENTES:")
print(f"   - Média de filhos por cliente: {df_Varejo['Num_Filhos'].mean():.2f}")
print(f"   - Clientes sem filhos: 50% (mediana = {df_Varejo['Num_Filhos'].median():.0f})")
print(f"   - Gênero que mais compra: {df_Varejo['Genero'].value_counts().idxmax()}")

print("\n🛒 PRODUTOS E CATEGORIAS:")
categoria_top = df_Varejo['Categoria'].value_counts().idxmax()
categoria_top_qtd = df_Varejo['Categoria'].value_counts().max()
print(f"   - Categoria mais vendida: {categoria_top} ({categoria_top_qtd:,} compras)")
print(f"   - Segunda categoria mais vendida: {df_Varejo['Categoria'].value_counts().index[1]} ({df_Varejo['Categoria'].value_counts().iloc[1]:,} compras)")

print("\n⚠️ PROBLEMAS REMANESCENTES:")
if '#N/D' in df_Varejo['Categoria'].values:
    qtd_nd = (df_Varejo['Categoria'] == '#N/D').sum()
    print(f"   - Categoria '#N/D' precisa ser tratada ({qtd_nd:,} registros)")
else:
    print("   - Nenhum problema remanescente identificado")

print("\n" + "="*70)
print("FIM DO RELATÓRIO")
print("="*70)


# In[ ]:


# Exportar DataFrame limpo para CSV
df_Varejo.to_csv('df_limpo_base_Varejo.csv', index=False)

print("Arquivo Data Frame criado com sucesso!")

