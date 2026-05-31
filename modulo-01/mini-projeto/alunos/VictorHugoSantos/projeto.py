import kagglehub
import pandas as pd
import os

# 1. Baixa o dataset e descobre o caminho real onde ele foi salvo no seu PC
path = kagglehub.dataset_download("namespaiva/base-varejo")

# 2. Junta o caminho da pasta com o nome do seu arquivo CSV

full_path = os.path.join(path, "Base Varejo.csv")

# 3. Lê o arquivo normalmente usando o Pandas
df = pd.read_csv(full_path, encoding='utf-8', sep=';')

print("First 5 records:")

df = df.drop(columns=["Unnamed: 10", "Unnamed: 11", "Unnamed: 12", "Unnamed: 13"])

df = df.rename(columns={"CO_ID": "N_fiscal", "CL_ID": "ID_Cliente", "CL_EC": "Estado_Civil", "CL_FHL": "Qtd_Filhos", "CL_SEG": "Seg_Economica", "PR_ID": "ID_Produto", "PR_CAT": "Cat_Produto",
                         "PR_NOME": "Nome_Produto"})
print(df.head())