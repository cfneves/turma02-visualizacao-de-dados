# Análise Exploratória de Dados (AED) - Base Varejo

## 📊 Descrição do Projeto

Este projeto implementa uma **Análise Exploratória de Dados (AED)** completa aplicada ao dataset "Base Varejo", um conjunto de dados reais de compras em varejo contendo informações sobre clientes, produtos, categorias e transações.

O objetivo educacional é aprender a transformar dados brutos em informações úteis, seguindo um processo estruturado de limpeza, transformação e análise de dados.

## 🎯 Objetivos

- **Verificar qualidade dos dados**: Identificar problemas como valores nulos, tipos incorretos e duplicados
- **Limpar e preparar dados**: Remover ou imputar nulos, eliminar duplicatas e ajustar tipos de dados
- **Gerar estatísticas descritivas**: Extrair métricas fundamentais dos dados
- **Explorar padrões**: Identificar relacionamentos e tendências através de agrupamentos
- **Comunicar insights**: Apresentar conclusões e recomendações de forma objetiva

## 📁 Estrutura do Projeto

```
├── analise_dados_varejo_kaggle.py     # Script principal de análise
├── README_AED_Varejo.md               # Este arquivo
```

## 🔧 Requisitos Técnicos

### Dependências
- **Python 3.7+**
- **pandas**: Manipulação e análise de dados
- **numpy**: Operações numéricas

### Instalação de Dependências
pip3 install pandas numpy
```

## 🚀 Como Executar

### Opção 1: Visual Studio Code (VsCode)

1. Abra o arquivo `analise_dados_varejo_kaggle.py` no VsCode
2. Clique em "Run Python File" (ícone de play no canto superior direito)
3. Ou use o atalho: `Ctrl + F5`
4. Observe a saída no terminal integrado

### Opção 2: Terminal/Command Line

```bash
# Navegue até o diretório do projeto
cd /caminho/para/o/projeto

# Execute o script
python3 analise_dados_varejo_kaggle.py
```

## 📋 Sprints de Desenvolvimento

### Sprint 1: Importação dos Dados
- Carregamento do dataset "Base Varejo" do Kaggle
- Exibição de informações básicas (número de registros, colunas, tipos de dados)
- Visualização das primeiras e últimas linhas

### Sprint 2: Transformação de Dados
- Conversão de tipos de dados (string, integer, float, datetime)
- Limpeza de strings (remoção de espaços, padronização)
- Tratamento de erros na conversão de tipos

### Sprint 3: Limpeza de Nulos e Duplicatas
- Identificação de valores nulos por coluna
- Remoção ou imputação de valores nulos (estratégias específicas por coluna)
- Remoção de duplicatas
- Verificação de inconsistências (datas inválidas, categorias vazias)

### Sprint 4: Estatística Descritiva
- Cálculo de métricas para a coluna "Número de Filhos":
  - Média, mediana, desvio padrão, moda
  - Máximo, mínimo, contagem
  - Quartis e intervalo interquartil
  - Distribuição de frequência

### Sprint 5: Agrupamentos e Padrões
- Análise por gênero do cliente
- Análise por categoria de produto
- Análise por segmento de cliente
- Análise temporal (por mês)
- Análise cruzada (gênero vs categoria)

### Sprint 6: Conclusões e Relatório
- Resumo executivo
- Principais insights
- Problemas remanescentes e recomendações
- Conclusões e próximas etapas

## 📊 Dados de Entrada

### Fonte
Dataset "Base Varejo" disponível em: https://www.kaggle.com/datasets/namespaiva/base-varejo

### Colunas do Dataset
| Coluna | Descrição | Tipo |
|--------|-----------|------|
| DATA | Data da compra | DateTime |
| CO_ID | ID da compra | Integer |
| CL_ID | ID do cliente | Integer |
| CL_GENERO | Gênero do cliente (M/F) | String |
| CL_EC | Estado civil do cliente | Integer |
| CL_FHL | Número de filhos do cliente | Integer |
| CL_SEG | Segmento do cliente | String |
| PR_ID | ID do produto | Integer |
| PR_CAT | Categoria do produto | String |
| PR_NOME | Nome do produto | String |

## 📈 Resultados Esperados

Após a execução do script, você verá no terminal:

1. **Informações básicas**: Número de registros, colunas e tipos de dados
2. **Verificação de qualidade**: Valores nulos, duplicatas e inconsistências
3. **Estatísticas descritivas**: Métricas detalhadas sobre número de filhos
4. **Análises de agrupamento**: Padrões por gênero, categoria, segmento e tempo
5. **Insights principais**: Descobertas importantes sobre o comportamento de compra
6. **Recomendações**: Sugestões para análises futuras

## 📁 Arquivos de Saída

- **Base_Varejo_Limpo.csv**: Dataset limpo e processado, pronto para análises avançadas

## 🔍 Principais Insights

O projeto identifica:
- **Distribuição de clientes**: Análise por gênero, segmento e perfil familiar
- **Padrões de compra**: Categorias mais vendidas, tendências temporais
- **Qualidade dos dados**: Taxa de completude, inconsistências identificadas
- **Oportunidades**: Segmentação refinada, previsão de demanda, análise de sazonalidade

## 💡 Conceitos Aprendidos

- Importação e manipulação de dados com pandas
- Limpeza e transformação de dados
- Tratamento de valores nulos e duplicatas
- Conversão de tipos de dados
- Cálculo de estatísticas descritivas
- Agrupamento e agregação de dados
- Análise exploratória e comunicação de insights

## 🛠️ Troubleshooting
### Erro: "UnicodeDecodeError"
**Solução**: O arquivo usa encoding 'latin-1'. Se necessário, ajuste o parâmetro `encoding` no `pd.read_csv()`


## 👨‍💼 Autor
Jakson Luis Madruga De Moraes

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas. Sinta-se livre para fazer fork, modificar e compartilhar!

**Última atualização**: 02 de junho de 2026

**Status**: ✅ Completo e testado
