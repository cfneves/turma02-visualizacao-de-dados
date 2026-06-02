"""
Autor: Professor Especialista Cláudio Ferreira Neves

Desafio

Crie um programa que simula um caixa de loja:

1. Peça nome de 3 produtos e seus preços
2. Calcule o total da compra
3. Aplique desconto de 10% se total > R$ 100
4. Exiba o valor final formatado

Envie via Pull Request em alunos/seu_nome/exercicio_01/

"""


# Sistema simples de cadastro de produtos
print("===== Sistema de Caixa da Loja =====")


# Entrada de dados
nome_produto1 = input("Nome do produto 1: ")
preco_produto1 = float(input(f"Preço do {nome_produto1}: R$ "))

nome_produto2 = input("Nome do produto 2: ")
preco_produto2 = float(input(f"Preço do {nome_produto2}: R$ "))

nome_produto3 = input("Nome do produto 3: ")
preco_produto3 = float(input(f"Preço do {nome_produto3}: R$ "))


# Cálculos
total = preco_produto1 + preco_produto2 + preco_produto3

desconto = 0
if total > 100:
    desconto = total * 0.10

valor_final = total - desconto


# Exibição formatada
print("\n===== Resumo da Compra =====")
print(f"{nome_produto1}: R$ {preco_produto1:.2f}")
print(f"{nome_produto2}: R$ {preco_produto2:.2f}")
print(f"{nome_produto3}: R$ {preco_produto3:.2f}")
print(f"\nTotal: R$ {total:.2f}")

if desconto > 0:
    print(f"Desconto (10%): -R$ {desconto:.2f}")

print(f"Valor final: R$ {valor_final:.2f}")


# Verificação de estoque
quantidade_produto1 = int(input(f"\nQuantidade em estoque de {nome_produto1}: "))
quantidade_produto2 = int(input(f"Quantidade em estoque de {nome_produto2}: "))
quantidade_produto3 = int(input(f"Quantidade em estoque de {nome_produto3}: "))

print("\n===== Situação do Estoque =====")

if quantidade_produto1 > 0:
    print(f"{nome_produto1}: {quantidade_produto1} unidade(s) disponível(is)")
else:
    print(f"{nome_produto1}: SEM ESTOQUE")

if quantidade_produto2 > 0:
    print(f"{nome_produto2}: {quantidade_produto2} unidade(s) disponível(is)")
else:
    print(f"{nome_produto2}: SEM ESTOQUE")

if quantidade_produto3 > 0:
    print(f"{nome_produto3}: {quantidade_produto3} unidade(s) disponível(is)")
else:
    print(f"{nome_produto3}: SEM ESTOQUE")
