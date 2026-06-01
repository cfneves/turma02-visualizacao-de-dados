# ============================================================
# EXERCÍCIO 5 — Outliers e Valores Inválidos
# ============================================================

import pandas as pd
import numpy as np  # numpy: biblioteca para operações matemáticas

caminho = r"filmes_imdb\dados\dados_excel\filmes_imdb.xlsx"
df_imdb = pd.read_excel(caminho)

# -----------------------------------------------------------
# 5.1 Verificando o rating_imdb
# O IMDb vai de 0.0 a 10.0 — qualquer valor fora disso é inválido
# Vamos identificar os filmes com rating inválido
# -----------------------------------------------------------
print("=== RATINGS FORA DO RANGE (0 a 10) ===")
ratings_invalidos = df_imdb[
    (df_imdb['rating_imdb'] < 0) | (df_imdb['rating_imdb'] > 10)
]
print(ratings_invalidos[['id_filme', 'titulo', 'rating_imdb']])

# -----------------------------------------------------------
# Substituindo ratings inválidos por NaN (dado ausente)
# np.nan é o valor padrão do pandas para "sem dado"
# Usamos np.where: se a condição for verdadeira → NaN
#                  se for falsa → mantém o valor original
# -----------------------------------------------------------
df_imdb['rating_imdb'] = np.where(
    (df_imdb['rating_imdb'] < 0) | (df_imdb['rating_imdb'] > 10),
    np.nan,          # valor substituto quando a condição é verdadeira
    df_imdb['rating_imdb']  # valor original quando a condição é falsa
)

# Preenchendo os NaN com a mediana dos ratings válidos
mediana_rating = df_imdb['rating_imdb'].median()
df_imdb['rating_imdb'] = df_imdb['rating_imdb'].fillna(mediana_rating)

print(f"\nMediana usada para substituir ratings inválidos: {mediana_rating}")

# -----------------------------------------------------------
# 5.2 Verificando 'duracao_min'
# A coluna tem valores como "152 min", "abc", "0"
# Precisamos converter para número e tratar os inválidos
# pd.to_numeric() tenta converter para número
# errors='coerce' → transforma o que não conseguir em NaN
# (em vez de dar erro e parar o programa)
# -----------------------------------------------------------
print("\n=== DURAÇÃO ANTES DA CONVERSÃO ===")
print(df_imdb['duracao_min'].unique())

df_imdb['duracao_min'] = pd.to_numeric(df_imdb['duracao_min'], errors='coerce')

# Substituindo duração = 0 por NaN (0 minutos não faz sentido)
df_imdb['duracao_min'] = df_imdb['duracao_min'].replace(0, np.nan)

# Preenchendo os NaN com a mediana das durações válidas
mediana_duracao = df_imdb['duracao_min'].median()
df_imdb['duracao_min'] = df_imdb['duracao_min'].fillna(mediana_duracao)

print("\n=== DURAÇÃO APÓS LIMPEZA (estatísticas) ===")
print(df_imdb['duracao_min'].describe())

# -----------------------------------------------------------
# 5.3 Verificando 'ano_lancamento'
# Existem valores como "197X" e "201" que não são anos válidos
# Convertemos para número e filtramos anos impossíveis
# -----------------------------------------------------------
df_imdb['ano_lancamento'] = pd.to_numeric(
    df_imdb['ano_lancamento'], errors='coerce'
)

# Anos válidos para filmes: entre 1888 (primeiro filme da história)
# e o ano atual
registros_invalidos = df_imdb[
    (df_imdb['ano_lancamento'] < 1888) |
    (df_imdb['ano_lancamento'] > 2026)
]
print("\n=== ANOS DE LANÇAMENTO INVÁLIDOS ===")
print(registros_invalidos[['id_filme', 'titulo', 'ano_lancamento']])

# Substituindo por NaN
df_imdb['ano_lancamento'] = np.where(
    (df_imdb['ano_lancamento'] < 1888) | (df_imdb['ano_lancamento'] > 2026),
    np.nan,
    df_imdb['ano_lancamento']
)