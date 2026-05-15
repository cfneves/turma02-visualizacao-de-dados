# Claude Guide para Aulas Práticas

Este arquivo é um guia para gerar aulas práticas de dados e código automaticamente.

## Como montar uma aula prática
1. Comece com um título claro e objetivos:
   - exemplo: `groupby · merge · pivot_table`
   - descreva o que o aluno vai aprender.
2. Crie um bloco de setup com importações e leitura de dados:
   - `import pandas as pd`
   - `import matplotlib.pyplot as plt`
   - `import numpy as np`
   - leia dados com `pd.read_excel()` ou `pd.read_csv()`.
3. Prepare os dados:
   - converta colunas de data com `pd.to_datetime()`.
   - crie colunas auxiliares como `Ano_Admissao`.
4. Desenvolva blocos temáticos:
   - use `groupby()` para agregar dados.
   - use `merge()` para cruzar tabelas.
   - use `pd.pivot_table()` para relatórios cruzados.
5. Para cada gráfico:
   - crie o gráfico com `matplotlib` ou `pandas.plot()`.
   - adicione um bloco markdown explicando:
     - `O que este gráfico mostra?`
     - `Como ler?` (opcional, para iniciantes)
     - `Por que isso importa?`
6. Termine com exercício prático e gabarito resumido.

## Padrões de conteúdo
- Seja objetivo e didático.
- Prefira frases curtas e exemplos concretos.
- Use listas para organizar o aprendizado.
- Adicione comentários no código explicando cada linha relevante.

## Layout de notebook ideal
- Markdown de título e objetivos
- Código de setup
- Markdown de explicação de cada exemplo
- Código do exemplo
- Gráfico ou resultado
- Markdown de interpretação
- Exercício final
- Gabarito rápido

## O que fazer quando o usuário só pede "adicione" ou "faça uma nova aula"
- não peça informação extra a menos que o tema seja ambíguo
- escolha um tópico comum e didático
- crie o notebook seguindo a estrutura acima
- nomeie o arquivo de forma sequencial: `aula03.ipynb`, `aula04.ipynb`, etc.

## Como agir com a base já existente
- use `aula02.ipynb` como referência de estilo
- mantenha a mesma clareza e o mesmo tipo de explicação
- acrescente conteúdo novo em formato de aula prática sem mudar o estilo

## Exemplos de frases de instrução para futuros trabalhos
- "Crie uma nova aula prática sobre análise de vendas com pandas e gráficos."
- "Adicione uma aula prática com `groupby` e `pivot_table` usando esta base."
- "Monte um notebook para iniciantes com explicações detalhadas e gráficos didáticos."
