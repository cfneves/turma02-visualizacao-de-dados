# Feedback — Christian Wislocki

> **Nota atualizada:** Após verificação no repositório GitHub, foram localizados dois arquivos README na pasta `Project/` que não estavam presentes localmente. A documentação estava completa — o critério foi corrigido de N1 para N2.

## Arquivos Entregues
- Código: `Project/Projeto_Varejo.ipynb`, `Project/Projeto_Varejo.py`
- Documentação: `Project/README.md` + `Project/README_Christian_Wislocki_Turma_Visualizacao_de_Dados.md`
- CSV de saída: Não (`.gitignore` exclui `*.csv`)

## Avaliação por Critério

| Critério | Nível | Pontos | Justificativa |
|---|---|---|---|
| Versionamento | N2 | 1,25 | Projeto entregue no repositório com commits. `.gitignore` presente excluindo `*.csv`. |
| Documentação | N2 | 1,25 | Dois READMEs na pasta `Project/`: `README.md` com objetivo, tecnologias (pandas, numpy, matplotlib, seaborn), tratamento de dados, insights e considerações finais; `README_Christian_Wislocki_Turma_Visualizacao_de_Dados.md` com instruções de execução (`pip install pandas numpy matplotlib seaborn` e `python Projeto_Varejo.py`). Cobertura completa dos requisitos. |
| Manipulação de Arquivos CSV | N2 | 0,75 | `pd.read_csv('Base Varejo.csv', sep=';', dtype={'CO_ID':str,'CL_ID':str,'CL_GENERO':'category',...})` com parâmetros `sep` e `dtype` explícitos. Não gerou CSV de saída. |
| Tratamento de Nulos e Condicionais | N3 | 1,50 | Verificou percentual de nulos por coluna. Identificou `#N/D` em `PR_CAT`, substituiu por `np.nan` com `.replace('#n/d', np.nan)` e aplicou `dropna(subset=['PR_CAT', 'PR_NOME'])`. Tratou duplicatas com lógica de negócio: criou coluna `QTD_PR` via `groupby(...).size()` em vez de deletar. |
| Regras de Negócio e Datas | N3 | 1,50 | `pd.to_datetime(df['DATA'], dayfirst=True)`. Criou colunas derivadas: `Ano_Mes` com `dt.to_period('M')`, `Dia_Semana` com `dt.dayofweek` e `Nome_Dia` mapeado para português. Agrupamentos temporais por mês e por segmento de cliente. |
| Padrões de Agrupamento | N3 | 1,50 | `groupby(['Ano_Mes', 'CL_SEG'])['QTD_PR'].sum()` com múltiplas variáveis; `groupby('CL_ID')['QTD_PR'].sum()` para volume por cliente; drill-down por produto dentro da categoria campeã. |
| Geração de Estatísticas Básicas | N3 | 1,50 | Função `descritivas()` customizada com CV (coeficiente de variação), Skewness e Kurtosis. `describe(include=['object', 'category'])` para categóricas. Gráficos de linha temporal segmentada e barras de distribuição. |

**Total: 9,25 / 10,00**

## Pontos Positivos
- Análise de duplicatas com raciocínio de negócio genuíno — preservou como quantidade (`QTD_PR`) em vez de deletar
- Função `descritivas()` customizada com CV, Skewness e Kurtosis — nível estatístico bem acima do esperado
- Criação de colunas `Ano_Mes` e `Nome_Dia` com mapeamento em português
- Uso de `dtype` no `read_csv` para otimização de memória com colunas `category`
- Dois READMEs complementares cobrindo objetivo, tecnologias, insights e instruções de execução
- Agrupamento temporal por segmento de cliente com múltiplas variáveis

## Pontos a Melhorar
- Não gerou CSV de saída com a base tratada — adicionar `df.to_csv(...)` completaria o pipeline
- Um gráfico apresentou `NameError: name 'compras_filho' is not defined` — célula não executada corretamente

## Mensagem do Professor

Christian, a sua abordagem às duplicatas foi a mais inteligente desta turma — ao invés de deletar, você identificou que cada linha representava um item de um carrinho de compras e criou a coluna `QTD_PR` para preservar essa informação de negócio. Isso demonstra que você pensa como analista, não como programador. A função `descritivas()` com Coeficiente de Variação, Skewness e Kurtosis está em um nível estatístico bem acima do esperado para este módulo.

A documentação estava completa nos dois READMEs — a nota foi atualizada para 9,25. O único ponto restante é a geração do CSV de saída com a base tratada (`df.to_csv(...)`) e a correção da célula com `NameError` referente a `compras_filho`. Com esses dois ajustes o projeto chegaria a 10. Para continuar: explore **pandas Styler** para formatar e colorir suas tabelas de análise; e estude **Plotly** para transformar seus gráficos de linha temporal em visualizações interativas.
