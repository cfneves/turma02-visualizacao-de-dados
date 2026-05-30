# Mini projeto - Análise exploratoria de dados da Base Varejo.

# Descrição:
    Este projeto foi desenvolvido como parte de um exercicio para aplicação das habilidades adquiridas no  curso Visualização de Dados e Business Intelligence modulo: Modelagem de dados do Senai (SETEC) e tem como finalidade de aplicar conceitos de limpeza de dados, tratamento com python e visualização de dados com panda e matplotlib.

# A base de dados contem:
    • DATA: Data da compra.
    • CO_ID: Identificação do número de compra (número da nota fiscal).
    • CL_ID: Identificação do cliente (número do cliente).
    • CL_GENERO: Sexo biológico informado pelo cliente.
    • CL_EC: Estado civil do cliente (1 Casado ou união estával, 2 Divorciado, 3 Separado, 4 Solteiro, 5 Viúvo).
    • CL_FHL: Número de filhos do cliente.
    • CL_SEG: Segmentação econômica do cliente (classe A, B ou C).
    • PR_ID: Código do produto (SKU) adquirido.
    • PR_CAT: Categoria do produto adquirido.
    • PR_NOME: Nome do produto adquirido.

# Realizações
    • Carregamento da Base de Dados.
    • Conversão da coluna DATA para DATATIME
    • Limpeza de colunas (Unnamed).
    • Criação das colunas de Datas.
    • Verificação de quantidades de linhas e colunas.
    • Verificação dos Tipos de dados.
    • Verificação de valores Nulos.
    • Tratamento da Categoria "#N/D".
    • Estatistica descritiva em cima da coluna CL_FHL (filhos).
    • Agrupamentos de categorias com GROUPBY.
    • Criação de uma base limpa.

# Insights Adquiridos:
    • A Coluna CL_FHL mostra uma concentração baixa de clientes com fihos (527 com nenhum filhos).
    • O ano de 2021 foi o ano com Maior número de compras.
    • O ano de 2022 foi o ano com Menor número de compras.
    • A categotia feminina possui o maior numero de compras por Gênero. 
    • A categoria ALIMENTOS concentra a maior parte dos registros de compra.

# Tecnologias Utilizadas:
    • Python.
    • jupterNotebook.
    • Pandas.
    • MatplotLib.

# Arquivo do projeto:
    mini-projeto
        base_limpa.csv
        Base_Varejo.csv
        projeto.ipynb
    README_marcos_bhering_analise_de_dados.md
    README.md

