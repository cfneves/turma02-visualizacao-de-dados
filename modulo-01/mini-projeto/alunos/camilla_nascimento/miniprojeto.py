# Para iniciar o Mini Projeto, vamos importar a biblioteca pandas e carregar o arquivo CSV contendo os dados do varejo. Certifique-se de que o caminho para o arquivo CSV esteja correto. 
import pandas as pd

print("Pandas importado com sucesso")

# Verificação que tinham separadores com ; - fazer a correção para o separador correto

df = pd.read_csv(
    r"C:\Users\Milla\Documents\GitHub\turma-visualizacao-de-dados\modulo-01\mini-projeto\alunos\camilla_nascimento\varejo.csv",
    sep=";"
)

print("Arquivo CSV carregado com sucesso")

print(df.head())
