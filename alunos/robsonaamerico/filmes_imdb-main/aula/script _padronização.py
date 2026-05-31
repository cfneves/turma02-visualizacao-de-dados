# ============================================================
# EXERCÍCIO 4 — Padronização de Texto
# ============================================================

import pandas as pd

caminho = r"filmes_imdb\dados\dados_excel\filmes_imdb.xlsx"
df_imdb = pd.read_excel(caminho)

# -----------------------------------------------------------
# 4.1 Verificando os valores únicos de 'genero'
# unique() lista todos os valores distintos de uma coluna
# Aqui vamos ver o caos: "Action", "ACTION", "Acton", etc.
# -----------------------------------------------------------
print("=== GÊNEROS ÚNICOS (antes da limpeza) ===")
print(sorted(df_imdb['genero'].dropna().unique()))

# -----------------------------------------------------------
# 4.2 Padronizando a coluna 'genero'
# .str.strip() → remove espaços no início e no final do texto
# .str.title() → coloca a primeira letra maiúscula em cada palavra
# Ex: "ACTION" → "Action" | " drama " → "Drama"
# -----------------------------------------------------------
df_imdb['genero'] = df_imdb['genero'].str.strip().str.title()

# -----------------------------------------------------------
# 4.3 Corrigindo abreviações e variações conhecidas
# replace() substitui um valor específico por outro
# Usamos um dicionário: {'valor_antigo': 'valor_novo'}
# -----------------------------------------------------------
mapa_generos = {
    'Anim'            : 'Animation',
    'Scifi'           : 'Sci-Fi',
    'Science Fiction' : 'Sci-Fi',
    'Science-Fiction' : 'Sci-Fi',
    'Thriler'         : 'Thriller',
    'Acton'           : 'Action',
    'Fantasia'        : 'Fantasy',
}

df_imdb['genero'] = df_imdb['genero'].replace(mapa_generos)

print("\n=== GÊNEROS ÚNICOS (após limpeza) ===")
print(sorted(df_imdb['genero'].dropna().unique()))

# -----------------------------------------------------------
# 4.4 Padronizando 'nome_pais' (caixa alta/baixa)
# .str.strip().str.title() resolve "estados unidos" → "Estados Unidos"
# -----------------------------------------------------------
print("\n=== PAÍSES ÚNICOS (antes) ===")
print(df_imdb['nome_pais'].dropna().unique())

df_imdb['nome_pais'] = df_imdb['nome_pais'].str.strip().str.title()

print("\n=== PAÍSES ÚNICOS (após) ===")
print(df_imdb['nome_pais'].dropna().unique())