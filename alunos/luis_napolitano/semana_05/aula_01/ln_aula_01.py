 # Aprendendo trabalhar com dados em Python

# Importando as bibliotecaas para uso
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Trazer o banco de dados para o ambiente de trabalho
URL = (
    "https://raw.githubusercontent.com/"
    "cfneves/turma-visualizacao-de-dados/"
    "master/aulas/semana_04/bases/base_rh.xlsx"
)

# Carregando o dataset em Excel
df = pd.read_excel(URL)

# Convertendo a coluna de data para o formato datetime
df["Data_Admissao"] = pd.to_datetime(
    df["Data_Admissao"],
    format="%d/%m/%Y",
    errors="coerce"
)

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Conhecendo a base de dados
print(f"Dataset carregado: {df.shape[0]} linhas x {df.shape[1]} colunas")

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Visualizando as primeiras linhas do dataset
print(df.head())

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Explorando as colunas da base de dados
print(df.head(7))       # 7 primeiras linhas
print(df.tail())        # últimas 5 linhas
print(df.columns)       # nomes das colunas
print(df.info())        # estrutura da base
print(df.describe())    # estatísticas numéricas

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Analisando uma coluna selecionada
salarios = df["Salario"]
print(f"Tipo  : {type(salarios)}")
print(f"shape : {salarios.shape}")   # (1000,) — 1 dimensão
print(f"dtype : {salarios.dtype}")
print(salarios.head(4))

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Analisando duas ou mais colunas ao mesmo tempo
sub = df[["Nome", "Salario", "Data_Admissao"]]
print(f"\nTipo  : {type(sub)}")
print(f"shape : {sub.shape}")         # (1000, 2) — 2 dimensões
print(sub.head(5))

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

print(f"\nMédia   : R$ {salarios.mean():,.2f}")
print(f"Mediana : R$ {salarios.median():,.2f}")
print(f"Mínimo  : R$ {salarios.min():,.2f}")
print(f"Máximo  : R$ {salarios.max():,.2f}")

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Histograma mostra como os salários estão distribuídos
# bins=10 divide o intervalo em 10 faixas iguais
plt.hist(df["Salario"], bins=10, color="darkgreen")
plt.title("Distribuição de Salários -Napo074")
plt.xlabel("Salário (R$)")
plt.ylabel("Quantidade de Funcionários")
plt.show()

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Índice padrão
print("Índice padrão:", df.index)

# set_index: ID_Funcionario vira o endereço
df_idx = df.set_index("ID_Funcionario")
print("\nFuncionário ID=3:")
print(df_idx.loc[350][["Nome", "Departamento", "Salario", "Data_Admissao"]])

# reset_index: volta ao numérico
df_volta = df_idx.reset_index()
print(f"\nColunas após reset_index: {df_volta.columns.tolist()}")

# Índice após filtro — não começa em 0!
ativos = df[df["Status"] == "Ativo"]
print(f"\nPrimeiro índice dos Ativos : {ativos.index[0]}")
print(f"Total de Ativos            : {len(ativos)}")
print(f"Total de Inativos          : {len(df) - len(ativos)}")

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

print("-- Mostrando Graficos --")

# Calculamos o que queremos mostrar
contagem = df["Status"].value_counts()

# Gráfico de barras: x = rótulos, height = valores
plt.bar(contagem.index, contagem.values, color=["steelblue", "LightCoral"])
plt.title("Funcionários por Status")
plt.xlabel("Status")
plt.ylabel("Quantidade")
plt.show()

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Ver as colunas antes de converter
print("Tipos ANTES conversão:")
print(df.dtypes)
print("\n")

# Converter colunas categóricas
for coluna in ["Departamento", "Cargo", "Genero", "Estado_Civil", "Status"]:
    df[coluna] = df[coluna].astype("category")

print("Tipos APÓS conversão:")
print(df.dtypes)

print(f"\nDepartamentos: {df['Departamento'].cat.categories.tolist()}")
print(f"Cargos       : {df['Cargo'].cat.categories.tolist()}")

print("\nFuncionários por departamento:")
print(df["Departamento"].value_counts())

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Barras horizontais — melhor quando os rótulos são longos
dist = df["Departamento"].value_counts()

plt.barh(dist.index, dist.values, color="blue")
plt.title("Funcionários por Departamento")
plt.xlabel("Quantidade")
plt.show()

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Uma linha → Series
print("Primeira linha (iloc[0]):")
print(df.iloc[0][["Nome", "Departamento", "Salario"]])

# Slice de linhas e colunas (posições 2,3,4 · colunas 1,2,3)
print("\niloc[2:9, 1:6]:")
print(df.iloc[2:10, 1:6].to_string())

# Última linha
print(f"\nÚltima linha — Nome: {df.iloc[-1]['Nome']}")

# Lista de posições específicas
amostra = df.iloc[[0, 99, 499, 999], [0, 1, 3, 4]]
print("\nAmostra (posições 0, 99, 499, 999):")
print(amostra.to_string())

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Histograma de idades — bins=10 agrupa em ~5 anos por faixa
plt.hist(df["Idade"], bins=10, color="steelblue")
plt.title("Distribuição de Idades")
plt.xlabel("Idade (anos)")
plt.ylabel("Quantidade de Funcionários")
plt.show()

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# 1. Por índice e nome de coluna
print("Linha 0, coluna Nome:", df.loc[0, "Nome"])

# 2. Condição booleana — cada condição entre parênteses!
producao = df.loc[
    df["Departamento"] == "Produção",
    ["Nome", "Cargo", "Salario"]
]
print(f"\nProdução: {len(producao)} funcionários (5 primeiros):")
print(producao.head(5).to_string(index=False))

# 3. Múltiplas condições: & = E, | = OU, ~ = NÃO
lideranca = df.loc[
    (df["Departamento"] == "Produção") &
    (df["Cargo"].isin(["Gerente", "Coordenador"])) &
    (df["Status"] == "Ativo"),
    ["Nome", "Cargo", "Salario", "Status"]
]
print(f"\nLiderança da Produção: {len(lideranca)}")
print(lideranca.to_string(index=False))

cargo_unico = df["Cargo"].unique()
print(f"\nCargos únicos: {cargo_unico}")


# 4. Atribuição segura — forma correta de criar colunas
df.loc[df["Salario"] >= 10000, "Faixa_Salarial"] = "Senior/Especialista"
df.loc[df["Salario"] <  10000, "Faixa_Salarial"] = "Pleno/Junior"
print("\nFaixa salarial:")
print(df["Faixa_Salarial"].value_counts())

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Calculamos primeiro, plotamos depois
media_cargo = df.groupby("Cargo")["Salario"].mean().sort_values(ascending=False)

plt.bar(media_cargo.index, media_cargo.values, color="orchid")
plt.title("Salário Médio por Cargo")
plt.xlabel("Cargo")
plt.ylabel("Salário Médio (R$)")
plt.show()

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# 1. query() básico
resultado = df.query("Salario > 8000 and Status == 'Ativo'")
print(f"Ativos com salario > R$ 8.000: {len(resultado)}")

# 2. query() com variável externa — prefixo @
sal_min = 9000
deptos = ["Producao", "Logistica"]
res2 = df.query("Salario >= @sal_min and Departamento in @deptos")
print(f"\nProducao/Logistica >= R$ {sal_min:,}: {len(res2)}")

# 3. isin() — filtro por lista de valores
lideranca = df.loc[df["Cargo"].isin(["Gerente", "Coordenador","Analista"])]
print(f"\nTotal de lideres: {len(lideranca)}")
print(lideranca.groupby("Cargo")["Salario"].agg(["count", "mean"]).round(2))

# 4. between() — filtro por intervalo (extremos inclusos)
faixa = df.loc[df["Idade"].between(30, 45)]
print(f"\nFuncionarios 30-45 anos: {len(faixa)}")
print(f"Salario medio          : R$ {faixa['Salario'].mean():,.2f}")

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Pizza funciona bem para "partes de um todo"
estado = df["Estado_Civil"].value_counts()

plt.pie(estado.values, labels=estado.index, autopct="%1.1f%%")
plt.title("Distribuição por Estado Civil")
plt.show()

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

lideranca_ti = df.loc[
    (df["Departamento"] == "TI") &
    (df["Status"] == "Ativo") &
    (df["Cargo"].isin(["Gerente", "Coordenador"])),
    ["Nome", "Cargo", "Salario", "Data_Admissao"]
].sort_values("Salario", ascending=False)

print(f"Lideres de TI ativos: {len(lideranca_ti)}")
print(lideranca_ti.to_string(index=False))

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

df.loc[df["Salario"] >  12000, "Faixa_Salarial"] = "Especialista"
df.loc[df["Salario"].between(8001, 12000), "Faixa_Salarial"] = "Senior"
df.loc[df["Salario"].between(4001,  8000), "Faixa_Salarial"] = "Pleno"
df.loc[df["Salario"] <= 4000, "Faixa_Salarial"] = "Junior"

print(df["Faixa_Salarial"].value_counts())

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Calcular primeiro
media_depto = (
    df.groupby("Departamento")["Salario"]
      .mean().round(2).sort_values()
)
# Plotar
plt.barh(media_depto.index, media_depto.values, color="steelblue")
plt.title("Salario Medio por Departamento")
plt.xlabel("Salario Medio (R$)")
plt.show()

print("\n" +"-"*21)
print("--- próxima etapa ---")
print("\n")

# Calcular primeiro
faixas = df["Faixa_Salarial"].value_counts()
# Plotar
plt.pie(faixas.values, labels=faixas.index, autopct="%1.1f%%")
plt.title("Distribuicao por Faixa Salarial")
plt.show()

