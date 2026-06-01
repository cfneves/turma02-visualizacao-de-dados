# %% [markdown]
# ## Carregamento dos Dados
# 
# - Nesta etapa, realizamos a leitura dos dados brutos. Para otimizar o uso de memória, já convertemos as colunas de IDs para string e as colunas categóricas para o tipo 'category'.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# importando a base de dados e modificando os tipos de dados para o ideal em cada coluna.
df  = pd.read_csv('Base Varejo.csv', sep=';', dtype= {'CO_ID':str,'CL_ID':str,'CL_GENERO':'category','CL_SEG':'category','PR_ID':str,'PR_CAT':'category'})

# criaçao da copia da nossa base de dados
df_copy = df.copy()

# alterando o formato da coluna 'DATA'
df_copy['DATA'] = pd.to_datetime(df['DATA'], dayfirst=True)

# %%
# recolhendo amostras
print(df_copy.head(10))

# %%
# verificaçao de tipos de dados
print(df_copy.info())

# %% [markdown]
# ## Identificando Problemas
# 
# - Antes de qualquer análise, precisamos garantir a confiabilidade da base. Vamos investigar a presença de valores nulos e possíveis registros duplicados.

# %%
# verificaçao com precentual de nulos:
print((df_copy.isnull().sum() / len(df_copy) * 100).round(2))

# %%
# verificando duplicatas
print(df_copy.duplicated().sum())


# %% [markdown]
# ## Tratamento e Limpeza dos Dados
# 
# - Ao investigar as duplicatas, notamos um padrão no espaçamento dos índices. Isso indica que não houve falha sistêmica, mas sim o registro sequencial de múltiplos produtos iguais no caixa.
# 
# 
# - Ação: Para não perder histórico de vendas valioso, criamos uma nova coluna QTD_PR agrupando essas ocorrências.

# %%
# exibiçao em dataframe, para analisarmos melhor a questao das duplicatas

# filtra a base, mostrando as linhas que possuem copias iguais
duplicatas = df_copy[df_copy.duplicated(keep=False)]

# como queremos descobrir se a questao das duplicatas tem algo haver com o id do cliente e o id do produto as ordemos dessa forma para  que facilite nossa analise
print(duplicatas.sort_values(by=['CO_ID', 'PR_ID']).head(10))


# %%
# apos a analise anterior, decidimos criar uma nova coluna de quantidade, contendo as linhas duplicadas
coluna = df_copy.columns.tolist()
df_copy = df_copy.groupby(coluna, dropna=False).size().reset_index(name='QTD_PR')

print(df_copy[df_copy['CO_ID'] == '1000'].head(10))

# %%
# removendo colunas inteiramente vazias, pois nao fara sentido ter elas dentro da nossa base de dados que posteriormente sera utilizada por alguem
df_copy = df_copy.drop(columns= ['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'])

# %%
# correcao de inconssisetncias nas colunas PR_CAT e PR_NOME
df_copy['PR_CAT'] = df_copy['PR_CAT'].str.capitalize()
df_copy['PR_NOME'] = df_copy['PR_NOME'].str.capitalize()

# %%
# modificando o estado civil para estar condizente com a documentaçao e as regras de negocio da empresa:
map_df = {1:'Casado/Uniao Estavel', 2:'Divorciado', 3:'Separado', 4:'Solteiro', 5:'Viuvo'}
df_copy['CL_EC'] = df_copy['CL_EC'].map(map_df)

# %%
# vendo quantas linhas temos valores nulos/ausentes ou #N/D
print(df_copy[df_copy['PR_CAT'] == '#n/d'].shape[0])

# %%
# vamos substituir a string '#N/D' por valores nulos, pois na etapa de verificaçao nao foi constatado
df_copy['PR_CAT'] = df_copy['PR_CAT'].replace('#n/d', np.nan)
df_copy['PR_NOME'] = df_copy['PR_NOME'].replace('#n/d', np.nan)

# removendo nulos
df_copy = df_copy.dropna(subset=['PR_CAT', 'PR_NOME'])

# transformando novamente o PR_CAT em categoria
df_copy['PR_CAT'] = df_copy['PR_CAT'].astype('category')



# %% [markdown]
# - Removemos os valores nulos apos analisar as colunas PR_CAT, PR_NOME e PR_ID pois com os dados atuais se torna impossivel de recuperar  <br> esses 3.228 valores nulos/ausentes, iremos remover eles pois como sao poucos e nao tem maneira alguma de os recuperar, nao farao falta na nossa base
# 
# 

# %% [markdown]
# ## Estatísticas Descritivas

# %%
# filtraremos apenas colunas de texto (object), categorias (category) e texto (strings)
print(df_copy.describe(include=['object', 'category', 'str']))

# %%
# obtendo as principais estatisticas descritivas dos dados
def descritivas(data):
  variaveis = data.select_dtypes(include=np.number)
  desc = variaveis.describe().T
  desc["CV"] = desc["std"]/desc["mean"]
  desc["Skew"] = variaveis.skew()
  desc["Kurtosis"] = variaveis.kurt()
  ordered_cols = [
      "count", "mean", "std", "CV",
      "min", "25%", "50%", "75%", "max",
      "Skew", "Kurtosis"
  ]
  desc = desc[ordered_cols]
  return desc.round(2)


# %%
# analise descritiva da coluna CL_FHL (quantidade de filhos por cliente)
print(descritivas(df_copy[['CL_FHL']]))

# %% [markdown]
# ## Analise Exploratorio e Agrupamentos

# %% [markdown]
# #### Quem compra mais?

# %%
# quem compra mais da categoria de generos

#agrupando os dados pelo gênero e somando o volume de produtos
volume_por_genero = df_copy.groupby('CL_GENERO')['QTD_PR'].sum().reset_index()
volume_por_genero = volume_por_genero.rename(columns={'QTD_PR': 'Volume_Total'})

volume_por_genero = volume_por_genero.sort_values(by='Volume_Total', ascending=False)

print(volume_por_genero)

# %%
# grafico do volume por genero
plt.figure(figsize=(8, 5)) 

sns.barplot(data=volume_por_genero, x='CL_GENERO', y='Volume_Total', palette='viridis')
plt.title('Volume Total de Produtos Comprados por Gênero', fontsize=14)
plt.xlabel('Gênero', fontsize=12)
plt.ylabel('Volume Total', fontsize=12)
sns.despine() 



# %%
# fazendo um Drill-Down para olharmos mais fundo
drill_down_genero_cat = df_copy.pivot_table(
    index='PR_CAT',       
    columns='CL_GENERO',  
    values='QTD_PR',      
    aggfunc='sum'         
)

print(drill_down_genero_cat)

# %%
# quem compra mais em volume de produtos?
volume_cliente = df_copy.groupby('CL_ID')['QTD_PR'].sum().reset_index()
volume_cliente = volume_cliente.rename(columns={'QTD_PR': 'Qtd_Produtos'})

top_clientes_volume = volume_cliente.sort_values(by='Qtd_Produtos', ascending=False).head(10)

print(top_clientes_volume)

# %%
# verificaçao de clientes padrao ouro

volume_cliente['Qtd_Produtos'].describe()
percentis = volume_cliente['Qtd_Produtos'].quantile([0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99])

print(percentis)

# %% [markdown]
# #### Quais categorias vendem mais (em volume total)?

# %%
# abaixo criamos um agrupamento para sabermos quais categorias mais vendem
vendas_categoria = df_copy.groupby('PR_CAT')['QTD_PR'].sum().reset_index()
vendas_categoria = vendas_categoria.rename(columns={'QTD_PR': 'Volume_Total_Vendido'})

# ordenando as categorias
vendas_categoria = vendas_categoria.sort_values(by='Volume_Total_Vendido', ascending=False)

print(vendas_categoria)

# %%
# grafico do ranking das vendas
plt.figure(figsize=(10, 6))

sns.barplot(data=vendas_categoria, x='Volume_Total_Vendido', y='PR_CAT', palette='coolwarm')

plt.title('Ranking de Vendas por Categoria', fontsize=14)
plt.xlabel('Volume Total Vendido', fontsize=12)
plt.ylabel('Categoria de Produto', fontsize=12)
sns.despine()



# %%
# abaixo estamos pegando a categoria vencedora do codigo anterior 
categoria_campea = vendas_categoria.iloc[0]['PR_CAT']
print(f"Analisando a Categoria Campeã: {categoria_campea}\n")

# filtra o dataframe so para essa categoria e agrupa por Produto
df_campea = df_copy[df_copy['PR_CAT'] == categoria_campea]

# criando agrupamento para vermos por dentro da categoria, quais produtos mais vendem
produtos_da_categoria = df_campea.groupby('PR_NOME')['QTD_PR'].sum().reset_index() 
produtos_da_categoria = produtos_da_categoria.rename(columns={'QTD_PR': 'Volume'})
produtos_da_categoria = produtos_da_categoria.sort_values(by='Volume', ascending=False).head(10)

print(produtos_da_categoria)

# %%

# grafico dos produtos mais vendidos
plt.figure(figsize=(10, 6))

sns.barplot(data=produtos_da_categoria, x='Volume', y='PR_NOME', palette='coolwarm')

plt.title(f'Top 10 Produtos Mais Vendidos: {categoria_campea}', fontsize=14)
plt.xlabel('Volume de Vendas', fontsize=12)
plt.ylabel('Produto', fontsize=12)
sns.despine()



# %% [markdown]
# #### Como variam as vendas ao longo do tempo?

# %%
# criaçao de uma coluna ano mes para nosso grafico abaixo
df_copy['Ano_Mes'] = df_copy['DATA'].dt.to_period('M')

# agrupando as vendas ao longo dos meses
vendas_tempo = df_copy.groupby('Ano_Mes')['QTD_PR'].sum().reset_index()

# conversao da coluna ano_mes para string, para facilitar a plotagem
vendas_tempo['Ano_Mes'] = vendas_tempo['Ano_Mes'].astype(str)

# abaixo iremos fazer um grafico de linha para termos noçao de como variam as vendas ao longo do tempo
plt.figure(figsize=(22, 5))
sns.lineplot(data=vendas_tempo, x='Ano_Mes', y='QTD_PR', marker='o')
plt.title('Variacao do Volume de Vendas ao Longo do Tempo')
plt.xlabel('Mes e Ano')
plt.ylabel('Volume de Produtos Vendidos')
plt.xticks(rotation=45)
plt.tight_layout()


# %%
# vamos extrair o dia da semana (0 = Segunda, 6 = Domingo)
df_copy['Dia_Semana'] = df_copy['DATA'].dt.dayofweek

dias_map = {0: 'Segunda', 1: 'Terça', 2: 'Quarta', 3: 'Quinta', 4: 'Sexta', 5: 'Sábado', 6: 'Domingo'}
df_copy['Nome_Dia'] = df_copy['Dia_Semana'].map(dias_map)

# agrupando o volume de vendas por dia da semana
vendas_por_dia = df_copy.groupby('Nome_Dia')['QTD_PR'].sum().reindex(list(dias_map.values())).reset_index()
print(vendas_por_dia)

# %%
# modificando a coluna ano mes para string, pois so assim dara para fazero grafico para melhor visualizaçao
df_copy['Ano_Mes'] = df_copy['DATA'].dt.to_period('M').astype(str)

# agrupamos por ano_mes E por segmento (CL_SEG)
vendas_tempo_segmento = df_copy.groupby(['Ano_Mes', 'CL_SEG'])['QTD_PR'].sum().reset_index()

# criaçao do gráfico de linha por segmento
plt.figure(figsize=(22, 5))
sns.lineplot(data=vendas_tempo_segmento, x='Ano_Mes', y='QTD_PR', hue='CL_SEG', marker='o', palette='Set1')

plt.title('Variação das Vendas ao Longo do Tempo por Segmento de Cliente')
plt.xlabel('Mes e Ano')
plt.ylabel('Volume de Produtos Vendidos')
plt.xticks(rotation=45)
plt.legend(title='Segmento')
plt.tight_layout()
plt.show()


print("""
=========================================================
🎯 CONCLUSÕES E INSIGHTS FINAIS
=========================================================
      
      1. Perfil do Cliente: A maioria absoluta da nossa carteira de clientes é composta por pessoas sem filhos (50%), caracterizando famílias de pequeno porte (média de 1,15 filhos).

      2. Motor de Vendas: A categoria "Alimentos" é a campeã isolada de volume, sendo puxada principalmente por produtos como Presunto Cozido e Sardinha.

      3. Sazonalidade (Dias da Semana): Identificamos picos de vendas na Sexta-feira, Domingo (representando 15,80% cada) e na Quarta-Feira (18,50%).

      4. Próximos Passos (Problemas Remanescentes): Seria recomendado acionar o setor de marketing para entender o baixo volume atípico de vendas aos Sábados (~11,37%) e investigar possíveis indisponibilidades de sistema ou falta de campanhas nesse dia.

      5. Clientes VIP (Top 10%): O nosso "Padrão Ouro" engloba clientes que compraram mais de 1.112 itens. Este grupo deve ser o alvo principal de ações de retenção e programas de fidelidade, dado o seu alto valor para o negócio.

      6. Atenção a Outliers: O maior comprador adquiriu 1.772 produtos, um valor significativamente acima do corte do percentil 99% (1.396). Isso levanta uma hipótese de negócio: podemos ter clientes corporativos (B2B) atuando em nossa base de varejo padrão.

      7. O Núcleo da Base: Metade dos nossos clientes (50%) consome entre 657 e 977 itens, indicando um comportamento de compra consistente e uma oportunidade clara para campanhas de cross-sell (venda cruzada).

      8. Liderança Feminina Contínua: As clientes do gênero feminino lideram o volume de compras em absolutamente todas as categorias.

      9. Proporção Estável: Independentemente do tipo de produto, a divisão de consumo é extremamente homogênea. Em todas as categorias, as mulheres representam uma fatia que varia entre 51,5% e 53%, enquanto os homens respondem pelo restante (cerca de 47% a 48,5%).

      10. O "Porquê": Isso nos diz que, nesta base de varejo específica, o comportamento de compra entre gêneros é muito similar e não há nenhum nicho de produto polarizado

      11. Evite Segmentação Extrema por Gênero: Como as proporções variam muito pouco (no máximo ~5% de diferença entre os gêneros), gastar muito orçamento de Marketing tentando criar campanhas exclusivamente masculinas ou femininas para categorias específicas terá um ROI (Retorno sobre Investimento) baixo. O gênero não é a principal alavanca de conversão aqui.

      12. A Estratégia de Cross-Selling: O verdadeiro abismo nos dados está no volume entre categorias. A categoria de "Alimentos" tem um volume quase 3 vezes maior do que "Higiene" e "Limpeza" somadas.

      13. Ação Prática: A estratégia ideal é usar "Alimentos" como isca. Como todo mundo (homens e mulheres) compra muito alimento, o sistema do varejo ou aplicativo deve sugerir combos promocionais de venda cruzada (cross-selling). Ex: "Compre X em Alimentos e ganhe 15% de desconto no departamento Pet ou de Acessórios". Isso alavanca os produtos que têm menor saída aproveitando o fluxo pesado da categoria principal.

=========================================================
      PROBLEMAS PARA O GESTOR
=========================================================
      
      1. Removemos cerca de 3.228 valores nulos da nossa base, pedir orientação do responsavel para tomarmos a melhor decisao possivel, deixar em aberto a questao do nulos, pois pode <br> ter a chance de recuperar, caso cruzemos com alguma outra base de dados da nossa empresa

      2. Relatar sobre a criaçao da nova coluna QTD_PR, para justificar a "perda" de linhas da nossa base de dados

""")
