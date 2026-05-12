import pandas as pd                       # biblioteca de análise de dados
import re                                 # expressão regulares (para limpar texto)
from datetime import datetime             # para eu trabalhar com datas

print(' pandas versão:', pd.__version__)
print(' Bibliotecas importadas com sucesso!')

CAMINHO = r"C:\Users\beatr\OneDrive\CURSO ANÁLISE DE DADOS\GIT E GITHUB - AULA VISUALIZACAO DE DADOS\turma-visualizacao-de-dados\alunos\beatriz_bruns\semana_04\aula_01\base_rh.csv"

df = pd.read_csv(
    CAMINHO,
    sep=';',                # separador de colunas é ';' e não ','
    encoding='cp1252',      # encoding do windows, para ler acentos
    decimal=','             # virgula como separado decimal
)

print('Dados carregados com sucesso!')
print(f' Total de linhas : {df.shape[0]}')
print(f' Total de colunas: {df.shape[1]}')

df.head(5)