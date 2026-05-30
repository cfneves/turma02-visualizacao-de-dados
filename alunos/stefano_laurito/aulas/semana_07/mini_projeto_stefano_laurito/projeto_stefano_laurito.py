
# Etapa 1 - Importação de bibliotecas e da base de dados
 
import pandas as pd

# Importação da base
df = pd.read_csv("base_varejo.csv", sep=";")

# Visualização inicial
print("\nVISUALIZAÇÃO INICIAL DA BASE")
print(df.head())

# Informações gerais do dataframe
print("\nVERIFICAÇÃO DOS TIPOS DE DADOS")
df.info()

print("\nPROBLEMA IDENTIFICADO:")
print("A coluna DATA foi carregada como texto (str) e precisará ser convertida para datetime.")

# Verificação de valores nulos
print("\nVERIFICAÇÃO DE VALORES NULOS")
print(df.isnull().sum())

print("\nPROBLEMA IDENTIFICADO:")
print("Foram encontradas colunas totalmente vazias (Unnamed), indicando inconsistência estrutural no arquivo CSV.")

# Criação de uma cópia da base original
df_limpo = df.copy()

print("\nCÓPIA DA BASE CRIADA COM SUCESSO")

# Remoção das colunas totalmente vazias
df_limpo = df_limpo.drop(columns=[
    "Unnamed: 10",
    "Unnamed: 11",
    "Unnamed: 12",
    "Unnamed: 13"
])

print("\nCOLUNAS VAZIAS REMOVIDAS")
print(df_limpo.info())

# Tratamento de categorias inconsistentes
print("\nTRATAMENTO DE CATEGORIAS INVÁLIDAS")

if "#N/D" in df_limpo["PR_CAT"].values:
    df_limpo["PR_CAT"] = df_limpo["PR_CAT"].replace("#N/D", "Sem Categoria")
    print("Categorias inválidas '#N/D' foram substituídas por 'Sem Categoria'.")
else:
    print("Nenhuma categoria inválida encontrada.")


# Validação da regra de negócio da coluna CO_ID
print("\nVALIDAÇÃO DO IDENTIFICADOR DE COMPRA")

compras_invalidas = (df_limpo["CO_ID"] <= 0).sum()

if compras_invalidas > 0:
    print(f"Foram encontrados {compras_invalidas} identificadores de compra inválidos.")
else:
    print("Todos os identificadores de compra são válidos.")


# Verificação de duplicatas
duplicatas = df_limpo.duplicated()
print("\nVERIFICAÇÃO DE DUPLICATAS")
print(f"Número de registros duplicados: {duplicatas.sum()}")

# Remoção de duplicatas
df_limpo = df_limpo.drop_duplicates()
print("\nDUPLICATAS REMOVIDAS")
print(f"Número total de registros após limpeza: {len(df_limpo)}")

# Conversão da coluna DATA para datetime
print("\nCONVERSÃO DA COLUNA DATA")

df_limpo["DATA"] = pd.to_datetime(
    df_limpo["DATA"],
    format="%d/%m/%Y"
)

print("\nTIPO DA COLUNA DATA APÓS CONVERSÃO:")
print(df_limpo["DATA"].dtype)

# Estatísticas descritivas da coluna CL_FHL
print("\nESTATÍSTICAS DESCRITIVAS - NÚMERO DE FILHOS")

print(f"Média: {df_limpo['CL_FHL'].mean():.2f}")
print(f"Mediana: {df_limpo['CL_FHL'].median()}")
print(f"Desvio padrão: {df_limpo['CL_FHL'].std():.2f}")
print(f"Moda: {df_limpo['CL_FHL'].mode()[0]}")
print(f"Valor máximo: {df_limpo['CL_FHL'].max()}")
print(f"Valor mínimo: {df_limpo['CL_FHL'].min()}")
print(f"Contagem de registros: {df_limpo['CL_FHL'].count()}")

# Agrupamento por gênero
print("\nAGRUPAMENTO - QUANTIDADE DE COMPRAS POR GÊNERO")

compras_genero = df_limpo.groupby("CL_GENERO")["CO_ID"].count()

print(compras_genero)

# Agrupamento por categoria de produto
print("\nAGRUPAMENTO - QUANTIDADE DE VENDAS POR CATEGORIA")

vendas_categoria = df_limpo.groupby("PR_CAT")["CO_ID"].count().sort_values(ascending=False)

print(vendas_categoria)

print("\nTRATAMENTO REALIZADO:")
print("Categorias inválidas '#N/D' foram tratadas e substituídas por 'Sem Categoria'.")

# Agrupamento combinado por gênero e categoria
print("\nAGRUPAMENTO - COMPRAS POR GÊNERO E CATEGORIA")

agrupamento_genero_categoria = df_limpo.groupby(
    ["CL_GENERO", "PR_CAT"]
)["CO_ID"].count()

print(agrupamento_genero_categoria)

# Conclusões finais da análise
print("\nCONCLUSÕES DA ANÁLISE")

print("""
1. A base apresentou boa integridade geral, com ausência de valores nulos nas principais colunas do dataset.

2. Foram identificadas colunas totalmente vazias (Unnamed), indicando inconsistências estruturais no arquivo CSV original.

3. Foram encontrados 96.553 registros duplicados, que foram removidos durante a etapa de limpeza dos dados.

4. A categoria ALIMENTOS apresentou o maior volume de vendas, demonstrando forte representatividade no varejo analisado.

5. Clientes do gênero feminino apresentaram maior quantidade de compras em relação ao gênero masculino.

6. Foram identificadas categorias inconsistentes, posteriormente tratadas como 'Sem Categoria'.
""")

# Exportação da base limpa
df_limpo.to_csv("df_limpo.csv", index=False)

print("\nBASE LIMPA EXPORTADA COM SUCESSO")