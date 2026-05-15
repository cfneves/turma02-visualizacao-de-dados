import pandas as pd
import re
from datetime import datetime
from pathlib import Path

print('pandas versão:', pd.__version__)
print('Bibliotecas carregadas com sucesso! ')

CAMINHO = Path(__file__).parent / 'base_rh.csv'
df = pd.read_csv(CAMINHO,
                 sep=';',
                 encoding='cp1252',
                 decimal=','
                 )
print('Dados carregados com sucesso! ')
print('Número de linhas e colunas:', df.shape)
print('Número de linhas: ', df.shape[0])
print('Número de colunas: ', df.shape[1])
