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
