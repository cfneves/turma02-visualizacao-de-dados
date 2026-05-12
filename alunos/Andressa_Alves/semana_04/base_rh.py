import pandas as pd
import re
from datetime import datetime

print('pandas versão:', pd.__version__)
print('Bibliotecas carregadas com sucesso! ')

CAMINHO = 'C:\\turma-visualizacao-de-dados\\alunos\\andressa_alves\\semana_04\\base_rh.csv'
df = pd.read_csv(CAMINHO, 
                 sep=';',
                 encoding='cp1252',
                 decimal=','
                 )
print('Dados carregados com sucesso! ')
print('Número de linhas e colunas:', df.shape)
print('Número de linhas: ', df.shape[0])
print('Número de colunas: ', df.shape[1])
