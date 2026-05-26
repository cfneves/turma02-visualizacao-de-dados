
=== EM CONSTRUÇÃO ===

1. CONTEXTUALIZAÇÃO
Você está desenvolvendo uma Análise Exploratória de Dados (AED) aplicada ao varejo para aprender como transformar dados brutos em informações úteis.

A base “Varejo” contém registros reais de compras (datas, clientes, produtos, categorias e valores). Aprender a verificar qualidade, limpar e sumarizar esses dados é uma habilidade prática essencial para quem trabalha com BI e Visualização de Dados.
Neste mini-projeto você vai praticar tarefas comuns no trabalho: identificar problemas nos dados (valores nulos, tipos incorretos, duplicados), tratar esses problemas com ferramentas como pandas e gerar estatísticas  simples e funções de agrupamento, para responder perguntas operacionais (quem compra mais, quais categorias vendem mais, como variam as vendas ao longo do tempo).
O objetivo educacional é que, ao final, você saiba preparar uma base para análises mais avançadas ou para alimentar um dashboard: entender os dados, limpá-los, extrair estatísticas descritivas e comunicar os principais insights de forma objetiva.

2. DESAFIO
Entregar um script em Python que realize uma Análise Exploratória da base Varejo seguindo etapas claras, documentadas e reproduzíveis.

Etapas obrigatórias:
* Carregar a base Varejo.csv com pandas e mostrar: número de registros, colunas e tipos de dados.
* Verificar e reportar ao menos dois problemas básicos: valores nulos por coluna, duplicatas e possíveis inconsistências (ex.: datas inválidas ou categorias vazias).
* Fazer as três etapas de limpeza mínima necessária: remover ou imputar nulos (explique a escolha), eliminar duplicatas relevantes e ajustar tipos de dados (ex.: converter coluna DATA para datetime).
* Gerar estatísticas descritivas básicas para coluna de número de filhos do cliente (média; mediana; desvio padrão; moda; máximo; mínimo; e contagem).
* Explorar padrões de agrupamento com pelo menos dois agrupamentos (por exemplo: gênero com mais vendas, compras), usando groupby() ou pivot_table().
* Produzir um pequeno bloco de conclusões (3–6 tópicos) com os principais insights obtidos e possíveis problemas remanescentes na base.

Requisitos técnicos mínimos:
* O script deve ser executável em VsCode ou Google Colab (arquivo .py).
* Usar pandas; outras bibliotecas são opcionais (NumPy, Matplotlib, Seaborn).

Base de dados (varejo) sugerida no Kaggle: https://www.kaggle.com/datasets/namespaiva/base-varejo/data 

Para que sua avaliação seja concluída com sucesso, você deve entregar:
Código-Fonte (Python): Um arquivo .py ou link do Google Colab contendo a lógica desenvolvida. O código deve estar comentado, explicando o que cada bloco de lógica realiza.
Repositório no GitHub: O projeto deve ser enviado para um repositório público no seu GitHub. Espera-se que:
O repositório tenha um arquivo README.md básico explicando o projeto.
Dica: Você pode tentar criar um histórico de commits demonstrando o progresso do seu trabalho ou enviar o projeto em um único commit.
Arquivo README_NomeDoAluno_Turma.md, com instruções simples (ex.: "Abra no VsCode ou Colab e rode todas as células" ou "python Miniprojeto_…py").
Os arquivos com a solução do mini-projeto deverão ser inseridos no Repositório GitHub da turma em modo público dentro de uma pasta com o próprio nome do aluno (seguindo o padrão Miniprojeto_NomeDoAluno_Turma).
O link do Repositório GitHub deverá ser submetido na tarefa Módulo 1 - Mini-Projeto Avaliativo, presente na semana 07 do AVA até o dia 01/06/2026 às 22h.