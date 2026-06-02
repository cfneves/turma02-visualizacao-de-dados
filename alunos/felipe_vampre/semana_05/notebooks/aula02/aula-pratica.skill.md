# Skill: Aula Prática de Dados

Esta skill descreve como gerar aulas práticas em Jupyter Notebook para alunos iniciantes.

## Objetivo
Criar notebooks de aula que incluam:
- contexto e objetivos claros
- configuração do ambiente e importação de bibliotecas
- leitura de dados e preparação básica
- análises passo a passo com `pandas`
- gráficos didáticos com `matplotlib` ou `seaborn`
- explicações textuais acessíveis e pontuais
- exercícios práticos e gabaritos resumidos

## Estrutura recomendada da aula
1. Título e objetivos
2. Bloco de setup
   - importações
   - leitura de dados
   - conversões básicas (datas, tipos)
3. Blocos de análise
   - `groupby`, `merge`, `pivot_table` ou outros tópicos conforme o tema
   - cada bloco deve ter código e explicações
4. Blocos de visualização
   - gráfico após análise
   - explicação em markdown com perguntas: `O que este gráfico mostra?` e `Por que isso importa?`
5. Exercício prático
   - instruções claras para o aluno repetir ou estender a análise
6. Gabarito resumido e observações finais

## Regras de escrita
- Use português simples e direto.
- Explique cada passo com frases curtas.
- Sempre prefira exemplos reais e analogias didáticas.
- Inclua comentários no código para ajudar o aluno a entender.
- Mostre os resultados com `print()` quando fizer sentido.

## Comportamento da skill
Quando o usuário pedir para montar a aula prática:
- identifique o tema ou a base de dados indicada
- escolha uma estrutura de aula consistente
- crie o notebook completo sem precisar de instruções extras
- adicione explicações didáticas abaixo de cada gráfico
- se o usuário disser "quero adicionar", entenda que ele quer um novo exercício/prática e monte o notebook automaticamente

## Exemplos de tópicos de aula
- `groupby`, `merge`, `pivot_table`
- análise salarial por departamento
- admissões por ano
- comparação de metas x resultados
- visualização de tendências e distribuições

## Nomeação de arquivos
- use `aulaXX.ipynb` para novas lições
- se já existir `aula02.ipynb`, crie `aula03.ipynb` ou seguinte disponível
- mantenha o padrão em português simples
