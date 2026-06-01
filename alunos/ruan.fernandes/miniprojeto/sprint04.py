import pandas as pd
from sprint03 import limpeza_dados

def analise_dados(df):
    
    analise_de_Gênero = (
        df.groupby("Gênero do Cliente")
        ["ID do Cliente"].nunique()
        .reset_index(name="Quantidade de Clientes")
    )
    
    analise_de_Categoria = (
        df.groupby("Categoria do Produto")
        ["ID do Produto"].nunique()
        .reset_index(name="Quantidade de Produtos")
    )
    
    analise_de_meses = (
        df.groupby(df["Data da Compra"].dt.month)
        ["ID"].count()
        .reset_index(name="Quantidade de Compras")
    )
    
    analise_de_filhos = (
        df.groupby("Quantidade de Filhos")
        ["ID do Cliente"].nunique()
        .reset_index(name="Quantidade de Clientes")
    )
    
    return {
        "genero": analise_de_Gênero,
        "categoria": analise_de_Categoria,
        "meses": analise_de_meses,
        "filhos": analise_de_filhos
    }
