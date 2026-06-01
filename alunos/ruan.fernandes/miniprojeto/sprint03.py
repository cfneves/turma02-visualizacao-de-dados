import pandas as pd
from sprint02 import tratamentos_dados

def ajuster_produtos(row):

    categoria = row["Categoria do Produto"]
    produto = row["Produtos"]

    if produto == "#N/D":

        if categoria == "#N/D":
            row["Produtos"] = "Não Identificado"
            row["Categoria do Produto"] = "Não Identificado"

        else:
            row["Produtos"] = f"Produto de {categoria}"

    return row

def limpeza_dados(df):

    df = df.apply(ajuster_produtos, axis=1)

    return df