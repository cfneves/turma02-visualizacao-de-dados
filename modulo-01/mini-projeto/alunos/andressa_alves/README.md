# Mini Projeto - Visualização de Dados

**Autor:** Andressa Alves  
**Turma:** VISUALIZAÇÃO DE DADOS E BI (T2)

## Visão geral do projeto
Este mini projeto explora um conjunto de dados de vendas no varejo (`Base_varejo.csv`) e aplica um processo de ETL simples para transformar os dados em resultados interpretáveis. A análise foi feita principalmente no arquivo `desafio.py`, com suporte exploratório em `desafio.ipynb` e `teste-desafio.ipynb`.

## Estrutura do projeto
A seguir, a estrutura de arquivos do mini projeto:

```
/mini-projeto
├── Base_varejo.csv
└── desafio.py
```

- `Base_varejo.csv`: dataset original com vendas, clientes e produtos.
- `desafio.py`: script principal que realiza a extração, transformação e análise dos dados.

## Processo de ETL aplicado
1. Extração
   - Importação dos dados de `Base_varejo.csv` com `pandas.read_csv`.
2. Transformação
   - Renomeação das colunas para nomes mais legíveis, como `produto_categoria`, `data_compra` e `cliente_genero`.
   - Conversão de tipos de dados: `codigo_id` para numérico e `data_compra` para `datetime`.
   - Substituição de valores faltantes e incorretos: todos os registros com `#N/D` em `produto_categoria` passam a ser `Sem Categoria`.
   - Remoção de colunas inteiras com valores ausentes e eliminação de duplicatas.
3. Carga
   - O DataFrame resultante fica pronto para análise descritiva e agrupamentos.

## Reflexão teórica obrigatória sobre ETL e qualidade de dados
O ETL (Extração, Transformação e Carga) é uma etapa essencial quando trabalhamos com dados reais.

- Extração: consiste em trazer dados brutos do arquivo original. No caso, isso significa carregar o CSV e verificar sua estrutura básica.
- Transformação: é o estágio mais crítico, onde os dados são limpos e preparados. Renomear colunas, ajustar tipos e corrigir valores como `#N/D` evita interpretações erradas e falhas posteriores.
- Carga: mesmo sem salvar em um banco, o DataFrame limpo é a carga lógica pronta para análise e visualização.

Qualidade de dados também deve ser tratada como prioridade. Dados inconsistentes, valores ausentes e duplicatas podem distorcer o entendimento do negócio e gerar conclusões incorretas. Ao substituir `#N/D` por `Sem Categoria`, a análise de categorias passa a ser mais confiável e menos sujeita a ruído.

## Insights obtidos da análise de dados
1. Muitas linhas tinham a categoria de produto faltante ou registrada como `#N/D`, o que indicava um problema de qualidade que afetaria qualquer agregação por categoria.
2. A transformação de `data_compra` para `datetime` permite análises temporais futuras, como tendências de vendas por período.
3. A limpeza de duplicatas garante que os resultados de contagem de compras não sejam inflacionados por registros repetidos.
4. A análise dos dados revelou a importância de categorizar corretamente os produtos antes de agrupar por gênero ou outra variável demográfica.
5. O número de filhos do cliente (`qtd_filhos_clientes`) foi tratado com estatísticas descritivas para entender a distribuição dos perfis de consumidores.
6. Os agrupamentos por `produto_categoria` mostraram quais categorias concentram mais vendas, ajudando a identificar segmentos mais lucrativos.
7. A segmentação por `produto_categoria` e `cliente_genero` permitiu comparar preferências de compra entre clientes masculinos e femininos.
8. A presença de `Sem Categoria` nos agrupamentos destacou a necessidade de melhorar a rotulagem de produtos para análises mais precisas.
9. O uso de `groupby` evidenciou como pequenas falhas de qualidade (como valores `#N/D`) podem distorcer os resultados agregados se não forem corrigidas.

## Considerações finais
Este mini projeto mostra que, mesmo em análises iniciais, o trabalho de ETL e qualidade de dados é determinante. A partir de uma base limpa, é possível gerar relatórios mais precisos e preparar o caminho para visualizações e modelos de dados robustos.
