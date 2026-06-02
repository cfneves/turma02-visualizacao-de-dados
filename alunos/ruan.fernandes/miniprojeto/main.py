from sprint01 import carregar_dados
from sprint02 import tratamento_dados
from sprint03 import limpeza_dados
from sprint04 import analise_dados
from sprint05 import gerar_relatorio
from sprint06 import gerar_graficos

# Sprint 01
df = carregar_dados()

# Sprint 02
df = tratamento_dados(df)

# Sprint 03
df = limpeza_dados(df)

# Sprint 04
analises = analise_dados(df)

# Sprint 05
gerar_relatorio(
    analises["genero"],
    analises["categoria"],
    analises["meses"],
    analises["filhos"]
)

# Sprint 06
gerar_graficos(
    analises["genero"],
    analises["categoria"],
    analises["meses"],
    analises["filhos"]
)