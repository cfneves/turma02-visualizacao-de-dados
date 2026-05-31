# ==========================================================
# MINI PROJETO AVALIATIVO - ANÁLISE EXPLORATÓRIA DE DADOS
# Visualização de Dados e Business Intelligence
#
# Autor: SEU NOME
# Turma: T2
#
# Objetivo:
# Realizar uma análise exploratória da base Varejo,
# aplicando técnicas de limpeza, tratamento e
# sumarização de dados utilizando Pandas.
# ==========================================================

import pandas as pd


print("=" * 60)
print("ANÁLISE EXPLORATÓRIA DE DADOS - BASE VAREJO")
print("=" * 60)

# ==========================================================
# SPRINT 1 - IMPORTAÇÃO DOS DADOS
# ==========================================================

url = "https://raw.githubusercontent.com/cfneves/turma-visualizacao-de-dados/master/modulo-01/base_do_projeto/Base%20Varejo.csv"

df = pd.read_csv(url, sep=";", encoding="cp1252")

print("\nBase carregada com sucesso!")

print("\nQuantidade de registros e colunas:")
print(df.shape)

print("\nColunas da base:")
print(df.columns.tolist())

print("\nTipos de dados:")
print(df.dtypes)

# ==========================================================
# SPRINT 2 - IDENTIFICAÇÃO DE PROBLEMAS
# ==========================================================

print("\n" + "=" * 60)
print("VERIFICAÇÃO DE QUALIDADE DOS DADOS")
print("=" * 60)

print("\nValores nulos por coluna:")
print(df.isnull().sum())

duplicados = df.duplicated().sum()

percentual_dup = (duplicados / len(df)) * 100

print(f"\nQuantidade de registros duplicados: {duplicados:,}")

print(
    f"Percentual de duplicidade: "
    f"{percentual_dup:.2f}%"
)

if "PR_CAT" in df.columns:

    categorias_vazias = (
        df["PR_CAT"]
        .astype(str)
        .str.strip()
        .eq("")
        .sum()
    )

    print(f"\nCategorias vazias encontradas: {categorias_vazias}")

if "PR_CAT" in df.columns:

    categorias_nd = (df["PR_CAT"] == "#N/D").sum()

    print(
        f"\nRegistros com categoria '#N/D': "
        f"{categorias_nd}")

# ==========================================================
# SPRINT 3 - LIMPEZA DOS DADOS
# ==========================================================

print("\n" + "=" * 60)
print("LIMPEZA DOS DADOS")
print("=" * 60)

# ----------------------------------------------------------
# Remoção de colunas totalmente vazias
# ----------------------------------------------------------

colunas_antes = df.shape[1]

df = df.dropna(axis=1, how="all")

colunas_depois = df.shape[1]

print(
    f"\nColunas totalmente vazias removidas: "
    f"{colunas_antes - colunas_depois}"
)

# ----------------------------------------------------------
# Tratamento de categorias vazias
# ----------------------------------------------------------

if "PR_CAT" in df.columns:

    # Caso existam categorias nulas,
    # elas serão preenchidas para evitar
    # perda de registros na análise.

    df["PR_CAT"] = df["PR_CAT"].fillna("Sem Categoria")

    df["PR_CAT"] = df["PR_CAT"].replace(
        "",
        "Sem Categoria"
    )

    print(
        "\nCategorias vazias tratadas com "
        "'Sem Categoria'."
    )

# ----------------------------------------------------------
# Tratamento de possíveis dimensões físicas
# ----------------------------------------------------------

possiveis_dimensoes = [
    "ALTURA",
    "LARGURA",
    "COMPRIMENTO",
    "PESO"
]

for coluna in possiveis_dimensoes:

    if coluna in df.columns:

        df[coluna] = df[coluna].fillna(0)

        print(f"\nNulos tratados na coluna {coluna}")

# ----------------------------------------------------------
# Remoção de duplicatas
# ----------------------------------------------------------

linhas_antes = len(df)

df = df.drop_duplicates()

linhas_depois = len(df)

print(
    f"\nDuplicatas removidas: "
    f"{linhas_antes - linhas_depois}"
)

# ----------------------------------------------------------
# Conversão de datas
# ----------------------------------------------------------

if "DATA" in df.columns:

    df["DATA"] = pd.to_datetime(
        df["DATA"],
        dayfirst=True,
        errors="coerce"
    )

    datas_invalidas = df["DATA"].isna().sum()

    print(
        f"\nConversão de datas concluída."
        f"\nDatas inválidas encontradas: {datas_invalidas}"
    )

# ==========================================================
# SPRINT 4 - ESTATÍSTICAS DESCRITIVAS
# ==========================================================

print("\n" + "=" * 60)
print("ESTATÍSTICAS DA COLUNA NÚMERO DE FILHOS")
print("=" * 60)

if "CL_FHL" in df.columns:

    media = df["CL_FHL"].mean()
    mediana = df["CL_FHL"].median()
    moda = df["CL_FHL"].mode()[0]
    desvio = df["CL_FHL"].std()
    minimo = df["CL_FHL"].min()
    maximo = df["CL_FHL"].max()
    contagem = df["CL_FHL"].count()

    print(f"\nMédia: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda}")
    print(f"Desvio padrão: {desvio:.2f}")
    print(f"Mínimo: {minimo}")
    print(f"Máximo: {maximo}")
    print(f"Contagem: {contagem}")

    print("\nResumo Estatístico Completo:")

    estatisticas = pd.DataFrame({
        "Indicador": [
            "Média",
            "Mediana",
            "Moda",
            "Desvio Padrão",
            "Mínimo",
            "Máximo",
            "Contagem"
        ],
        "Valor": [
            media,
            mediana,
            moda,
            desvio,
            minimo,
            maximo,
            contagem
        ]
    })

    print(estatisticas)

# ==========================================================
# SPRINT 5 - AGRUPAMENTOS
# ==========================================================

print("\n" + "=" * 60)
print("AGRUPAMENTOS E PADRÕES")
print("=" * 60)

# ----------------------------------------------------------
# AGRUPAMENTO 1
# Compras por gênero
# ----------------------------------------------------------

if "CL_GENERO" in df.columns and "CO_ID" in df.columns:

    print("\nCompras por gênero:")

    compras_genero = (
        df.groupby("CL_GENERO")["CO_ID"]
        .count()
        .sort_values(ascending=False)
    )

    print(compras_genero)

# ----------------------------------------------------------
# AGRUPAMENTO 2
# Compras por categoria
# ----------------------------------------------------------

if "PR_CAT" in df.columns and "CO_ID" in df.columns:

    print("\nCompras por categoria:")

    compras_categoria = (
        df.groupby("PR_CAT")["CO_ID"]
        .count()
        .sort_values(ascending=False)
    )

    print(compras_categoria)

# ----------------------------------------------------------
# PIVOT TABLE 1
# Filhos x Categoria
# ----------------------------------------------------------

if (
    "CL_FHL" in df.columns
    and "PR_CAT" in df.columns
    and "CO_ID" in df.columns
):

    print("\nTabela dinâmica - Filhos x Categoria:")

    tabela_pivot = pd.pivot_table(
        df,
        index="CL_FHL",
        columns="PR_CAT",
        values="CO_ID",
        aggfunc="count",
        fill_value=0
    )

    print(tabela_pivot)

# ----------------------------------------------------------
# PIVOT TABLE 2
# Gênero x Categoria
# ----------------------------------------------------------

if (
    "CL_GENERO" in df.columns
    and "PR_CAT" in df.columns
    and "CO_ID" in df.columns
):

    print("\nTabela dinâmica - Gênero x Categoria:")

    pivot_genero = pd.pivot_table(
        df,
        index="CL_GENERO",
        columns="PR_CAT",
        values="CO_ID",
        aggfunc="count",
        fill_value=0
    )

    print(pivot_genero)

# ==========================================================
# CONCLUSÕES
# ==========================================================

print("\n" + "=" * 60)
print("PRINCIPAIS INSIGHTS")
print("=" * 60)

print("""
1. Foram identificados 96.553 registros duplicados,
   representando aproximadamente 11,63% da base original.
   Esse resultado demonstra a importância da validação dos
   dados antes da realização de análises.

2. Quatro colunas apresentavam 100% dos valores nulos e
   foram removidas por não possuírem utilidade para a
   análise exploratória.

3. A categoria ALIMENTOS foi a mais representativa da base,
   registrando 384.197 compras, muito acima das demais
   categorias analisadas.

4. Clientes do gênero feminino realizaram 382.427 compras,
   enquanto clientes do gênero masculino realizaram
   351.020 compras.

5. A variável número de filhos apresentou média de 1,15,
   porém mediana e moda iguais a zero, indicando que a
   maior parte dos clientes possui poucos ou nenhum filho.

6. A categoria '#N/D' permaneceu presente após a limpeza,
   indicando possível inconsistência cadastral que poderia
   ser tratada em futuras etapas de qualidade de dados.
""")

print("\nProcesso concluído com sucesso!")
print("=" * 60)