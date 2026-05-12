"""
Desafio Final

Crie um programa que simula um caixa de loja:

1. Peça nome de 3 produtos e seus preços
2. Calcule o total da compra
3. Aplique desconto de 10% se total > R$ 100
4. Exiba o valor final formatado

Envie via Pull Request em alunos/seu_nome/exercicio_01/

"""

#criar o dicionário:
cadastro = {}

#solicitar ao usuario as informações para cadastro:
for i in range(3):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    cadastro[nome] = preco 

print(cadastro)

#calcular o total da compra:
total_compra = sum(cadastro.values())

print(total_compra)

#aplicar o desconto caso atenda à condicionante:
if total_compra > 100:
    desconto = total_compra * 0.10
    total_com_desconto = total_compra - desconto
else: 
    total_com_desconto = total_compra

print(total_com_desconto)

#exibir valor final formatado:
print(f"O valor final do total da compra é de R$ {total_com_desconto}")








#exibir o cadastro:
