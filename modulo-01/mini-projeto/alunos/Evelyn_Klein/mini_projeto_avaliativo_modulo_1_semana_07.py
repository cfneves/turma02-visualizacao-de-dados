# -*- coding: utf-8 -*-
"""Mini_Projeto_Avaliativo_Módulo_1_Semana_07 (1).ipynb

Automatically generated from the notebook.
"""

"""# **Introdução**

Este notebook reúne uma análise exploratória da base de varejo disponibilizada para o Mini Projeto Avaliativo.

O foco é entender o comportamento de compra, identificar padrões de consumo e destacar diferenças entre perfis de clientes, sempre com uma apresentação organizada e fácil de acompanhar."""

"""Nesta análise, o conteúdo foi organizado em etapas para facilitar a leitura:

- entendimento inicial da base;
- limpeza e padronização;
- criação de variáveis derivadas;
- análises por tempo, produto e perfil de cliente;
- síntese final dos principais achados."""

"""# **Importação de Bibliotecas e Carregamento dos Dados**

Nesta etapa, carregamos as bibliotecas que sustentam toda a análise.

- `pandas` é usado para manipulação, organização e agregação dos dados;
- `numpy` apoia cálculos numéricos e operações auxiliares;
- `matplotlib` e `seaborn` são responsáveis pelos gráficos e visualizações.

O conjunto de dados é lido a partir de uma URL pública do GitHub e copiado para um dataframe de trabalho. Isso deixa o notebook mais reproduzível e evita alterações na base original durante a análise."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
url = "https://raw.githubusercontent.com/evelynkleinenf-cloud/varejo_mini_projeto_sctec/3bfe704f63ba0c279c157134da1525f7ef63d79e/Base%20Varejo.csv"

df_original = pd.read_csv(url, sep=';')
df = df_original.copy()
print('Bibliotecas e data set "Varejo" carregados com sucesso!')

"""## **Entendimento dos Dados**

Antes de qualquer tratamento, observamos a estrutura da base para entender o volume de registros, os tipos de variáveis e possíveis lacunas.

Embora o material de apoio descreva um recorte mais amplo, o arquivo carregado neste notebook apresenta registros observáveis entre 2019 e 2022. Essa será a janela considerada nas interpretações seguintes."""

df.head()

df.info()

"""A leitura inicial com `df.head()` e `df.info()` confirma que a base bruta possui 830.000 linhas e 14 colunas.

Também fica evidente que quatro colunas (`Unnamed: 10` a `Unnamed: 13`) estão vazias, além da necessidade de padronizar tipos de dados e categorias antes de seguir para a análise.

Em resumo, essa etapa serve para enxergar a estrutura geral da base e antecipar quais ajustes serão necessários na limpeza."""

"""O dataset utilizado apresenta 10 colunas realmente úteis para a análise:

- `DATA`: data da compra;
- `CO_ID`: identificação do número de compra;
- `CL_ID`: identificação do cliente;
- `CL_GENERO`: sexo biológico informado pelo cliente;
- `CL_EC`: estado civil do cliente;
- `CL_FHL`: número de filhos do cliente;
- `CL_SEG`: segmentação econômica do cliente;
- `PR_ID`: código do produto adquirido;
- `PR_CAT`: categoria do produto adquirido;
- `PR_NOME`: nome do produto adquirido.

Essa leitura ajuda a separar variáveis de identificação, perfil do cliente e características do produto, o que será essencial nas próximas etapas."""

df.describe()

"""A tabela gerada por `df.describe()` resume as variáveis numéricas da base e mostra medidas de tendência central, dispersão e amplitude.

Os campos vazios (`Unnamed: 10` a `Unnamed: 13`) não agregam informação analítica e, por isso, serão desconsiderados.

Em linhas gerais:

- `CO_ID` e `CL_ID` funcionam como identificadores e, por isso, apresentam grande amplitude;
- `CL_EC` e `CL_FHL` têm valores discretos e concentrados;
- `PR_ID` mostra distribuição intermediária entre os produtos cadastrados.

Esses resultados reforçam que a base tem boa estrutura numérica para seguir com a limpeza e a análise."""

df_principais = df.copy()
df_principais = df.drop(columns=['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'])
df_principais.head()

"""Após entender a composição da base, mantemos apenas as colunas relevantes para a análise.

A remoção das colunas vazias simplifica o dataframe, reduz ruído e evita que informações sem utilidade analítica interfiram nas próximas etapas."""

"""# **Limpeza e Tratamento dos Dados + Feature Engineering**

Nesta fase, a base é padronizada para aumentar a confiabilidade da análise.

Aqui trabalhamos com três objetivos principais:

- eliminar redundâncias;
- corrigir e padronizar tipos de dados;
- criar variáveis derivadas que ajudem a enxergar sazonalidade e comportamento de compra."""

"""## **Tratamento de Duplicatas**

A presença de linhas duplicadas pode inflar resultados e distorcer leituras de volume.

Por isso, o primeiro passo é identificar duplicidades exatas e removê-las, garantindo uma base mais consistente para as análises seguintes."""

num_duplicatas = df_principais.duplicated().sum()
print(f'Número de linhas duplicadas no dataset: {num_duplicatas}')

df_limpo = df_principais.drop_duplicates().copy()
num_duplicatas_apos = df_limpo.duplicated().sum()
print(f'Número de linhas duplicadas no dataset: {num_duplicatas_apos}')

"""Com a remoção das duplicatas exatas, a base passa a refletir apenas registros únicos.

Isso evita contagens infladas e deixa os volumes analisados mais confiáveis."""

"""## **Correção dos Tipos de Dados**

Nesta etapa, cada coluna é ajustada para o formato mais adequado:

- datas em `datetime`;
- códigos e identificadores em inteiros nulos seguros (`Int64`);
- textos e categorias padronizados em maiúsculas e sem espaços extras.

Esse tratamento evita erros em cálculos, agrupamentos e visualizações."""

# Confirmar o formato das datas válidas
df_limpo['DATA'].min(), df_limpo['DATA'].max()

# Conversão de string para datetime (assim o pandas entende como data de verdade)
df_limpo['DATA'] = pd.to_datetime(df_limpo['DATA'],format='%d/%m/%Y',errors='coerce') # errors='coerce' para evitar surgimento de erros com datas inválidas

# Confirmar se o errors='coerce' realmente evitou o surgimento de algum valor inválido
df_limpo['DATA'].isna().sum()

# Remover possíveis espaços invisíveis nos nomes das colunas para evitar erros ao acessá-las
df_limpo.columns = df_limpo.columns.str.strip()

# Converter colunas numéricas para tipo inteiro(Int64 é melhor que int64 porque aceita valores ausentes sem dar erro, assegurando que cálculos estatísticos e análises quantitativas possam ser realizados corretamente)
colunas_inteiras = ['CO_ID', 'CL_ID', 'CL_EC', 'CL_FHL', 'PR_ID']
for col in colunas_inteiras:
    df_limpo[col] = pd.to_numeric(df_limpo[col], errors='coerce').astype('Int64')

# Padronizar colunas categóricas curtas: evita categorias duplicadas por erro de digitação
colunas_categoricas = ['CL_GENERO', 'CL_SEG']
for col in colunas_categoricas:
    df_limpo[col] = df_limpo[col].astype('string').str.strip().str.upper()

# Padronizar colunas textuais removendo possíveis espaços extras e alterando todas as letras para maiúsculas
colunas_texto = ['PR_CAT', 'PR_NOME']
for col in colunas_texto:
    df_limpo[col] = df_limpo[col].astype('string').str.strip().str.upper()

# Padronizar colunas string para categoria, facilitando análises e agrupamentos
for col in ['CL_GENERO', 'CL_SEG', 'PR_CAT', 'PR_NOME']:
    df_limpo[col] = df_limpo[col].astype('category')

"""## **Tratamento de Valores Ausentes**

Depois das conversões, verificamos novamente a presença de valores nulos.

Essa checagem é importante porque datas inválidas podem virar `NaT` e conversões numéricas inconsistentes podem gerar `NaN`, indicando onde ainda seria necessário investigar a origem do problema."""

print(df_limpo.isna().sum())

"""Após as conversões, não surgiram `NaN`/`NaT` nas colunas principais.

Isso confirma que a padronização foi bem-sucedida e que a base segue consistente para os próximos cruzamentos analíticos."""

"""## **Checagem de Qualidade (Data Consistency) + Mini-relatório de Inconsistências**

Com a base limpa, fazemos uma validação final para confirmar se os tipos estão corretos, se não há datas inválidas e se os identificadores seguem padrões coerentes.

A ideia aqui é transformar a limpeza em uma etapa verificável, e não apenas em uma sequência de transformações."""

# Confirmar se cada coluna ficou com o tipo correto
print(df_limpo.dtypes)

# Datas inválidas????
df_limpo['DATA'].isna().sum()

# Conferência de identificadores numéricos
for col in ['CO_ID', 'CL_ID', 'CL_EC', 'CL_FHL', 'PR_ID']:
    print(f'\nColuna: {col}')
    print('nulos:', df_limpo[col].isna().sum())
    print('menor valor:', df_limpo[col].min())
    print('maior valor:', df_limpo[col].max())
    print('valores negativos:', (df_limpo[col] < 0).sum())

"""A checagem dos identificadores numéricos confirma que não há valores nulos nem negativos nas colunas analisadas.

Os intervalos encontrados são compatíveis com a lógica da base:

- `CO_ID` representa compras;
- `CL_ID` representa clientes;
- `CL_EC` e `CL_FHL` representam perfis discretos;
- `PR_ID` representa produtos.

Isso indica que os códigos estão prontos para uso nas análises comparativas e nos cruzamentos com outras variáveis."""

"""***Mini-relatório de Inconsistências***

O mini-relatório abaixo resume os principais pontos que merecem atenção na base.

Ele ajuda a separar inconsistências reais de variações esperadas de preenchimento, deixando o diagnóstico final mais objetivo."""

pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 200)

# Regras de validação de acordo com os valores encontrados no dataset
valid_genero = {'M', 'F'}
valid_seg = {'A', 'B', 'C'}
valid_pr_cat = {
    'ACESSORIOS',
    'ALIMENTOS',
    'BEBIDAS',
    'HIGIENE',
    'LIMPEZA',
    'PET'}

# Datas inválidas
datas_invalidas_mask = df_limpo['DATA'].isna()
qtd_datas_invalidas = int(datas_invalidas_mask.sum())
datas_invalidas = df_limpo.loc[
    datas_invalidas_mask,
    ['DATA', 'CO_ID', 'CL_ID', 'PR_ID']].copy()

# Categorias fora do padrão
regras = {'CL_GENERO': valid_genero,'CL_SEG': valid_seg,'PR_CAT': valid_pr_cat,}
resumo_categorias = []
tabelas_invalidas = {}

for col, validos in regras.items():
    serie = df_limpo[col].astype('string').str.strip().str.upper()
    mask = ~serie.isin(validos) & serie.notna()

    resumo_categorias.append({
        'coluna': col,
        'qtd_fora_padrao': int(mask.sum()),
        'valores_diferentes_encontrados': sorted(serie.loc[mask].drop_duplicates().tolist())})

    tabelas_invalidas[col] = (
        df_limpo.loc[mask, [col, 'CO_ID', 'CL_ID', 'PR_ID']]
        .drop_duplicates()
        .sort_values(col)
        .reset_index(drop=True)    )

resumo_categorias_df = pd.DataFrame(resumo_categorias)

# Inconsistências entre PR_NOME e PR_ID
nomes_com_ids_df = (
    df_limpo.groupby('PR_NOME', dropna=False, observed=False)['PR_ID']
    .nunique()
    .reset_index(name='qtd_PR_ID'))

nomes_com_ids_diferentes_df = (
    nomes_com_ids_df[nomes_com_ids_df['qtd_PR_ID'] > 1]
    .sort_values(['qtd_PR_ID', 'PR_NOME'], ascending=[False, True])
    .reset_index(drop=True))

ids_com_nomes_df = (
    df_limpo.groupby('PR_ID', dropna=False, observed=False)['PR_NOME']
    .nunique()
    .reset_index(name='qtd_PR_NOME'))

ids_com_nomes_diferentes_df = (
    ids_com_nomes_df[ids_com_nomes_df['qtd_PR_NOME'] > 1]
    .sort_values(['qtd_PR_NOME', 'PR_ID'], ascending=[False, True])
    .reset_index(drop=True))

# Resumo geral
resumo_geral_df = pd.DataFrame({
    'verificacao': [
        'Datas inválidas',
        'CL_GENERO fora do padrão',
        'CL_SEG fora do padrão',
        'PR_CAT fora do padrão',
        'PR_NOME com mais de um PR_ID',
        'PR_ID com mais de um PR_NOME',
    ],
    'quantidade': [
        qtd_datas_invalidas,
        int(resumo_categorias_df.loc[resumo_categorias_df['coluna'] == 'CL_GENERO', 'qtd_fora_padrao'].iloc[0]),
        int(resumo_categorias_df.loc[resumo_categorias_df['coluna'] == 'CL_SEG', 'qtd_fora_padrao'].iloc[0]),
        int(resumo_categorias_df.loc[resumo_categorias_df['coluna'] == 'PR_CAT', 'qtd_fora_padrao'].iloc[0]),
        len(nomes_com_ids_diferentes_df),
        len(ids_com_nomes_diferentes_df),]})

# Exibição do mini-relatório
print('RESUMO GERAL')
display(resumo_geral_df)

print('CATEGORIAS FORA DO PADRÃO')
display(resumo_categorias_df)

print('EXEMPLOS DE DATAS INVÁLIDAS')
display(datas_invalidas.head(10))

print('EXEMPLOS DE VALORES FORA DO PADRÃO')
for col, tabela in tabelas_invalidas.items():
    print(f'\nColuna: {col}')
    display(tabela.head(10))

print('PR_NOME COM MAIS DE UM PR_ID')
display(nomes_com_ids_diferentes_df.head(10))

print('PR_ID COM MAIS DE UM PR_NOME')
display(ids_com_nomes_diferentes_df.head(10))

"""Os testes apontam duas frentes de atenção: registros de `PR_CAT` classificados como `#N/D` e produtos com o mesmo nome associados a IDs diferentes.

Como não apareceu o caso inverso, o problema parece estar mais ligado à padronização das descrições do que à identidade do produto."""

"""Os testes apontam os seguintes destaques:

- não foram encontrados problemas relevantes em `CL_GENERO` e `CL_SEG`;
- a coluna `PR_CAT` contém registros classificados como `#N/D`, o que indica categoria não informada ou não classificada;
- há produtos com o mesmo nome associados a mais de um ID, o que merece atenção na padronização;
- não foi identificado o caso inverso, ou seja, um mesmo ID apontando para nomes diferentes.

Em resumo, a base está consistente nas variáveis centrais, mas ainda possui inconsistências de classificação em produtos."""

"""## **Base de Trabalho**

Criamos uma cópia da base limpa para preservar a etapa de tratamento original.

A partir dela, as novas variáveis e as análises exploratórias são feitas sem alterar o dataframe já validado, o que deixa o fluxo mais seguro e fácil de acompanhar."""

df_feat = df_limpo.copy()

"""## **Feature Engineering**

Com a base limpa em mãos, passamos a criar variáveis derivadas que ampliam o poder de análise.

Esses atributos adicionais permitem estudar sazonalidade, comportamento de compra e perfil dos clientes com mais detalhe do que os campos originais oferecem sozinhos."""

sns.set_theme(style='whitegrid') # define o estilo visual de todos os gráficos gerados pelo Seaborn para 'whitegrid'. Este estilo é caracterizado por um fundo claro com uma grade, o que geralmente melhora a legibilidade de vários tipos de gráficos.
pd.set_option('display.max_colwidth', None) #  Esta opção do pandas é usada para evitar o truncamento do conteúdo dentro das colunas de um DataFrame quando ele é exibido. Ao definir como None, o pandas mostrará o conteúdo completo de cada coluna, independentemente do seu comprimento.
pd.set_option('display.width', 200) # Esta opção do pandas determina a largura máxima de exibição para DataFrames, em caracteres. Um valor de 200 significa que o pandas tentará ajustar a saída do DataFrame dentro de 200 caracteres, possivelmente quebrando o conteúdo ou ajustando o número de colunas visíveis.

"""### **Variáveis Temporais e Indicador de Item**

A partir da coluna `DATA`, criamos `ANO`, `MES`, `TRIMESTRE`, `DIA_SEMANA_NUM`, além dos nomes do mês e do dia da semana.

Também incluímos a variável `ITEM`, que funciona como um marcador simples para contar o volume de linhas em cada agrupamento.

Essas novas colunas são essenciais para transformar datas em leitura analítica prática e comparável."""

df_feat['ANO'] = df_feat['DATA'].dt.year
df_feat['MES'] = df_feat['DATA'].dt.month
df_feat['TRIMESTRE'] = df_feat['DATA'].dt.quarter
df_feat['DIA_SEMANA_NUM'] = df_feat['DATA'].dt.dayofweek

mapa_meses = {
    1: 'JANEIRO', 2: 'FEVEREIRO', 3: 'MARCO', 4: 'ABRIL',
    5: 'MAIO', 6: 'JUNHO', 7: 'JULHO', 8: 'AGOSTO',
    9: 'SETEMBRO', 10: 'OUTUBRO', 11: 'NOVEMBRO', 12: 'DEZEMBRO'}

mapa_dias = {
    0: 'SEGUNDA', 1: 'TERCA', 2: 'QUARTA', 3: 'QUINTA',
    4: 'SEXTA', 5: 'SABADO', 6: 'DOMINGO'}

df_feat['NOME_MES'] = df_feat['MES'].map(mapa_meses)
df_feat['NOME_DIA'] = df_feat['DIA_SEMANA_NUM'].map(mapa_dias)

ordem_meses = [
    'JANEIRO', 'FEVEREIRO', 'MARCO', 'ABRIL', 'MAIO', 'JUNHO',
    'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']

ordem_dias = ['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA', 'SABADO', 'DOMINGO']

df_feat['ITEM'] = 1

"""Com `ANO`, `MES`, `TRIMESTRE`, `NOME_MES` e `NOME_DIA`, a base passa a responder perguntas de sazonalidade com mais clareza.

A variável `ITEM` funciona como contador de linhas, facilitando somas por qualquer grupo."""

"""### **Variáveis de Família e Classe Social**

Os cruzamentos com `CL_FHL` e `CL_EC` ajudam a observar como o comportamento de consumo varia segundo tamanho da família e faixa de classe social.

Essas relações são úteis para identificar perfis com maior representatividade em determinadas combinações de produtos."""

pd.crosstab(df_limpo['CL_FHL'], df_limpo['PR_CAT'])
pd.crosstab(df_limpo['CL_EC'], df_limpo['PR_CAT'])
pd.crosstab(df_limpo['CL_FHL'], df_limpo['CL_EC'])

"""Esses cruzamentos mostram como categoria, classe social e tamanho da família se distribuem em conjunto.

A leitura combinada ajuda a identificar quais perfis aparecem com mais força em cada grupo de produtos."""

"""### **Variáveis da Compra**

Agora o foco passa para o nível da transação.

Os indicadores calculados por compra permitem enxergar:

- quantos itens foram comprados;
- quantos produtos diferentes apareceram na mesma nota;
- quantas categorias distintas compuseram a compra.

Essa visão é importante porque mostra o formato da cesta de consumo, e não apenas a frequência dos produtos."""

resumo_compra = df_limpo.groupby('CO_ID').agg(
    qtd_itens=('PR_ID', 'count'),
    qtd_produtos_diferentes=('PR_ID', 'nunique'),
    qtd_categorias=('PR_CAT', 'nunique')
).reset_index()

"""# **Análise Exploratória**

A partir daqui, os gráficos e tabelas passam a responder perguntas mais objetivas sobre sazonalidade, produtos, perfil de cliente e evolução do consumo ao longo do tempo."""

"""## **Sazonalidade das Vendas**

Nesta etapa, analisamos como o volume de itens vendidos se distribui ao longo dos meses, dias da semana e trimestres.

Esse recorte temporal ajuda a identificar períodos de maior movimentação e possíveis padrões sazonais no consumo."""

# Vendas por mês
vendas_por_mes = (
    df_feat.groupby('NOME_MES')['ITEM']
    .sum()
    .reindex(ordem_meses)
    .reset_index(name='qtd_itens'))
display(vendas_por_mes)

# Vendas por dia
vendas_por_dia = (
    df_feat.groupby('NOME_DIA')['ITEM']
    .sum()
    .reindex(ordem_dias)
    .reset_index(name='qtd_itens'))
display(vendas_por_dia)

# Vendas por Trimestre
sazonalidade_trimestre = (
    df_feat.groupby('TRIMESTRE')['ITEM']
    .sum()
    .reindex([1, 2, 3, 4])
    .reset_index(name='qtd_itens'))
display(sazonalidade_trimestre)

# Épocas do ano em que se vende mais
df_limpo.groupby('MES')['PR_ID'].count()
pd.pivot_table(
    df_limpo,
    index='NOME_MES',
    columns='PR_CAT',
    values='PR_ID',
    aggfunc='count',
    fill_value=0)

# Dias da semana com mais vendas
df_limpo.groupby('NOME_DIA')['PR_ID'].count()

"""Leitura dos resultados: janeiro foi o mês com maior volume e novembro o menor; quarta-feira concentrou mais itens do que os outros dias, enquanto sábado ficou com a menor marca; no recorte trimestral, o 1º trimestre liderou e o 4º trimestre teve o menor volume.

O padrão indica concentração de consumo no início do ano e uma desaceleração no fim da série."""

"""## **Produtos e Categorias Mais Vendidos**

Aqui observamos quais categorias concentram mais volume de itens e quais produtos aparecem com maior frequência no conjunto analisado.

Esse tipo de leitura é útil para entender o mix de consumo predominante na base."""

# Vendas por Categoria
vendas_por_categoria = (
    df_feat.groupby('PR_CAT')['ITEM']
    .sum()
    .sort_values(ascending=False)
    .reset_index(name='qtd_itens'))
display(vendas_por_categoria)

# Top 20 Produtos Mais Vendidos
top_produtos = (
    df_feat['PR_NOME']
    .value_counts()
    .head(20)
    .reset_index())
top_produtos.columns = ['PR_NOME', 'qtd_itens']
display(top_produtos)

# Produtos/categorias mais frequentes
df_limpo['PR_CAT'].value_counts()
df_limpo['PR_NOME'].value_counts().head(20)

# Gráfico
plt.figure(figsize=(12, 7))
sns.barplot(data=top_produtos, y='PR_NOME', x='qtd_itens', color='darkorange')
plt.title('Top 20 produtos mais vendidos')
plt.xlabel('Quantidade de itens')
plt.ylabel('Produto')
plt.tight_layout()
plt.show()

"""Há forte concentração em `ALIMENTOS`, seguida por `HIGIENE` e `LIMPEZA`.

Entre os produtos, o top 20 é relativamente próximo em frequência, o que sugere uma cesta dominada por itens recorrentes e não por um único produto isolado."""

"""## **Resumo da Compra**

Nesta parte, resumimos cada compra em três indicadores:

- quantidade total de itens;
- quantidade de produtos diferentes;
- quantidade de categorias distintas.

Essas métricas mostram o tamanho e a diversidade da cesta de compra, permitindo comparar compras mais enxutas com compras mais completas."""

# Resumo da Compra
resumo_compra = (
    df_feat.groupby(['CO_ID', 'CL_ID', 'DATA'])
    .agg(
        qtd_itens=('ITEM', 'sum'),
        qtd_produtos_diferentes=('PR_ID', 'nunique'),
        qtd_categorias=('PR_CAT', 'nunique')).reset_index())
display(resumo_compra.head())

"""Em média, cada compra reúne cerca de 45 itens, 40 produtos distintos e 5 categorias.

Isso caracteriza cestas com boa diversidade e abre espaço para análises futuras de ticket médio e fidelidade."""

"""## **Perfil de Consumo dos Clientes**

Agora a análise passa para o comportamento por perfil.

O objetivo é entender como o consumo se distribui entre classe social, tamanho da família e gênero, verificando quais grupos concentram maior volume de itens."""

# Consumo por Classe, Família e Gênero
consumo_por_classe = df_feat.groupby('CL_EC')['ITEM'].sum().sort_values(ascending=False).reset_index(name='qtd_itens')
consumo_por_familia = df_feat.groupby('CL_FHL')['ITEM'].sum().sort_values(ascending=False).reset_index(name='qtd_itens')
consumo_por_genero = df_feat.groupby('CL_GENERO')['ITEM'].sum().sort_values(ascending=False).reset_index(name='qtd_itens')
display(consumo_por_classe)
display(consumo_por_familia)
display(consumo_por_genero)

# Perfil de consumo por gênero
pd.pivot_table(
    df_limpo,
    index='CL_GENERO',
    columns='PR_CAT',
    values='PR_ID',
    aggfunc='count',
    fill_value=0)

"""A leitura por perfil indica volume ligeiramente maior no gênero feminino e reforça que a classe 3 e as famílias sem filhos concentram os maiores volumes observados.

O cruzamento por gênero e categoria complementa essa visão ao mostrar preferências específicas de compra."""

"""## **Cruzamentos entre Perfil e Categoria**

As tabelas cruzadas ajudam a enxergar quais categorias aparecem com mais força em cada grupo de clientes.

Esse cruzamento é importante porque conecta o perfil do consumidor ao tipo de produto comprado, revelando preferências que não aparecem em uma análise isolada."""

# Categoria por Classe, Família e Gênero
cat_por_classe = pd.crosstab(df_feat['CL_EC'], df_feat['PR_CAT'])
cat_por_familia = pd.crosstab(df_feat['CL_FHL'], df_feat['PR_CAT'])
cat_por_genero = pd.crosstab(df_feat['CL_GENERO'], df_feat['PR_CAT'])
display(cat_por_classe)
display(cat_por_familia)
display(cat_por_genero)

# Gráfico
plt.figure(figsize=(12, 6))
cat_por_classe.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='tab20')
plt.title('Categorias por classe social')
plt.xlabel('CL_EC')
plt.ylabel('Quantidade de itens')
plt.legend(title='PR_CAT', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

"""## **Classe Social e Tamanho da Família**

Os mapas de calor comparam classe social e tamanho da família em duas leituras complementares: valor absoluto e porcentagem.

A primeira mostra volume bruto de registros; a segunda facilita a comparação proporcional entre as classes, deixando a interpretação mais justa entre grupos de tamanhos diferentes."""

# Classe Social e Tamanho da Família (HeatMap - Valor Absoluto)
heatmap_ec_fhl = pd.crosstab(df_feat['CL_EC'], df_feat['CL_FHL'])
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_ec_fhl, annot=True, fmt='d', cmap='YlGnBu', linewidths=0.3, linecolor='white')
plt.title('Classe social (CL_EC) x Tamanho da familia (CL_FHL)')
plt.xlabel('CL_FHL')
plt.ylabel('CL_EC')
plt.tight_layout()
plt.show()

# Classe Social e Tamanho da Família (HeatMap - Porcentagem)
heatmap_ec_fhl_pct = pd.crosstab(df_feat['CL_EC'], df_feat['CL_FHL'], normalize='index') * 100
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_ec_fhl_pct, annot=True, fmt='.1f', cmap='Blues', linewidths=0.3, linecolor='white')
plt.title('CL_EC x CL_FHL em porcentagem por classe social')
plt.xlabel('CL_FHL')
plt.ylabel('CL_EC')
plt.tight_layout()
plt.show()

"""O mapa percentual complementa o absoluto ao mostrar a composição relativa de cada classe social.

Assim, fica mais fácil comparar grupos com tamanhos diferentes sem deixar o maior volume bruto dominar a interpretação."""

"""## **Evolução Temporal das Vendas**

Nesta seção observamos como o volume de itens vendidos varia ao longo dos anos, meses, trimestres e dias da semana.

A leitura temporal é importante porque revela tendências, picos e quedas que podem estar ligados ao calendário, ao comportamento do consumidor ou à estrutura da operação."""

# Evolução Anual das Vendas - Ano Mais e Menos Vendido
vendas_por_ano = (
    df_feat.groupby('ANO')['ITEM']
    .sum()
    .reset_index(name='qtd_itens')
    .sort_values('qtd_itens', ascending=False))
display(vendas_por_ano)
ano_mais_vendido = vendas_por_ano.iloc[0]['ANO']
ano_menos_vendido = vendas_por_ano.iloc[-1]['ANO']
print(f'Ano com mais vendas: {ano_mais_vendido}')
print(f'Ano com menos vendas: {ano_menos_vendido}')

# Gráfico
plt.figure(figsize=(10, 5))
sns.barplot(data=vendas_por_ano, x='ANO', y='qtd_itens', color='steelblue')
plt.title('Quantidade de itens vendidos por ano')
plt.xlabel('Ano')
plt.ylabel('Quantidade de itens')
plt.tight_layout()
plt.show()

# Itens Mais Vendidos por Ano
plt.figure(figsize=(10, 5))
sns.barplot(data=vendas_por_ano, x='ANO', y='qtd_itens', color='steelblue')
plt.title('Quantidade de itens vendidos por ano')
plt.xlabel('Ano')
plt.ylabel('Quantidade de itens')
plt.tight_layout()
plt.show()

"""A análise anual mostra que 2021 concentrou o maior volume de itens vendidos, enquanto 2022 ficou com o menor volume dentro do período observado.

Isso sugere uma desaceleração no final da série e reforça a importância de acompanhar a base ao longo do tempo para entender mudanças de comportamento."""

# Vendas por Mês
vendas_mensais = (
    df_feat.groupby(['ANO', 'MES'])['ITEM']
    .sum()
    .reset_index(name='qtd_itens'))
vendas_mensais['DATA_REF'] = pd.to_datetime(
    vendas_mensais['ANO'].astype(str) + '-' + vendas_mensais['MES'].astype(str) + '-01')

plt.figure(figsize=(14, 5))
sns.lineplot(data=vendas_mensais, x='DATA_REF', y='qtd_itens', marker='o')
plt.title('Evolucao mensal da quantidade de itens vendidos')
plt.xlabel('Mes')
plt.ylabel('Quantidade de itens')
plt.tight_layout()
plt.show()

# Vendas por Trimestre
vendas_trimestre_ano = (
    df_feat.groupby(['ANO', 'TRIMESTRE'])['ITEM']
    .sum()
    .reset_index(name='qtd_itens'))

vendas_trimestre_ano['PERIODO'] = vendas_trimestre_ano['ANO'].astype(str) + ' T' + vendas_trimestre_ano['TRIMESTRE'].astype(str)
plt.figure(figsize=(12, 5))
sns.barplot(data=vendas_trimestre_ano, x='PERIODO', y='qtd_itens', color='steelblue')
plt.title('Evolucao trimestral da quantidade de itens vendidos')
plt.xlabel('Periodo')
plt.ylabel('Quantidade de itens')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Vendas por Dia da Semana
plt.figure(figsize=(10, 5))
sns.barplot(data=vendas_por_dia, x='NOME_DIA', y='qtd_itens', color='seagreen')
plt.title('Quantidade de itens vendidos por dia da semana')
plt.xlabel('Dia da semana')
plt.ylabel('Quantidade de itens')
plt.tight_layout()
plt.show()

# Categorias por Classe Social
plt.figure(figsize=(12, 6))
cat_por_classe.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='tab20')
plt.title('Categorias por classe social')
plt.xlabel('CL_EC')
plt.ylabel('Quantidade de itens')
plt.legend(title='PR_CAT', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

"""Os gráficos complementares reforçam a sazonalidade observada: a série mensal oscila ao longo do período, o recorte por dia da semana destaca diferenças claras entre os dias úteis e o fim de semana, e o gráfico empilhado confirma que `ALIMENTOS` domina todas as classes sociais."""

"""# **Conclusões**"""

"""A análise mostra que a base de varejo é rica para entender padrões de consumo por tempo, categoria e perfil de cliente.

Os principais aprendizados foram:

- a base ficou mais limpa e confiável após a remoção de colunas vazias, duplicatas e padronização de tipos;
- `ALIMENTOS` domina o volume de vendas, seguido por `HIGIENE` e `LIMPEZA`;
- a classe social 3 e a classe 4 concentram os maiores volumes de consumo;
- clientes do gênero feminino aparecem ligeiramente à frente no total de itens;
- janeiro e o primeiro trimestre concentram maiores volumes, enquanto novembro e o quarto trimestre mostram menor movimentação;
- 2021 foi o ano mais forte em vendas, e 2022 ficou no extremo oposto.

Como continuidade, seria interessante aprofundar a análise por ticket médio, recorrência de clientes e comparação entre categorias ao longo dos anos."""

