import pandas as pd
from pathlib import Path

csv_file = Path(r"C:\Users\jakso_sdyff07\OneDrive\Documentos\git_sc_tec\turma-visualizacao-de-dados\alunos\jakson_luis\exercicios\semana_4\base_rh.csv")
df = pd.read_csv(csv_file, sep=';', encoding='cp1252', decimal=',')
df.info()
df.describe()

"""3. Converta `Data_Admissao` para datetime. Crie as colunas:  
    `Ano_Admissao`, `Mes_Admissao`, `Tempo_Casa_Anos` e `Faixa_Tempo_Casa`.
"""

df['Data_Admissao'] = pd.to_datetime(df['Data_Admissao'], format='%d/%m/%Y', errors='coerce')
df['Ano_Admissao'] = df['Data_Admissao'].dt.year
df['Mes_Admissao'] = df['Data_Admissao'].dt.month
df['Tempo_Casa_Anos'] = ((pd.Timestamp.today() - df['Data_Admissao']).dt.days / 365.25).round(2)
df['Faixa_Tempo_Casa'] = pd.cut(
    df['Tempo_Casa_Anos'],
    bins=[-1, 1, 3, 5, 10, 100],
    labels=['0-1', '1-3', '3-5', '5-10', '10+']
)

df.head()


"""4. Responda com groupby,
    "→ Qual departamento tem a **maior** média de tempo de casa?,
    "→ Qual tem a **menor** média de tempo de casa?,
"""

tempo_medio = df.groupby('Departamento')['Tempo_Casa_Anos'].mean().sort_values()
print('Departamento com menor tempo médio de casa:', tempo_medio.idxmin())
print('Departamento com maior tempo médio de casa:', tempo_medio.idxmax())



from pathlib import Path

output_file = Path(r"C:\Users\jakso_sdyff07\OneDrive\Documentos\git_sc_tec\turma-visualizacao-de-dados\alunos\jakson_luis\exercicios\semana_4\base_rh_deptos.xlsx")
output_file.parent.mkdir(parents=True, exist_ok=True)

with pd.ExcelWriter(output_file) as writer:
    df.to_excel(writer, sheet_name='Completo', index=False)
    for dept in df['Departamento'].unique():
        df[df['Departamento'] == dept].to_excel(writer, sheet_name=dept, index=False)

print(f"Arquivo salvo em: {output_file}")