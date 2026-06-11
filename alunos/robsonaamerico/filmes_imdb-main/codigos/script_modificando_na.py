
"""
Contexto: O que temos no dataset
Olhando o filmes_imdb.xlsx, temos alguns casos perfeitos para praticar:

---------------------------------------------------------------------
Linha  | (index)	| Filme	                 | Problema
---------------------------------------------------------------------
36     | (row 37)	| Inglourious Basterds   | bilheteria_dolares vazia
42     | (row 43)	| Pulp Fiction	         | duracao_min vazia
46     | (row 47)	| Forrest Gump	         | data_lancamento vazia
49     |(row 50)	| (título vazio)         | titulo vazio
---------------------------------------------------------------------

Obs.: Note que são problemas pontuais, ou seja, apenas um valor errado ou ausente em cada linha. 
Isso é ótimo para praticar a modificação de células específicas usando .loc[].

"""

# MÉTODOS/FORMAS POSSÍVEIS DE RESOLVE RO PROBLEMA 

# 1

# ============================================================
# MODIFICANDO UMA CÉLULA ESPECÍFICA COM .loc[]
# ============================================================

import pandas as pd

caminho = r"filmes_imdb\dados\dados_excel\filmes_imdb.xlsx"
df_imdb = pd.read_excel(caminho)

# -----------------------------------------------------------
# SINTAXE BÁSICA:
# df.loc[índice_da_linha, 'nome_da_coluna'] = novo_valor
#
# → índice_da_linha: número da linha no DataFrame (começa em 0)
# → 'nome_da_coluna': exatamente o nome da coluna
# → novo_valor: o valor que você quer inserir
# -----------------------------------------------------------

# CASO 1: Inglourious Basterds (index 36) — bilheteria vazia
# O filme arrecadou $321.5 milhões de dólares
df_imdb.loc[36, 'bilheteria_dolares'] = 321500000

print("Linha 36 após correção:")
print(df_imdb.loc[36, ['titulo', 'bilheteria_dolares']])

# -----------------------------------------------------------

# CASO 2: Pulp Fiction (index 42) — duração vazia
# O filme tem 154 minutos de duração
df_imdb.loc[42, 'duracao_min'] = 154

print("\nLinha 42 após correção:")
print(df_imdb.loc[42, ['titulo', 'duracao_min']])

# -----------------------------------------------------------

# CASO 3: Forrest Gump duplicata (index 46) — data_lancamento vazia
# Data de lançamento: 06 de julho de 1994
df_imdb.loc[46, 'data_lancamento'] = pd.Timestamp('1994-07-06')

print("\nLinha 46 após correção:")
print(df_imdb.loc[46, ['titulo', 'data_lancamento']])

# -----------------------------------------------------------

# CASO 4: Linha 49 — título vazio (linha sem nome de filme)
# Vamos nomear como 'Desconhecido' para manter o registro
df_imdb.loc[49, 'titulo'] = 'Desconhecido'

print("\nLinha 49 após correção:")
print(df_imdb.loc[49, ['titulo', 'ano_lancamento', 'genero']])

print("\nFim do script de modificação de células específicas: Método 1.")

# ===========================================================================


# 2

# ============================================================
# LOCALIZANDO A LINHA PELO CONTEÚDO E DEPOIS EDITANDO
# ============================================================

import pandas as pd

caminho = r"filmes_imdb\dados\dados_excel\filmes_imdb.xlsx"
df_imdb = pd.read_excel(caminho)

# -----------------------------------------------------------
# PASSO 1: Encontrar o índice da linha pelo título do filme
# .index retorna os índices das linhas onde a condição é True
# [0] pega o primeiro resultado encontrado
# -----------------------------------------------------------
indice = df_imdb[df_imdb['titulo'] == 'Inglourious Basterds'].index[0]

print(f"Índice encontrado para 'Inglourious Basterds': {indice}")

# PASSO 2: Usar o índice encontrado para corrigir a célula
df_imdb.loc[indice, 'bilheteria_dolares'] = 321500000

print(f"Valor corrigido: {df_imdb.loc[indice, 'bilheteria_dolares']}")

# -----------------------------------------------------------
# EXEMPLO EXTRA: Corrigindo múltiplas colunas de UMA vez
# na mesma linha usando um dicionário
# -----------------------------------------------------------

# Queremos preencher nome_pais, continente e idioma_principal
# para a linha 47 (Unknown Movie) que tem #N/A
indice_unknown = df_imdb[df_imdb['titulo'] == 'Unknown Movie'].index[0]

# Atualizando várias colunas de uma vez com .loc e um dicionário
df_imdb.loc[indice_unknown, ['nome_pais', 'continente', 'idioma_principal']] = [
    'França',   # nome_pais
    'Europa',   # continente
    'Francês'   # idioma_principal
]

print("\nUnknown Movie após correção:")
print(df_imdb.loc[indice_unknown,
      ['titulo', 'nome_pais', 'continente', 'idioma_principal']])


print("\nFim do script de modificação de células específicas: Método 2.")

# ===========================================================================

# 3

# ============================================================
# PREENCHENDO SOMENTE CÉLULAS VAZIAS (NaN)
# SEM SOBRESCREVER VALORES EXISTENTES
# ============================================================

import pandas as pd
import numpy as np

caminho = r"filmes_imdb\dados\dados_excel\filmes_imdb.xlsx"
df_imdb = pd.read_excel(caminho)

# -----------------------------------------------------------
# PASSO 1: Verificar se a célula está realmente vazia
# pd.isna() retorna True se o valor for NaN, None ou NaT
# Usamos isso como uma "trava de segurança" antes de editar
# -----------------------------------------------------------

linha   = 36                    # índice da linha
coluna  = 'bilheteria_dolares'  # coluna que queremos verificar

if pd.isna(df_imdb.loc[linha, coluna]):
    # A célula está vazia → podemos preencher com segurança
    df_imdb.loc[linha, coluna] = 321500000
    print(f"Célula preenchida com sucesso na linha {linha}!")
else:
    # A célula já tem dado → não fazemos nada
    print(f"Atenção: a linha {linha} já tem valor: {df_imdb.loc[linha, coluna]}")

# -----------------------------------------------------------
# VERIFICAÇÃO FINAL: Mostrar a linha completa após a edição
# -----------------------------------------------------------
print("\nLinha completa após verificação:")
print(df_imdb.loc[linha])

print("\nFim do script de modificação de células específicas: Método 3.")

# ===========================================================================




"""

Resumo Visual — Quando usar cada método
---------------------------------------------------------------------:
# ✅ Você SABE o índice e quer editar 1 coluna
df_imdb.loc[36, 'bilheteria_dolares'] = 321500000

# ✅ Você SABE o índice e quer editar VÁRIAS colunas de uma vez
df_imdb.loc[36, ['nome_pais', 'continente']] = ['França', 'Europa']

# ✅ Você NÃO sabe o índice — localiza pelo título primeiro
idx = df_imdb[df_imdb['titulo'] == 'Inglourious Basterds'].index[0]
df_imdb.loc[idx, 'bilheteria_dolares'] = 321500000

# ✅ Quer editar SOMENTE SE estiver vazio (mais seguro)
if pd.isna(df_imdb.loc[36, 'bilheteria_dolares']):
    df_imdb.loc[36, 'bilheteria_dolares'] = 321500000

"""