
# Módulo 01 — Mini-Projeto Avaliativo: Análise Exploratória de Dados (Varejo)

Este repositório contém o desenvolvimento do Mini-Projeto Avaliativo do Módulo 01, focado na condução de uma **Análise Exploratória de Dados (AED)** aplicada ao setor de varejo. O principal objetivo deste projeto é demonstrar a capacidade de transformar dados brutos e desalinhados em inteligência de negócios utilizável para tomadas de decisão estratégicas.

---

## Estrutura do Repositório

* `Projeto_Varejo.py`: Script Python principal contendo toda a pipeline de tratamento, limpeza, análise estatística descritiva e visualização gráfica dos dados.
* `README.md`: Documentação completa do projeto, metodologias e sumário executivo de insights.

---

## Tecnologias e Otimizações Utilizadas

O projeto foi inteiramente desenvolvido em **Python**, utilizando o ecossistema padrão de Data Science para garantir performance e escalabilidade:

* **Pandas:** Responsável por toda a manipulação, agrupamento, pivotagem e engenharia de atributos.
* **NumPy:** Utilizado para suporte em operações matemáticas e tratamento de valores ausentes (`np.nan`).
* **Matplotlib & Seaborn:** Frameworks gráficos aplicados para construir visualizações limpas, auto-intuitivas e sem poluição visual (*data-to-ink ratio* otimizado), aplicando remoção de bordas desnecessárias (`sns.despine()`).

### Engenharia de Performance (Otimização de Memória)
A base bruta possui um volume considerável de registros. Para garantir que o script rode de forma otimizada em qualquer máquina de Help Desk ou ambiente local, foi implementada a **tipagem seletiva de dados** no carregamento do arquivo (`pd.read_csv`):
* Identificadores e chaves primárias/estrangeiras (`CO_ID`, `CL_ID`, `PR_ID`) foram forçados como strings para evitar truncamento numérico.
* Variáveis categóricas de baixa cardinalidade (`CL_GENERO`, `CL_SEG`, `PR_CAT`) foram convertidas para o tipo `category`, reduzindo drasticamente a pegada de memória RAM do DataFrame.

---

## Pipeline de Tratamento e Limpeza de Dados

Antes de extrair métricas de negócio, a confiabilidade da base foi assegurada através de etapas rigorosas de tratamento de dados:

1.  **Tratamento de Falsas Duplicatas (Estratégia de Negócio):** Foi identificada uma grande quantidade de registros idênticos na base. Em vez de simplesmente eliminá-los (o que destruiria o histórico real de vendas), uma análise de ordenação revelou que se tratava do registro sequencial de múltiplos produtos iguais no mesmo caixa. **Solução:** Agrupamos essas ocorrências e criamos a métrica incremental `QTD_PR` (Quantidade de Produtos), preservando o volume real vendido.
2.  **Padronização de Texto:** Correção de inconsistências de digitação e caixas de texto nas colunas `PR_CAT` e `PR_NOME` utilizando capitalização padronizada.
3.  **Dicionário de Regras de Negócio:** Mapeamento da coluna de Estado Civil (`CL_EC`) substituindo códigos numéricos por suas respectivas descrições formais (Ex: Casado/União Estável, Solteiro, Divorciado), alinhando a base às regras corporativas.
4.  **Expurgo de Dados Irrecuperáveis:** Identificação de strings corrompidas do tipo `#N/D`. Como representavam um percentual irrelevante da base e não possuíam correspondência sistêmica para recuperação, foram convertidas em valores nulos legítimos e removidas com segurança para não distorcer as estatísticas.

---

## Estatísticas Descritivas Robustas

Para compreender a dispersão e o comportamento das variáveis quantitativas (como a quantidade de filhos por cliente `CL_FHL`), criamos uma função estatística personalizada capaz de retornar:
* Tendência Central e Dispersão (Média, Mediana, Desvio Padrão, Mínimo e Máximo).
* **Coeficiente de Variação (CV):** Para avaliar a homogeneidade dos dados.
* **Asimetria (Skewness) e Curtose (Kurtosis):** Para entender a fuga da normalidade e a concentração de caudas na distribuição dos perfis de clientes.

---

## Sumário Executivo: Insights de Negócio e Planos de Ação

Após consolidar os agrupamentos analíticos e plotar as visualizações simultâneas do projeto, foram extraídos os seguintes direcionamentos estratégicos:

### 1. Perfil de Consumo por Gênero
* **O Dado:** O agrupamento de volume revelou proporções extremamente equilibradas entre os gêneros masculino e feminino, apresentando uma variação máxima de apenas ~5% dependendo da categoria.
* **Ação Estratégica:** Recomenda-se evitar gastos elevados com orçamentos de marketing voltados a campanhas de segmentação exclusivas por gênero, visto que o ROI (Retorno sobre Investimento) tende a ser baixo. O gênero não se provou a principal alavanca de conversão neste cenário.

### 2. Dominância de Categorias e Estratégia de Cross-Selling
* **O Dado:** O ranking volumétrico apontou que a categoria **Alimentos** possui uma saída massiva, apresentando um volume de vendas quase 3 vezes superior às categorias de *Higiene* e *Limpeza* somadas.
* **Ação Estratégica:** "Alimentos" deve ser tratada tecnicamente como a categoria-isca da empresa. O plano de ação ideal envolve o desenvolvimento de regras de associação no sistema de recomendação ou promoções casadas no PDV físicas (Cross-Selling). Exemplo: *"Na compra de itens da categoria Alimentos, ganhe 15% de desconto em Acessórios ou Limpeza"*. Isso aproveita o tráfego pesado da categoria líder para escoar e rentabilizar os setores de menor giro.

### 3. Segmentação de Clientes Ouro
* **O Dado:** A análise de percentis sobre o volume total de compras por cliente permitiu isolar com precisão o comportamento do grupo "Padrão Ouro" (Top 10 clientes e caudas superiores da distribuição).
* **Ação Estratégica:** Criar réguas de relacionamento e fidelidade exclusivas para essa faixa de clientes de alta recorrência, blindando o faturamento contra a concorrência.

### 4. Análise Temporal e Sazonalidade por Segmento
* **O Dado:** A transformação da coluna de datas em períodos mensais (`Ano_Mes`) e dias da semana, cruzada com a segmentação econômica do cliente (`CL_SEG`), revelou oscilações sazonais claras de volume ao longo dos anos.
* **Ação Estratégica:** Permite ao gestor de estoque e logística antecipar picos de demanda por classe econômica, otimizando a cadeia de suprimentos antes de períodos de alta sazonalidade.

---

## ⚠️ Notas de Atenção para a Gestão Geral

1.  **Tratamento de Dados Omissos:** Cerca de 3.228 registros nulos foram removidos preventivamente nesta etapa por incapacidade de recuperação imediata. Sugere-se que o gestor valide com a equipe de engenharia de dados a possibilidade de cruzamento com tabelas históricas de notas fiscais para tentar resgatar essas chaves em análises futuras.
2.  **Consolidação de Linhas:** A volumetria final de linhas da tabela foi reduzida devido à estratégia de criação da coluna `QTD_PR`. É fundamental ressaltar que nenhuma informação de venda foi perdida, apenas houve uma reestruturação de granularidade de "registro por produto digitado" para "quantidade consolidada por item na nota".





