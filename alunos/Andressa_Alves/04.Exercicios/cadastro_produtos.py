"""
Desafio Final

Crie um programa que simula um caixa de loja:

1. Peça nome de 3 produtos e seus preços
2. Calcule o total da compra
3. Aplique desconto de 10% se total > R$ 100
4. Exiba o valor final formatado

Envie via Pull Request em alunos/seu_nome/exercicio_01/

"""

# Sistema simples de cadastro de produtos

# Entrada de dados

produto1 = input("Digite o nome do primeiro produto: ")
preco1 = float(input(f"Digite o preço do produto {produto1}: R$ "))

produto2 = input("Digite o nome do segundo produto: ")
preco2 = float(input(f"Digite o preço do produto {produto2}: R$ "))

produto3 = input("Digite o nome do terceiro produto: ")
preco3 = float(input(f"Digite o preço do produto {produto3}: R$ "))

# Cálculos

total = preco1 + preco2 + preco3

desconto = 0

if total > 100:
    desconto = total * 0.10

valor_final = total - desconto

# Exibição formatada

print("\n========== RESUMO DA COMPRA ==========")
print(f"Produto 1: {produto1} - R$ {preco1:.2f}")
print(f"Produto 2: {produto2} - R$ {preco2:.2f}")
print(f"Produto 3: {produto3} - R$ {preco3:.2f}")

print(f"\nTotal da compra: R$ {total:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")

# Verificação de estoque

estoque = input("\nDigite se tem em estoque: S/N ")

if estoque.upper() == "S":
    print("Produto disponível em estoque.")
else:
    print("Produto fora de estoque.")