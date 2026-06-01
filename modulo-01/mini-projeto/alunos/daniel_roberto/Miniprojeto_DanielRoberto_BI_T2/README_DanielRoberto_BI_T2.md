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
* **Sprint 1:** Carregamento do arquivo `Varejo.csv` direto da pasta compartilhada do projeto usando caminhos relativos.
* **Sprint 2 & 3:** Limpeza de strings com expressões regulares (RegEx), conversão da coluna de data para o formato correto (`datetime`) e remoção de mais de 96 mil linhas duplicadas.
* **Sprint 4:** Análise descritiva detalhada sobre a quantidade de filhos dos clientes (Média, Mediana, Moda e Desvio Padrão).
* **Sprint 5:** Criação de tabelas dinâmicas e agrupamentos cruzando segmentos, gêneros e categorias de produtos.

## Tecnologias Utilizadas:
* Python
* Pandas
* NumPy
* OS (Navegação de diretórios)
* Re (Expressões Regulares para higienização avançada de strings)

## 🔄 Versionamento e Reflexão sobre o Pipeline de ETL

O desenvolvimento deste mini-projeto foi estruturado utilizando o versionamento com Git para garantir a rastreabilidade de cada etapa do processo de engenharia e análise de dados:

* **Etapa de Transformação e Higienização (`commit 6dcb29b`):** Nesta fase, o foco total foi a qualidade dos dados (Data Quality). Foi o momento de aplicar Expressões Regulares (RegEx) para limpar caracteres corrompidos nas colunas de texto e número de filhos, além de converter a coluna `DATA` de texto comum para o tipo `datetime` nativo do Pandas. Também eliminamos 96.553 linhas duplicadas que estavam inflando a base e distorceriam as médias estatísticas.
* **Etapa de Sincronização e Integração (`commit f9382c6`):** Demonstra a integração final do projeto local com o repositório centralizado da turma (`turma-visualizacao-de-dados`), garantindo que a entrega ocorresse sem conflitos com as pastas e arquivos dos outros alunos.

Com essa estrutura, garantimos que a base de dados passasse por um processo de ETL (Extração, Transformação e Carga) seguro, gerando tabelas dinâmicas de Business Intelligence limpas e confiáveis para a tomada de decisão.

## 💻 Como Executar o Projeto
Abra o arquivo `miniprojeto_daniel_roberto.ipynb` no seu VS Code ou Jupyter Notebook e execute as células de cima para baixo em sequência para visualizar os outputs gerados.
