import pandas as pd

# Carregando a base (certifique-se de que o caminho está correto)
CAMINHO = r'C:\Users\Milla\Documents\turma-visualizacao-de-dados\datasets\base_rh.csv'
df = pd.read_csv(CAMINHO, sep=';', encoding='cp1252', decimal=',')

# --- MÓDULO 3: PRIMEIRAS OLHADAS ---
print("\n--- PRIMEIROS 5 REGISTROS ---")
print(df.head(5))

print("\n--- ÚLTIMOS 5 REGISTROS ---")
print(df.tail(5))

print('\n--- COLUNAS DO DATASET ---')
print(df.columns.tolist())

# --- MÓDULO 4: DIAGNÓSTICO (TIPOS E NULOS) ---
print('\n === RESUMO GERAL DA BASE === ')
df.info()

print('\n--- TOTAL DE NULOS POR COLUNA ---')
print(df.isnull().sum())

print('\n--- PERCENTUAL DE NULOS (%) ---')
print((df.isnull().sum() / len(df) * 100).round(2))

# --- MÓDULO 5: ESTATÍSTICA (NÚMEROS) ---
print('\n--- ESTATÍSTICA DAS COLUNAS NUMÉRICAS ---')
# O round(2) deixa o dinheiro e a idade com apenas 2 casas decimais
print(df.describe().round(2))

# --- MÓDULO 6: CATEGORIAS (TEXTOS) ---
print("\n--- VALORES ÚNICOS POR COLUNA ---")
print(df.nunique())

# Analisando a contagem de cada categoria (essencial para o RH)
for col in ['Departamento', 'Cargo', 'Genero', 'Status', 'Estado_Civil']:
    print(f'\n-- Contagem por: {col} --')
    print(df[col].value_counts())
