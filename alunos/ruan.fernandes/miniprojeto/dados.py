import pandas as pd
import datetime as dt


caminho = r'C:\Users\PICHAU\Documents\Ruan\SCTEC\Aula\turma-visualizacao-de-dados\alunos\ruan.fernandes\miniprojeto'

df = pd.read_csv(
    caminho,
    sep=';',                
    encoding='cp1252',      
    decimal=','        
)

print('Dados carregados com sucesso!')



