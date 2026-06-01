""""
======================================================================================
MÓDULO 1: VISUALIZAÇÃO DE DADOS E BUSINESS INTELLIGENCE [T2]
MINI-PROJETO AVALIATIVO - SEMANA 07

Aluna: Camilla Nascimento de Oliveira
Data de Entrega: 01/06/2026
Ambiente de Desenvolvimento: VS Code - escolhida a utilização do arquivo (.py)
--------------------------------------------------------------------------------------

1. CONTEXTO DO PROJETO E JUSTIFICATIVA DE NEGÓCIO
No universo de Business Intelligence (BI) e Análise de Dados, os dados brutos raramente 
estão prontos para gerar insights imediatos. É comum encontrar inconsistências como 
valores nulos, tipos de dados incorretos (como datas tratadas como texto ou outros caracteres) e registos 
duplicados. Tomar decisões estratégicas com base em dados "sujos" pode direcionar uma 
empresa a investimentos errados e prejuízos operacionais, interferindo diretamente na gestão de decisões e na eficiência dos processos internos.

Este mini projeto aplica os fundamentos da Análise Exploratória de Dados (AED) sobre uma 
base de dados real de varejo. O objetivo principal é construir um script automatizado 
e replicável que identifique falhas de qualidade, limpe e estruture os dados, 
deixando a base 100% confiável para alimentar dashboards analíticos ou relatórios.

2. ABORDAGEM TEÓRICA: O PROCESSO DE ETL (Extract, Transform, Load)
Para garantir a integridade da informação e alcançar a pontuação máxima nos critérios 
de avaliação, o script foi desenhado seguindo as etapas metodológicas de um pipeline ETL:
  * EXTRACT (Extração): Leitura estruturada e nativa do ficheiro CSV utilizando o 
    módulo 'csv.DictReader', garantindo precisão linha a linha.
  * TRANSFORM (Transformação): Aplicação das regras de negócio solicitadas, como o uso 
    de lógica condicional (if/else) para preencher categorias vazias com "Sem Categoria", 
    tratamento de dimensões físicas nulas, eliminação de duplicados pelo identificador 
    da compra e conversão de strings temporais através do módulo nativo 'datetime'.
  * LOAD (Carga): Exportação da base de dados perfeitamente higienizada para um novo 
    ficheiro otimizado ('df_limpo.csv'), pronto para consumo ágil no Power BI.

3. CRONOGRAMA DE EXECUÇÃO (MAPEAMENTO DAS SPRINTS)
O código encontra-se organizado e documentado em blocos lógicos sequenciais:
  * Sprint 1: Importação estruturada dos dados (Nativa via DictReader).
  * Sprint 2 e 3: Funções de limpeza, tratamento de nulos/duplicados e conversão para datetime.
  * Sprint 4: Geração de Estatísticas Descritivas Completas (Coluna: 'Numero_Filhos').
  * Sprint 5: Padrões de Agrupamento Estratégico (groupby/pivot_table) e Relatório Final.
  * Sprint 6: Exportação dos resultados e preparação para o versionamento no GitHub.
======================================================================================
"""



# Para iniciar o Mini Projeto, vamos importar a biblioteca pandas e carregar o arquivo CSV contendo os dados do varejo. Certifique-se de que o caminho para o arquivo CSV esteja correto. 
import csv
from datetime import datetime
import pandas as pd

print("Pandas importado com sucesso")

# Verificação que tinham separadores com ; - fazer a correção para o separador correto

df = pd.read_csv(
    r"C:\Users\Milla\Documents\GitHub\turma-visualizacao-de-dados\datasets\Varejo.csv",
    sep=";"
)

print("Arquivo CSV carregado com sucesso")

print(df.head())

