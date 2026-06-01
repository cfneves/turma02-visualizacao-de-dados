# Mini Projeto  Avaliativo - T2
# Aluno: Luís Napolitano
# Data: 01/06/2026

# O Miniprojeto consiste em criar um programa para importação, tratamento de banco de dados específico e entregar graficos e conclusões relevantes, pela perpectiva do aluno.

# São 6 scripts sugeridos pela equipe criadora e avaliadora do mini projeto.

# Script 1 - Importação dos dados
# Script 2 - Transformação de strings (str)m, Integers (int) e Floats (float) e Datetimes (datetime): desenvolver funções para limpeza de textos, inteiros e decimaisusando métodos e experessões regulares;
# Script 3 - Tratamento de dados, limpeza de Nulos e Duplicados): Aplicação de condicionais e funções para identifica, substituir valores e transformar dados str para datetime;
# Script 4 - Estatística Descritiva - aplicação de funções estatísticas e criação para coletar parametros da coluna de Número de filhos do cliente; 
# Script 5 - Relatório e Documentação: construção de contadores do relatório final exibido no terminal, finalização do README.md com reflexao teórica e submissão do link AVA
# Script 6 - Versionamento: Envio dos arquivos (script + README.md + df_limpo), via Git para o repositório da turma no Githu.

# =====================================================================
# SPRINT 1: IMPORTAÇÃO DOS DADOS
# =====================================================================
print("\n" * 2)
print("******** IMPORTAÇÃO DOS DADOS - SPRINT 1 ********")

# Importação das bibliotecas necessárias para o Miniprojeto
import pandas as pd
import numpy as np

print("ln - Bibliotecas importadas com sucesso!")
print("\n")

CaminhoBaseVarejo = r"modulo-01/base_do_projeto/Base Varejo.csv"

df = pd.read_csv(
    CaminhoBaseVarejo,
    encoding="utf-8",
    sep=";",
    decimal=",",
)

print("ln - BANCO DE DADOS (dataset) ACESSADO COM SUCESSO!")
print("\n" * 2)

# Consultando a base de dados como foi importada para entendimento e analise de limpeza e formatação
# 1. consultando a quantidade de linhas e colunas
print(f"O nosso df possui {df.shape[0]} linhas e {df.shape[1]} colunas.")
print("\n" * 2)

# 2. Consultando as 5 primeiras linhas da base de dados ...
print("ln - Exibindo as 5 primeiras linhas do df, informações gerais e formato do df:")
print(df.head(5))
print("\n" * 2)

# 3. Consultado as informações derais da base de dados ...
print("ln - Exibindo as informações gerais do dataframe:")
print(df.info())
print("\n" * 2)

#-----------------------------------------------------------------------------------------------
# =====================================================================
# SPRINT 2: TRANSFORMAÇÃO DE STR, INT, FLOAT E DATETIME
# =====================================================================

# 5. Transformando a coluna DATA para o formato datetime, usando errors="coerce" tratamento de erros.
try:
    df["DATA"] = pd.to_datetime(
        df["DATA"],
        format="%d/%m/%Y",
        errors="coerce",
    )

    print("Conversão realizada com sucesso!")

except Exception as erro:
    print("Erro encontrado:")
    print(erro)

print("\n")
print("ln - Coluna DATA passou para o formato 'datetime' com tratamento do 'errors'.")
print("\n" * 2)

#-----------------------------------------------------------------------------------------------
# =====================================================================
# SPRINT 3: LIMPEZA DE NULOS E DUPLICADAS
# =====================================================================

print(" LIMPEZA DE NULOS E DUPLICADOS - SPRINT 3")

# 6. Identificando a quantade de valores nulos e duplicados no dataframe
print("ln - Identificando a quantidade de valores nulos e duplicados no dataframe:")
print(f"Valores nulos por coluna:\n{df.isna().sum()}")
print("\n" * 2)

# 7. Identificando a quantidade de linhas duplicadas ...
print(f"Quantidade de linhas duplicadas: {df.duplicated().sum()}")
print("\n")

print(df[df.duplicated()])
print("\n" * 2 )

# OBSERVAÇÃO PARA ANALISTA: Indentificado que a quantidade de duplicadoos são valores que devem continuar para que a analise seja o mais fidedigna possível

# 8. Limpando as colunos identificadas sem dados ...
df = df.drop(
    ["Unnamed: 10", "Unnamed: 11", "Unnamed: 12", "Unnamed: 13"],
    axis=1,
)
print("\n" * 2)

# 9. Exibindo a nova formatação das colunas após limpeza ...
print("ln - Exibindo os nomes das colunas do dataframe após limpeza de colunas:")
print(df.columns.tolist(),"\n")
print(df.info())
print("\n" * 2)

# 10. Contando as datas inválidas - conferindo a conversão da coluna DATA para datetime
print("ln - Contando as datas inválidas - conferindo a conversão da coluna DATA para datetime:")
print(f"Quantidade de datas inválidas: {df['DATA'].isna().sum()}")
print("\n")

# 11. Criando colunas dia, mês, ano e mesano a partir da coluna DATA
df["Dia"] = df["DATA"].dt.day       #Criando a coluna Dia para possível análise de sazonalidade e tendências diárias
df["Mês"] = df["DATA"].dt.month     #Criando a coluna Mês para possível análise de sazonalidade e tendências mensais
df["Ano"] = df["DATA"].dt.year      #Criando a coluna Ano para possível análise de sazonalidade e tendências anuais
df["MesAno"] = df["DATA"].dt.to_period("M")  #Criando a coluna MêsAno para possível análise de sazonalidade e tendências mensais e anuais

# 12. Exibindo a lista e informações das colunas após criação de novas ...
print("ln - Exibindo os nomes das colunas do dataframe após criação de novas")
print(df.columns.tolist())
print(df.info())
print("\n" * 2)
# 12.1 Exibindo as 5 primeiras linhas do df após criação das colunas de novas ...
print("Exibindo as 5 primeiras linhas do df após criação das colunas de novas:")
print(df.head(5))
print("\n" * 2)

# 13. Tratando as informações de cada coluna que possuam "N/D"
print(" Exibindo as quantidade de valores unicos nas colunas")
print(df.nunique())
df["PR_CAT"].value_counts()

print("\n" * 2)

print("Coluna CO_ID     : ",(df["CO_ID"] == "n/d").sum())
print("Coluna CL_ID     : ",(df["CL_ID"] == "n/d").sum())
print("Coluna CL_GENERO : ",(df["CL_GENERO"] == "n/d").sum())
print("Coluna CL_EC     : ",(df["CL_EC"] == "n/d").sum())
print("Coluna CL_FHL    : ",(df["CL_FHL"] == "n/d").sum())
print("Coluna CL_SEG    : ",(df["CL_SEG"] == "n/d").sum())
print("Coluna PR_ID     : ",(df["PR_ID"] == "n/d").sum())
print("Coluna PR_CAT    : ",(df["PR_CAT"] == "n/d").sum())
print("Coluna PR_NOME   : ",(df["PR_NOME"] == "n/d").sum())