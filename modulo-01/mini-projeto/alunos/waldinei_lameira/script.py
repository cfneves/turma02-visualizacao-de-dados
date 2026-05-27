import pandas as pd
# Definindo a URL do arquivo CSV
URL = "C:\\Users\\waldinei.rosa\\Downloads\\Base Varejo.csv\\Base Varejo.csv"

# Lendo o arquivo CSV usando pandas
df = pd.read_csv(URL)
# Exibindo as primeiras linhas do DataFrame
print(df.head())
print(df.shape)



