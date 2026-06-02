# Script para análise de dados do IMDb

# Importando as bibliotecas necessárias
import pandas as pd
import openpyxl
 
# saudacao = "Olá Mundo, Olá Alunos, Sabado de sol"
# print(saudacao)


"""

['id_filme', 'titulo', 'ano_lancamento', 
'genero', 'duracao_min', 'rating_imdb', 
'orcamento_milhoes', 'data_lancamento', 
'bilheteria_dolares', 'nome_pais', 'continente', 
'idioma_principal', 'moeda', 'capital', 
'nome_produtora', 'ano_fundacao', 'pais_sede']

"""

caminho = r"filmes_imdb\dados\dados_excel\filmes_imdb.xlsx"

df_imdb = pd.read_excel(caminho)

print(df_imdb.head(10))

print(df_imdb.info())

print(df_imdb.shape)

print(df_imdb.columns.tolist())

#to_save 

df_imdb.to_csv(r"C:\projects\imdb\filmes_imdb\dados\dados_csv\tab_imdb.csv", index=False)

df_imdb.to_excel(r"C:\projects\imdb\filmes_imdb\dados\dados_excel\tab_imdb.xlsx", index=False)

print("Fim")