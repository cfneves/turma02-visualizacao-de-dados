# 🛒 Mini-Projeto: Análise de Dados de Varejo

**Aluno:** Isaac Trenard  
**Turma:** Visualização de Dados e Business Intelligence [T2]  
**Curso:** SCTEC / SESI / SENAI  

---

## 📌 Sobre o Projeto

Este projeto é uma **Análise Exploratória de Dados (AED)** aplicada a uma base de dados real de varejo. O objetivo foi praticar todo o fluxo de trabalho de um analista de dados: importar, limpar, transformar, analisar e extrair insights de uma base de dados.

---

## 📂 Arquivos do Projeto

| Arquivo | Descrição |
|---------|-----------|
| `PROJETO_ETL_Isaac_Trenard.py` | Script principal com toda a análise |
| `df_limpo_base_Varejo.csv` | Base de dados limpa após o tratamento |
| `README_Isaac_Trenard_TURMA_Visualização_de_dados_2.md` | Este arquivo de documentação |

---

## 🚀 Como Executar o Projeto

### VS Code

1. Abra o arquivo `PROJETO_ETL_Isaac_Trenard.py` no VS Code
2. Certifique-se de ter o Python instalado com as bibliotecas: `pandas`, `matplotlib`
3. Execute o script com o botão play ou com o comando:
   ```bash
   python PROJETO_ETL_Isaac_Trenard.py

📊 # O que o Projeto Faz
Etapas realizadas:
Sprint	Etapa	Descrição
1	Importação	Carregou a base de dados e bibliotecas
2	Limpeza	Renomeou colunas, removeu espaços e padronizou nomes
3	Transformação	Converteu a coluna de data para formato datetime
4	Tratamento de nulos	Removeu 4 colunas totalmente vazias e 96 mil linhas duplicadas
5	Estatísticas	Calculou média, mediana, moda, desvio padrão da coluna Num_Filhos
6	Agrupamentos	Analisou compras por gênero e categoria
7	Relatório	Gerou um resumo final com os principais insights

🧠 # Principais Aprendizados (Reflexão Teórica)
Como um aluno iniciante em Python e análise de dados, este projeto me ensinou muito:

1. Importância da limpeza de dados

"Dados sujos geram análises erradas"

Aprendi que antes de qualquer análise, é preciso:

Verificar valores nulos

Remover colunas vazias (como as Unnamed que encontrei)

Eliminar linhas duplicadas

Padronizar nomes de colunas

2. Converter tipos de dados é essencial

A coluna Data estava como texto (str) e não como data (datetime). Sem essa conversão, eu não conseguiria fazer análises temporais no futuro.

3. Estatísticas descritivas contam histórias

Com a coluna Num_Filhos eu descobri que:

A média de filhos é 1,15

A maioria (moda) tem 0 filhos

Metade dos clientes não tem filhos (mediana = 0)

4. Groupby ajuda a encontrar padrões
Agrupar os dados por Genero e Categoria me mostrou que:

Mulheres compram mais que homens

ALIMENTOS é a categoria mais vendida

5. Versionamento é parte do trabalho
Aprender a usar Git e GitHub para enviar o projeto foi tão importante quanto escrever o código.

⚠️ # Problemas Remanescentes

Foi identificada uma categoria chamada #N/D (provavelmente "Não Disponível"), representando por de 3.228 registros. Em um próximo projeto, eu trataria esses dados renomeando a categoria para Outros ou investigaria quais produtos estão sem categoria definida para incorporarlos nas categorias correspondentes.

📁 #Estrutura do Repositório

MiniProjeto_Isaac_Trenard/
├── PROJETO_ETL_Isaac_Trenard.py                             # Script principal
├── df_limpo_base_Varejo.csv                                 # Base de dados limpa
├── README_Isaac_Trenard_TURMA_Visualização_de_dados_2.md    # Documentação
└── Base_Varejo.csv                                          # Base original (não enviada por questões de tamanho)

✅ # Conclusão

Este mini-projeto foi uma experiência completa de como é o dia a dia de um analista de dados. Saí da zona de conforto do Jupyter Notebook e entreguei um script .py funcional, documentado e versionado no GitHub. Me sinto mais preparado para os próximos desafios!

📅 Data da Entrega: 01/Junho/2026
🐙 Repositório: https://github.com/cfneves/turma-visualizacao-de-dados/tree/master/modulo-01/mini-projeto/alunos/MiniProjeto_Isaac_Trenard_TURMA_Visuliza%C3%A7%C3%A3o_de_Dados_2/MiniProjeto_Isaac_Trenard_TURMA_Visualiza%C3%A7%C3%A3o_de_Dados_2

