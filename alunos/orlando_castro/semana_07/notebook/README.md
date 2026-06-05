# Semana 07 — Web Scraping: Introdução com requests e BeautifulSoup

Aula prática de Web Scraping para iniciantes. Pré-requisitos: noções básicas de pandas e matplotlib.

---

## Estrutura de Arquivos

```
semana_07/
└── notebook/
    ├── README.md
    └── aula_semana07.ipynb
```

---

## Conteúdo da Aula | 19h – 22h

**Web Scraping: Introdução com requests e BeautifulSoup**

| Horário | Conteúdo |
|---------|----------|
| 19h – 19h30 | O que é Web Scraping? Usos e cuidados |
| 19h30 – 20h | HTML básico — entendendo a estrutura web |
| 20h – 20h30 | Biblioteca `requests` — buscando páginas |
| 20h30 – 21h30 | `BeautifulSoup` — extraindo dados do HTML |
| 21h30 – 22h | Scraping de múltiplas páginas com loop |

**O que será praticado:**
- O que é scraping, cuidados e boas práticas (robots.txt, `time.sleep`)
- HTML básico — como usar o F12 no navegador
- `requests.get()` + códigos de status HTTP (200, 404, 403...)
- `BeautifulSoup`: `find()`, `find_all()`, atributos de classe
- Site de prática: `books.toscrape.com` — extrai título, preço e avaliação
- Loop para coletar múltiplas páginas com pausa entre requisições
- 3 exercícios práticos com resolução incluída

---

## Site de Prática

> Criado especificamente para aprender scraping — uso 100% liberado.

- **books.toscrape.com** — livraria fictícia com preços e avaliações
- **quotes.toscrape.com** — citações famosas com autores e tags

---

## Bibliotecas Necessárias

```bash
pip install requests beautifulsoup4 pandas matplotlib
```
=======
# Semana 07 — Web Scraping: Introdução com requests e BeautifulSoup

Aula prática de Web Scraping para iniciantes. Pré-requisitos: noções básicas de pandas e matplotlib.

---

## Estrutura de Arquivos

```
semana_07/
└── notebook/
    ├── README.md
    └── aula_semana07.ipynb
```

---

## Conteúdo da Aula | 19h – 22h

**Web Scraping: Introdução com requests e BeautifulSoup**

| Horário | Conteúdo |
|---------|----------|
| 19h – 19h30 | O que é Web Scraping? Usos e cuidados |
| 19h30 – 20h | HTML básico — entendendo a estrutura web |
| 20h – 20h30 | Biblioteca `requests` — buscando páginas |
| 20h30 – 21h30 | `BeautifulSoup` — extraindo dados do HTML |
| 21h30 – 22h | Scraping de múltiplas páginas com loop |

**O que será praticado:**
- O que é scraping, cuidados e boas práticas (robots.txt, `time.sleep`)
- HTML básico — como usar o F12 no navegador
- `requests.get()` + códigos de status HTTP (200, 404, 403...)
- `BeautifulSoup`: `find()`, `find_all()`, atributos de classe
- Site de prática: `books.toscrape.com` — extrai título, preço e avaliação
- Loop para coletar múltiplas páginas com pausa entre requisições
- 3 exercícios práticos com resolução incluída

---

## Site de Prática

> Criado especificamente para aprender scraping — uso 100% liberado.

- **books.toscrape.com** — livraria fictícia com preços e avaliações
- **quotes.toscrape.com** — citações famosas com autores e tags

---

## Bibliotecas Necessárias

```bash
pip install requests beautifulsoup4 pandas matplotlib
```