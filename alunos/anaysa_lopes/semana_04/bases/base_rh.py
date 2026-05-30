# sempre a primeira célula do notebook, importar o que vc vai usar.
# se apareça erro aqui, a biblioteca não está instalada.
# solução: abra o terminal e rode: pip install pandas openpyxl


import pandas as pd                       # biblioteca de análise de dados
import re                                 # expressão regulares (para limpar texto)
from datetime import datetime             # para eu trabalhar com datas


# confirmar que as importações fucionaram

print(' pandas versão:', pd.__version__)
print(' Bibliotecas importadas com sucesso!')

CAMINHO = r"D:\SENAI\Análise de Dados\Visualização de dados\aula_bases\turma-visualizacao-de-dados\alunos\anaysa_lopes\semana_04\bases\base_rh.csv"

df = pd.read_csv(
    CAMINHO,
    sep=';',                # separador de colunas é ';' e não ','
    encoding='cp1252',      # encoding do windows, para ler acentos
    decimal=','             # virgula como separado decimal
)

print('Dados carregados com sucesso!')
print(f' Total de linhas : {df.shape[0]}')
print(f' Total de colunas: {df.shape[1]}')