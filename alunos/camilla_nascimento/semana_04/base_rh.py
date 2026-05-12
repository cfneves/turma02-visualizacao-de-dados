
import pandas as pd

# 1. Caminho exato do seu arquivo CSV
CAMINHO = r'C:\Users\Milla\Documents\turma-visualizacao-de-dados\datasets\base_rh.csv'

# 2. Carregando os dados (A "Mágica" acontece aqui)
# sep=';' -> Porque o TOTVS usa ponto-e-vírgula
# encoding='cp1252' -> Para aceitar acentos (Produção, Gestão, etc)
# decimal=',' -> Para o Python entender que 1500,50 é um número

df = pd.read_csv(CAMINHO, sep=';', encoding='cp1252', decimal=',')
# 3. Verificando se os dados foram carregados corretamente
print(df.head())  # Mostra as primeiras linhas do DataFrame
print(df.info())  # Mostra informações sobre as colunas e tipos de dados
print(df.describe())  # Mostra estatísticas descritivas para colunas numéricas

# CONFIGURAÇÃO DE EXIBIÇÃO: Essas linhas removem os limites do terminal
pd.set_option('display.max_rows', 1000)    # Força mostrar até 1000 linhas
pd.set_option('display.max_columns', None) # Força mostrar todas as colunas
pd.set_option('display.width', None)       # Ajusta a largura para não quebrar a linha

# 1. Caminho do arquivo
CAMINHO = r'C:\Users\Milla\Documents\turma-visualizacao-de-dados\datasets\base_rh.csv'

# 2. Lendo o arquivo
df = pd.read_csv(CAMINHO, sep=';', encoding='cp1252', decimal=',')

# 3. Exibindo as 1000 linhas
print("--- RELATÓRIO COMPLETO: 1000 LINHAS ---")
print(df.head(1000))

df.head(5)

df.tail(3)

print('Colunas do dataset:')
print(df.columns.tolist())

# Diagnóstico de tipos e nulos

df.info()

print('Quantidade de nulos por coluna:')
print(df.isnull().sum())

print()

print('Percentual de nulos por coluna:')
print((df.isnull().sum() / len(df) * 100).round(2))

# Estatísticas das colunas numéricas

df.describe().round(2)

# Explorando colunas categóricas

print('Valores únicos por coluna:')
print(df.nunique())

for col in ['Departamento', 'Cargo', 'Genero', 'Status', 'Estado_Civil']:
    print(f'\n── {col} ──')   # f-string: {} insere o valor da variável
    print(df[col].value_counts())

# Selecionando colunas e filtrando linhas

df['Nome'].head(5)

df[['Nome', 'Departamento', 'Cargo', 'Salario']].head(6)

ativos = df[df['Status'] == 'Ativo']

print(f'Total de funcionários : {len(df)}')
print(f'Funcionários ativos   : {len(ativos)}')
print(f'Funcionários inativos : {len(df) - len(ativos)}')

gerentes_ti = df[
    (df['Cargo'] == 'Gerente') & (df['Departamento'] == 'TI')
]

print(f'Gerentes na área de TI: {len(gerentes_ti)}')
print()
gerentes_ti[['Nome', 'Salario', 'Status', 'Data_Admissao']]

print(f"Salário médio : R$ {df['Salario'].mean():,.2f}")
print(f"Salário máximo: R$ {df['Salario'].max():,.2f}")
print(f"Salário mínimo: R$ {df['Salario'].min():,.2f}")
print(f"Salário mediana:R$ {df['Salario'].median():,.2f}")

# Exportando para JSON

import json  # biblioteca nativa do Python para manipular JSON

# df.to_json() → converte o DataFrame para JSON e salva no arquivo
df.to_json(
    'base_rh.json',
    orient='records',      # cada linha vira um objeto {}
    force_ascii=False,     # False = salva ã, é, ç como estão
    indent=2               # 2 espaços de indentação → arquivo legível
)

print('✓ base_rh.json gerado!')

# Ler de volta para confirmar
df_json = pd.read_json('base_rh.json')
print(f'  Linhas lidas do JSON: {len(df_json)}')

# Visualizar os 2 primeiros registros no formato JSON
with open('base_rh.json', 'r', encoding='utf-8') as f:
    amostra = json.load(f)
print('\nPrimeiros 2 registros no JSON:')
print(json.dumps(amostra[:2], ensure_ascii=False, indent=2))

# Exportando para Excel

# Exportação simples: tudo em uma aba
df.to_excel('base_rh.xlsx', index=False, sheet_name='Funcionarios')
print('✓ base_rh.xlsx (aba única) gerado!')

# Exportação avançada: uma aba por departamento
with pd.ExcelWriter('base_rh_por_depto.xlsx', engine='openpyxl') as writer:

    # Aba 1: dataset completo
    df.to_excel(writer, sheet_name='Todos', index=False)
    print('  Aba Todos: todos os registros')

    # df['Departamento'].unique() → lista de departamentos sem repetição
    # sorted() → ordena em ordem alfabética
    for depto in sorted(df['Departamento'].unique()):

        # Filtrar só os funcionários desse departamento
        df_depto = df[df['Departamento'] == depto]

        # Limite do Excel: nomes de aba têm no máximo 31 caracteres
        nome_aba = depto[:31]

        df_depto.to_excel(writer, sheet_name=nome_aba, index=False)
        print(f'  Aba "{nome_aba}": {len(df_depto)} registros')

print('\n✓ base_rh_por_depto.xlsx gerado!')

# Arquivo json - baixar

import pandas as pd

df = pd.read_csv(
    r'C:\Users\Milla\Documents\turma-visualizacao-de-dados\alunos\camilla_nascimento\semana_04\base_rh (1).csv',
    sep=';',
    encoding='cp1252'
)


print(df.shape)

df.to_json('base_rh.json', orient='records', force_ascii=False)

df.to_excel('base_rh.xlsx', index=False)

# Corrigindo
import pandas as pd

df = pd.read_excel(
    r'C:\Users\Milla\Documents\turma-visualizacao-de-dados\alunos\camilla_nascimento\semana_04\base_rh.xlsx'
)

print(df.shape)

df.to_json('base_rh.json', orient='records', force_ascii=False)

df.to_excel('base_rh.xlsx', index=False)
