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

    print(f"[Sprint 01] Dados carregados: {df.shape[0]} linhas, {df.shape[1]} colunas.")
    return df
 
 
if __name__ == "__main__":
    df = carregar_dados()
    print(df.head())