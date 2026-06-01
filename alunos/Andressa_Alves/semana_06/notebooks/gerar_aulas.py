# -*- coding: utf-8 -*-
"""Gera os notebooks da Semana 06 — Limpeza e Transformação de Dados"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

def src(text):
    lines = text.split('\n')
    result = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            result.append(line + '\n')
        elif line:
            result.append(line)
    return result or ['']

def md(id_, text):
    return {"cell_type": "markdown", "id": id_, "metadata": {}, "source": src(text)}

def code(id_, text):
    return {"cell_type": "code", "execution_count": None, "id": id_,
            "metadata": {}, "outputs": [], "source": src(text)}

def nb(cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"codemirror_mode": {"name": "ipython", "version": 3},
                              "file_extension": ".py", "mimetype": "text/x-python",
                              "name": "python", "version": "3.10.0"}
        },
        "nbformat": 4, "nbformat_minor": 5
    }

def save(nb_dict, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb_dict, f, ensure_ascii=False, indent=1)
    print(f"  OK: {path}")

# ─────────────────────────────────────────────────────────────────────────────
# AULA 01 — TERÇA: Dados Sujos — Missings e Duplicatas
# ─────────────────────────────────────────────────────────────────────────────
aula01_cells = [

md("a1-titulo", """# Aula 01 — Dados Sujos no Mundo Real: Missings e Duplicatas

**Semana 06 · Dia 01 (Terça-feira) · SENAI — Visualização de Dados**

Você já ouviu a expressão *"garbage in, garbage out"*? Em análise de dados ela significa: se você usa dados ruins, o resultado será ruim — não importa o quanto o código seja sofisticado.

Hoje vamos aprender a **identificar e corrigir** os dois problemas mais comuns em bases reais:

1. **Valores ausentes** (NaN, None, NA) — campos vazios onde deveria haver informação
2. **Duplicatas** — registros repetidos por erro de importação ou digitação

A base que usaremos é de **vendas de supermercado** — 250 transações reais. Vamos primeiro explorar os dados originais e depois criar uma versão "suja" para praticar cada técnica de limpeza.

> **Por que praticar com dados sujos artificiais?** Em sala de aula, criamos os problemas propositalmente para entender exatamente o que aconteceu. No mercado de trabalho, os problemas já vêm prontos — e piores."""),

md("a1-b0-doc", """## Bloco 0 — Setup: Importando e Carregando os Dados

Nesta aula usamos três bibliotecas:

- `pandas` — manipulação de dados
- `numpy` — operações numéricas (vamos usá-lo para criar dados sujos)
- `matplotlib` — gráficos

O arquivo `base_vendas_supermercado.xlsx` está na pasta `base/`, que fica **ao lado deste notebook**. O caminho `../base/` significa: *"sobe uma pasta e entra na pasta base"*."""),

code("a1-b0-code", """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Caminho relativo: sobe uma pasta (../) e entra em base/
df = pd.read_excel("../base/base_vendas_supermercado.xlsx")

print(f"Dataset carregado: {df.shape[0]} linhas x {df.shape[1]} colunas")
print(f"Período das vendas: {df['Data'].min().date()} até {df['Data'].max().date()}")
print()
print("Colunas disponíveis:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i:2}. {col}")"""),

md("a1-exp-doc", """## Explorando a Base: Checklist Inicial

Todo analista tem um "checklist" que roda assim que recebe uma base nova. Vamos rodar o nosso:

| Método | Para que serve |
|---|---|
| `head()` | Ver as primeiras linhas — estrutura e exemplos de valores |
| `info()` | Tipo de dado de cada coluna e quantidade de valores não-nulos |
| `describe()` | Estatísticas das colunas numéricas (média, mínimo, máximo...) |

O `info()` é especialmente útil: ele mostra de cara se alguma coluna tem valores nulos (non-null count menor que o total)."""),

code("a1-exp-code", """print("=== Primeiras 5 linhas ===")
print(df.head().to_string())
print()
print("=== Estrutura da base ===")
df.info()
print()
print("=== Estatísticas numéricas ===")
print(df.describe().round(2).to_string())"""),

md("a1-exp-analise", """### O que essas informações nos dizem?

- **250 linhas** — base pequena, mas representativa para aprender
- **Tipos mistos** — colunas de data, texto e números convivem na mesma tabela
- **Valor Líquido** vai de ~R$ 3 a ~R$ 197 — já vemos uma variação grande
- O `info()` mostra **250 non-null** em todas as colunas → a base original está limpa!

> Isso é incomum na vida real. Para praticar as técnicas de limpeza, vamos criar uma versão "suja" no próximo bloco."""),

md("a1-b1-doc", """## Bloco 1 — Valores Ausentes: O Que São e Como Detectar

### Por que surgem valores ausentes?

No mundo real, dados ficam vazios por muitos motivos:
- **Erro de digitação** → operador deixou o campo em branco
- **Sistema não registrou** → integração falhou no momento da venda
- **Dado não se aplica** → campo "Desconto" vazio significa 0%, não informação faltando
- **Coleta incompleta** → cliente não informou e-mail no cadastro

Em pandas, valores ausentes aparecem como **NaN** (*Not a Number*) para números, **None** para objetos, e **NaT** (*Not a Time*) para datas."""),

code("a1-criar-sujo", """# ── Criando uma versão "suja" para prática ─────────────────────────────────
# Em sala de aula inserimos os problemas propositalmente.
# No mercado, eles já chegam prontos (e piores).

np.random.seed(42)           # garante que os resultados sejam iguais sempre
df_sujo = df.copy()          # nunca modifique a base original!

# 1. Inserir NaN em colunas específicas (simula falhas de sistema)
nan_config = {
    'Categoria':          14,   # 14 registros sem categoria
    'Preço Unitário':     12,   # 12 preços não registrados
    'Forma de Pagamento': 10,   # 10 pagamentos sem forma
    'Quantidade':          8,   # 8 quantidades ausentes
}
for coluna, qtd in nan_config.items():
    indices = np.random.choice(df_sujo.index, size=qtd, replace=False)
    df_sujo.loc[indices, coluna] = np.nan

# 2. Inserir duplicatas (simula importação dupla de planilha)
duplicatas = df_sujo.sample(n=12, random_state=7)
df_sujo = pd.concat([df_sujo, duplicatas], ignore_index=True)
df_sujo = df_sujo.sample(frac=1, random_state=3).reset_index(drop=True)

print("=== Comparação: Original vs Sujo ===")
print(f"{'Métrica':<30} {'Original':>10} {'Sujo':>10}")
print("-" * 52)
print(f"{'Linhas':<30} {df.shape[0]:>10} {df_sujo.shape[0]:>10}")
print(f"{'Colunas':<30} {df.shape[1]:>10} {df_sujo.shape[1]:>10}")
print(f"{'Total de NaN':<30} {df.isnull().sum().sum():>10} {df_sujo.isnull().sum().sum():>10}")
print(f"{'Duplicatas':<30} {df.duplicated().sum():>10} {df_sujo.duplicated().sum():>10}")"""),

md("a1-nan-detect-doc", """## Detectando Valores Ausentes

O pandas tem dois métodos equivalentes para verificar valores ausentes:
- `isnull()` → retorna `True` onde há NaN
- `isna()` → exatamente a mesma coisa (é um apelido)

Sozinhos, eles retornam um DataFrame inteiro de True/False, o que é difícil de ler.
A combinação com `.sum()` é o que usamos na prática: conta os True por coluna."""),

code("a1-nan-detect-code", """# isnull() retorna True onde há NaN — soma conta os True por coluna
nan_por_coluna = df_sujo.isnull().sum()
print("=== NaN por coluna ===")
print(nan_por_coluna.to_string())

print()
print(f"Total de células ausentes: {df_sujo.isnull().sum().sum()}")
print(f"Total de linhas com pelo menos 1 NaN: {df_sujo.isnull().any(axis=1).sum()}")"""),

md("a1-nan-pct-doc", """### Percentual de Ausentes

Em vez de contar valores absolutos, é mais informativo calcular **o percentual** de ausentes por coluna. Isso permite comparar colunas independentemente do tamanho da base.

> **Regra prática:** se uma coluna tem mais de **30% de ausentes**, questione se ela deve ser mantida."""),

code("a1-nan-pct-code", """# Percentual de NaN por coluna (só mostra colunas com NaN)
pct_nan = (df_sujo.isnull().sum() / len(df_sujo) * 100).round(1)
pct_nan_filtrado = pct_nan[pct_nan > 0].sort_values(ascending=False)

print("=== Percentual de valores ausentes ===")
for coluna, pct in pct_nan_filtrado.items():
    barras = '█' * int(pct / 2)
    print(f"  {coluna:<25} {pct:5.1f}%  {barras}")"""),

code("a1-nan-grafico", """# Gráfico de barras: % de ausentes por coluna
pct_nan = df_sujo.isnull().mean() * 100
pct_nan = pct_nan[pct_nan > 0].sort_values(ascending=False)

plt.figure(figsize=(8, 4))
plt.bar(pct_nan.index, pct_nan.values, color='salmon', edgecolor='white')
plt.axhline(5, color='orange', linestyle='--', linewidth=1.5, label='Limite 5%')
plt.title('Percentual de Valores Ausentes por Coluna')
plt.xlabel('Coluna')
plt.ylabel('% de NaN')
plt.legend()
plt.tight_layout()
plt.show()"""),

md("a1-nan-grafico-analise", """---
### O que este gráfico mostra?

Cada barra mostra qual **porcentagem das linhas** de cada coluna está vazia. A linha tracejada em 5% é uma referência informal — acima dela, vale investigar o porquê dos ausentes.

### Por que isso importa?

Antes de tratar, entender **por que** os dados estão ausentes é fundamental:
- Se `Forma de Pagamento` está vazia em vendas antigas, pode ser que o sistema de pagamento não registrava esse dado
- Se `Preço Unitário` está vazio em produtos específicos, pode ser erro de importação
- Esse diagnóstico define qual estratégia de tratamento usar"""),

md("a1-b2-doc", """## Bloco 2 — Tratando Valores Ausentes: Quatro Estratégias

Não existe uma única forma certa de tratar ausentes. A escolha depende de:
- **Tipo de dado** (numérico, categórico, data)
- **Motivo do ausente** (erro de sistema, dado opcional, etc.)
- **Impacto na análise** (quanto esse campo importa para o que queremos responder)

As quatro estratégias principais são:

| Estratégia | Quando usar |
|---|---|
| `dropna()` | Quando a linha inteira não tem salvação |
| `fillna(valor)` | Quando sabemos o que colocar (ex: 0, "Desconhecido") |
| `fillna(estatística)` | Quando queremos a média, mediana ou moda |
| `ffill()` / `bfill()` | Para séries temporais ou dados ordenados |"""),

md("a1-dropna-doc", """### Estratégia 1 — `dropna()`: Remover linhas com NaN

`dropna()` remove qualquer linha que tenha pelo menos um NaN.

> **Cuidado:** se usarmos sem parâmetros em nosso `df_sujo`, perderemos ~44 linhas (registros com NaN em qualquer coluna). Às vezes vale a pena ser mais seletivo: remover apenas linhas com NaN em colunas críticas.

**Parâmetros úteis:**
- `subset=['col1', 'col2']` — só remove se NaN estiver nessas colunas
- `how='all'` — só remove se **todas** as colunas estiverem vazias
- `thresh=N` — remove se tiver menos de N valores não-nulos"""),

code("a1-dropna-code", """# Quantas linhas perderíamos com dropna() padrão?
antes = len(df_sujo)
df_sem_nan = df_sujo.dropna()
depois = len(df_sem_nan)
print(f"Antes : {antes} linhas")
print(f"Depois: {depois} linhas")
print(f"Perdemos {antes - depois} linhas ({(antes-depois)/antes*100:.1f}%)")

print()
# Sendo mais seletivo: só remove se Preço Unitário for nulo
df_sem_preco_nulo = df_sujo.dropna(subset=['Preço Unitário'])
print(f"Removendo apenas NaN em 'Preço Unitário': {len(df_sem_preco_nulo)} linhas mantidas")"""),

md("a1-fillna-doc", """### Estratégia 2 — `fillna()`: Substituir NaN por um Valor

`fillna()` substitui os NaN por um valor que você define.

**Para colunas categóricas** (texto), costumamos preencher com:
- `"Desconhecido"` ou `"Não informado"` — mantém transparência de que o dado falta
- A moda (valor mais frequente) — boa quando a maioria dos valores é previsível

**Para colunas numéricas**, costumamos preencher com:
- Média — quando a distribuição é simétrica
- Mediana — quando há outliers puxando a média
- 0 — apenas quando ausente realmente significa zero"""),

code("a1-fillna-cat", """# Trabalharemos sobre uma cópia limpa para não misturar os exemplos
df_tratado = df_sujo.copy()

# ── Colunas categóricas: preencher com moda ou "Não informado" ─────────────
# moda() retorna uma Series; [0] pega o primeiro valor (o mais frequente)
moda_categoria = df_tratado['Categoria'].mode()[0]
moda_pagamento = df_tratado['Forma de Pagamento'].mode()[0]

df_tratado['Categoria']          = df_tratado['Categoria'].fillna(moda_categoria)
df_tratado['Forma de Pagamento'] = df_tratado['Forma de Pagamento'].fillna(moda_pagamento)

print(f"Moda de 'Categoria'         : {moda_categoria}")
print(f"Moda de 'Forma de Pagamento': {moda_pagamento}")
print()
print("NaN restantes nas colunas tratadas:")
print(df_tratado[['Categoria', 'Forma de Pagamento']].isnull().sum().to_string())"""),

code("a1-fillna-num", """# ── Colunas numéricas: preencher com mediana ──────────────────────────────
mediana_preco    = df_tratado['Preço Unitário'].median()
mediana_qtd      = df_tratado['Quantidade'].median()

df_tratado['Preço Unitário'] = df_tratado['Preço Unitário'].fillna(mediana_preco)
df_tratado['Quantidade']     = df_tratado['Quantidade'].fillna(mediana_qtd)

print(f"Mediana 'Preço Unitário': R$ {mediana_preco:.2f}")
print(f"Mediana 'Quantidade'    : {mediana_qtd:.1f}")
print()
print("NaN restantes após tratamento:")
print(df_tratado.isnull().sum().to_string())
print()
print(f"Dataset tratado: {len(df_tratado)} linhas, {df_tratado.isnull().sum().sum()} NaN")"""),

md("a1-ffill-doc", """### Estratégia 3 — `ffill()` e `bfill()`: Propagação

`ffill()` (*forward fill*) copia o valor da linha **anterior** para preencher o NaN.
`bfill()` (*backward fill*) copia o valor da próxima linha.

**Quando usar?** Em dados **ordenados por tempo** — como registros de vendas por data — faz sentido propagar o último valor conhecido. Por exemplo: se a loja não registrou a categoria em 2 vendas consecutivas, assumir a mesma categoria da venda anterior pode ser razoável.

> **Atenção:** não use ffill/bfill sem verificar a ordenação dos dados! Se os dados não estiverem ordenados por tempo, o resultado pode ser sem sentido."""),

code("a1-ffill-code", """# Exemplo: vamos ver o efeito de ffill em uma coluna com NaN
# Primeiro, ordena por Data para que a propagação faça sentido
df_temporal = df_sujo.sort_values('Data').copy()

# Mostra linhas com NaN em 'Categoria' antes e depois
nan_idx = df_temporal[df_temporal['Categoria'].isna()].index[:5]
print("Antes do ffill:")
print(df_temporal.loc[nan_idx, ['Data', 'Loja', 'Categoria']].to_string())

df_temporal['Categoria'] = df_temporal['Categoria'].ffill()

print()
print("Depois do ffill:")
print(df_temporal.loc[nan_idx, ['Data', 'Loja', 'Categoria']].to_string())

print()
print(f"NaN restantes em 'Categoria' após ffill: {df_temporal['Categoria'].isna().sum()}")"""),

md("a1-estrategia-doc", """### Qual estratégia usar? Guia rápido

```
Dado ausente
├── A linha inteira é inútil sem ele?
│   └── SIM → dropna(subset=[...])
├── É um texto/categoria?
│   ├── Há um valor padrão claro?  → fillna("Desconhecido")
│   └── Não há → fillna(moda)
├── É um número?
│   ├── Distribuição simétrica?    → fillna(média)
│   ├── Há outliers?               → fillna(mediana)
│   └── Ausente = zero de verdade? → fillna(0)
└── Dados ordenados por tempo?    → ffill() ou bfill()
```"""),

code("a1-comparacao", """# Comparação visual: NaN antes vs depois do tratamento
nan_antes  = df_sujo.isnull().sum()
nan_depois = df_tratado.isnull().sum()

# Mostra apenas colunas que tinham NaN
cols_com_nan = nan_antes[nan_antes > 0].index.tolist()
fig, ax = plt.subplots(figsize=(8, 4))

x = range(len(cols_com_nan))
largura = 0.35
ax.bar([i - largura/2 for i in x], nan_antes[cols_com_nan], largura,
       label='Antes (com NaN)', color='salmon')
ax.bar([i + largura/2 for i in x], nan_depois[cols_com_nan], largura,
       label='Depois (tratado)', color='steelblue')

ax.set_xticks(list(x))
ax.set_xticklabels(cols_com_nan, rotation=15)
ax.set_title('Valores Ausentes: Antes vs Depois do Tratamento')
ax.set_ylabel('Quantidade de NaN')
ax.legend()
plt.tight_layout()
plt.show()"""),

md("a1-comparacao-analise", """---
### O que este gráfico mostra?

As barras vermelhas mostram quantos NaN cada coluna tinha **antes** do tratamento, e as barras azuis mostram o que restou **depois**. Como tratamos todas as colunas, as barras azuis devem ser zero.

### Por que isso importa?

Ter uma métrica clara de "antes e depois" é essencial para documentar o trabalho de limpeza — especialmente quando você precisar justificar as escolhas para um gestor ou colega."""),

md("a1-b3-doc", """## Bloco 3 — Duplicatas: Detectando e Removendo Registros Repetidos

### O que são duplicatas?

Uma **duplicata** é um registro que aparece mais de uma vez na base. Causas comuns:
- Planilha foi importada duas vezes por engano
- Sistema registrou a mesma transação duas vezes
- Merge de duas bases com registros em comum

Em um sistema de vendas, uma duplicata pode significar que vendemos mais do que realmente vendemos — o que distorce faturamento, estoque e metas.

> `df.duplicated()` retorna uma Series boolean: `True` para linhas que já apareceram antes, `False` para a primeira ocorrência."""),

code("a1-dup-detect", """# duplicated() retorna True para a 2ª ocorrência em diante
duplicatas_mask = df_sujo.duplicated()
print(f"Total de duplicatas: {duplicatas_mask.sum()}")
print()

# Ver as linhas duplicadas
linhas_dup = df_sujo[duplicatas_mask].head(5)
print("Primeiras 5 linhas duplicadas:")
print(linhas_dup[['Data', 'Loja', 'Produto', 'Quantidade', 'Valor Líquido']].to_string())
print()

# Qual loja tem mais duplicatas?
dup_por_loja = df_sujo[duplicatas_mask]['Loja'].value_counts()
print("Duplicatas por loja:")
print(dup_por_loja.to_string())"""),

md("a1-dup-remove-doc", """### Removendo Duplicatas com `drop_duplicates()`

`drop_duplicates()` remove as linhas duplicadas, mantendo a **primeira ocorrência** por padrão.

**Parâmetros úteis:**
- `keep='first'` (padrão) — mantém a primeira ocorrência
- `keep='last'`  — mantém a última ocorrência
- `keep=False`   — remove **todas** as cópias, incluindo a original
- `subset=['col1', 'col2']` — considera duplicata apenas se essas colunas forem iguais"""),

code("a1-dup-remove", """# Remove todas as duplicatas (mantém primeira ocorrência)
df_sem_dup = df_sujo.drop_duplicates()

print(f"Antes : {len(df_sujo)} linhas")
print(f"Depois: {len(df_sem_dup)} linhas")
print(f"Removidas: {len(df_sujo) - len(df_sem_dup)} duplicatas")
print()

# Verificação: ainda há duplicatas?
print(f"Duplicatas restantes: {df_sem_dup.duplicated().sum()}")
print()

# keep=False remove TODAS as cópias (inclusive a original)
df_sem_qualquer_dup = df_sujo.drop_duplicates(keep=False)
print(f"Com keep=False: {len(df_sem_qualquer_dup)} linhas (remove original e cópia)")"""),

code("a1-pipeline-final", """# ── Pipeline completo: tratar NaN E duplicatas ─────────────────────────────
# Este é o fluxo que usaremos na prática real

df_limpo = df_sujo.copy()

# Passo 1: Remover duplicatas
df_limpo = df_limpo.drop_duplicates()
print(f"Após remover duplicatas: {len(df_limpo)} linhas")

# Passo 2: Preencher NaN categóricos com moda
df_limpo['Categoria']          = df_limpo['Categoria'].fillna(df_limpo['Categoria'].mode()[0])
df_limpo['Forma de Pagamento'] = df_limpo['Forma de Pagamento'].fillna(df_limpo['Forma de Pagamento'].mode()[0])

# Passo 3: Preencher NaN numéricos com mediana
df_limpo['Preço Unitário'] = df_limpo['Preço Unitário'].fillna(df_limpo['Preço Unitário'].median())
df_limpo['Quantidade']     = df_limpo['Quantidade'].fillna(df_limpo['Quantidade'].median()).astype(int)

# Verificação final
print(f"NaN restantes: {df_limpo.isnull().sum().sum()}")
print(f"Duplicatas restantes: {df_limpo.duplicated().sum()}")
print()
print(f"{'Base Original':<20} {df.shape[0]} linhas, {df.isnull().sum().sum()} NaN")
print(f"{'Base Suja':<20} {df_sujo.shape[0]} linhas, {df_sujo.isnull().sum().sum()} NaN")
print(f"{'Base Limpa':<20} {df_limpo.shape[0]} linhas, {df_limpo.isnull().sum().sum()} NaN")"""),

md("a1-exercicio", """## Exercício Prático — Aula 01

Use o `df_sujo` criado nesta aula para responder:

1. Qual coluna tem o **maior percentual** de valores ausentes? Calcule e exiba.

2. Preencha os NaN da coluna `'Forma de Pagamento'` com o valor `'Pix'` (simula uma decisão de negócio: qualquer pagamento sem forma registrada foi via Pix). Confirme que não há mais NaN.

3. Para a coluna `'Preço Unitário'`, em vez da mediana, use a **média por Categoria** para preencher os NaN. Ou seja: cada produto deve ter seu NaN preenchido com a média dos outros produtos da mesma categoria. Dica: `groupby + transform('mean')`.

4. Verifique se existem duplicatas apenas considerando as colunas `['Data', 'Loja', 'Produto', 'Quantidade']` (ignora o restante). Quantas encontrou?

5. Crie um gráfico de pizza mostrando a distribuição de **Forma de Pagamento** após a limpeza completa."""),

md("a1-gabarito", """## Gabarito — Pontos Principais

### Exercício 1 — Coluna com maior % de NaN
```python
pct = df_sujo.isnull().mean() * 100
print(pct.sort_values(ascending=False))
# Categoria tem ~5,5% (14/262 linhas)
```

### Exercício 3 — fillna com média por grupo
```python
media_por_cat = df_tratado.groupby('Categoria')['Preço Unitário'].transform('mean')
df_tratado['Preço Unitário'] = df_tratado['Preço Unitário'].fillna(media_por_cat)
```

### Exercício 4 — Duplicatas por subconjunto de colunas
```python
n = df_sujo.duplicated(subset=['Data','Loja','Produto','Quantidade']).sum()
print(f"Duplicatas (subset): {n}")
```

### Exercício 5 — Pizza de Forma de Pagamento
```python
pag = df_limpo['Forma de Pagamento'].value_counts()
plt.pie(pag.values, labels=pag.index, autopct='%1.1f%%')
plt.title('Distribuição de Forma de Pagamento')
plt.show()
```"""),

md("a1-final", """## Observações Finais

Hoje você aprendeu:

- **Dados sujos são a regra**, não a exceção — a maioria das bases do mundo real tem problemas
- `isnull().sum()` → conta NaN por coluna
- `isnull().mean() * 100` → percentual de NaN (melhor para comparar)
- `fillna()` com moda para categorias, mediana para números
- `ffill()` / `bfill()` para dados temporais ordenados
- `duplicated()` detecta, `drop_duplicates()` remove
- **Nunca modifique a base original** — sempre trabalhe em `.copy()`

---
**Na próxima aula (quinta-feira):** vamos aprender a detectar e tratar *outliers* (valores extremos), normalizar dados e aplicar transformações nas colunas."""),

]  # end aula01_cells

# ─────────────────────────────────────────────────────────────────────────────
# AULA 02 — QUINTA: Outliers, Normalização e Transformações
# ─────────────────────────────────────────────────────────────────────────────
aula02_cells = [

md("a2-titulo", """# Aula 02 — Outliers, Normalização e Transformações de Dados

**Semana 06 · Dia 02 (Quinta-feira) · SENAI — Visualização de Dados**

Na aula anterior tratamos missings e duplicatas. Hoje vamos nos aprofundar em outros três pilares da limpeza e preparação de dados:

1. **Outliers** — valores extremos que fogem do padrão e podem distorcer análises
2. **Normalização** — deixar colunas numéricas na mesma escala para comparação justa
3. **Transformações** — criar novas colunas a partir das existentes usando funções, condições e categorias

Continuaremos com a **base de vendas do supermercado**, mas vamos enriquecê-la com dados "sujos" para praticar."""),

md("a2-b0-doc", """## Bloco 0 — Setup

Carregamos a base e criamos a versão suja da aula anterior.
Dessa vez, também vamos inserir **outliers** — valores de vendas absurdamente altos ou baixos que simulam erros de digitação."""),

code("a2-setup", """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("../base/base_vendas_supermercado.xlsx")

# Limpa a base (repete o pipeline da aula 01)
df_limpo = df.copy()

# Inserindo outliers manualmente para prática
np.random.seed(99)
df_outlier = df_limpo.copy()

# Simula erros de digitação: preços absurdos e quantidades inválidas
idx_preco_alto  = np.random.choice(df_outlier.index, 4, replace=False)
idx_preco_baixo = np.random.choice(df_outlier.index, 3, replace=False)
idx_qtd_alta    = np.random.choice(df_outlier.index, 3, replace=False)

df_outlier.loc[idx_preco_alto,  'Valor Líquido'] = [850.0, 1200.0, 980.0, 760.0]   # preços 10x acima
df_outlier.loc[idx_preco_baixo, 'Valor Líquido'] = [0.50, 0.30, 0.10]               # preços impossíveis
df_outlier.loc[idx_qtd_alta,    'Quantidade']    = [50, 80, 120]                     # quantidades impossíveis

print(f"Dataset com outliers: {df_outlier.shape}")
print(f"Valor Líquido: min={df_outlier['Valor Líquido'].min():.2f} | max={df_outlier['Valor Líquido'].max():.2f}")
print(f"Quantidade: min={df_outlier['Quantidade'].min()} | max={df_outlier['Quantidade'].max()}")"""),

md("a2-b1-doc", """## Bloco 1 — Outliers: O Que São e Por Que Importam

### O que é um outlier?

Um **outlier** é um valor que se afasta muito dos outros — pode ser:
- **Erro de digitação** → alguém digitou R$ 850 em vez de R$ 8,50
- **Erro de sistema** → bug que multiplicou o valor por 100
- **Evento real mas excepcional** → venda de final de ano que foi 10x a média

### Por que outliers são um problema?

Eles **distorcem estatísticas**. Se um produto custou R$ 1.200 por erro de digitação:
- A **média** sobe e não representa mais a realidade
- A **correlação** entre variáveis pode ser completamente alterada
- Modelos de machine learning podem ser enganados

### Como detectar?

Existem dois métodos principais:
1. **Boxplot visual** — vê os outliers nos "bigodes" do gráfico
2. **IQR (Interquartile Range)** — método estatístico objetivo"""),

code("a2-boxplot", """# Boxplot: visualização mais intuitiva de outliers
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Valor Líquido
axes[0].boxplot(df_outlier['Valor Líquido'], vert=True)
axes[0].set_title('Boxplot — Valor Líquido (com outliers)')
axes[0].set_ylabel('R$')

# Quantidade
axes[1].boxplot(df_outlier['Quantidade'], vert=True)
axes[1].set_title('Boxplot — Quantidade (com outliers)')
axes[1].set_ylabel('Unidades')

plt.tight_layout()
plt.show()"""),

md("a2-boxplot-analise", """---
### Como ler um Boxplot?

```
         │
    ┌────┴────┐   ← Q3 (75° percentil)
    │         │
    │  ─────  │   ← Mediana (Q2 / 50°)
    │         │
    └────┬────┘   ← Q1 (25° percentil)
         │
    ○ ○ ○        ← Outliers (pontos fora dos bigodes)
```

- A **caixa** contém 50% dos dados (entre Q1 e Q3)
- Os **bigodes** se estendem até 1,5× o IQR (Interquartile Range)
- **Pontos fora dos bigodes** → outliers

### IQR = Q3 - Q1

Quanto maior o IQR, mais "espalhados" estão os dados centrais."""),

md("a2-iqr-doc", """### Método IQR: Detectando Outliers Estatisticamente

O método IQR define limites objetivos para "normal":

```
Limite inferior = Q1 - 1.5 × IQR
Limite superior = Q3 + 1.5 × IQR

Qualquer valor fora desses limites é considerado outlier.
```

Esse é exatamente o critério que o boxplot usa para desenhar os bigodes e marcar os pontos fora."""),

code("a2-iqr-code", """# Calculando outliers com IQR para 'Valor Líquido'
Q1 = df_outlier['Valor Líquido'].quantile(0.25)
Q3 = df_outlier['Valor Líquido'].quantile(0.75)
IQR = Q3 - Q1

limite_inf = Q1 - 1.5 * IQR
limite_sup = Q3 + 1.5 * IQR

print(f"Q1 (25°)        : R$ {Q1:.2f}")
print(f"Q3 (75°)        : R$ {Q3:.2f}")
print(f"IQR (Q3 - Q1)   : R$ {IQR:.2f}")
print(f"Limite inferior : R$ {limite_inf:.2f}")
print(f"Limite superior : R$ {limite_sup:.2f}")
print()

# Quais linhas são outliers?
mask_outlier = (df_outlier['Valor Líquido'] < limite_inf) | (df_outlier['Valor Líquido'] > limite_sup)
print(f"Outliers detectados: {mask_outlier.sum()} linhas")
print()
print("Valores outliers:")
print(df_outlier.loc[mask_outlier, ['Data', 'Produto', 'Quantidade', 'Valor Líquido']].to_string())"""),

md("a2-outlier-tratamento-doc", """### Tratando Outliers: Três Abordagens

1. **Remover** (`dropna` / boolean mask) — quando o erro é certamente um erro
2. **Substituir pela mediana** — quando não quer perder a linha, mas quer um valor razoável
3. **Capping** — substitui por um limite máximo/mínimo (menos agressivo que remover)

> **Regra de ouro:** antes de remover, entenda o porquê do outlier. Um R$ 197 pode ser legítimo (venda grande de carne); um R$ 1.200 quase certamente é erro de digitação para a nossa base."""),

code("a2-outlier-tratamento", """# Abordagem 1: Remover outliers
df_sem_outlier = df_outlier[~mask_outlier].copy()
print(f"Após remover outliers: {len(df_sem_outlier)} linhas (removidas {mask_outlier.sum()})")

# Abordagem 2: Capping — substituir pelo limite
df_capped = df_outlier.copy()
df_capped['Valor Líquido'] = df_capped['Valor Líquido'].clip(lower=limite_inf, upper=limite_sup)
print(f"Após capping: máximo = R$ {df_capped['Valor Líquido'].max():.2f}")

# Comparação das médias
print()
print(f"{'Versão':<30} {'Média Valor Líquido':>20}")
print("-" * 52)
print(f"{'Com outliers':<30} R$ {df_outlier['Valor Líquido'].mean():>16.2f}")
print(f"{'Sem outliers (removido)':<30} R$ {df_sem_outlier['Valor Líquido'].mean():>16.2f}")
print(f"{'Com capping':<30} R$ {df_capped['Valor Líquido'].mean():>16.2f}")
print(f"{'Mediana (referência)':<30} R$ {df_outlier['Valor Líquido'].median():>16.2f}")"""),

md("a2-b2-doc", """## Bloco 2 — Normalização: Deixando os Dados na Mesma Escala

### Por que normalizar?

Imagine comparar **Quantidade** (1–8 unidades) com **Valor Líquido** (R$ 3 a R$ 200).
Se você somar ou comparar diretamente, o Valor vai "dominar" por ter escala maior.

Normalização resolve isso: transforma todas as colunas para **a mesma faixa de valores**.

### Dois métodos principais:

| Método | Fórmula | Resultado | Quando usar |
|---|---|---|---|
| **Min-Max** | `(x - min) / (max - min)` | Valores entre 0 e 1 | Quando sabe os limites do dado |
| **Z-Score** | `(x - média) / desvio_padrão` | Média=0, Desvio=1 | Quando quer neutralizar a escala completamente |"""),

code("a2-minmax", """# Normalizando com Min-Max (sem sklearn — só pandas/numpy)
df_norm = df_sem_outlier.copy()

colunas_numericas = ['Quantidade', 'Preço Unitário', 'Desconto %', 'Valor Líquido']

for col in colunas_numericas:
    min_val = df_norm[col].min()
    max_val = df_norm[col].max()
    df_norm[col + '_norm'] = (df_norm[col] - min_val) / (max_val - min_val)

print("Estatísticas após normalização Min-Max (intervalo 0–1):")
cols_norm = [c + '_norm' for c in colunas_numericas]
print(df_norm[cols_norm].describe().round(3).to_string())"""),

code("a2-zscore", """# Normalizando com Z-Score
df_zscore = df_sem_outlier.copy()

for col in ['Quantidade', 'Preço Unitário', 'Valor Líquido']:
    media = df_zscore[col].mean()
    desvio = df_zscore[col].std()
    df_zscore[col + '_z'] = (df_zscore[col] - media) / desvio

print("Estatísticas após Z-Score (média≈0, desvio≈1):")
cols_z = ['Quantidade_z', 'Preço Unitário_z', 'Valor Líquido_z']
print(df_zscore[cols_z].describe().round(3).to_string())"""),

code("a2-norm-grafico", """# Comparação visual: original vs normalizado
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

for ax, col in zip(axes, ['Valor Líquido', 'Preço Unitário', 'Quantidade']):
    ax.hist(df_sem_outlier[col], bins=15, color='salmon', alpha=0.6, label='Original')
    ax.hist(df_norm[col + '_norm'] * df_sem_outlier[col].max(), bins=15,
            color='steelblue', alpha=0.6, label='Normalizado×max')
    ax.set_title(col)
    ax.legend(fontsize=8)

plt.suptitle('Distribuição: Original vs Normalizado (Min-Max)')
plt.tight_layout()
plt.show()"""),

md("a2-norm-analise", """---
### O que este gráfico mostra?

A forma das distribuições **não muda** com a normalização — apenas a escala do eixo X muda. Isso é esperado: normalizar não "inventa" dados, apenas os reescala.

### Por que isso importa?

- **Comparação de produtos** com preços e quantidades muito diferentes fica justa
- **Algoritmos de machine learning** (que vêm mais à frente na carreira) requerem dados normalizados
- Alguns gráficos (como heatmaps de correlação) ficam mais interpretáveis com dados na mesma escala"""),

md("a2-b3-doc", """## Bloco 3 — Transformações: Criando Novas Colunas

### Por que criar colunas novas?

Raramente os dados chegam exatamente no formato que precisamos para análise. Precisamos:
- Extrair o **mês** de uma coluna de data
- Calcular a **margem de lucro** a partir de custo e receita
- Categorizar clientes em **faixas de gasto**
- Limpar e padronizar textos

Existem três ferramentas principais para isso:

| Ferramenta | Para que serve |
|---|---|
| `.apply(função)` | Aplicar qualquer função a cada linha/coluna |
| `pd.cut()` | Dividir valores numéricos em faixas (bins) |
| `np.where()` / `np.select()` | Transformações condicionais (if/else vetorizados) |"""),

md("a2-apply-doc", """### `apply()`: Aplicando Funções Personalizadas

`apply()` aplica uma função a cada **elemento** (axis padrão=0 para linhas, axis=1 para colunas).

Dois formatos comuns:
1. **Lambda** → função de uma linha, descartável
2. **Função nomeada** → quando a lógica é mais complexa"""),

code("a2-apply-code", """df_transf = df_sem_outlier.copy()

# Exemplo 1: extrair mês e dia da semana da coluna Data
df_transf['Mês']          = df_transf['Data'].dt.month
df_transf['Nome_Mês']     = df_transf['Data'].dt.strftime('%B')
df_transf['Dia_Semana']   = df_transf['Data'].dt.day_name()

# Exemplo 2: padronizar texto com lambda
df_transf['Loja_Upper'] = df_transf['Loja'].apply(lambda x: x.upper())

# Exemplo 3: função personalizada (classificar tamanho da compra)
def tamanho_compra(valor):
    if valor < 20:
        return 'Pequena'
    elif valor < 60:
        return 'Média'
    else:
        return 'Grande'

df_transf['Tamanho_Compra'] = df_transf['Valor Líquido'].apply(tamanho_compra)

print(df_transf[['Data', 'Nome_Mês', 'Dia_Semana', 'Valor Líquido', 'Tamanho_Compra']].head(8).to_string(index=False))"""),

code("a2-apply-grafico", """# Vendas por dia da semana
vendas_dia = df_transf.groupby('Dia_Semana')['Valor Líquido'].sum()

# Ordenar pelos dias da semana corretamente
ordem_dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
vendas_dia = vendas_dia.reindex([d for d in ordem_dias if d in vendas_dia.index])

plt.bar(vendas_dia.index, vendas_dia.values, color='steelblue')
plt.title('Total de Vendas por Dia da Semana')
plt.xlabel('Dia')
plt.ylabel('Valor Total (R$)')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()"""),

md("a2-cut-doc", """### `pd.cut()`: Criando Faixas de Valores

`pd.cut()` divide uma coluna numérica em **intervalos definidos por você**, atribuindo um rótulo a cada faixa.

Muito útil para:
- Faixas de preço (`'Barato'`, `'Médio'`, `'Caro'`)
- Faixas de quantidade
- Segmentação de clientes por valor de compra

```python
pd.cut(serie, bins=[limites], labels=['rótulos'])
```
O número de rótulos deve ser igual ao número de intervalos (= len(bins) - 1)."""),

code("a2-cut-code", """# Faixas de valor líquido da compra
bins_valor  = [0, 20, 60, 120, 300]
labels_valor = ['Ticket Baixo', 'Ticket Médio', 'Ticket Alto', 'Ticket Premium']

df_transf['Faixa_Ticket'] = pd.cut(
    df_transf['Valor Líquido'],
    bins=bins_valor,
    labels=labels_valor,
    right=True    # intervalos fechados à direita: (0,20]
)

print("Distribuição de Faixas de Ticket:")
print(df_transf['Faixa_Ticket'].value_counts().sort_index().to_string())

print()
print("Ticket médio por categoria:")
print(df_transf.groupby('Faixa_Ticket', observed=True)['Valor Líquido'].mean().round(2).to_string())"""),

code("a2-cut-grafico", """faixas = df_transf['Faixa_Ticket'].value_counts().sort_index()
cores  = ['#60a5fa', '#34d399', '#fbbf24', '#f87171']

plt.bar(faixas.index, faixas.values, color=cores, edgecolor='white')
for i, v in enumerate(faixas.values):
    plt.text(i, v + 1, str(v), ha='center', va='bottom', fontweight='bold')

plt.title('Quantidade de Compras por Faixa de Ticket')
plt.xlabel('Faixa de Ticket')
plt.ylabel('Quantidade de Vendas')
plt.tight_layout()
plt.show()"""),

md("a2-cut-analise", """---
### O que este gráfico mostra?

A distribuição das vendas por faixa de valor — quantas compras foram "pequenas" (Ticket Baixo) e quantas foram expressivas (Ticket Premium).

### Por que isso importa?

Segmentar por ticket é uma das análises mais usadas em varejo:
- Concentração em ticket baixo pode indicar clientes do tipo "compra rápida"
- Poucos tickets premium podem ser vendas para empresas (B2B)
- Essa segmentação pode guiar estratégias de promoção e mix de produtos"""),

md("a2-npwhere-doc", """### `np.where()` e `np.select()`: Condições Vetorizadas

`np.where(condição, valor_se_true, valor_se_false)` é o `if/else` do NumPy.
`np.select(lista_condições, lista_escolhas, default)` para múltiplas condições.

São muito mais rápidos que `apply()` com `if/elif/else` — especialmente em bases grandes."""),

code("a2-npwhere-code", """# np.where: coluna binária (tem desconto ou não?)
df_transf['Tem_Desconto'] = np.where(df_transf['Desconto %'] > 0, 'Sim', 'Não')

# np.select: classificar tipo de cliente por comportamento
condicoes = [
    df_transf['Cliente'] == 'Clube Fidelidade',
    df_transf['Cliente'] == 'Empresa',
    df_transf['Cliente'] == 'Delivery',
]
categorias = ['Fiel', 'Corporativo', 'Digital']

df_transf['Perfil_Cliente'] = np.select(condicoes, categorias, default='Avulso')

print("Perfil de Cliente por tipo:")
print(df_transf['Perfil_Cliente'].value_counts().to_string())

print()
print("Vendas com desconto vs sem desconto:")
print(df_transf['Tem_Desconto'].value_counts().to_string())"""),

code("a2-perfil-grafico", """fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Perfil de cliente
perfil = df_transf['Perfil_Cliente'].value_counts()
axes[0].bar(perfil.index, perfil.values, color='steelblue')
axes[0].set_title('Vendas por Perfil de Cliente')
axes[0].set_ylabel('Quantidade')

# Desconto
desc = df_transf['Tem_Desconto'].value_counts()
axes[1].pie(desc.values, labels=desc.index, autopct='%1.1f%%',
            colors=['#34d399', '#f87171'])
axes[1].set_title('Vendas com e sem Desconto')

plt.tight_layout()
plt.show()"""),

md("a2-exercicio", """## Exercício Prático — Aula 02

Use o `df_outlier` e `df_sem_outlier` criados nesta aula:

1. **Outliers em Quantidade**: usando o método IQR, detecte e liste os outliers da coluna `'Quantidade'`. Quantos são?

2. **Z-Score manual**: normalize a coluna `'Preço Unitário'` usando Z-Score. Verifique que a média resultante é ≈ 0 e o desvio padrão ≈ 1.

3. **apply() com lógica**: crie a coluna `'Horário_Venda'` a partir da coluna `'Data'`, classificando:
   - Hora < 12 → `'Manhã'`
   - Hora < 18 → `'Tarde'`
   - Caso contrário → `'Noite'`
   Dica: use `df['Data'].dt.hour`.

4. **pd.cut() com quantis**: use `pd.qcut()` (em vez de `pd.cut()`) para dividir `'Valor Líquido'` em 4 quartis iguais. Qual a diferença entre `cut` e `qcut`?

5. **Gráfico**: plote um gráfico de barras mostrando a **soma do Valor Líquido por Categoria**, com as barras ordenadas do maior para o menor."""),

md("a2-gabarito", """## Gabarito — Pontos Principais

### Exercício 1 — Outliers em Quantidade
```python
Q1 = df_outlier['Quantidade'].quantile(0.25)
Q3 = df_outlier['Quantidade'].quantile(0.75)
IQR = Q3 - Q1
limite_sup = Q3 + 1.5 * IQR
outliers_qtd = df_outlier[df_outlier['Quantidade'] > limite_sup]
print(f"Outliers em Quantidade: {len(outliers_qtd)}")
```

### Exercício 3 — apply() com horário
```python
# Como 'Data' é datetime sem hora, hora sempre será 0
# Para simular: df['Data'].dt.hour
# Mas se todas forem 0, o resultado será 'Manhã' para todas
```

### Exercício 4 — Diferença cut vs qcut
```python
# pd.cut()  → bins com largura IGUAL (divide o intervalo igualmente)
# pd.qcut() → bins com FREQUÊNCIA IGUAL (cada bin tem mesma qtd de registros)
df_sem_outlier['Quartil'] = pd.qcut(df_sem_outlier['Valor Líquido'], q=4,
                                    labels=['Q1','Q2','Q3','Q4'])
print(df_sem_outlier['Quartil'].value_counts().sort_index())
```

### Exercício 5 — Soma por Categoria
```python
vendas_cat = df_sem_outlier.groupby('Categoria')['Valor Líquido'].sum().sort_values(ascending=False)
plt.barh(vendas_cat.index, vendas_cat.values, color='steelblue')
plt.title('Total de Vendas por Categoria')
plt.xlabel('Valor Total (R$)')
plt.tight_layout()
plt.show()
```"""),

md("a2-final", """## Observações Finais

Hoje você aprendeu:

- **Boxplot** → visualização imediata de outliers
- **IQR** → método estatístico objetivo para detectar outliers
- **Capping** → `clip(lower, upper)` substitui sem remover linhas
- **Min-Max** → escala 0 a 1, preserva a distribuição
- **Z-Score** → centraliza em 0, unidade em desvio padrão
- `apply()` → flexível para qualquer função
- `pd.cut()` → bins com largura definida; `pd.qcut()` → bins com frequência igual
- `np.where()` / `np.select()` → if/else vetorizado, muito mais rápido que apply

---
**Na próxima aula (sexta-feira — revisão):** vamos aprender a **juntar bases de dados** com `concat` e `merge`, e construir um **pipeline completo** de limpeza do zero."""),

]  # end aula02_cells

# ─────────────────────────────────────────────────────────────────────────────
# AULA 03 — SEXTA: Junção de Dados + Pipeline Completo (Revisão)
# ─────────────────────────────────────────────────────────────────────────────
aula03_cells = [

md("a3-titulo", """# Aula 03 — Junção de Dados e Pipeline Completo de Limpeza (Revisão)

**Semana 06 · Dia 03 (Sexta-feira) · SENAI — Visualização de Dados**

Sexta é dia de **revisão e consolidação**. Hoje vamos fechar a semana com dois tópicos novos e depois construir juntos um **pipeline completo** de limpeza de dados.

**O que vamos fazer hoje:**

1. **Concatenação** — empilhar DataFrames com `pd.concat()`
2. **Merge/Join** — cruzar tabelas com `pd.merge()` (como SQL JOIN)
3. **Pipeline completo** — aplicar tudo que aprendemos na semana do zero ao clean
4. **Exercício de revisão** da Semana 06"""),

md("a3-b0-doc", """## Bloco 0 — Setup

Carregamos a base e preparamos algumas tabelas auxiliares para os exemplos de merge."""),

code("a3-setup", """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("../base/base_vendas_supermercado.xlsx")

print(f"Base carregada: {df.shape[0]} linhas x {df.shape[1]} colunas")
print()
print("Colunas:", df.columns.tolist())
print()
print("Categorias:", df['Categoria'].unique().tolist())
print("Lojas:", df['Loja'].unique().tolist())"""),

md("a3-b1-doc", """## Bloco 1 — Concatenação: Empilhando DataFrames

### Quando usar `pd.concat()`?

Imagine que você recebeu os dados de **Janeiro** e **Fevereiro** em arquivos separados. Para analisar os dois meses juntos, você precisa **empilhar** os dois DataFrames — um embaixo do outro. Isso é concatenação.

`pd.concat([df1, df2], ignore_index=True)` — a opção `ignore_index=True` reinicia a numeração das linhas."""),

code("a3-concat-criar", """# Dividindo nossa base por mês para simular dois arquivos separados
df['Mes'] = df['Data'].dt.month

df_jan = df[df['Mes'] == 1].drop(columns='Mes').reset_index(drop=True)
df_fev = df[df['Mes'] == 2].drop(columns='Mes').reset_index(drop=True)
df_mar = df[df['Mes'] == 3].drop(columns='Mes').reset_index(drop=True)

print(f"Janeiro : {len(df_jan)} vendas")
print(f"Fevereiro: {len(df_fev)} vendas")
print(f"Março   : {len(df_mar)} vendas")
print(f"Total   : {len(df_jan) + len(df_fev) + len(df_mar)} vendas")"""),

code("a3-concat-code", """# Concatenando os três meses
df_trimestre = pd.concat([df_jan, df_fev, df_mar], ignore_index=True)

print(f"DataFrame concatenado: {df_trimestre.shape}")
print()
print("Primeiras linhas:")
print(df_trimestre.head(3).to_string(index=False))
print()
print("Últimas linhas:")
print(df_trimestre.tail(3).to_string(index=False))
print()
# Verificação: sum dos tamanhos deve bater
print(f"Soma dos originais: {len(df_jan)+len(df_fev)+len(df_mar)} | Concatenado: {len(df_trimestre)}")"""),

code("a3-concat-axis1", """# concat com axis=1 — une colunas lado a lado (menos comum, mas útil)
# Exemplo: juntar tabela de vendas com tabela de metas lado a lado

# Metas representam o total esperado para o período analisado (Jan-Mai 2026)
metas_lojas = pd.DataFrame({
    'Loja':          ['Loja Shopping', 'Loja Centro', 'Loja Norte', 'Loja Bairro Alto'],
    'Meta_Periodo':  [3000, 2500, 3000, 2800]
})

# Resumo de vendas por loja
vendas_loja = df.groupby('Loja')['Valor Líquido'].sum().reset_index()
vendas_loja.columns = ['Loja', 'Total_Vendido']

print("Vendas por loja:")
print(vendas_loja.to_string(index=False))
print()
print("Metas:")
print(metas_lojas.to_string(index=False))"""),

md("a3-b2-doc", """## Bloco 2 — Merge: Cruzando Tabelas

### Quando usar `pd.merge()`?

Imagine que temos:
- **Tabela A**: vendas (Data, Loja, Produto, Valor)
- **Tabela B**: metas por loja (Loja, Meta_Mensal)

Para saber se cada venda atingiu a meta da sua loja, precisamos **cruzar** as duas tabelas pela coluna `Loja`. Isso é exatamente o que `merge()` faz — é o equivalente do `JOIN` do SQL.

### Tipos de merge

```
Tabela A    Tabela B
  Loja A  ←── Loja A   → inner: só os que existem nos dois
  Loja B           →   left: todos de A, NaN onde B não tem
          Loja C   →   right: todos de B, NaN onde A não tem
  Loja B  Loja C   →   outer: todos de A e B, NaN onde não combina
```"""),

code("a3-merge-code", """# ── Criando tabelas auxiliares para o merge ────────────────────────────────

# Metas do período Jan–Mai 2026 para cada loja (valores realistas com a base)
metas = pd.DataFrame({
    'Loja':          ['Loja Shopping', 'Loja Centro', 'Loja Norte', 'Loja Bairro Alto'],
    'Meta_Periodo':  [3000, 2500, 3000, 2800]
})

# Tabela de margem por categoria
margem_cat = pd.DataFrame({
    'Categoria':    ['Açougue', 'Bebidas', 'Frios', 'Higiene',
                     'Hortifruti', 'Laticínios', 'Limpeza', 'Mercearia', 'Padaria'],
    'Margem_Pct':   [0.25, 0.35, 0.30, 0.40, 0.20, 0.28, 0.38, 0.32, 0.45]
})

print("Metas por loja:")
print(metas.to_string(index=False))
print()
print("Margem por categoria:")
print(margem_cat.to_string(index=False))"""),

code("a3-merge-inner", """# ── inner join: só o que existe nos dois lados ────────────────────────────
vendas_por_loja = df.groupby('Loja')['Valor Líquido'].sum().reset_index()
vendas_por_loja.columns = ['Loja', 'Total_Vendido']

resultado_metas = pd.merge(
    vendas_por_loja,
    metas,
    on='Loja',          # coluna em comum
    how='inner'         # só linhas que existem nos dois DataFrames
)

resultado_metas['Atingiu_Meta'] = resultado_metas['Total_Vendido'] >= resultado_metas['Meta_Periodo']
resultado_metas['Diferença']    = (resultado_metas['Total_Vendido'] - resultado_metas['Meta_Periodo']).round(2)

print("Resultado: Vendas vs Metas")
print(resultado_metas.to_string(index=False))"""),

code("a3-merge-grafico", """# Comparação: total vendido vs meta por loja
x = range(len(resultado_metas))
largura = 0.35

plt.bar([i - largura/2 for i in x],
        resultado_metas['Total_Vendido'], largura,
        label='Total Vendido', color='steelblue')
plt.bar([i + largura/2 for i in x],
        resultado_metas['Meta_Periodo'], largura,
        label='Meta', color='salmon')

plt.xticks(list(x), resultado_metas['Loja'], rotation=15)
plt.title('Total Vendido vs Meta por Loja')
plt.ylabel('R$')
plt.legend()
plt.tight_layout()
plt.show()"""),

md("a3-merge-analise", """---
### O que este gráfico mostra?

Para cada loja, duas barras lado a lado: total vendido (azul) e meta (salmão). Quando a barra azul ultrapassa a salmão, a meta foi atingida.

### Por que isso importa?

Em varejo, **comparar realizado vs meta** é um dos relatórios mais solicitados pela gestão. O `merge` permite fazer essa comparação de forma automática — sem precisar cruzar tabelas manualmente no Excel."""),

code("a3-merge-left", """# ── left join: todos de A, NaN onde B não tem match ──────────────────────
# Exemplo: enriquecendo cada venda com a margem da sua categoria

df_enriquecido = pd.merge(
    df,
    margem_cat,
    on='Categoria',
    how='left'        # mantém todas as linhas de df (esquerda)
)

# Calculando lucro estimado
df_enriquecido['Lucro_Estimado'] = (
    df_enriquecido['Valor Líquido'] * df_enriquecido['Margem_Pct']
).round(2)

print(f"Linhas originais: {len(df)} | Após merge: {len(df_enriquecido)}")
print()
print("Primeiras 5 linhas com margem:")
print(df_enriquecido[['Data', 'Categoria', 'Valor Líquido', 'Margem_Pct', 'Lucro_Estimado']].head(5).to_string(index=False))
print()
print(f"Lucro total estimado: R$ {df_enriquecido['Lucro_Estimado'].sum():,.2f}")"""),

code("a3-merge-lucro-grafico", """# Lucro estimado por categoria
lucro_cat = df_enriquecido.groupby('Categoria')['Lucro_Estimado'].sum().sort_values(ascending=False)

plt.barh(lucro_cat.index, lucro_cat.values, color='steelblue')
plt.title('Lucro Estimado por Categoria')
plt.xlabel('R$')
plt.tight_layout()
plt.show()"""),

md("a3-b3-doc", """## Bloco 3 — Pipeline Completo de Limpeza

### O que é um pipeline de dados?

Um **pipeline** é uma sequência de passos bem definidos que transforma dados brutos em dados prontos para análise. Como uma linha de montagem: cada etapa faz uma coisa específica e passa o resultado para a próxima.

### Nosso pipeline da Semana 06:

```
Dados brutos
   ↓
1. Remoção de duplicatas
   ↓
2. Tratamento de missings
   ↓
3. Detecção e remoção de outliers
   ↓
4. Criação de colunas derivadas
   ↓
5. Enriquecimento com dados externos (merge)
   ↓
Dados prontos para análise
```

Agora vamos executar esse pipeline completo em um dataset "sujo" criado do zero."""),

code("a3-pipeline-dados-sujos", """# ── Criando um dataset sujo para o pipeline ────────────────────────────────
np.random.seed(55)
df_raw = df.copy()

# 1. Inserir NaN
for col, n in [('Categoria', 10), ('Preço Unitário', 8), ('Forma de Pagamento', 7)]:
    idx = np.random.choice(df_raw.index, n, replace=False)
    df_raw.loc[idx, col] = np.nan

# 2. Inserir duplicatas
dup = df_raw.sample(8, random_state=11)
df_raw = pd.concat([df_raw, dup], ignore_index=True).sample(frac=1, random_state=22).reset_index(drop=True)

# 3. Inserir outliers
idx_out = np.random.choice(df_raw.index, 5, replace=False)
df_raw.loc[idx_out[:3], 'Valor Líquido'] = [1500.0, 2000.0, 1800.0]
df_raw.loc[idx_out[3:], 'Valor Líquido'] = [0.10, 0.05]

print("=== Dataset Bruto (simulado) ===")
print(f"Linhas      : {len(df_raw)}")
print(f"NaN total   : {df_raw.isnull().sum().sum()}")
print(f"Duplicatas  : {df_raw.duplicated().sum()}")
print()
print("NaN por coluna:")
print(df_raw.isnull().sum()[df_raw.isnull().sum() > 0].to_string())"""),

code("a3-pipeline-exec", """# ── PIPELINE COMPLETO ──────────────────────────────────────────────────────

print("=" * 50)
print("PIPELINE DE LIMPEZA — BASE VENDAS SUPERMERCADO")
print("=" * 50)

df_clean = df_raw.copy()

# ── PASSO 1: Remover duplicatas ────────────────────
antes = len(df_clean)
df_clean = df_clean.drop_duplicates()
print(f"\\nPasso 1 — Duplicatas")
print(f"  Removidas: {antes - len(df_clean)} | Restam: {len(df_clean)} linhas")

# ── PASSO 2: Tratar missings ───────────────────────
nan_antes = df_clean.isnull().sum().sum()
df_clean['Categoria']          = df_clean['Categoria'].fillna(df_clean['Categoria'].mode()[0])
df_clean['Forma de Pagamento'] = df_clean['Forma de Pagamento'].fillna(df_clean['Forma de Pagamento'].mode()[0])
df_clean['Preço Unitário']     = df_clean['Preço Unitário'].fillna(df_clean['Preço Unitário'].median())
nan_depois = df_clean.isnull().sum().sum()
print(f"\\nPasso 2 — Missings")
print(f"  NaN tratados: {nan_antes - nan_depois} | Restam: {nan_depois}")

# ── PASSO 3: Remover outliers (IQR) ───────────────
Q1  = df_clean['Valor Líquido'].quantile(0.25)
Q3  = df_clean['Valor Líquido'].quantile(0.75)
IQR = Q3 - Q1
lim_sup = Q3 + 1.5 * IQR
lim_inf = Q1 - 1.5 * IQR

antes = len(df_clean)
df_clean = df_clean[df_clean['Valor Líquido'].between(lim_inf, lim_sup)]
print(f"\\nPasso 3 — Outliers (Valor Líquido)")
print(f"  Removidos: {antes - len(df_clean)} | Restam: {len(df_clean)} linhas")

# ── PASSO 4: Criar colunas derivadas ──────────────
df_clean['Mês']          = df_clean['Data'].dt.month
df_clean['Dia_Semana']   = df_clean['Data'].dt.day_name()
df_clean['Faixa_Ticket'] = pd.cut(df_clean['Valor Líquido'],
                                   bins=[0, 20, 60, 120, 9999],
                                   labels=['Baixo','Médio','Alto','Premium'])
print(f"\\nPasso 4 — Colunas derivadas criadas: Mês, Dia_Semana, Faixa_Ticket")

# ── PASSO 5: Enriquecer com margem (merge) ─────────
df_clean = pd.merge(df_clean, margem_cat, on='Categoria', how='left')
df_clean['Lucro_Estimado'] = (df_clean['Valor Líquido'] * df_clean['Margem_Pct']).round(2)
print(f"Passo 5 — Merge com tabela de margens concluído")

print(f"\\n{'='*50}")
print(f"RESULTADO FINAL: {len(df_clean)} linhas x {df_clean.shape[1]} colunas")
print(f"NaN restantes: {df_clean.isnull().sum().sum()}")
print(f"Duplicatas restantes: {df_clean.duplicated().sum()}")"""),

code("a3-pipeline-analise", """# ── Análise final do dataset limpo ─────────────────────────────────────────
print("=== Análise do Dataset Limpo ===")
print()

# Top 5 produtos por lucro estimado
top_prod = df_clean.groupby('Produto')['Lucro_Estimado'].sum().sort_values(ascending=False).head(5)
print("Top 5 Produtos por Lucro Estimado:")
for prod, lucro in top_prod.items():
    print(f"  {prod:<30} R$ {lucro:,.2f}")

print()
# Faturamento e lucro por loja
resumo_loja = df_clean.groupby('Loja').agg(
    Vendas=('Valor Líquido', 'sum'),
    Lucro=('Lucro_Estimado', 'sum'),
    Transacoes=('Valor Líquido', 'count')
).round(2)
print("Resumo por Loja:")
print(resumo_loja.to_string())"""),

code("a3-dashboard", """# Dashboard final: 4 gráficos em um
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Dashboard — Vendas Supermercado (Dataset Limpo)', fontsize=14, fontweight='bold')

# 1. Faturamento por Categoria
fat_cat = df_clean.groupby('Categoria')['Valor Líquido'].sum().sort_values()
axes[0, 0].barh(fat_cat.index, fat_cat.values, color='steelblue')
axes[0, 0].set_title('Faturamento por Categoria')
axes[0, 0].set_xlabel('R$')

# 2. Faixas de Ticket
faixas = df_clean['Faixa_Ticket'].value_counts().sort_index()
cores = ['#60a5fa', '#34d399', '#fbbf24', '#f87171']
axes[0, 1].bar(faixas.index, faixas.values, color=cores[:len(faixas)])
axes[0, 1].set_title('Distribuição de Faixas de Ticket')
axes[0, 1].set_ylabel('Quantidade')

# 3. Forma de Pagamento
pag = df_clean['Forma de Pagamento'].value_counts()
axes[1, 0].pie(pag.values, labels=pag.index, autopct='%1.1f%%')
axes[1, 0].set_title('Formas de Pagamento')

# 4. Vendas mensais
vendas_mes = df_clean.groupby('Mês')['Valor Líquido'].sum()
axes[1, 1].plot(vendas_mes.index, vendas_mes.values, marker='o', color='steelblue')
axes[1, 1].set_title('Faturamento Mensal')
axes[1, 1].set_xlabel('Mês')
axes[1, 1].set_ylabel('R$')
axes[1, 1].set_xticks(vendas_mes.index)

plt.tight_layout()
plt.show()"""),

md("a3-dashboard-analise", """---
### O que este dashboard mostra?

Quatro visões complementares dos dados limpos:

1. **Faturamento por Categoria** — quais produtos geram mais receita
2. **Faixas de Ticket** — como se distribui o valor das compras
3. **Formas de Pagamento** — qual o método preferido dos clientes
4. **Faturamento Mensal** — tendência ao longo do tempo

### Por que isso importa?

Este é o ponto de chegada de toda a semana: você partiu de um dado bruto, com problemas de qualidade, e chegou a um dashboard limpo e informativo. Esse é exatamente o fluxo real de trabalho de um analista de dados."""),

md("a3-exercicio", """## Exercício de Revisão — Semana 06

Este exercício integra todos os tópicos da semana. Use a base `base_vendas_supermercado.xlsx`.

### Cenário
Você foi contratado para analisar as vendas do supermercado. O arquivo chegou com problemas e você precisa limpá-lo antes de entregar o relatório ao gerente.

### Passos

1. **Carregue** a base e crie uma versão suja:
   - Insira 10 NaN em `'Categoria'` e 8 NaN em `'Quantidade'`
   - Insira 5 valores absurdos em `'Valor Líquido'` (ex: R$ 5000, R$ 0.01)
   - Duplique 7 linhas aleatórias

2. **Diagnóstico**: exiba um relatório com:
   - % de NaN por coluna
   - Número de duplicatas
   - Limites IQR para `'Valor Líquido'` (inferior e superior)

3. **Limpeza completa**:
   - Remova duplicatas
   - Preencha NaN de `'Categoria'` com a moda
   - Preencha NaN de `'Quantidade'` com a mediana
   - Remova outliers de `'Valor Líquido'` pelo método IQR

4. **Transformações**:
   - Crie a coluna `'Mes_Nome'` com o nome do mês (ex: "January")
   - Crie a coluna `'Perfil_Compra'` com `pd.cut()` em 3 faixas de `'Valor Líquido'`
   - Crie a coluna `'Tem_Desconto'` com `np.where()`

5. **Enriquecimento**:
   - Crie uma tabela de metas mensais por loja (defina valores à sua escolha)
   - Faça um `merge` do resumo mensal de vendas com essa tabela de metas
   - Identifique quais lojas atingiram a meta em cada mês

6. **Relatório final**: plote um gráfico mostrando o total de vendas por loja e mês."""),

md("a3-gabarito", """## Gabarito — Resumo dos Pontos Principais

### Passo 1 — Criando dados sujos
```python
np.random.seed(42)
df_raw = df.copy()
for col, n in [('Categoria', 10), ('Quantidade', 8)]:
    idx = np.random.choice(df_raw.index, n, replace=False)
    df_raw.loc[idx, col] = np.nan
idx_out = np.random.choice(df_raw.index, 5, replace=False)
df_raw.loc[idx_out[:3], 'Valor Líquido'] = [5000, 4500, 3800]
df_raw.loc[idx_out[3:], 'Valor Líquido'] = [0.01, 0.05]
dup = df_raw.sample(7, random_state=1)
df_raw = pd.concat([df_raw, dup], ignore_index=True)
```

### Passo 3 — Pipeline de limpeza
```python
df_clean = df_raw.drop_duplicates()
df_clean['Categoria'] = df_clean['Categoria'].fillna(df_clean['Categoria'].mode()[0])
df_clean['Quantidade'] = df_clean['Quantidade'].fillna(df_clean['Quantidade'].median())
Q1, Q3 = df_clean['Valor Líquido'].quantile([0.25, 0.75])
IQR = Q3 - Q1
df_clean = df_clean[df_clean['Valor Líquido'].between(Q1 - 1.5*IQR, Q3 + 1.5*IQR)]
```

### Passo 4 — Transformações
```python
df_clean['Mes_Nome']      = df_clean['Data'].dt.month_name()
df_clean['Perfil_Compra'] = pd.cut(df_clean['Valor Líquido'],
                                   bins=[0, 25, 80, 9999],
                                   labels=['Pequeno','Médio','Grande'])
df_clean['Tem_Desconto']  = np.where(df_clean['Desconto %'] > 0, 'Sim', 'Não')
```

### Passo 5 — Merge com metas
```python
metas = pd.DataFrame({'Loja': ['Loja Shopping','Loja Centro','Loja Norte','Loja Bairro Alto'],
                      'Meta': [5000, 4500, 3800, 3500]})
vendas_loja = df_clean.groupby('Loja')['Valor Líquido'].sum().reset_index()
vendas_loja.columns = ['Loja', 'Total']
resultado = pd.merge(vendas_loja, metas, on='Loja')
resultado['Atingiu'] = resultado['Total'] >= resultado['Meta']
```"""),

md("a3-final", """## Fechamento da Semana 06

**Parabéns!** Você completou a semana de Limpeza e Transformação de Dados. Aqui está o que você aprendeu:

### Resumo dos tópicos

| Tópico | O que você sabe fazer |
|---|---|
| **Missings** | Detectar com `isnull()`, tratar com `fillna()`, `dropna()`, `ffill()` |
| **Duplicatas** | Identificar com `duplicated()`, remover com `drop_duplicates()` |
| **Outliers** | Visualizar com boxplot, detectar com IQR, tratar com capping ou remoção |
| **Normalização** | Min-Max e Z-Score sem dependências externas |
| **Funções** | `apply()` com lambda e funções personalizadas |
| **Faixas** | `pd.cut()` e `pd.qcut()` para segmentação |
| **Condicionais** | `np.where()` e `np.select()` vetorizados |
| **Concatenação** | `pd.concat()` para empilhar DataFrames |
| **Merge/Join** | `pd.merge()` com inner, left, right, outer |
| **Pipeline** | Construir um fluxo completo do dado bruto ao limpo |

---
**Próxima semana:** Visualizações avançadas com Seaborn e Plotly — gráficos profissionais e interativos."""),

]  # end aula03_cells

# ─────────────────────────────────────────────────────────────────────────────
# Gerando os arquivos .ipynb
# ─────────────────────────────────────────────────────────────────────────────
notebooks = [
    (aula01_cells, os.path.join(BASE, "aula01", "aula_01.ipynb")),
    (aula02_cells, os.path.join(BASE, "aula02", "aula_02.ipynb")),
    (aula03_cells, os.path.join(BASE, "aula03", "aula_03.ipynb")),
]

print("Gerando notebooks da Semana 06...")
for cells, path in notebooks:
    save(nb(cells), path)

print("\nConcluído! 3 notebooks gerados.")
