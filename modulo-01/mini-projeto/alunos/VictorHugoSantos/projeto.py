#SCTEC - Mini-Projeto Avaliativo - Módulo 1

import kagglehub
import pandas as pd
import os

print("INICIANDO DADOS")

# IMPORTAÇÃO E INSPEÇÃO DOS DADOS

# Baixa o dataset via Kagglehub e mapeia o caminho (Certifique-se de ter a lib instalada no VSCode)
path = kagglehub.dataset_download("namespaiva/base-varejo")
full_path = os.path.join(path, "Base Varejo.csv")

# Leitura do dataset
df = pd.read_csv(full_path, encoding='utf-8', sep=';')

# Verificando registros, colunas, tipos e valores nulos
print(f"Total de registros originais: {df.shape[0]} | Total de colunas: {df.shape[1]}")
print("\nInformações do DataFrame (Verificação de Nulos e Tipos):")
df.info() # O .info() já imprime a contagem de não-nulos e os tipos de dados

# LIMPEZA E TRANSFORMAÇÃO
# Remoção de colunas vazias
df = df.drop(columns=["Unnamed: 10", "Unnamed: 11", "Unnamed: 12", "Unnamed: 13"])

# Renomeando colunas
df = df.rename(columns={
    "CO_ID": "N_fiscal", "CL_ID": "ID_Cliente", "CL_GENERO": "Genero", 
    "CL_EC": "Estado_Civil", "CL_FHL": "Qtd_Filhos", "CL_SEG": "Seg_Economica", 
    "PR_ID": "ID_Produto", "PR_CAT": "Cat_Produto", "PR_NOME": "Nome_Produto"
})

# Tratamento de Inconsistências (Valores #N/D)
df["Cat_Produto"] = df["Cat_Produto"].replace("#N/D", "Sem Categoria")
df["Nome_Produto"] = df["Nome_Produto"].replace("#N/D", "Sem Nome")

# Mapeamento do Estado Civil para valores legíveis
dic_estado_civil = {1: "Casado/UE", 2: "Divorciado", 3: "Separado", 4: "Solteiro", 5: "Viúvo", 6: "Viúvo(a)"}
df["Estado_Civil"] = df["Estado_Civil"].map(dic_estado_civil)

# Remoção de Duplicatas
dup_mask = df.duplicated()
print(f"Total de duplicatas encontradas: {dup_mask.sum()}")

df_limpo = df.drop_duplicates()
perc_removida = (len(df) - len(df_limpo)) / len(df) * 100
print(f"Duplicatas removidas. Tamanho final: {len(df_limpo)} linhas (Redução de {perc_removida:.2f}%).")


# ESTATÍSTICA DESCRITIVA

print("=" * 50)
print("Análise Estatística da Coluna 'Qtd_Filhos'")
print()
print(f"Média:         {df_limpo['Qtd_Filhos'].mean():.2f}")
print(f"Mediana:       {df_limpo['Qtd_Filhos'].median()}")
print(f"Desvio Padrão: {df_limpo['Qtd_Filhos'].std():.2f}")
print(f"Moda:          {df_limpo['Qtd_Filhos'].mode().iloc[0]}")
print(f"Valor Máximo:  {df_limpo['Qtd_Filhos'].max()}")
print(f"Valor Mínimo:  {df_limpo['Qtd_Filhos'].min()}")
print(f"Contagem Total:{df_limpo['Qtd_Filhos'].count()}")
print("=" * 50)


# ETAPA DE AGRUPAMENTOS

# Agrupamento combinando Gênero, Estado Civil e Quantidade de Filhos
agrupamento = df_limpo.groupby(["Genero", "Estado_Civil", "Qtd_Filhos"]).size().reset_index(name="Quantidade")
agrupamento["Porcentagem"] = (agrupamento["Quantidade"] / len(df_limpo)) * 100

# Ordena os dados para mostrar os grupos mais representativos primeiro e formata
agrupamento = agrupamento.sort_values("Porcentagem", ascending=False)
agrupamento["Porcentagem"] = agrupamento["Porcentagem"].round(2).map('{:.2f}%'.format)

print("\nTop 5 Perfis de Clientes (Gênero x Estado Civil x Filhos):")
print(agrupamento.head(5).to_string(index=False))


# SPRINT 5: RELATÓRIO E CONCLUSÕES

# Preparando variáveis para o relatório
filhos_ate_2 = df_limpo.query("Qtd_Filhos in [0, 1, 2]").shape[0] / len(df_limpo) * 100
cat_principal = df_limpo.query("Cat_Produto in ['HIGIENE', 'ALIMENTOS']").shape[0] / len(df_limpo) * 100
segmento_a = df_limpo.query("Seg_Economica == 'A'").shape[0] / len(df_limpo) * 100
segmento_b = df_limpo.query("Seg_Economica == 'B'").shape[0] / len(df_limpo) * 100
mulheres = df_limpo.query("Genero == 'F'").shape[0] / len(df_limpo) * 100

print("\n" + "-" * 20 + " RELATÓRIO FINAL " + "-" * 20)
print(f"""1. Estrutura Familiar: A grande maioria dos clientes possui 0, 1 ou 2 filhos, representando {filhos_ate_2:.2f}% de toda a base.
2. Preferência de Consumo: Produtos de primeira necessidade dominam. HIGIENE e ALIMENTOS correspondem a {cat_principal:.2f}% das vendas.
3. Perfil Socioeconômico: O público de classe média (Segmento B) é o pilar da empresa com {segmento_b:.2f}%. O segmento premium (A) representa {segmento_a:.2f}%.
4. Demografia: O público feminino é a ligeira maioria com {mulheres:.2f}% das compras totais.
5. Principal Persona: O maior perfil isolado de clientes é composto por mulheres, solteiras e sem filhos, cujo foco absoluto está no setor de ALIMENTOS.

=> INSIGHT DE NEGÓCIO: 
Recomenda-se direcionar campanhas de marketing de alimentos práticos e porções individuais voltadas para mulheres solteiras sem filhos (maior volume).""")
print("-" * 50)

# EXPORTAÇÃO DOS DADOS LIMPOS
# Salvando em CSV (usando separador ';' igual à base original)
df_limpo.to_csv("df_limpo.csv", index=False, sep=";")

print("Arquivo 'df_limpo.csv' salvo com sucesso na mesma pasta do script!")
print("-" * 50)