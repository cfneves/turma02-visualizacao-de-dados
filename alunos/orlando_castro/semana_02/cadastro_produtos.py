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
# cria um dicionário para armazenar os produtos e seus preços
produtos = {}

# Entrada de dados
for i in range(3):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    produtos[nome] = preco

# Cálculos
total = sum(produtos.values())
if total > 100:
    total_com_desconto = total * 0.9
    print(f"Valor final: R$ {total:.2f}")
    print(f"Valor final com desconto: R$ {total_com_desconto:.2f}")
else:
    print(f"Valor final: R$ {total:.2f}")

# Criando um dicionário de estoque para os produtos cadastrados
estoque = {f"Produto {i+1}": 10 - i for i in range(3)}
# Atualizando o estoque com os produtos cadastrados
estoque.update({nome: 10 for nome in produtos})

for produto in produtos:
    if produto in estoque:
        if estoque[produto] > 0:
            print(f"{produto} está disponível em estoque.")
        else:
            print(f"{produto} está esgotado.")
    else:
        print(f"{produto} não encontrado no estoque.")  

