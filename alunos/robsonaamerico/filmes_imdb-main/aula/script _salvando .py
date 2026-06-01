# ============================================================
# EXERCÍCIO 6 — Exportando o Dataset Limpo
# ============================================================

import pandas as pd
import numpy as np

caminho = r"filmes_imdb\dados\dados_excel\filmes_imdb.xlsx"
df_imdb = pd.read_excel(caminho)

# --- Aqui você aplicaria todos os tratamentos dos exercícios 2 a 5 ---
# (em aula, a ideia é juntar tudo em um único script de limpeza)

# -----------------------------------------------------------
# Salvando como CSV
# index=False → não salva o índice do pandas como coluna extra
# encoding='utf-8-sig' → garante que acentos apareçam corretamente
# no Excel ao abrir o CSV
# sep=';' → usa ponto e vírgula como separador (padrão brasileiro)
# -----------------------------------------------------------
df_imdb.to_csv(
    r"filmes_imdb\dados\dados_csv\tab_imdb_limpo.csv",
    index=False,
    encoding='utf-8-sig',
    sep=';'
)

# -----------------------------------------------------------
# Salvando como Excel
# index=False → não salva o índice como coluna extra
# sheet_name → define o nome da aba dentro do Excel
# -----------------------------------------------------------
df_imdb.to_excel(
    r"filmes_imdb\dados\dados_excel\tab_imdb_limpo.xlsx",
    index=False,
    sheet_name='filmes_limpo'
)

# -----------------------------------------------------------
# Relatório final de conferência
# -----------------------------------------------------------
print("=== RELATÓRIO FINAL DO DATASET LIMPO ===")
print(f"Total de linhas   : {df_imdb.shape[0]}")
print(f"Total de colunas  : {df_imdb.shape[1]}")
print(f"\nValores nulos restantes:")
print(df_imdb.isnull().sum())
print("\nArquivos salvos com sucesso!")