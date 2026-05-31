"""
Desafio

Crie um programa que simula um caixa de loja:

1. Peça nome de 3 produtos e seus preços
2. Calcule o total da compra
3. Aplique desconto de 10% se total > R$ 100
4. Exiba o valor final formatado

"""
#Criando um sistema simples para cadastar produtos e calcular o total da compra
print("===== Caixa da Loja - Bem Vindo =====")

#Entrada dos dados dos produtos
nome_produto1 = input("Nome do produto 1: ")
preco_produto1 = float(input("Preço do produto 1: "))#inserindo o comando float para converter o valor inserido em número decimal

nome_produto2 = input("Nome do produto 2: ")
preco_produto2 = float(input("Preço do produto 2: "))#inserindo o comando float para converter o valor inserido em número decimal

nome_produto3 = input("Nome do produto 3: ")
preco_produto3 = float(input("Preço do produto 3: "))#inserindo o comando float para converter o valor inserido em número decimal

#Calculando o total da compra
total_compra = preco_produto1 + preco_produto2 + preco_produto3
print(f"Total da compra: R$ {total_compra:.2f}") #exibindo o total da compra. O comando :.2f é usado para formatar o número com 2 casas decimais


#Calculando o desconto
desconto = 0 #inserindo o valor 0, para criar a variável
if total_compra > 100:
    desconto = total_compra * 0.10 #calculando o desconto de 10%, se o valor total da compra for maior que 100
    print(f"Desconto aplicado: R$ {desconto:.2f}") #exibindo o desconto aplicado

#Calculando o valor final
valor_final = total_compra - desconto
print(f"Valor final: R$ {valor_final:.2f}") #exibindo o valor final formatado

#Imprimindo o resumo da compra
print("\n===== Resumo da Compra =====")
print(f"{nome_produto1}: R$ {preco_produto1:.2f}")
print(f"{nome_produto2}: R$ {preco_produto2:.2f}")
print(f"{nome_produto3}: R$ {preco_produto3:.2f}")
print(f"\nTotal: R$ {total_compra:.2f}")

#Verificando o estoque dos produtos
quantidade_produto1 = int(input(f"\nQuantidade em estoque de {nome_produto1}: "))
quantidade_produto2 = int(input(f"Quantidade em estoque de {nome_produto2}: "))
quantidade_produto3 = int(input(f"Quantidade em estoque de {nome_produto3}: "))

print("\n===== Situação do Estoque dos Produtos =====")
if quantidade_produto1 > 0:
    print(f"{nome_produto1}: {quantidade_produto1} unidades em estoque")
else:    print(f"{nome_produto1}: Produto esgotado")
if quantidade_produto2 > 0:
    print(f"{nome_produto2}: {quantidade_produto2} unidades em estoque")
else:    print(f"{nome_produto2}: Produto esgotado")
if quantidade_produto3 > 0:
    print(f"{nome_produto3}: {quantidade_produto3} unidades em estoque")
else:    print(f"{nome_produto3}: Produto esgotado")