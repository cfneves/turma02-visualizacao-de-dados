import matplotlib.pyplot as plt

def gerar_graficos(genero, categoria, meses, filhos):

    # Gráfico 1 - Clientes por gênero
    plt.figure(figsize=(8, 5))
    plt.bar(
        genero["Gênero do Cliente"],
        genero["Quantidade de Clientes"]
    )
    plt.title("Clientes por Gênero")
    plt.ylabel("Quantidade de Clientes")
    plt.tight_layout()
    plt.show()


    # Gráfico 2 - Produtos por categoria
    plt.figure(figsize=(12, 6))
    plt.bar(
        categoria["Categoria do Produto"],
        categoria["Quantidade de Produtos"]
    )
    plt.title("Produtos por Categoria")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


    # Gráfico 3 - Compras por mês
    plt.figure(figsize=(8, 5))
    plt.plot(
        meses["Data da Compra"],
        meses["Quantidade de Compras"],
        marker="o"
    )
    plt.title("Compras por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Quantidade de Compras")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


    # Gráfico 4 - Clientes por quantidade de filhos
    plt.figure(figsize=(8, 5))
    plt.bar(
        filhos["Quantidade de Filhos"],
        filhos["Quantidade de Clientes"]
    )
    plt.title("Clientes por Quantidade de Filhos")
    plt.xlabel("Número de Filhos")
    plt.ylabel("Quantidade de Clientes")
    plt.tight_layout()
    plt.show()