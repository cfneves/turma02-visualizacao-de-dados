ORIENTAÇÕES INICIAIS:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
* O presente estudo foi realizado para obtenção de avaliação do Módulo "Modelagem de Dados", do curso "Visualização de Dados e Business Intelligence", Turma 2, do SCTec
* Abrir o arquivo em notebook Jupyter, no VS Code, e rode todas as células
* Data de elaboração: Navegantes/SC, 31/05/2026
* Versão 01

DECODIFICAÇÃO DAS COLUNAS VÁLIDAS:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
0 - DATA = data da compra
1 - CO_ID = Id compra (nota fiscal)
2 - CL_ID = Id cliente
3 - CL_GENERO = sexo cliente
4 - CL_EC = estado civil (1. casado, união estável/2. divorciado/3. separado/4. solteiro/5. viúvo)
5 - CL_FHL = n. de filhos cliente
6 - CL_SEG = classe econômica cliente (A/B/C)
7 - PR_ID = código do produto adquirido
8 - PR_CAT = categoria do produto adquirido
9 - PR_NOME = nome do produto adquirido

ANALISE PRÉVIA: VERIFICAÇÃO DE PROBLEMAS:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1) Primeiro problema verificado: todas as 14 colunas estavam agrupadas em apenas 1 coluna. o csv não havia separado as colunas por virgula. 
2) Foram verificadas a existência de 4 colunas finais com dados nulos.
3) Verificou-se que a coluna "datas" está na forma de 'string', havendo a necessidade de transforma-la em 'datetime'. As colunas CO_ID, CL_ID, CL_EC e PR_ID estão no formado de n. inteiros. Como se trata apenas de uma codificação das informações, devemos formata-las como 'category', a fim de, posteriormente, tratar os dados como variáveis textuais. As demais colunas estão formatadas corretamente (para as colunas CL_EC e PR_ID,'category' será uma opção melhor que 'string' por se tratar de grupos repetitivos; seguiremos o mesmo padrão para as colunas CO_ID, CL_ID, apesar de se tratarem de dados únicos). 
4) Ao analisar a função 'df.nunique()', podemos verificar: (4.1) foram analisados 333 dias de compras; (4.2) foram realizadas nesse período 18.471 compras por 1.000 clientes diferentes; (4.3) constam na base de dados 229 produtos distribuídos em 7 categorias.
5) Pela função 'df.duplicated()', foram verificados 96.553 valores duplicados. Referida função informa a duplicidade idêntica dos dados (linha inteira idêntica). Portanto, essas linhas deverão ser excluídas.

TRATAMENTO DA BASE DE DADOS:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
inicialmente:
1) Inserção do parâmetro (sep=';') ao transformar a base de dados em dataframe para o pandas fazer a análise corretamente (distribuição das colunas).
2) Alteração dos tipos dos dados para que não haja erros na codificação: transformar a coluna "data" no tipo 'datetime', e as colunas numéricas CO_ID, CL_ID, CL_EC e PR_ID no tipo 'category'. 
3) Exclusão das colunas 10, 11, 12 e 13 pela ausência total de dados para analisar.
4) Foi verificada a existência de valores N/A nas categorias de produtos, representando 0,44% das linhas. Em relação ao consumo, esse percentual representa um valor ínfimo. no entanto, a exclusão desses dados pode impactar em outras abordagens, como n. de compras e perfil de clientes. Assim, optei pelo tratamento dessas informações, substituindo o texto "N/A" por "Dado Ausente" (texto sem acentos ortográficos) para evitar possíveis problemas futuros.
*** após o tratamento, diminuímos o tamanho da base de dados (de 830.000 linhas, para 733.447; e de 88.7MB para 38.6MB)

ANALISANDO OS DADOS OBTIDOS:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
* Pela AED, percebe-se tratar-se de uma base de dados de um mercado
1) Compra equilibrada por gênero (mulheres: 52.14% x homens: 47.86%);
2) A maioria dos clientes são da classe B (63.88%);
3) Os maiores consumidores são clientes que não tem filhos (52.49%);
4) Os clientes adquiriram, em média, 39 produtos por compra;
5) Os alimentos foram a categoria mais consumida (52.38%);
6) O 'presunto' foi disparado o item mais vendido (1.73%), seguido da sardinha (0.90%) e banana (0.89%);
7) As quartas-feiras foram os dias de maior movimento (3.450 transações). Sábados, o de menor movimento (2.140 transações);
8) No total, janeiro é o mês que mais vendeu; novembro é o mês com menor número de transações;
9) Constam dados de 333 dias diferentes no dataframe. No entanto, verificou-se o intervalo entre a data inicial e final da base: 04/01/2019 até 08/12/2022. Pode-se concluir que os dados não tem uma constância. Dentro de um período de 1434 dias, foram escolhidos dados de somente 333 dias. Isso pode significar 2 possibilidades: 1) trata-se de dados aleatórios, em que qualquer conclusão deva ser analisada com cautela, ou 2) existem problemas sérios na obtenção dos dados, que pode ser por falha humana ou do próprio sistema. O mesmo pode ser entendido em relação aos meses de setembro e outubro de 2022. Nesses meses, houve uma queda drástica nas transações (34 e 59 compras durante todo o mês, respectivamente);
10) Aproximadamente, 53% das transações foram realizadas por pessoas que não têm filhos. Esse grupo adquiriu aproximadamente 52% dos produtos vendidos durante o período analisado;
11) Outro fator interessante em relação à existência de filhos: os clientes que têm 1, 2 ou 3 filhos realizaram, aproximadamente, 12% das transações cada grupo. No entanto, clientes com 4 filhos foram responsáveis por somente 9% das transações. No entanto, a média de produtos adquiridos pelos clientes em relação à existência e a quantidade de filhos é bastante equilibrada: aproximadamente 38 produtos. Isso pode significar que os clientes com 4 filhos foram menos vezes ao mercado, mas adquiriram, em média, praticamente a mesma quantidade de produtos que os clientes com menos filhos ou com nenhum filho. Por outro lado, podemos perceber que os clientes sem filhos são a categoria mais consumidora: foram mais vezes ao mercado e adquiriram mais de 50% dos produtos.
12) Um fato curioso: papinha infantil é o 5. produto mais consumido pelos clientes que não têm filhos!

 
