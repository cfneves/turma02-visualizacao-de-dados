"""
Mini-Projeto Evaluativo: Análise Exploratória de Dados - Módulo 1 
Visualização de Dados e Business Intelligence [T2]

Aluna: Anaysa Pereira Lopes

Descrição: Este script realiza uma Análise Exploratória de Dados (EDA) em um conjunto de dados de vendas.
O objetivo é identificar padrões, tendências e insights que possam ser úteis para a tomada de decisões estratégicas. 

"""

#=========================================================================================
# SPRINT 1: CONFIGURAÇÃO DO AMBIENTE E IMPORTAÇÃO DOS DADOS
#=========================================================================================

# Centralizando as bibliotecas que utilizaremos ao longo de todo o projeto
import os
import pandas as pd
import matplotlib.pyplot as plt

# Descobre a pasta onde o script atual está salvo (pasta 'src')
pasta_atual = os.path.dirname(os.path.abspath(__file__))

# Monta o caminho dinâmico para a pasta data/raw
url_base = os.path.join(pasta_atual, "..", "data", "raw", "base_varejo.csv")

# Tratamento de erros na leitura do arquivo
try:
    # Leitura do CSV tratando o separador e o encoding do Excel
    df_varejo = pd.read_csv(url_base, sep=";", encoding="utf-8-sig")
    print("✓ Arquivo carregado com sucesso!")
except FileNotFoundError:
    print(f"❌ Erro: Arquivo não encontrado em: {url_base}")
    exit()

# Remoção de colunas vazias criadas pelo Excel
colunas_vazias = [col for col in df_varejo.columns if col.startswith("Unnamed")]
df_varejo = df_varejo.drop(columns=colunas_vazias)

# Extração do tamanho da base (linhas e colunas)
linhas, colunas = df_varejo.shape

# Diagnóstico estrutural do DataFrame
print("\n ---> TAMANHO DO DATASET\n")
print(f"Linhas: {linhas}")
print(f"Colunas: {colunas}")

print("\n ------------#------------ \n")
print("\n ---> TIPOS DE DADOS SEM TRANSFORMAÇÃO\n")
print(df_varejo.dtypes)

print("\n ------------#------------ \n")
print("\n ---> PRIMEIRAS LINHAS\n")
print(df_varejo.head(5).to_string())

print("\n ------------#------------ \n")
print("\n ---> DESCRIÇÃO DOS DADOS\n")
print(df_varejo.describe().round(2))

print("\n ============================================================================== \n")

#=========================================================================================
# SPRINT 2: TRANSFORMAÇÃO DE STRINGS, NÚMEROS E DATETIME
#=========================================================================================

# Gerar uma cópia do DataFrame original para aplicar as transformações sem perder os dados brutos
df_tratado = df_varejo.copy()

# Transformação de Strings: Padronização de texto (remover espaços e converter para maiúsculas)
df_tratado['CL_GENERO'] = df_tratado['CL_GENERO'].str.strip().str.upper()
df_tratado['CL_SEG']   = df_tratado['CL_SEG'].str.strip().str.upper()
df_tratado['PR_CAT']   = df_tratado['PR_CAT'].str.strip().str.upper()
df_tratado['PR_NOME']  = df_tratado['PR_NOME'].str.strip().str.upper()

# Transformação de Números: Conversão de colunas numéricas tratando erros e garantindo a tipagem correta de identificadores
df_tratado['CL_FHL'] = pd.to_numeric(df_tratado['CL_FHL'], errors='coerce').astype('Int64')
df_tratado['CL_EC']  = pd.to_numeric(df_tratado['CL_EC'], errors='coerce').astype('Int64')
df_tratado['PR_ID']  = pd.to_numeric(df_tratado['PR_ID'], errors='coerce').astype('Int64')
df_tratado['CO_ID']  = pd.to_numeric(df_tratado['CO_ID'], errors='coerce').astype('Int64')

# Métricas de validação estrutural do DataFrame modificado 
print("\n ---> DIAGNÓSTICO DOS DADOS APÓS TRANSFORMAÇÕES\n")

# Transformação de Datas: Conversão cronológica da string para formato temporal estruturado
df_tratado['DATA'] = pd.to_datetime(df_tratado['DATA'], format="%d/%m/%Y", errors='coerce')
print(f"  • Tipo final verificado da coluna DATA: {df_tratado['DATA'].dtypes} \n")
print(df_tratado.dtypes)

print("\n ------------#------------ \n")
print("\n ---> AMOSTRAGEM DOS DADOS TRATADOS\n")
print(df_tratado.head(5).to_string())

print("\n ============================================================================== \n")

#=========================================================================================
# SPRINT 3: AUDITORIA, IDENTIFICAÇÃO E LIMPEZA DE DADOS 
#=========================================================================================

# Gerar uma cópia do DataFrame tratado para aplicar as limpezas sem perder os dados intermediários
df_limpo = df_tratado.copy()

# Auditoria inicial para identificar nulos, duplicatas e inconsistências antes do tratamento
print("  • Valores nulos por coluna antes do tratamento:\n")
print(df_limpo.isnull().sum())
print("---\n")
print(f"\n  • Quantidade de registros duplicados detectados:\n --> {df_limpo.duplicated().sum()}")

print("\n ------------#------------ \n")

# Remoção física de registros duplicados para purificação da base de dados, mantendo a primeira ocorrência
df_limpo = df_limpo.drop_duplicates()

# Limpeza de dados ausentes na coluna de categoria de produtos (PR_CAT) utilizando uma função personalizada
def preencher_categoria_vazia(cat):
    if pd.isna(cat) or str(cat).strip() == "" or str(cat).upper() == "NAN":
        return 'Sem Categoria'
    else:
        return cat

df_limpo['PR_CAT'] = df_limpo['PR_CAT'].apply(preencher_categoria_vazia)

# Imputação de dados ausentes nas dimensões categóricas residuais utilizando a abordagem de moda
df_limpo['CL_GENERO'] = df_limpo['CL_GENERO'].fillna(df_limpo['CL_GENERO'].mode()[0])
df_limpo['CL_SEG']   = df_limpo['CL_SEG'].fillna(df_limpo['CL_SEG'].mode()[0])
df_limpo['PR_NOME']  = df_limpo['PR_NOME'].fillna(df_limpo['PR_NOME'].mode()[0])

# Imputação de dados ausentes nas colunas numéricas estruturais utilizando a abordagem de mediana
df_limpo['CL_FHL'] = df_limpo['CL_FHL'].fillna(df_limpo['CL_FHL'].median())
df_limpo['CL_EC']  = df_limpo['CL_EC'].fillna(df_limpo['CL_EC'].median())
df_limpo['PR_ID']  = df_limpo['PR_ID'].fillna(df_limpo['PR_ID'].median())
df_limpo['CO_ID']  = df_limpo['CO_ID'].fillna(df_limpo['CO_ID'].median())

# Auditoria final para identificar a quantidade de valores nulos e registros duplicados depois do tratamento
print("\n ---> AUDITORIA FINAL DE VALIDAÇÃO DOS DADOS LIMPOS\n")
print(f"Registros duplicados residuais: {df_limpo.duplicated().sum()}")
print(f"Total de valores nulos residuais: {df_limpo.isnull().sum().sum()}")

print("\n ============================================================================== \n")

#=========================================================================================
# SPRINT 4: ESTATÍSTICA DESCRITIVA
#=========================================================================================

print("\n ---> ANÁLISE DESCRITIVA DA COLUNA DE FILHOS")

print("\n • A coluna 'CL_FHL' representa o número de filhos que os clientes possuem, sendo um indicador importante para entender a dimensão familiar do público-alvo. A análise estatística dessa coluna pode revelar tendências e padrões relacionados ao perfil dos clientes.")

# Distribuição de Frequência de Filhos - Análise de Tendências e Padrões na Dimensão Familiar dos Clientes
print(f"\nContagem Total de Filhos dos Clientes : {df_limpo['CL_FHL'].count():,}".replace(",", "."))
print(f"Mínimo de Filhos Registrado   : {df_limpo['CL_FHL'].min()}")
print(f"Máximo de Filhos Registrado   : {df_limpo['CL_FHL'].max()}")
print(f"Média Aritmética de Filhos    : {df_limpo['CL_FHL'].mean():.2f}")
print(f"Média Geométrica de Filhos (Ponto Central)   : {df_limpo['CL_FHL'].median():.2f}")
print(f"Desvio Padrão de Filhos    : {df_limpo['CL_FHL'].std():.4f}")
print(f"Padrão de Filhos por Cliente (Moda)  : {df_limpo['CL_FHL'].mode().tolist()}")

print("\n • Distribuição de Frequência de Filhos:\n")

# Distribuição de Frequência de Filhos calculada com value_counts() e ordenada por índice
distribuicao_freq = df_limpo['CL_FHL'].value_counts().sort_index()

# Criação da barra de visualização com base na distribuição de frequência
for valor, quantidade in distribuicao_freq.items():
    tamanho_barra = int(quantidade / distribuicao_freq.max() * 25)
    barra_visual = "█" * tamanho_barra
    print(f"  {int(valor)} filho(s): {quantidade:>7,} registros | {barra_visual}")

print("\n============================================================================== \n")

#=========================================================================================
# EXPLORAÇÃO DE AGRUPAMENTOS E PADRÕES OPERACIONAIS 
#=========================================================================================

print("\n ---> ANÁLISE DE AGRUPAMENTOS E PADRÕES OPERACIONAIS\n")

# Volume de transações de compras únicas por gênero do cliente 
print(" • Volume de Transações de Compras Únicas por Gênero do Cliente: \n")

compras_por_genero = df_limpo.groupby("CL_GENERO")["CO_ID"].nunique().sort_values(ascending=False)
print(compras_por_genero.to_string())

# Renderização do gráfico de barras com base na distribuição de compras por gênero
plt.figure(figsize=(6, 4))
plt.bar(compras_por_genero.index, compras_por_genero.values, color="rebeccapurple")
plt.title("Compras Únicas por Gênero do Cliente")
plt.xlabel("Gênero")
plt.ylabel("Quantidade de Transações")
plt.tight_layout()
plt.show()

print("\n ------------#------------ \n")

# Análise de evolução temporal do total de itens vendidos por ano de processamento
print(" • Evolução Temporal — Total de Itens Vendidos por Ano de Processamento:\n")

df_limpo['ANO_COMPRA'] = df_limpo['DATA'].dt.year
itens_por_ano = df_limpo.groupby("ANO_COMPRA").size()
print(itens_por_ano.to_string())

# Geração de um gráfico de linha para visualizar a evolução temporal
plt.figure(figsize=(7, 4))
plt.plot(itens_por_ano.index, itens_por_ano.values, marker="o", color="orchid", linewidth=2)
plt.title("Evolução Temporal de Itens Vendidos")
plt.xlabel("Ano de Processamento")
plt.ylabel("Total de Itens")
plt.xticks(itens_por_ano.index)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# Removendo a coluna temporária ANO_COMPRA para manter a estrutura original do DataFrame limpo
df_limpo = df_limpo.drop(columns=['ANO_COMPRA'])

print("\n ------------#------------ \n")

# Relatório de cruzamento de segmento econômico por gênero do cliente
print(" • Tabela Dinâmica — Cruzamento de Segmento Econômico por Gênero:\n")

tabela_segmento_genero = pd.pivot_table(
    df_limpo,
    values="CO_ID",
    index="CL_SEG",
    columns="CL_GENERO",
    aggfunc="count",
    fill_value=0
).astype(int)

print(tabela_segmento_genero.to_string())

# Plotagem do gráfico de barras agrupadas para visualizar a distribuição de segmento econômico por gênero do cliente
tabela_segmento_genero.plot(kind="bar", color=["olivedrab", "blueviolet"], figsize=(8, 4))
plt.title("Distribuição de Segmento Econômico por Gênero")
plt.xlabel("Segmento do Cliente")
plt.ylabel("Volume de Registros")
plt.xticks(rotation=0)
plt.legend(title="Gênero")
plt.tight_layout()
plt.show()

print("\n ============================================================================== \n")

#=========================================================================================
# SPRINT 5: RELATÓRIO FINAL E CONCLUSÕES 
#=========================================================================================

# INDICADORES DE LIMPEZA DOS DADOS
print("\n ---> RELATÓRIO DE LIMPEZA DOS DADOS\n")

total_final = len(df_limpo) 
duplicatas_removidas = df_varejo.shape[0] - df_limpo.shape[0]
erros_nd_tratados = (df_varejo['PR_CAT'].isna() | (df_varejo['PR_CAT'] == '#N/D')).sum()

print(f" • Quantidade de linhas salvas após a limpeza: {total_final:,}".replace(",", "."))
print(f" • Quantidade de compras duplicadas apagadas : {duplicatas_removidas:,}".replace(",", "."))
print(f" • Quantidade de erros '#N/D' corrigidos      : {erros_nd_tratados:,}".replace(",", "."))

print("\n ------------#------------ \n")

# PERFIL DE FAMILIAR DOS CLIENTES
print("\n ---> PERFIL FAMILIAR DOS CLIENTES\n")

print(f" • Quantidade de filhos mais comum (Moda) : {df_limpo['CL_FHL'].mode().tolist()} filho(s)")
print(f" • Média de filhos por cliente na base    : {df_limpo['CL_FHL'].mean():.2f} filho(s)")
print("   Conclusão: A grande maioria dos clientes desta base possui família pequena (zero ou um filho).")

print("\n ------------#------------ \n")

# DESTAQUES E INSIGHTS DAS ANÁLISES
print("\n ---> DESTAQUES E INSIGHTS DAS NOSSAS ANÁLISES\n")

genero_campeao = compras_por_genero.index[0]
compras_campeao = compras_por_genero.iloc[0]
ano_campeao = itens_por_ano.sort_values(ascending=False).index[0]
itens_campeao = itens_por_ano.sort_values(ascending=False).iloc[0]
segmento_campeao = tabela_segmento_genero.sum(axis=1).sort_values(ascending=False).index[0]

print(f" • Gênero que fez mais compras únicas: {genero_campeao} ({compras_campeao:,} transações registradas)".replace(",", "."))
print(f" • Ano com maior volume de vendas    : {ano_campeao} ({itens_campeao:,} produtos vendidos)".replace(",", "."))
print(f" • Segmento de cliente mais forte    : Classe {segmento_campeao}")

print("\n ------------#------------ \n")

# CONCLUSÕES DO PROJETO
print("\n ---> CONCLUSÕES E INSIGHTS DO PROJETO\n")
print(" • Tópico 1 (Limpeza): a base de dados foi purificada com sucesso, eliminando os registros duplicados e aplicando a classificação condicional 'Sem Categoria' nos campos vazios da coluna de categoria do produto.")
print(" • Tópico 2 (Família): a análise descritiva comprovou estatisticamente que o público-alvo é composto por famílias pequenas, registrando baixa concentração na coluna de número de filhos dos clientes.")
print(" • Tópico 3 (Demografia): o agrupamento por gênero isolou o volume de transações operacionais e identificou com precisão qual perfil lidera o engajamento comercial baseado no identificador numérico de compra.")
print(" • Tópico 4 (Tempo e Estrutura): a análise temporal e a matriz da tabela dinâmica revelaram de forma exata onde se concentram os volumes operacionais por segmento econômico.")

print("\n ------------#------------ \n")

#=========================================================================================
# SPRINT 6: VERSIONAMENTO E SALVAMENTO DOS DADOS LIMPOS
#=========================================================================================

# Cria o caminho dinâmico para a pasta de dados limpos
url_salvamento = os.path.join(pasta_atual, "..", "data", "processed", "base_varejo_limpa.csv")

# Salva o dataframe limpo em um arquivo CSV
df_limpo.to_csv(url_salvamento, index=False, sep=";", encoding="utf-8-sig")

print("\n ----> TODA A ANÁLISE FOI CONCLUÍDA COM SUCESSO! <----\n")