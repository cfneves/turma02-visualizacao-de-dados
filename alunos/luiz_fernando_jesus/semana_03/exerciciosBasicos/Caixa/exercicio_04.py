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
print("==== Sistema de Caixa da Loja ====")

# Entrada de dados
nome_produto1 = input("\nNome do produto 1: ")
preco_produto1 = float(input(f"Preço do {nome_produto1}: R$ "))

nome_produto2 = input("Nome do produto 2: ")
preco_produto2 = float(input(f"Preço do {nome_produto2}: R$ "))

nome_produto3 = input("Nome do produto 3: ")
preco_produto3 = float(input(f"Preço do {nome_produto3}: R$ "))


# Calculando o total da compra.
total_compra = preco_produto1 + preco_produto2 + preco_produto3
# print(f"Total da compra: R$ {total_compra}")


# Cálculos # Se a compra for maior que R$ 100, aplicar desconto de 10%
desconto = 0
if total_compra >= 100:
    desconto = total_compra * 0.10

valor_final = total_compra - desconto
# print(f"Desconto das compras: R$ {valor_final:.2f}")


# Exibição formatada
print(f"\n==== Resumo Fiscal da Compra ====")
print(f"{nome_produto1}: R$ {preco_produto1:.2f}")
print(f"{nome_produto2}: R$ {preco_produto2:.2f}")
print(f"{nome_produto3}: R$ {preco_produto3:.2f}")
print(f"=================================")

if total_compra > 100.00:
    desconto = total_compra * 0.10
    valor_final = total_compra - desconto
    print(f"Valor Total da Compra: R$ {total_compra:.2f}")
    print(f"Desconto Aplicado: R$ {desconto:.2f}")
    print(f'=================================')
    print(f"Valor Final da compra: R$ {valor_final:.2f}")
else:
    print(f"Total a Pagar: R$ {total_compra:.2f}")


# Verificação de estoque
quantidade_produto1 = int(input(f'Digite a quantidade em estoque do {nome_produto1}: '))
quantidade_produto2 = int(input(f'Digite a quantidade em estoque do {nome_produto2}: '))
quantidade_produto3 = int(input(f'Digite a quantidade em estoque do {nome_produto3}: '))

print("\n==== Situação do Estoque ====")
if quantidade_produto1 > 0:
    print(f'{nome_produto1} está disponivel para venda.')
else:
    print(f'{nome_produto1} não está disponivel para venda.')

if quantidade_produto2 > 0:
    print(f'{nome_produto2} está disponivel para venda.')
else:
    print(f'{nome_produto2} não está disponivel para venda.')

if quantidade_produto3 > 0:
    print(f'{nome_produto3} está disponivel para venda.')
else:
    print(f'{nome_produto3} não está disponivel para venda.')