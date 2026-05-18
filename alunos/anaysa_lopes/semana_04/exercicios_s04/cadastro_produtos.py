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

produtos = []
precos = []

print("Cadastro de Produtos")

for i in range(3):
    nome = input(f"Digite o nome do {i+1}º produto: ")
    preco = float(input(f"Digite o preço do produto {i+1}: R$ "))
    produtos.append(nome)
    precos.append(preco)


# Cálculos

total_bruto = sum(precos)
desconto = 0 

if total_bruto > 100:
    desconto = total_bruto * 0.10
    
total_final = total_bruto - desconto

# Exibição formatada
print("\nResumo da Compra:")

for i in range(3):
    print(f"{produtos[i]}: R$ {precos[i]:.2f}")

print(f"Total Bruto: R$ {total_bruto:.2f}")
print(f"Desconto (10%): - R$ {desconto:.2f}")
print(f"Total Final: R$ {total_final:.2f}")


# Verificação de estoque

print("\nVenda Finalizada. Obrigado pela compra!")