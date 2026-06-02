import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

print("\n" + "="*80) 
print("SPRINT 1: IMPORTAÇÃO DOS DADOS")
print("="*80)

### Sprint 1: Importação dos Dados
# Carregando o dataset "Base Varejo" do Kaggle
BASE_DIR = Path("C:/Users/jakso_sdyff07/OneDrive/Documentos/git_sc_tec")
arquivo_dataset = BASE_DIR / "Base_Varejo.csv"

# Lendo o arquivo CSV com separador ';' (ponto-e-vírgula)
# O encoding é 'latin-1' para suportar caracteres especiais em português
df = pd.read_csv(arquivo_dataset, sep=';', encoding='latin-1')

# Exibindo informações básicas sobre o dataset
print("\n1. INFORMAÇÕES BÁSICAS DO DATASET:")
print("-" * 80)
print(f"   Número de registros (linhas): {df.shape[0]:,}")
print(f"   Número de colunas: {df.shape[1]}")
print(f"   Tamanho total: {df.shape[0] * df.shape[1]:,} células")

# Exibindo os nomes e tipos de dados de cada coluna
print("\n2. COLUNAS E TIPOS DE DADOS:")
print("-" * 80)
print(df.dtypes)

# Exibindo as primeiras 5 linhas do dataset
print("\n3. PRIMEIRAS 5 REGISTROS DO DATASET:")
print("-" * 80)
print(df.head())

# Exibindo as últimas 5 linhas do dataset
print("\n4. ÚLTIMAS 5 REGISTROS DO DATASET:")
print("-" * 80)
print(df.tail())

# ============================================================================
# SPRINT 2: TRANSFORMAÇÃO DE STRINGS, INTEGER E FLOAT E DATETIME
# ============================================================================
# Descrição: Desenvolvimento das funções de limpeza de texto, inteiros e 
#            decimais usando métodos e expressões regulares.

print("\n" + "="*80)
print("SPRINT 2: TRANSFORMAÇÃO DE STRINGS, INTEGER, FLOAT E DATETIME")
print("="*80)

# Função para limpar e padronizar strings
def limpar_string(valor):
    """
    Função para limpar strings removendo espaços em branco extras
    e convertendo para maiúsculas para padronização.
    """
    if pd.isna(valor):
        return valor
    return str(valor).strip().upper()

# Função para converter para inteiro com tratamento de erros
def converter_inteiro(valor):
    """
    Função para converter valores para inteiro, retornando NaN em caso de erro.
    """
    try:
        return int(float(valor))
    except (ValueError, TypeError):
        return np.nan

# Função para converter para float com tratamento de erros
def converter_float(valor):
    """
    Função para converter valores para float, retornando NaN em caso de erro.
    """
    try:
        return float(valor)
    except (ValueError, TypeError):
        return np.nan

# Função para converter para datetime com tratamento de erros
def converter_datetime(valor):
    """
    Função para converter valores para datetime no formato DD/MM/YYYY,
    retornando NaT (Not a Time) em caso de erro.
    """
    try:
        return pd.to_datetime(valor, format='%d/%m/%Y')
    except (ValueError, TypeError):
        return pd.NaT

print("\n1. APLICANDO TRANSFORMAÇÕES DE TIPO DE DADOS:")
print("-" * 80)

# Convertendo a coluna DATA para datetime
print("   - Convertendo coluna DATA para datetime...")
df['DATA'] = df['DATA'].apply(converter_datetime)

# Convertendo colunas numéricas para inteiro
print("   - Convertendo colunas numéricas para inteiro...")
df['CO_ID'] = df['CO_ID'].apply(converter_inteiro)
df['CL_ID'] = df['CL_ID'].apply(converter_inteiro)
df['CL_FHL'] = df['CL_FHL'].apply(converter_inteiro)  # Número de filhos
df['PR_ID'] = df['PR_ID'].apply(converter_inteiro)

# Limpando strings (removendo espaços e padronizando)
print("   - Limpando strings...")
df['CL_GENERO'] = df['CL_GENERO'].apply(limpar_string)
df['CL_SEG'] = df['CL_SEG'].apply(limpar_string)
df['PR_CAT'] = df['PR_CAT'].apply(limpar_string)
df['PR_NOME'] = df['PR_NOME'].apply(limpar_string)

print("Transformações aplicadas com sucesso!")

# ============================================================================
# SPRINT 3: LIMPEZA DE NULOS E DUPLICATAS
# ============================================================================
# Descrição: Aplicação das condicionais e funções para identificação e 
#            substituição de valores vazios e de str para valores de data 
#            tipo datetime, na tabela de varejo.

print("\n" + "="*80)
print("SPRINT 3: LIMPEZA DE NULOS E DUPLICATAS")
print("="*80)

# Verificando valores nulos antes da limpeza
print("\n1. VERIFICAÇÃO DE VALORES NULOS ANTES DA LIMPEZA:")
print("-" * 80)
valores_nulos = df.isnull().sum()
print(valores_nulos[valores_nulos > 0])

# Removendo colunas completamente vazias (todas as colunas extras no final)
print("\n2. REMOVENDO COLUNAS VAZIAS:")
print("-" * 80)
colunas_vazias = df.columns[df.isnull().all()].tolist()
if colunas_vazias:
    print(f"   Colunas removidas: {colunas_vazias}")
    df = df.dropna(axis=1, how='all')
else:
    print("Nenhuma coluna completamente vazia encontrada.")

# Tratando valores nulos em colunas específicas
print("\n3. TRATAMENTO DE VALORES NULOS:")
print("-" * 80)

# Para DATA: removendo linhas com datas inválidas
print("Removendo linhas com datas inválidas...")
df_antes = len(df)
df = df.dropna(subset=['DATA'])
df_depois = len(df)
print(f"Linhas removidas: {df_antes - df_depois}")

# Para CL_GENERO: preenchendo com 'DESCONHECIDO' se vazio
print("Preenchendo CL_GENERO com 'DESCONHECIDO' se vazio...")
df['CL_GENERO'] = df['CL_GENERO'].fillna('DESCONHECIDO')

# Para CL_FHL (Número de filhos): preenchendo com a moda (valor mais frequente)
print("Preenchendo CL_FHL (Número de filhos) com a moda...")
moda_filhos = df['CL_FHL'].mode()[0] if not df['CL_FHL'].mode().empty else 0
df['CL_FHL'] = df['CL_FHL'].fillna(moda_filhos)

# Para CL_EC: preenchendo com a moda
print("Preenchendo CL_EC com a moda...")
moda_ec = df['CL_EC'].mode()[0] if not df['CL_EC'].mode().empty else 0
df['CL_EC'] = df['CL_EC'].fillna(moda_ec)

# Para CL_SEG: preenchendo com 'DESCONHECIDO' se vazio
print("Preenchendo CL_SEG com 'DESCONHECIDO' se vazio...")
df['CL_SEG'] = df['CL_SEG'].fillna('DESCONHECIDO')

# Para PR_CAT: preenchendo com 'DESCONHECIDO' se vazio
print("Preenchendo PR_CAT com 'DESCONHECIDO' se vazio...")
df['PR_CAT'] = df['PR_CAT'].fillna('DESCONHECIDO')

# Para PR_NOME: preenchendo com 'DESCONHECIDO' se vazio
print("Preenchendo PR_NOME com 'DESCONHECIDO' se vazio...")
df['PR_NOME'] = df['PR_NOME'].fillna('DESCONHECIDO')

# Verificando valores nulos após tratamento
print("\n4. VERIFICAÇÃO DE VALORES NULOS APÓS TRATAMENTO:")
print("-" * 80)
valores_nulos_apos = df.isnull().sum()
if valores_nulos_apos.sum() == 0:
    print("Nenhum valor nulo encontrado!")
else:
    print(valores_nulos_apos[valores_nulos_apos > 0])

# Verificando e removendo duplicatas
print("\n5. VERIFICAÇÃO E REMOÇÃO DE DUPLICATAS:")
print("-" * 80)
duplicatas_antes = df.duplicated().sum()
print(f"Duplicatas encontradas: {duplicatas_antes}")

if duplicatas_antes > 0:
    df = df.drop_duplicates()
    duplicatas_depois = df.duplicated().sum()
    print(f"Duplicatas removidas: {duplicatas_antes - duplicatas_depois}")
    print(f"Registros após remoção: {len(df):,}")
else:
    print("Nenhuma duplicata encontrada!")

# Verificando inconsistências (datas inválidas, categorias vazias, etc.)
print("\n6. VERIFICAÇÃO DE INCONSISTÊNCIAS:")
print("-" * 80)

# Verificando se há datas no futuro ou muito antigas
datas_futuro = df[df['DATA'] > datetime.now()].shape[0]
datas_antigas = df[df['DATA'] < pd.Timestamp('2010-01-01')].shape[0]
print(f"Datas no futuro: {datas_futuro}")
print(f"Datas antes de 2010: {datas_antigas}")

# Verificando categorias vazias ou desconhecidas
print(f"Categorias desconhecidas: {(df['PR_CAT'] == 'DESCONHECIDO').sum()}")
print(f"Gêneros desconhecidos: {(df['CL_GENERO'] == 'DESCONHECIDO').sum()}")

# Verificando valores negativos ou zero em campos que não deveriam ter
print(f"IDs de cliente inválidos (zero ou negativo): {(df['CL_ID'] <= 0).sum()}")
print(f"IDs de produto inválidos (zero ou negativo): {(df['PR_ID'] <= 0).sum()}")

print("\n7. RESUMO DO DATASET APÓS LIMPEZA:")
print("-" * 80)
print(f"Número de registros: {df.shape[0]:,}")
print(f"Número de colunas: {df.shape[1]}")
print(f"Período de dados: {df['DATA'].min().date()} a {df['DATA'].max().date()}")

# ============================================================================
# SPRINT 4: ESTATÍSTICA DESCRITIVA
# ============================================================================
# Descrição: Aplicação das funções estatísticas para coletar parâmetros da 
#            coluna de Número de filhos do cliente.

print("\n" + "="*80)
print("SPRINT 4: ESTATÍSTICA DESCRITIVA")
print("="*80)

# Coluna de interesse: CL_FHL (Número de filhos)
coluna_filhos = df['CL_FHL']

print("\n1. ESTATÍSTICAS DESCRITIVAS - NÚMERO DE FILHOS (CL_FHL):")
print("-" * 80)

# Calculando as estatísticas solicitadas
media = coluna_filhos.mean()
mediana = coluna_filhos.median()
desvio_padrao = coluna_filhos.std()
moda = coluna_filhos.mode()[0] if not coluna_filhos.mode().empty else np.nan
maximo = coluna_filhos.max()
minimo = coluna_filhos.min()
contagem = coluna_filhos.count()

# Exibindo as estatísticas
print(f"   Média (Mean):              {media:.4f}")
print(f"   Mediana (Median):          {mediana:.4f}")
print(f"   Desvio Padrão (Std Dev):   {desvio_padrao:.4f}")
print(f"   Moda (Mode):               {moda:.0f}")
print(f"   Máximo (Max):              {maximo:.0f}")
print(f"   Mínimo (Min):              {minimo:.0f}")
print(f"   Contagem (Count):          {contagem:,}")

# Calculando quartis
q1 = coluna_filhos.quantile(0.25)
q3 = coluna_filhos.quantile(0.75)
iqr = q3 - q1

print(f"\n   Quartil 1 (Q1 - 25%):      {q1:.0f}")
print(f"   Quartil 3 (Q3 - 75%):      {q3:.0f}")
print(f"   Intervalo Interquartil:    {iqr:.0f}")

# Distribuição de frequência
print("\n2. DISTRIBUIÇÃO DE FREQUÊNCIA - NÚMERO DE FILHOS:")
print("-" * 80)
distribuicao = coluna_filhos.value_counts().sort_index()
print(distribuicao)

# Percentuais
print("\n3. PERCENTUAIS - NÚMERO DE FILHOS:")
print("-" * 80)
percentuais = (coluna_filhos.value_counts(normalize=True).sort_index() * 100)
for valor, percentual in percentuais.items():
    print(f"   {valor:.0f} filhos: {percentual:.2f}%")

# ============================================================================
# SPRINT 5: AGRUPAMENTOS E ANÁLISE DE PADRÕES
# ============================================================================
# Descrição: Exploração de padrões de agrupamento com pelo menos dois 
#            agrupamentos (por exemplo: gênero com mais vendas, compras).

print("\n" + "="*80)
print("SPRINT 5: AGRUPAMENTOS E ANÁLISE DE PADRÕES")
print("="*80)

# Agrupamento 1: Por Gênero (CL_GENERO)
print("\n1. AGRUPAMENTO POR GÊNERO DO CLIENTE:")
print("-" * 80)

# Contando o número de compras por gênero
compras_por_genero = df['CL_GENERO'].value_counts()
print("\n   Número de compras por gênero:")
print(compras_por_genero)

# Percentual de compras por gênero
print("\n   Percentual de compras por gênero:")
percentual_genero = (compras_por_genero / compras_por_genero.sum() * 100)
for genero, percentual in percentual_genero.items():
    print(f"   {genero}: {percentual:.2f}%")

# Agrupamento 2: Por Categoria de Produto (PR_CAT)
print("\n2. AGRUPAMENTO POR CATEGORIA DE PRODUTO:")
print("-" * 80)

# Contando o número de compras por categoria
compras_por_categoria = df['PR_CAT'].value_counts()
print("\n   Número de compras por categoria:")
print(compras_por_categoria)

# Percentual de compras por categoria
print("\n   Percentual de compras por categoria:")
percentual_categoria = (compras_por_categoria / compras_por_categoria.sum() * 100)
for categoria, percentual in percentual_categoria.items():
    print(f"   {categoria}: {percentual:.2f}%")

# Agrupamento 3: Por Segmento de Cliente (CL_SEG)
print("\n3. AGRUPAMENTO POR SEGMENTO DE CLIENTE:")
print("-" * 80)

# Contando o número de compras por segmento
compras_por_segmento = df['CL_SEG'].value_counts()
print("\n   Número de compras por segmento:")
print(compras_por_segmento)

# Agrupamento 4: Por Mês (extraído da coluna DATA)
print("\n4. AGRUPAMENTO POR MÊS:")
print("-" * 80)

# Extraindo mês e ano da coluna DATA
df['MES_ANO'] = df['DATA'].dt.to_period('M')

# Contando o número de compras por mês
compras_por_mes = df['MES_ANO'].value_counts().sort_index()
print("\n   Número de compras por mês:")
print(compras_por_mes)

# Agrupamento 5: Análise cruzada - Gênero vs Categoria
print("\n5. ANÁLISE CRUZADA - GÊNERO vs CATEGORIA DE PRODUTO:")
print("-" * 80)

# Criando uma tabela cruzada (pivot table)
tabela_cruzada = pd.crosstab(df['CL_GENERO'], df['PR_CAT'], margins=True)
print("\n   Tabela cruzada (Gênero x Categoria):")
print(tabela_cruzada)

# ============================================================================
# SPRINT 6: CONCLUSÕES E RELATÓRIO FINAL
# ============================================================================
# Descrição: Construção dos contadores do relatório final exibido no terminal, 
#            finalização da documentação com reflexão teórica.

print("\n" + "="*80)
print("SPRINT 6: CONCLUSÕES E RELATÓRIO FINAL")
print("="*80)

print("\n1. RESUMO:")
print("-" * 80)
print(f"""
   O dataset "Base Varejo" foi analisado com sucesso, contendo {df.shape[0]:,} 
   registros de compras e {df.shape[1]} colunas de informações sobre clientes, 
   produtos e transações.
   
   Período de análise: {df['DATA'].min().date()} a {df['DATA'].max().date()}
   
   Total de clientes únicos: {df['CL_ID'].nunique():,}
   Total de produtos únicos: {df['PR_ID'].nunique():,}
   Total de categorias: {df['PR_CAT'].nunique()}
""")

print("\n2. PRINCIPAIS INSIGHTS:")
print("-" * 80)

# Insight 1: Distribuição de clientes por gênero
genero_dominante = compras_por_genero.idxmax()
percentual_dominante = (compras_por_genero.max() / compras_por_genero.sum() * 100)
print(f"""
   a) DISTRIBUIÇÃO DE CLIENTES POR GÊNERO:
      - Gênero dominante: {genero_dominante} ({percentual_dominante:.1f}% das compras)
      - Distribuição equilibrada: {percentual_dominante < 60}
""")

# Insight 2: Categoria mais vendida
categoria_top = compras_por_categoria.idxmax()
compras_top = compras_por_categoria.max()
percentual_top = (compras_top / compras_por_categoria.sum() * 100)
print(f"""
   b) CATEGORIA MAIS VENDIDA:
      - Categoria: {categoria_top}
      - Número de compras: {compras_top:,} ({percentual_top:.1f}%)
""")

# Insight 3: Número médio de filhos
print(f"""
   c) PERFIL FAMILIAR DOS CLIENTES:
      - Número médio de filhos: {media:.2f}
      - Número mais frequente de filhos: {moda:.0f}
      - Variação (desvio padrão): {desvio_padrao:.2f}
      - Maioria dos clientes tem entre {q1:.0f} e {q3:.0f} filhos
""")

# Insight 4: Tendência temporal
mes_mais_ativo = compras_por_mes.idxmax()
compras_mes_ativo = compras_por_mes.max()
print(f"""
   d) TENDÊNCIA TEMPORAL:
      - Mês mais ativo: {mes_mais_ativo} ({compras_mes_ativo:,} compras)
      - Variação mensal: {compras_por_mes.std():.0f} compras (desvio padrão)
""")

# Insight 5: Segmentação de clientes
segmento_top = compras_por_segmento.idxmax()
print(f"""
   e) SEGMENTAÇÃO DE CLIENTES:
      - Segmento principal: {segmento_top}
      - Número de segmentos identificados: {df['CL_SEG'].nunique()}
""")

print("\n3. PROBLEMAS REMANESCENTES E RECOMENDAÇÕES:")
print("-" * 80)
print(f"""
   a) QUALIDADE DOS DADOS:
      - Registros com gênero desconhecido: {(df['CL_GENERO'] == 'DESCONHECIDO').sum():,}
      - Registros com segmento desconhecido: {(df['CL_SEG'] == 'DESCONHECIDO').sum():,}
      - Recomendação: Investigar a origem desses valores ausentes
   
   b) CONSISTÊNCIA TEMPORAL:
      - Período coberto: {(df['DATA'].max() - df['DATA'].min()).days} dias
      - Lacunas potenciais: Verificar se há dias sem registros
      - Recomendação: Investigar padrões sazonais
   
   c) COBERTURA DE DADOS:
      - Clientes únicos: {df['CL_ID'].nunique():,}
      - Produtos únicos: {df['PR_ID'].nunique():,}
      - Recomendação: Aumentar a cobertura de produtos para análises mais robustas
   
   d) ANÁLISES FUTURAS:
      - Correlação entre número de filhos e padrão de compra
      - Análise de sazonalidade por categoria
      - Segmentação de clientes mais refinada (RFM - Recency, Frequency, Monetary)
      - Previsão de demanda por categoria
""")

print("\n4. CONCLUSÃO:")
print("-" * 80)
print(f"""
   A análise exploratória do dataset "Base Varejo" foi concluída com sucesso.
   Os dados foram limpos, transformados e analisados, revelando padrões 
   importantes sobre o comportamento de compra dos clientes.
   
   O dataset está pronto para análises mais avançadas, modelagem preditiva
   ou alimentação de dashboards de Business Intelligence.
   
   Total de registros processados: {df.shape[0]:,}
   Total de colunas utilizadas: {df.shape[1]}
   Taxa de completude: {((df.shape[0] * df.shape[1] - df.isnull().sum().sum()) / (df.shape[0] * df.shape[1]) * 100):.2f}%
""")

# ============================================================================
# SALVANDO O DATASET LIMPO
# ============================================================================
# Salvando o dataframe limpo em um arquivo CSV para uso futuro

print("\n" + "="*80)
print("SALVANDO DATASET LIMPO")
print("="*80)

# Removendo a coluna temporária MES_ANO antes de salvar
df_salvo = df.drop('MES_ANO', axis=1)

# Salvando em CSV
arquivo_saida = 'C:\\Users\\jakso_sdyff07\\OneDrive\\Documentos\\git_sc_tec\\Base_Varejo_Limpo.csv'
df_salvo.to_csv(arquivo_saida, sep=';', encoding='latin-1', index=False)
print(f"\n✓ Dataset limpo salvo em: {arquivo_saida}")

# Exibindo informações finais
print("\n" + "="*80)
print("ANÁLISE CONCLUÍDA COM SUCESSO!")
print("="*80)
print(f"\nArquivo de saída: {arquivo_saida}")
print(f"Registros processados: {df_salvo.shape[0]:,}")
print(f"Colunas: {df_salvo.shape[1]}")
print(f"Data/Hora de conclusão: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
print("\n" + "="*80 + "\n")
