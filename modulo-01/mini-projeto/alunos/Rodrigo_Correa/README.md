# Mini Projeto Avaliativo - Analise de Dados de Varejo

**Aluno:** Rodrigo Correa  
**E-mail:** rodrigodll46@gmail.com  
**GitHub:** https://github.com/rodrigodll46

Este projeto apresenta uma analise exploratoria da base `Base Varejo.csv`, com foco em limpeza, tratamento, estatistica descritiva e identificacao de padroes de consumo.

## Objetivo

Organizar a base de dados, verificar sua qualidade e extrair insights sobre perfil dos clientes, categorias de produtos, sazonalidade e comportamento de compra.

## O que foi feito

- importacao e entendimento inicial da base;
- remocao de colunas vazias;
- tratamento de duplicatas;
- correcao dos tipos de dados;
- verificacao de valores ausentes e inconsistencias;
- estatistica descritiva da coluna de numero de filhos;
- analises com `groupby()` e `pivot_table()`;
- conclusoes com os principais insights encontrados.

## Principais insights

- `ALIMENTOS` e a categoria mais vendida;
- `PRESUNTO COZIDO` aparece entre os produtos mais fortes do ranking;
- clientes do genero feminino realizam mais compras;
- o segmento `B` se destaca em volume total de compras;
- clientes sem filhos apresentam o maior volume de compras;
- a classe social 3 concentra forte participacao nas analises;
- os resultados mostram boa base para exploracao analitica, com poucos ajustes restantes na padronizacao.

## Estrutura da entrega

- `Mini Projeto 01.ipynb`: notebook principal;
- `mini_projeto_rodrigo.py`: versao em script do notebook;
- `df_limpo.csv`: base limpa gerada apos o tratamento;
- `dados/Base Varejo.csv`: base bruta;
- `README_RodrigoCorrea _Turma2.md`: instrucoes simples de execucao.

## Como executar

```bash
pip install pandas numpy matplotlib seaborn
```

Depois, abra o notebook no VSCode ou no Google Colab e execute todas as celulas. Se preferir, rode o script `mini_projeto_rodrigo.py`.

## Reflexao final

A etapa de ETL foi essencial para reduzir ruido, eliminar duplicidades e deixar a base pronta para analises confiaveis. A partir disso, foi possivel interpretar o comportamento de compra com mais seguranca e clareza.
