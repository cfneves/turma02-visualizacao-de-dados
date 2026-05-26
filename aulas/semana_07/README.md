# Semana 07 — Python para Iniciantes: Fontes de Dados

Curso de Python para iniciantes com foco em coleta e análise de dados reais.
Pré-requisitos: noções básicas de pandas, matplotlib e numpy.

---

## Estrutura de Arquivos

```
semana-07/
├── dia_01_dados_publicos_kaggle.ipynb    ← Aula 26/05
├── dia_02_web_scraping_introducao.ipynb  ← Aula 28/05
├── dia_03_web_scraping_projeto.ipynb     ← Aula 29/05
├── gerar_slides.py                       ← Script gerador dos slides
├── dados/                                ← CSVs salvos durante as aulas
└── slides/
    ├── dia_01_slides.pptx
    ├── dia_02_slides.pptx
    └── dia_03_slides.pptx
```

---

## Conteúdo por Dia

### Dia 1 — 26/05/2026 | 19h – 22h
**Fontes de Dados Públicos (.gov) e Kaggle**

| Horário | Conteúdo |
|---------|----------|
| 19h – 19h30 | O que são fontes de dados? |
| 19h30 – 20h30 | Dados do governo (.gov) — IBGE, dados.gov.br |
| 20h30 – 21h | Kaggle — cadastro e download de datasets |
| 21h – 22h | Prática: carregar e explorar dados reais |

**O que será praticado:**
- Portais públicos: IBGE, dados.gov.br, INEP, DATASUS
- Dataset real: população dos estados (Censo IBGE 2022) com cálculo de densidade demográfica
- Dataset Kaggle: Titanic com análise de sobrevivência por sexo e classe
- Dataset IDEB por estado com gráfico comparativo por região
- 4 exercícios práticos com resolução incluída

---

### Dia 2 — 28/05/2026 | 19h – 22h
**Web Scraping: Introdução com requests e BeautifulSoup**

| Horário | Conteúdo |
|---------|----------|
| 19h – 19h30 | O que é Web Scraping? Usos e cuidados |
| 19h30 – 20h | HTML básico — entendendo a estrutura web |
| 20h – 20h30 | Biblioteca `requests` — buscando páginas |
| 20h30 – 21h30 | `BeautifulSoup` — extraindo dados do HTML |
| 21h30 – 22h | Scraping de múltiplas páginas com loop |

**O que será praticado:**
- O que é scraping, cuidados e boas práticas (robots.txt, time.sleep)
- HTML básico — como usar o F12 no navegador
- `requests.get()` + códigos de status HTTP (200, 404, 403...)
- `BeautifulSoup`: `find()`, `find_all()`, atributos de classe
- Site de prática: `books.toscrape.com` — extrai título, preço e avaliação
- Loop para coletar múltiplas páginas com pausa entre requisições

---

### Dia 3 — 29/05/2026 | 19h – 22h
**Web Scraping: Tabelas HTML + Prática**

| Horário | Conteúdo |
|---------|----------|
| 19h – 19h30 | Revisão — o que aprendemos até aqui |
| 19h30 – 20h | `pandas.read_html()` — o atalho para tabelas |
| 20h – 20h45 | Scraping da Wikipedia com BeautifulSoup |
| 20h45 – 21h15 | `quotes.toscrape.com` — prática com citações |
| 21h15 – 22h | Visualizando e salvando os dados coletados |

**O que será praticado:**
- `pd.read_html()` — atalho direto para tabelas HTML (sem BeautifulSoup)
- Scraping da Wikipedia: tabelas de países por área e população
- `quotes.toscrape.com` — extração de citações, autores e tags
- Visualizações com matplotlib: top autores, gráficos de barra e pizza
- Salvar dados coletados em CSV

---

## Datasets Utilizados

| Dataset | Fonte | Dia |
|---------|-------|-----|
| População por estado — Censo IBGE 2022 | IBGE (dados reais) | Dia 1 |
| IDEB por estado | INEP/MEC (dados reais) | Dia 1 |
| Titanic | Kaggle / URL direta (GitHub) | Dia 1 |
| Livros — Books to Scrape | books.toscrape.com | Dias 2 e 3 |
| Citações famosas | quotes.toscrape.com | Dias 2 e 3 |
| Países por área/população | Wikipedia | Dia 3 |

---

## Sites de Prática para Scraping

Estes sites foram criados especificamente para aprender scraping — uso 100% liberado:

- **books.toscrape.com** — livraria fictícia com preços e avaliações
- **quotes.toscrape.com** — citações famosas com autores e tags
- **toscrape.com** — hub com vários exercícios de scraping

---

## Portais de Dados Públicos (Brasil)

| Portal | URL | O que tem |
|--------|-----|-----------|
| dados.gov.br | dados.gov.br | Portal central do governo federal |
| IBGE | ibge.gov.br | População, censo, economia |
| INEP | inep.gov.br | Educação, ENEM, IDEB |
| DATASUS | datasus.saude.gov.br | Saúde pública |
| ANS | ans.gov.br | Saúde suplementar |

---

## Slides

Os slides têm fundo branco e foram gerados com `python-pptx`. Cada apresentação contém:

- Slide de título (data e horário)
- Slide de agenda com horários coloridos
- Slides de conteúdo explicativo
- Slides de código com fundo escuro (estilo VS Code)
- Slide de exercícios práticos
- Slide de resumo com o que foi aprendido e próximos passos

**Estrutura por dia:**
- Dia 1: 16 slides — API IBGE, Banco Central, Censo, dados.gov.br, Kaggle, IDEB
- Dia 2: 15 slides — requests, HTML, BeautifulSoup, extração passo a passo, múltiplas páginas
- Dia 3: 13 slides — read_html, Wikipedia, quotes.toscrape.com, visualizações

Para regenerar os slides:

```bash
python gerar_slides.py
```

---

## Bibliotecas Necessárias

```bash
pip install pandas matplotlib requests beautifulsoup4 python-pptx
```

---

## Próximos Passos (após o curso)

- **Selenium** — scraping de páginas dinâmicas (JavaScript)
- **APIs REST** — outra forma de coletar dados estruturados
- **SQL** — trabalhar com bancos de dados relacionais
- **Kaggle** — praticar com competições para iniciantes
