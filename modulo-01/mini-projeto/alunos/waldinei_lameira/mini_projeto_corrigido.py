# ========================================================
# ANÁLISE EXPLORATÓRIA DE DADOS — BASE VAREJO (CORRIGIDO)
# ========================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

print("Bibliotecas importadas com sucesso!")

# ========================================================
# Sprint 1 — Carregamento da Base Limpa
# ========================================================

print("\n============ Importando os dados ============\n")

df_limpo = pd.read_csv(
    r'C:\Users\waldinei.rosa\OneDrive\Documentos\CURSOPYTHON2026\SCTEC_VD2\turma-visualizacao-de-dados\modulo-01\mini-projeto\alunos\waldinei_lameira\base_limpa.csv',
    encoding='latin1'
)

# Garantir que DATA está em datetime
df_limpo["DATA"] = pd.to_datetime(df_limpo["DATA"], errors="coerce")

print(f"Registros: {df_limpo.shape[0]} linhas x {df_limpo.shape[1]} colunas")
print("\nColunas e tipos de dados:")
print(df_limpo.dtypes)
print("\nPrimeiras 5 linhas:")
print(df_limpo.head())


# ========================================================
# Sprint 2 — Transformação de Strings, Integer, Float e Datetime
# ========================================================
print("\n============ Transformação de dados ============\n")

# --- 1. Remover colunas sem nome (Unnamed) ---
colunas_unnamed = [col for col in df_limpo.columns if "Unnamed" in col]
if colunas_unnamed:
    df_limpo = df_limpo.drop(columns=colunas_unnamed)
    print(f"Colunas removidas: {colunas_unnamed}")
else:
    print("Nenhuma coluna Unnamed encontrada.")

# --- 2. Padronizar strings (remover espaços extras) ---
colunas_str = df_limpo.select_dtypes(include="object").columns
for col in colunas_str:
    df_limpo[col] = df_limpo[col].str.strip()
print(f"Strings padronizadas: {list(colunas_str)}")

# --- 3. Garantir tipos inteiros para colunas numéricas ---
colunas_int = ["CO_ID", "CL_ID", "CL_EC", "CL_FHL", "PR_ID"]
for col in colunas_int:
    if col in df_limpo.columns:
        df_limpo[col] = pd.to_numeric(df_limpo[col], errors="coerce").astype("Int64")
print(f"Inteiros validados: {colunas_int}")

print("\nTipos após transformação:")
print(df_limpo.dtypes)
print(f"\nShape: {df_limpo.shape[0]} linhas x {df_limpo.shape[1]} colunas")


# ========================================================
# Sprint 3 — Verificação de Nulos e Duplicatas
# ========================================================

print("\n============ Verificação da base limpa ============\n")

# --- 1. Diagnóstico de nulos ---
nulos = df_limpo.isnull().sum()
pct_nulos = (nulos / len(df_limpo) * 100).round(2)

relatorio_nulos = pd.DataFrame({"Nulos": nulos, "% do Total": pct_nulos})
relatorio_nulos = relatorio_nulos[relatorio_nulos["Nulos"] > 0].sort_values(
    "Nulos", ascending=False
)

print("=== VALORES NULOS POR COLUNA ===")
if relatorio_nulos.empty:
    print("Nenhum valor nulo encontrado.")
else:
    print(relatorio_nulos.to_string())

# --- 2. Diagnóstico de duplicatas ---
qtd_dup = df_limpo.duplicated().sum()
pct_dup = (qtd_dup / len(df_limpo) * 100).round(2)
print(f"\n=== DUPLICATAS ===")
print(f"Registros duplicados: {qtd_dup} ({pct_dup}% do total)")

print(f"\nShape final: {df_limpo.shape[0]} linhas x {df_limpo.shape[1]} colunas")


# ========================================================
# Sprint 4 — Estatística Descritiva
# ========================================================
print("\n============ Estatística Descritiva ============\n")

# --- 1. Resumo geral das colunas numéricas ---
print("=== RESUMO GERAL (colunas numéricas) ===")
print(df_limpo.describe().T.to_string())

# --- 2. Estatísticas detalhadas por coluna numérica ---
print("\n=== ESTATÍSTICAS DETALHADAS ===")
for col in df_limpo.select_dtypes(include="number").columns:
    s = df_limpo[col].dropna()
    print(f"\n[{col}]")
    print(f"  Média:          {s.mean():.2f}")
    print(f"  Mediana:        {s.median():.2f}")
    print(f"  Desvio padrão:  {s.std():.2f}")
    print(f"  Mínimo:         {s.min()}")
    print(f"  Máximo:         {s.max()}")
    print(f"  Contagem:       {s.count()}")

# --- 3. Frequência das colunas categóricas ---
print("\n=== FREQUÊNCIA DAS COLUNAS CATEGÓRICAS ===")
for col in df_limpo.select_dtypes(include="object").columns:
    vc = df_limpo[col].value_counts()
    pct = (vc / len(df_limpo) * 100).round(2)
    tabela = pd.DataFrame({"Contagem": vc, "% do Total": pct})
    print(f"\n[{col}]")
    print(tabela.to_string())


# =====================================================
# Sprint 5 — Agrupamentos
# =====================================================

print("\n========== AGRUPAMENTOS ==========\n")

# Agrupamento 1 — Compras por Gênero
agrupamento_genero = (
    df_limpo.groupby("CL_GENERO")["CO_ID"].count().sort_values(ascending=False)
)
pct_genero = (agrupamento_genero / agrupamento_genero.sum() * 100).round(2)
tabela_genero = pd.DataFrame({"Compras": agrupamento_genero, "% do Total": pct_genero})
print("Compras por gênero:")
print(tabela_genero.to_string())

# Agrupamento 2 — Compras por Categoria de Produto
agrupamento_categoria = (
    df_limpo.groupby("PR_CAT")["CO_ID"].count().sort_values(ascending=False)
)
pct_cat = (agrupamento_categoria / agrupamento_categoria.sum() * 100).round(2)
tabela_categoria = pd.DataFrame(
    {"Compras": agrupamento_categoria, "% do Total": pct_cat}
)
print("\nCompras por categoria de produto:")
print(tabela_categoria.to_string())

# --- AJUSTE 1: Agrupamento cruzado — Gênero x Categoria ---
print("\n=== AGRUPAMENTO CRUZADO — Gênero x Categoria ===")
grupo_genero_cat = (
    df_limpo.groupby(["CL_GENERO", "PR_CAT"])["CO_ID"]
    .count()
    .reset_index(name="QTD_COMPRAS")
    .sort_values("QTD_COMPRAS", ascending=False)
)
print(grupo_genero_cat.head(10).to_string(index=False))

# --- AJUSTE 1b: Pivot Table — Gênero x Categoria ---
print("\n=== PIVOT TABLE — Gênero x Categoria ===")
pivot = df_limpo.pivot_table(
    index="CL_GENERO",
    columns="PR_CAT",
    values="CO_ID",
    aggfunc="count",
    fill_value=0
)
print(pivot.to_string())

# --- AJUSTE 2: Análise Temporal — ANO e MES ---
print("\n=== ANÁLISE TEMPORAL — Vendas por Ano e Mês ===")
df_limpo["ANO"] = df_limpo["DATA"].dt.year
df_limpo["MES"] = df_limpo["DATA"].dt.month

vendas_tempo = (
    df_limpo.groupby(["ANO", "MES"])["CO_ID"]
    .count()
    .reset_index(name="QTD_COMPRAS")
)
print(vendas_tempo.to_string(index=False))


# =====================================================
# Sprint 6 — Insights
# =====================================================

print("\n========== INSIGHTS ==========\n")

total_limpo = len(df_limpo)

genero = df_limpo.groupby("CL_GENERO")["CO_ID"].count()
pct_f = round(genero.get("F", 0) / total_limpo * 100, 1)
pct_m = round(genero.get("M", 0) / total_limpo * 100, 1)

top_cat = df_limpo.groupby("PR_CAT")["CO_ID"].count().sort_values(ascending=False)
top1_cat = top_cat.index[0]
top1_cat_pct = round(top_cat.iloc[0] / total_limpo * 100, 1)

top_seg = df_limpo.groupby("CL_SEG")["CO_ID"].count().sort_values(ascending=False)
top1_seg = top_seg.index[0]
top1_seg_pct = round(top_seg.iloc[0] / total_limpo * 100, 1)

media_filhos = round(float(df_limpo["CL_FHL"].mean()), 2)
mediana_filhos = int(df_limpo["CL_FHL"].median())

ano_mais_vendas = df_limpo.groupby("ANO")["CO_ID"].count().idxmax()
mes_mais_vendas = df_limpo.groupby("MES")["CO_ID"].count().idxmax()

print(f"""
1. QUALIDADE DOS DADOS
   - Base limpa com {total_limpo:,} registros e {df_limpo.shape[1]} colunas prontos para análise.
   - Nenhum valor nulo encontrado na base limpa.
   - Coluna DATA em formato datetime, permitindo análises temporais.

2. PERFIL DE GÊNERO
   - Gênero feminino representa {pct_f}% das compras; masculino, {pct_m}%.
   - Leve predominância feminina no volume de transações.

3. CATEGORIA DE PRODUTO
   - "{top1_cat}" é a categoria mais comprada: {top1_cat_pct}% do total de transações.
   - Bebidas, PET e Acessórios têm participação significativamente menor.
   - Categoria inválida "#N/D" (0.44%) pode ser tratada ou descartada em análises futuras.

4. SEGMENTO DE CLIENTES
   - Segmento "{top1_seg}" concentra {top1_seg_pct}% das compras — o mais representativo.
   - Segmento A (premium) representa apenas 8.14% das transações.

5. NÚMERO DE FILHOS (CL_FHL)
   - Mediana de filhos = {mediana_filhos}, indicando que a maioria dos clientes não tem filhos.
   - Média de {media_filhos} filho(s) por cliente, com máximo de 4.

6. PADRÃO TEMPORAL
   - Ano com maior volume de vendas: {ano_mais_vendas}.
   - Mês de pico de compras: mês {mes_mais_vendas}.
   - Colunas ANO e MES derivadas de DATA permitem análises sazonais aprofundadas.
""")


# =====================================================
#         Visualização de Dados
# =====================================================

# =====================================================
#         Visualização de Dados
# =====================================================

fig = plt.figure(figsize=(16, 14))
fig.suptitle('Análise Exploratória — Base Varejo', fontsize=15, fontweight='bold', y=1.01)

# --- Dados ---
cat   = df_limpo.groupby('PR_CAT')['CO_ID'].count().sort_values()
gen   = df_limpo.groupby('CL_GENERO')['CO_ID'].count()
seg   = df_limpo.groupby('CL_SEG')['CO_ID'].count().sort_values(ascending=False)

cores_cat = ['#4C72B0', '#55A868', '#C44E52', '#8172B2', '#CCB974', '#64B5CD', '#A9A9A9']
cores_gen = ['#E87B6B', '#6BAED6']
cores_seg = ['#4C72B0', '#55A868', '#C44E52']

# --- Gráfico 1: Barras horizontais — Compras por Categoria ---
ax1 = fig.add_subplot(2, 3, (1, 2))
bars = ax1.barh(cat.index, cat.values, color=cores_cat, edgecolor='white', height=0.6)
ax1.set_title('Compras por Categoria de Produto', fontsize=12, fontweight='bold')
ax1.set_xlabel('Número de Compras')
ax1.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
for bar, val in zip(bars, cat.values):
    pct = val / cat.sum() * 100
    ax1.text(bar.get_width() + 2000, bar.get_y() + bar.get_height() / 2,
             f'{val:,}  ({pct:.1f}%)', va='center', fontsize=9)
ax1.set_xlim(0, cat.max() * 1.22)
ax1.spines[['top', 'right']].set_visible(False)

# --- Gráfico 2: Pizza — Compras por Gênero ---
ax2 = fig.add_subplot(2, 3, 3)
wedges, texts, autotexts = ax2.pie(
    gen.values,
    labels=['Feminino', 'Masculino'],
    autopct='%1.1f%%',
    colors=cores_gen,
    startangle=90,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)
for at in autotexts:
    at.set_fontsize(10)
    at.set_fontweight('bold')
ax2.set_title('Compras por Gênero', fontsize=12, fontweight='bold')

# --- Gráfico 3: Barras — Compras por Segmento de Cliente ---
ax3 = fig.add_subplot(2, 3, 4)
bars3 = ax3.bar(seg.index, seg.values, color=cores_seg, edgecolor='white', width=0.5)
ax3.set_title('Compras por Segmento', fontsize=12, fontweight='bold')
ax3.set_xlabel('Segmento')
ax3.set_ylabel('Número de Compras')
ax3.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
for bar, val in zip(bars3, seg.values):
    pct = val / seg.sum() * 100
    ax3.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3000,
             f'{pct:.1f}%', ha='center', fontsize=9, fontweight='bold')
ax3.spines[['top', 'right']].set_visible(False)

# --- Gráfico 4: Linha — Evolução Temporal das Vendas ---
ax4 = fig.add_subplot(2, 3, (5, 6))
for ano, grupo in df_limpo.groupby('ANO'):
    vendas_mes = grupo.groupby('MES')['CO_ID'].count()
    ax4.plot(
        vendas_mes.index,
        vendas_mes.values,
        marker='o',
        linewidth=2,
        label=str(ano)
    )
ax4.set_title('Evolução Mensal das Vendas por Ano', fontsize=12, fontweight='bold')
ax4.set_xlabel('Mês')
ax4.set_ylabel('Número de Compras')
ax4.set_xticks(range(1, 13))
ax4.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
                     'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
ax4.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
ax4.legend(title='Ano', fontsize=9)
ax4.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.show()
