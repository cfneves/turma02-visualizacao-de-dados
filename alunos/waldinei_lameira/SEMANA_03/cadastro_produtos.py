# """
# Desafio Final

# Crie um programa que simula um caixa de loja:

# 1. Peça nome de 3 produtos e seus preços
# 2. Calcule o total da compra
# 3. Aplique desconto de 10% se total > R$ 100
# 4. Exiba o valor final formatado

# Envie via Pull Request em alunos/seu_nome/exercicio_01/

# """

# Sistema simples de cadastro de produtos


# Entrada de dados

produtos = []

for i in range(1, 4):
    nome = input(f"Nome do produto {i}: ")
    preco = float(input(f"Preço do produto {i}: R$ "))
    produtos.append({"nome": nome, "preco": preco})


# Cálculo Total

total = sum(p["preco"] for p in produtos)

# Aplicar desconto de 10% se total > 100

if total > 100:
    desconto = total * 0.10
    total_final = total - desconto
    print(f"\nDesconto de 10% aplicado: -R$ {desconto:.2f}")
else:
    total_final = total

# Exibição formatada

print("\n====== RESUMO DA COMPRA ======")
for p in produtos:
    print(f"  {p['nome']}:  R$ {p['preco']:.2f}")
print(f"-------------------------")
print(f"  Total: R$ {total_final:.2f}")


# Verificação de estoque
