
## Resumo

Repositório com coleções de dados e códigos em Python relacionados a filmes do IMDb e dados de bilheteria. Útil como base para análises, exercícios de aula ou projetos de ciência de dados que envolvem scraping, limpeza e análise de datasets cinematográficos.
Estrutura do repositório

/aula/ — Materiais e exemplos usados em aulas (notebooks, slides ou scripts didáticos).
/codigos/ — Scripts e notebooks em Python para processar, limpar e analisar os dados.
/dados/ — Arquivos de dados (CSV/JSON) contendo listas de filmes, informações do IMDb e dados de bilheteria.
README.md — (este arquivo) explicando o propósito e como começar.
Objetivos do projeto

Fornecer um dataset organizado de filmes com metadados do IMDb e bilheteria.
Oferecer exemplos práticos em Python para importação, limpeza, exploração e visualização dos dados.
Servir como material de apoio para cursos, estudos ou projetos pessoais de análise de dados sobre cinema.
Conteúdo principal

Listas de filmes (IDs do IMDb, títulos, ano, gênero, diretor, elenco).
Dados de bilheteria (receita doméstica, internacional, total, orçamentos quando disponíveis).
Scripts de pré-processamento (remoção de duplicatas, tratamento de valores nulos, conversão de tipos).
Notebooks de análise exploratória (gráficos de receita por ano, gênero, distribuidores, correlações entre orçamento e receita).
Exemplos de uso: carregar CSVs, agregar por ano/gênero, gerar gráficos com matplotlib/seaborn/plotly.
Requisitos

Python 3.8+ recomendado
Bibliotecas comuns (exemplos):
pandas
numpy
matplotlib / seaborn / plotly
jupyter / notebook ou jupyterlab
(opcional) requests / BeautifulSoup / IMDbPY — se houver scripts de coleta
Como começar (exemplo)

Clone o repositório: git clone https://github.com/RGBRUNINI/filmes_imdb
Crie e ative um ambiente virtual: python -m venv .venv source .venv/bin/activate (Linux/Mac) ou .venv\Scripts\activate (Windows)
Instale dependências: pip install -r requirements.txt (se não existir requirements.txt, instale manualmente pandas, matplotlib, etc.)
Abra os notebooks em /codigos/ ou /aula/ com Jupyter: jupyter lab
Explore os dados em /dados/ e rode os notebooks/scripts de exemplo.
Boas práticas e notas

Verifique a licença dos dados originais (IMDb e fontes de bilheteria) antes de redistribuir.
Dados de bilheteria podem ter diferentes moedas — normalize para uma única moeda se fizer comparações históricas.
Documente qualquer processo de coleta (data, fonte, método) para garantir reprodutibilidade.
Contribuição

Sugestões de melhoria, correções e pull requests são bem-vindos.
Para contribuições: abra uma issue descrevendo a proposta; implemente em um branch e submeta um pull request.
Licença

Não encontrei arquivo de licença no repositório público. Recomenda-se adicionar um LICENSE (por exemplo MIT) e declarar a origem das fontes de dados se for reutilizá-las.
Contato

Para dúvidas ou mais informações, abra uma issue no repositório ou contate o mantenedor RGBRUNINI via GitHub, Discord ou e-mail.