# ============================================================
# EXERCÍCIO 3 — Duplicatas
# ============================================================

import pandas as pd

caminho = r"filmes_imdb\dados\dados_excel\filmes_imdb.xlsx"
df_imdb = pd.read_excel(caminho)

# -----------------------------------------------------------
# 3.1 Verificando duplicatas pela combinação título + ano
# duplicated() marca como True toda linha que já apareceu antes
# subset define quais colunas usar para comparar
# keep='first' mantém a primeira ocorrência e marca o resto
# -----------------------------------------------------------
print("=== LINHAS DUPLICADAS (mesmo título e ano) ===")

duplicatas = df_imdb[df_imdb.duplicated(
    subset=['titulo', 'ano_lancamento'],
    keep='first'
)]

print(duplicatas[['id_filme', 'titulo', 'ano_lancamento',
                   'rating_imdb', 'duracao_min']])

print(f"\nTotal de duplicatas encontradas: {len(duplicatas)}")

# -----------------------------------------------------------
# 3.2 Removendo as duplicatas
# drop_duplicates() remove as linhas marcadas como duplicata
# keep='first' → mantém a primeira ocorrência de cada grupo
# inplace=True → aplica a mudança no próprio DataFrame
# (sem precisar criar uma nova variável)
# -----------------------------------------------------------
df_imdb.drop_duplicates(
    subset=['titulo', 'ano_lancamento'],
    keep='first',
    inplace=True
)

# Resetando o índice após remoção
# Após deletar linhas, os índices ficam com "buracos" (ex: 0,1,3,5...)
# reset_index reorganiza para 0,1,2,3...
# drop=True evita que o índice antigo vire uma nova coluna
df_imdb.reset_index(drop=True, inplace=True)

print(f"\nLinhas após remoção de duplicatas: {len(df_imdb)}")