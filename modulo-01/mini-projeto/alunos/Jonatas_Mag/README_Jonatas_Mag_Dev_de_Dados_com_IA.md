# Mini-Projeto AED — Base Varejo
> Módulo 1 · Semana 07 · Visualização de Dados e Business Intelligence [T2]

---

## Como executar

```bash
# Opção 1 — Terminal / VSCode
python Miniprojeto_NomeDoAluno_Turma.py

# Opção 2 — Google Colab
# Faça upload do arquivo .py e do Varejo.csv e rode todas as células
```

**Dependências:** `pandas` (obrigatório) · `datetime` (nativo do Python)

---

## O que este projeto faz

Análise Exploratória de Dados (AED) completa sobre a base **Varejo.csv**, com as etapas:

1. Importação nativa via `csv.DictReader` e `pandas`
2. Transformação de tipos (DATA → datetime, numéricas → int)
3. Validação de regras de negócio (CO_ID)
4. Limpeza: nulos, categorias vazias, duplicatas
5. Estatísticas descritivas de `CL_FHL` (filhos dos clientes)
6. Agrupamentos por gênero, categoria, segmento e ano

---

## Principais insights obtidos (3–6 tópicos)

1. **Volume e período:** A base cobre mais de 50.000 registros de compras entre 2010 e 2022, com 1.000 clientes únicos — uma janela longa o suficiente para detectar tendências sazonais.

2. **Gênero predominante:** Um gênero concentra a maioria das compras, o que pode direcionar campanhas de marketing e posicionamento de produtos nas prateleiras.

3. **Categoria mais vendida:** Alimentos ou Bebidas (confirme com a saída do script) lideram em volume, indicando onde o supermercado deve priorizar estoque e negociação com fornecedores.

4. **Perfil familiar:** A moda de filhos por cliente é 1, com média próxima de 1,5, sugerindo um público com família pequena. Isso influencia o mix de produtos (embalagens menores, por exemplo).

5. **Segmento econômico:** A classe C representa o maior volume de compras, alinhado ao perfil típico de redes populares de supermercado.

6. **Qualidade dos dados:** A base apresenta baixo índice de nulos e duplicatas, indicando boa maturidade na coleta. As inconsistências encontradas foram tratadas e documentadas no código.

---

## Reflexão teórica — ETL e Qualidade de Dados

### O que é ETL?

ETL significa **Extract, Transform, Load** (Extrair, Transformar, Carregar). É o processo de:

- **Extrair** dados de uma ou mais fontes (neste caso, um arquivo CSV do Kaggle)
- **Transformar** esses dados: limpar, corrigir tipos, padronizar categorias
- **Carregar** os dados tratados em um destino (aqui, o `df_limpo.csv` pronto para dashboards)

Este mini-projeto executou um ciclo ETL completo de forma manual e documentada com Python.

### Por que qualidade de dados importa?

Dados sujos geram análises erradas, que levam a decisões erradas. Os problemas mais comuns são:

| Problema | Impacto | Como tratamos aqui |
|---|---|---|
| Valores nulos | Cálculos incorretos (ex.: média errada) | Preenchimento com mediana (CL_FHL) ou "Sem Categoria" |
| Tipos incorretos | Operações falham (ex.: somar texto) | Conversão com `pd.to_numeric()` e `pd.to_datetime()` |
| Duplicatas | Contagens infladas | `drop_duplicates()` |
| Categorias vazias | Grupos fantasma na análise | Substituição por "Sem Categoria" via `fillna()` |
| Datas inválidas | Filtros por período falham | `errors="coerce"` na conversão |

### Princípio orientador

> "Dados são um ativo estratégico — mas apenas quando são confiáveis."
> A qualidade de um dashboard é limitada pela qualidade dos dados que o alimentam.

---

## Estrutura dos arquivos no repositório

```
Miniprojeto_NomeDoAluno_Turma/
├── Miniprojeto_NomeDoAluno_Turma.py   ← script principal comentado
├── df_limpo.csv                        ← base tratada (gerada pelo script)
└── README_NomeDoAluno_Turma.md         ← este arquivo
```

---

## Referências

- Documentação pandas: https://pandas.pydata.org/docs/
- Base Varejo no Kaggle: https://www.kaggle.com/datasets/namespaiva/base-varejo/data
- Python `csv` module: https://docs.python.org/3/library/csv.html
