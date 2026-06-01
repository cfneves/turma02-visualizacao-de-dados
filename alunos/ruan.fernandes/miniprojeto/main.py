from sprint01 import carregar_dados
from sprint02 import tratamentos_dados
from sprint03 import limpeza_dados
from sprint04 import analise_dados

# Sprint 1
df = carregar_dados()

# Sprint 2
df = tratamentos_dados(df)

# Sprint 3
df = limpeza_dados(df)

# Sprint 4
resultado = analise_dados(df)

resultado = analise_dados(df)

print(resultado["genero"])
print(resultado["categoria"])
print(resultado["meses"])
print(resultado["filhos"])