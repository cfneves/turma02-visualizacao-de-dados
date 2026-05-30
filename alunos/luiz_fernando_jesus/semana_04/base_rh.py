# sempre a primeira célula do notebook, importar o que vc vai usar de bibliotecas.
# se apareça erro aqui, a biblioteca não está instalada.
# solução: abra o terminal e rode: pip install pandas openpyxl

import pandas as pd  # biblioteca de análise de dados
import re  # expressão regulares (para limpar texto)
from datetime import datetime  # para eu trabalhar com datas

# confirmar que as importações fucionaram

print(" pandas versão:", pd.__version__)
print(" Bibliotecas importadas com sucesso!")

# pd.read_csv()  # para ler arquivos .csv
# CAMINHO = onde está o arquivo. Como ele está na MESMA pasta que este notebook..................????????
# basta passar o nome do arquivo, entre aspas, para a função ler o arquivo e criar um DataFrame (tabela) com os dados.

CAMINHO = r"C:\Users\ferna\OneDrive\Área de Trabalho\SCTEC-Pratica\turma-visualizacao-de-dados\alunos\claudio_neves\semana_04\base_rh.csv"

df = pd.read_csv(
    CAMINHO,
    sep=";",  # separador de colunas é ';' e não ','
    encoding="cp1252",  # encoding do windows, para ler acentos
    decimal=",",  # virgula como separado decimal
)

print("Dados carregados com sucesso!")
print(f" Total de linhas : {df.shape[0]}")
print(f" Total de colunas: {df.shape[1]}")
