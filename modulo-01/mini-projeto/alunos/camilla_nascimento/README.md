# Mini Projeto Avaliativo - Análise Exploratória de Dados no Varejo

## Sobre o Projeto

Este projeto foi desenvolvido como atividade avaliativa da disciplina de Visualização de Dados e Business Intelligence.

O objetivo foi realizar uma Análise Exploratória de Dados (AED) em uma base de varejo, aplicando técnicas de importação, limpeza, transformação, análise estatística e agrupamento de dados utilizando Python e a biblioteca Pandas.

A análise permitiu transformar dados brutos em informações relevantes para compreensão do perfil dos clientes e do comportamento das vendas.

---

# Objetivos

- Importar e inspecionar uma base de dados de varejo.
- Identificar problemas de qualidade dos dados.
- Realizar limpeza e transformação dos dados.
- Aplicar estatística descritiva.
- Explorar padrões por meio de agrupamentos.
- Gerar insights para apoio à tomada de decisão.
- Documentar e versionar todo o processo.

---

# Ferramentas Utilizadas

- Python 3
- Pandas
- VS Code
- Git
- GitHub

---

# Base de Dados

A base utilizada contém informações de transações realizadas no varejo, incluindo:

- Data da compra
- Identificador da compra
- Identificador do cliente
- Gênero do cliente
- Estado civil
- Número de filhos
- Segmentação do cliente
- Identificador do produto
- Categoria do produto
- Nome do produto

---

# Desenvolvimento do Projeto

## Sprint 1 – Importação e Diagnóstico Inicial

### Atividades realizadas

- Importação da base utilizando Pandas.
- Verificação da quantidade de registros e colunas.
- Análise dos tipos de dados.
- Identificação de valores nulos.
- Verificação de registros duplicados.
- Identificação de colunas completamente vazias.

### Resultados

- 830.000 registros encontrados.
- 14 colunas identificadas.
- 4 colunas totalmente vazias.
- 96.553 registros duplicados.
- Nenhum valor nulo nas colunas úteis para análise.

---

## Sprint 2 – Transformação dos Dados

### Atividades realizadas

- Criação de cópia da base original.
- Conversão da coluna DATA para o formato datetime.
- Verificação de datas inválidas.
- Padronização dos campos textuais.
- Conferência dos tipos de dados após as transformações.

### Resultados

- Conversão da coluna DATA realizada com sucesso.
- Nenhuma data inválida encontrada.
- Campos de texto padronizados.

---

## Sprint 3 – Limpeza de Nulos e Duplicatas

### Atividades realizadas

- Remoção das colunas completamente vazias.
- Verificação de valores nulos.
- Identificação de registros duplicados.
- Remoção dos registros duplicados.

### Resultados

- 4 colunas vazias removidas.
- Nenhum valor nulo encontrado.
- 96.553 registros duplicados removidos.

### Base após limpeza

- 733.447 registros
- 10 colunas

---

## Sprint 4 – Estatística Descritiva

A análise estatística foi realizada na coluna **CL_FHL (Número de Filhos)**.

### Resultados

| Estatística | Valor |
|------------|--------|
| Média | 1,15 |
| Mediana | 0 |
| Moda | 0 |
| Desvio Padrão | 1,42 |
| Mínimo | 0 |
| Máximo | 4 |
| Quantidade de Registros | 733.447 |

### Frequência do Número de Filhos

| Número de Filhos | Quantidade |
|-----------------|-----------:|
| 0 | 384.986 |
| 1 | 90.845 |
| 2 | 94.168 |
| 3 | 92.407 |
| 4 | 71.041 |

### Interpretação

Os resultados demonstram que a maioria dos clientes não possui filhos, fato confirmado pela mediana e moda iguais a zero. Apesar disso, existe uma parcela significativa de clientes com filhos, elevando a média para aproximadamente 1,15 filho por cliente.

---

## Sprint 5 – Agrupamentos e Insights

### Agrupamento por Gênero

| Gênero | Quantidade |
|---------|-----------:|
| Feminino | 382.427 |
| Masculino | 351.020 |

### Insight

O público feminino representa aproximadamente 52% dos registros da base, apresentando uma leve predominância em relação ao público masculino.

---

### Agrupamento por Categoria de Produto

| Categoria | Quantidade |
|------------|-----------:|
| ALIMENTOS | 384.197 |
| HIGIENE | 137.702 |
| LIMPEZA | 128.632 |
| BEBIDAS | 38.264 |
| PET | 28.553 |
| ACESSORIOS | 12.871 |
| #N/D | 3.228 |

### Insight

A categoria ALIMENTOS apresentou a maior participação na base, seguida pelas categorias HIGIENE e LIMPEZA. Também foram identificados registros classificados como "#N/D", indicando possíveis problemas de categorização dos dados.

---

# Principais Insights Obtidos

1. A maioria dos clientes cadastrados não possui filhos.
2. O público feminino representa a maior parcela dos registros analisados.
3. A categoria ALIMENTOS concentra a maior quantidade de vendas registradas.
4. A base apresentou boa qualidade de dados após o processo de limpeza.
5. Foram removidos 96.553 registros duplicados.
6. Foram identificados registros sem classificação de categoria, representados pelo valor "#N/D".

---

# Arquivos Entregues

- `miniprojeto.ipynb`
- `df_limpo.csv`
- `README.md`

---

# Conclusão

O desenvolvimento deste projeto permitiu aplicar conceitos fundamentais de Análise Exploratória de Dados, incluindo importação, transformação, limpeza, estatística descritiva e agrupamento de informações.

A utilização da biblioteca Pandas possibilitou a identificação de problemas de qualidade dos dados e a extração de informações relevantes sobre o perfil dos clientes e o comportamento das vendas, demonstrando a importância da preparação dos dados para análises mais avançadas e para a construção de dashboards e soluções de Business Intelligence.