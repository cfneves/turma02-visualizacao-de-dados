import pandas as pd
from sprint01 import carregar_dados

df = carregar_dados()
print(df.info())



def tratamentos_dados(df):
    df = df.drop(columns=["CL_SEG","CL_EC","Unnamed: 10", "Unnamed: 11", "Unnamed: 12", "Unnamed: 13"])
    df = df.rename(columns={"DATA": "Data da Compra", "CO_ID": "ID", "CL_ID": "ID do Cliente", "CL_GENERO": "Gênero do Cliente", "PR_ID": "ID do Produto",
                            "PR_CAT" : "Categoria do Produto","PR_NOME" : "Produtos",
                            "CL_FHL" : "Quantidade de Filhos"})
    df["Data da Compra"] = pd.to_datetime(
        df["Data da Compra"], 
        dayfirst=True
        )
    df["Gênero do Cliente"] = df["Gênero do Cliente"].map({"F": "Feminino", "M": "Masculino"})
    
          
    return df


df=carregar_dados()
df=tratamentos_dados(df)
print(df.head())
print(df.info())


   