def limpeza_dados(df):

    mask_produto_nd = df["Produtos"] == "#N/D"
    mask_categoria_nd = df["Categoria do Produto"] == "#N/D"

    # Ambos não identificados
    df.loc[
        mask_produto_nd & mask_categoria_nd,
        ["Produtos", "Categoria do Produto"]
    ] = "Não Identificado"

    # Produto não identificado
    df.loc[
        mask_produto_nd & ~mask_categoria_nd,
        "Produtos"
    ] = (
        "Produto de "
        + df.loc[
            mask_produto_nd & ~mask_categoria_nd,
            "Categoria do Produto"
        ]
    )

    print(f"[Sprint 03] Limpeza concluída. Registros: {len(df)}")

    return df