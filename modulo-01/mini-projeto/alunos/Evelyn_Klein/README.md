# Mini Projeto Avaliativo - Modulo 1 - Semana 07

Este repositorio reune a solucao do mini projeto de analise exploratoria de dados desenvolvido a partir da base `Varejo.csv`.

O objetivo do trabalho foi preparar a base, verificar sua qualidade e extrair insights sobre comportamento de compra, perfil dos clientes, sazonalidade e padroes de consumo.

## Visao Geral

O projeto foi organizado para seguir um fluxo de ETL simples e bem documentado:

1. **Extracao**: leitura da base bruta de varejo.
2. **Transformacao**: remocao de colunas vazias, tratamento de duplicatas, correcao de tipos e padronizacao de textos.
3. **Carga**: geracao da base limpa `df_limpo.csv` para uso nas analises.

Alem da limpeza, o notebook tambem inclui uma etapa de **feature engineering**, na qual foram criadas variaveis temporais e um indicador de item para apoiar os agrupamentos e graficos.

## Estrutura do projeto

- `Mini_Projeto.ipynb`: notebook principal com todo o desenvolvimento da analise.
- `mini_projeto_avaliativo_modulo_1_semana_07.py`: versao em script do projeto.
- `df_limpo.csv`: base limpa final, pronta para reuso.
- `dados/Base Varejo.csv`: base bruta utilizada como ponto de partida.

## Etapas analisadas

O notebook cobre as seguintes frentes:

- entendimento inicial da base;
- limpeza e tratamento dos dados;
- checagem de qualidade e inconsistencias;
- criacao de novas variaveis;
- analise exploratoria;
- conclusao final com sintese dos principais achados.

## Principais achados

Alguns resultados se destacam na analise:

- `ALIMENTOS` e a categoria mais vendida com folga;
- `PRESUNTO COZIDO` lidera o ranking dos produtos;
- a compra tipica reune cerca de 40 itens e pouco mais de 5 categorias;
- o consumo se concentra nas classes sociais 1 a 4, com destaque para a classe 3;
- 2021 foi o ano com maior volume de vendas;
- janeiro aparece como o mes de maior movimento e novembro como o menor;
- quarta-feira foi o dia da semana com maior volume de itens vendidos.

## Qualidade dos dados

A base passou por uma limpeza importante antes da analise:

- remocao de colunas vazias;
- eliminacao de duplicatas;
- correcao do tipo da coluna `DATA`;
- padronizacao de identificadores e campos textuais;
- verificacao de inconsistencias pontuais em categorias e nomes de produtos.

O resultado final foi uma base limpa com **733.447 registros** e **10 colunas uteis**.

## Reflexao sobre ETL e qualidade de dados

Este projeto reforca que a qualidade do resultado analitico depende diretamente da qualidade da base. Um processo de ETL bem executado evita distorcoes, melhora a confiabilidade dos indicadores e torna a leitura dos dados muito mais segura.

Mesmo quando a base parece valida a primeira vista, pequenas inconsistencias como colunas vazias, duplicatas ou diferencas de padronizacao podem alterar os agrupamentos e comprometer conclusoes. Por isso, a etapa de limpeza nao deve ser vista como algo secundario, mas como parte essencial da analise.

## Como executar

Para reproduzir a analise:

```bash
pip install pandas numpy matplotlib seaborn
```

Depois, abra o notebook `Mini_Projeto.ipynb` no VSCode ou no Google Colab e execute todas as celulas.

Se preferir rodar a versao em script:

```bash
python mini_projeto_avaliativo_modulo_1_semana_07.py
```

## Observacao final

O notebook foi mantido no formato final de entrega, com a narrativa reorganizada para ficar mais clara, mais logica e mais adequada a apresentacao dos resultados.
