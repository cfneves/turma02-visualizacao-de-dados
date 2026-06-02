# Análise Exploratória de Dados — Base Varejo

Mini-projeto avaliativo do curso de Analista de Dados. Aplicação prática de AED (Análise Exploratória de Dados) sobre uma base real de varejo brasileiro.

*Aluno:* Waldinei Lameira
*Módulo:* 01 — Visualização de Dados

---

## Objetivo

Transformar dados brutos de compras em informações úteis, praticando as etapas fundamentais do trabalho de um analista: importar, entender, limpar, analisar e comunicar dados.

---

## Dataset

| Atributo | Valor |
|---|---|
| Fonte | Kaggle — [Base Varejo](https://www.kaggle.com/datasets/namespaiva/base-varejo) |
| Registros originais | 830.000 linhas × 14 colunas |
| Período | Janeiro/2019 a Dezembro/2022 |
| Domínio | Varejo brasileiro (supermercado) |

### Colunas principais

| Coluna | Tipo | Descrição |
|---|---|---|
| `DATA` | datetime | Data da compra |
| `CO_ID` | int | ID do pedido/compra |
| `CL_ID` | int | ID do cliente |
| `CL_GENERO` | str | Gênero do cliente (M/F) |
| `CL_EC` | int | Estado civil (1–5) |
| `CL_FHL` | int | Número de filhos (0–4) |
| `CL_SEG` | str | Segmento do cliente (A/B/C) |
| `PR_ID` | int | ID do produto |
| `PR_CAT` | str | Categoria do produto |
| `PR_NOME` | str | Nome do produto |

---

## Tecnologias utilizadas

| Biblioteca | Finalidade |
|---|---|
| `pandas` | Manipulação e análise de dados tabulares |
| `kagglehub` | Download automático do dataset do Kaggle |
| `matplotlib` | Criação de gráficos e visualizações |
| `pathlib` | Manipulação de caminhos de arquivo multiplataforma |

---

## Estrutura do Projeto — Sprints

### Sprint 1 — Importação dos Dados
Download automático via `kagglehub` e carregamento do CSV com separador `;`. A base original continha 830.000 registros e 14 colunas.

### Sprint 2 — Transformação de Tipos
- Remoção de 4 colunas `Unnamed` completamente vazias
- Conversão da coluna `DATA` de string para `datetime` (formato `dd/mm/aaaa`)
- Padronização de strings (remoção de espaços extras)
- Conversão de colunas numéricas para o tipo `Int64`

### Sprint 3 — Limpeza de Nulos e Duplicatas
- Diagnóstico: **nenhum valor nulo** encontrado após a transformação
- **96.553 duplicatas removidas** (11,6% do total)
- Base final: **733.447 registros × 10 colunas**

### Sprint 4 — Estatística Descritiva
- Resumo estatístico das colunas numéricas (`média`, `mediana`, `desvio padrão`, `min`, `max`)
- Tabela de frequência das colunas categóricas com percentual do total

### Sprint 5 — Agrupamentos
- Compras agrupadas por **gênero** do cliente
- Compras agrupadas por **categoria de produto**

### Sprint 6 — Insights
Principais conclusões extraídas dos dados:

1. **Qualidade:** base original com 830 mil registros reduzida a 733 mil após limpeza
2. **Gênero:** feminino com 52,1% das compras; leve predominância sobre o masculino (47,9%)
3. **Produto:** `ALIMENTOS` representa 52,4% de todas as transações
4. **Segmento:** segmento `B` concentra 63,9% das compras; segmento `A` (premium) apenas 8,1%
5. **Filhos:** mediana igual a 0 — a maioria dos clientes não possui filhos; média de 1,15

### Sprint 7 — Visualização de Dados
Dashboard com três gráficos gerados via `matplotlib`:

- **Barras horizontais:** compras por categoria de produto (com valores absolutos e percentuais)
- **Pizza:** distribuição de compras por gênero
- **Barras verticais:** compras por segmento de cliente

---

## Resultados em Destaque

| Métrica | Resultado |
|---|---|
| Registros após limpeza | 733.447 |
| Duplicatas removidas | 96.553 (11,6%) |
| Valores nulos | 0 |
| Categoria líder | ALIMENTOS (52,4%) |
| Gênero predominante | Feminino (52,1%) |
| Segmento mais ativo | B (63,9%) |
| Produto mais comprado | PRESUNTO COZIDO (1,73%) |
| Mediana de filhos | 0 |

---

## Como executar

```bash
# 1. Instalar dependências
pip install pandas kagglehub matplotlib

# 2. Abrir o notebook
jupyter notebook mini_projeto.ipynb
```

> É necessário ter uma conta no Kaggle e o arquivo `~/.kaggle/kaggle.json` configurado para o download automático via `kagglehub`.

---

## Arquivos

| Arquivo | Descrição |
|---|---|
| `mini_projeto.ipynb` | Notebook principal com todas as sprints |
| `mini_projeto.py` | Versão em script Python |
| `base_limpa.csv` | Dataset exportado após limpeza |
| `README.md` | Documentação detalhada do projeto |
| `README_WaldineiLameira_VD2.md` | Descrição resumida do projeto |
