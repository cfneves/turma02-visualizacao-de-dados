#Identificando e Tratando Valores Nulos  
#Objetivo: Encontrar, visualizar e decidir o que fazer com cada valor ausente.



# ============================================================
# EXERCÍCIO 2 — Valores Nulos
# ============================================================

import pandas as pd

caminho = r"filmes_imdb\dados\dados_excel\filmes_imdb.xlsx"
df_imdb = pd.read_excel(caminho)

# -----------------------------------------------------------
# 2.1 Visualizando as linhas que contêm pelo menos um nulo
# isnull() → cria tabela de True/False para cada célula
# any(axis=1) → verifica se há pelo menos um True na linha
# O resultado é usado para filtrar o DataFrame original
# -----------------------------------------------------------
print("=== LINHAS COM VALORES NULOS ===")
linhas_com_nulo = df_imdb[df_imdb.isnull().any(axis=1)]
print(linhas_com_nulo[['id_filme', 'titulo', 'ano_lancamento',
                         'duracao_min', 'rating_imdb',
                         'orcamento_milhoes', 'bilheteria_dolares']])

# -----------------------------------------------------------
# 2.2 Tratamento 1: Preencher nulos em 'orcamento_milhoes'
# com a MEDIANA da coluna (mais resistente a valores extremos)
# fillna() substitui os NaN pelo valor que você passar
# -----------------------------------------------------------
mediana_orcamento = df_imdb['orcamento_milhoes'].median()
print(f"\nMediana do orçamento: {mediana_orcamento} milhões")

df_imdb['orcamento_milhoes'] = df_imdb['orcamento_milhoes'].fillna(mediana_orcamento)

# -----------------------------------------------------------
# 2.3 Tratamento 2: Preencher nulos em 'bilheteria_dolares'
# com 0 — pois se não há registro, assumimos sem bilheteria
# -----------------------------------------------------------
df_imdb['bilheteria_dolares'] = df_imdb['bilheteria_dolares'].fillna(0)

# -----------------------------------------------------------
# 2.4 Tratamento 3: Remover linhas onde o TÍTULO é nulo
# Um registro sem título não tem utilidade analítica
# dropna() com subset remove apenas as linhas onde
# a coluna especificada é nula
# -----------------------------------------------------------
print(f"\nLinhas antes de remover títulos nulos: {len(df_imdb)}")

df_imdb = df_imdb.dropna(subset=['titulo'])

print(f"Linhas após remover títulos nulos: {len(df_imdb)}")

# -----------------------------------------------------------
# 2.5 Conferindo se ainda restam nulos
# -----------------------------------------------------------
print("\n=== NULOS RESTANTES POR COLUNA ===")
print(df_imdb.isnull().sum())
