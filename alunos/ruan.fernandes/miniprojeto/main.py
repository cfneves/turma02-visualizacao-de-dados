from sprint01 import carregar_dados
from sprint02 import tratamentos_dados
from sprint03 import limpeza_dados
from sprint04 import analise_dados
from sprint05 import gerar_relatorio

df = carregar_dados()
df = tratamentos_dados(df)
df = limpeza_dados(df)


genero, categoria, meses, filhos = analise_dados(df)

gerar_relatorio(
    genero,
    categoria,
    meses,
    filhos
)