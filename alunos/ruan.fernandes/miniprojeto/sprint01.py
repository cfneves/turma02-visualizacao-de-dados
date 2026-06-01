import pandas as pd

def carregar_dados():

    caminho =(
    r"C:\Users\PICHAU\Documents\Ruan\SCTEC\Aula\turma-visualizacao-de-dados\alunos\ruan.fernandes\miniprojeto\Base_Varejo.csv"
    )

    df = pd.read_csv(
        caminho,
        sep=';',                
        encoding='cp1252',      
        decimal=','        
    )

    return df
