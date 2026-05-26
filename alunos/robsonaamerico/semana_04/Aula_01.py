"""
aula_01.py — Semana 04 · Dia 01
Leitura de arquivos (CSV, JSON, Excel) + Módulo datetime

Pipeline:
    1. Leitura do CSV via URL RAW
    2. Exploração básica
    3. Exportação para JSON e Excel
    4. Conversão e manipulação de datas
    5. Geração do dataset enriquecido

Autor  : Robson Américo
Turma  : T2 — SENAI BI
"""

import pandas as pd
import json
from datetime import datetime

# ═══════════════════════════════════════════════════════════
# 1. CONFIGURAÇÃO
# ═══════════════════════════════════════════════════════════

URL = (
    "https://raw.githubusercontent.com/"
    "cfneves/turma-visualizacao-de-dados/"
    "master/datasets/base_rh.csv"
)


# ═══════════════════════════════════════════════════════════
# 2. EXTRAÇÃO — leitura do CSV com parâmetros corretos
# ═══════════════════════════════════════════════════════════

df = pd.read_csv(URL, sep=";", encoding="cp1252", decimal=",")
print(f"[1] CSV carregado: {df.shape[0]} linhas × {df.shape[1]} colunas")

# ═══════════════════════════════════════════════════════════
# 3. EXPLORAÇÃO BÁSICA
# ═══════════════════════════════════════════════════════════

print("\n[2] Tipos de dados:")
print(df.dtypes)

print("\n[3] Nulos por coluna:")
print(df.isnull().sum())

print("\n[4] Estatísticas numéricas:")
print(df.describe().round(2))

print("\n[5] Valores únicos por coluna:")
print(df.nunique())

print("\n[6] Distribuição — Departamento:")
print(df["Departamento"].value_counts())

# ═══════════════════════════════════════════════════════════
# 4. EXPORTAÇÃO — JSON e Excel
# ═══════════════════════════════════════════════════════════

# JSON
df.to_json("base_rh.json", orient="records", force_ascii=False, indent=2)
print("\n[7] base_rh.json gerado")

# Excel — uma aba por departamento
with pd.ExcelWriter("base_rh_deptos.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Completo", index=False)
    for depto in sorted(df["Departamento"].unique()):
        df[df["Departamento"] == depto].to_excel(
            writer, sheet_name=depto[:31], index=False
        )
print("[8] base_rh_deptos.xlsx gerado")

# ═══════════════════════════════════════════════════════════
# 5. TRANSFORMAÇÃO DE DATAS
# ═══════════════════════════════════════════════════════════

# Converter string → datetime
df["Data_Admissao"] = pd.to_datetime(
    df["Data_Admissao"], format="%d/%m/%Y", errors="coerce"
)
print(f"\n[9] Data_Admissao convertida: {df['Data_Admissao'].dtype}")
print(f"    NaT gerados: {df['Data_Admissao'].isna().sum()}")

# Colunas derivadas
hoje = pd.Timestamp.today()
df["Ano_Admissao"]    = df["Data_Admissao"].dt.year
df["Mes_Admissao"]    = df["Data_Admissao"].dt.month
df["Trimestre"]       = df["Data_Admissao"].dt.quarter
df["Tempo_Casa_Anos"] = ((hoje - df["Data_Admissao"]).dt.days / 365.25).round(1)

def classificar_tempo(anos):
    if   anos < 1: return "Menos de 1 ano"
    elif anos < 3: return "1 a 3 anos"
    elif anos < 5: return "3 a 5 anos"
    else:           return "Mais de 5 anos"

df["Faixa_Tempo_Casa"] = df["Tempo_Casa_Anos"].apply(classificar_tempo)
print("\n[10] Colunas derivadas criadas: Ano_Admissao, Mes_Admissao, Trimestre,")
print("      Tempo_Casa_Anos, Faixa_Tempo_Casa")

# ═══════════════════════════════════════════════════════════
# 6. ANÁLISE — tempo de casa por departamento
# ═══════════════════════════════════════════════════════════

media_depto = (
    df.groupby("Departamento")["Tempo_Casa_Anos"]
      .mean().round(1)
      .sort_values(ascending=False)
      .rename("Media_Anos")
      .reset_index()
)
print("\n[11] Tempo médio de casa por departamento:")
print(media_depto.to_string(index=False))

# ═══════════════════════════════════════════════════════════
# 7. LOAD — salvar dataset enriquecido
# ═══════════════════════════════════════════════════════════

df.to_csv("base_rh_dia01.csv", index=False, sep=";", encoding="utf-8-sig")
print("\n[12] base_rh_dia01.csv salvo — pronto para o Dia 02")
print("      Colunas finais:", df.columns.tolist())
print("\n✓ Pipeline do Dia 01 concluído.")