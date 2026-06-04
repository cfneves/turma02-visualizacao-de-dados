# Mini-Projeto 01: Análise Exploratória de Dados (Varejo)

* **Curso:** Visualização de Dados e Business Intelligence [T2]
* **Aluno:** Daniel Roberto
* **Ambiente de Desenvolvimento:** VS Code / Jupyter Notebook (`.ipynb`)
* **Data de Entrega:** 01/06/2026

---

### 📝 Contextualização do Projeto
Este relatório apresenta a Análise Exploratória de Dados (AED) realizada sobre a base central de varejo da turma. O objetivo é higienizar os dados brutos, converter os tipos de variáveis e extrair os primeiros agrupamentos e métricas estatísticas para suportar futuras tomadas de decisão em Business Intelligence.
Este repositório contém o meu mini-projeto de Análise Exploratória desenvolvido no módulo de Visualização de Dados e BI.

## O que foi feito:
* **Sprint 1:** Carregamento do arquivo `Base_Varejo.csv` utilizando caminhos locais diretos e diagnóstico estrutural das colunas.
* **Sprint 2 & 3:** Limpeza de strings com expressões regulares (RegEx), conversão da coluna de data para o formato correto (`datetime`), engenharia de recursos (criação das colunas de `MES` e `ANO`) e remoção de mais de 96 mil linhas duplicadas.
* **Sprint 3 (Visualização):** Criação de análises visuais utilizando a biblioteca `Matplotlib`, incluindo um gráfico de barras empilhadas (Segmento x Gênero) e um gráfico de linha temporal para monitorar o volume de transações mensal.
* **Sprint 4:** Análise descritiva detalhada sobre a quantidade de filhos dos clientes (Média, Mediana, Moda e Desvio Padrão).
* **Sprint 5:** Criação de tabelas dinâmica (Pivot Tables) e visões multidimensionais de BI cruzando segmentos, gêneros e categorias de produtos. Geração e exportação de um novo arquivo consolidado e limpo (`Base_Varejo_Tratada.csv`) para uso em ferramentas de BI (como Power BI).

## Tecnologias Utilizadas:
* Python
* Pandas (Manipulação de DataFrames)
* NumPy (Suporte matemático e tratamento de nulos estruturados)
* OS (Mapeamento de diretórios locais)
* Re (Expressões Regulares para higienização avançada de strings)
* Matplotlib (Construção de gráficos estatísticos e temporais)

## 🔄 Versionamento e Reflexão sobre o Pipeline de ETL

O desenvolvimento deste mini-projeto foi estruturado utilizando o versionamento com Git para garantir a rastreabilidade de cada etapa do processo de engenharia e análise de dados:

* **Etapa de Ajustes e Visualização (`commit 6f76640`):** Implementação das melhorias solicitadas no feedback do professor. Criação de rotinas visuais de análise temporal e volumétrica, além da esteira de carga (Load) gerando o arquivo final limpo em formato CSV.
* **Etapa de Transformação e Higienização (`commit 6dcb29b`):** Nesta fase, o foco total foi a qualidade dos dados (Data Quality). Foi o momento de aplicar Expressões Regulares (RegEx) para limpar caracteres corrompidos nas colunas de texto e número de filhos, além de converter a coluna `DATA` de texto comum para o tipo `datetime` nativo do Pandas. Também eliminamos 96.553 linhas duplicadas que estavam inflando a base e distorceriam as médias estatísticas.
* **Etapa de Sincronização e Integração (`commit f9382c6`):** Demonstra a integração final do projeto local com o repositório centralizado da turma (`turma-visualizacao-de-dados`), garantindo que a entrega ocorresse sem conflitos com as pastas e arquivos dos outros alunos.

Com essa estrutura, garantimos que a base de dados passasse por um processo de ETL (Extração, Transformação e Carga) seguro, gerando tabelas dinâmicas de Business Intelligence limpas e confiáveis para a tomada de decisão.

## 💻 Como Executar o Projeto
1. Certifique-se de que o arquivo `Base_Varejo.csv` está na mesma pasta do notebook.
2. Abra o arquivo `Miniprojeto_DanielRoberto_BI_T2.ipynb` no seu VS Code.
3. Execute as células de cima para baixo em sequência.
4. Após a execução da última célula, o arquivo `Base_Varejo_Tratada.csv` será gerado automaticamente na mesma pasta.
