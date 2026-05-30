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

print("\n----SIMULADOR DE CAIXA----")

# Entrada de dados


nomes = input("Insira o nome de 3 produtos (separado por virgulas):")
a, b, c = nomes.split(",")


precos = input("Insira o preço dos 3 produtos (separado por virgula):")
d, e, f = map(float,precos.split(","))

# Cálculos

total_compra  = d + e + f

if total_compra > 100:
    desconto = total_compra * 0.10
    valor_final = total_compra = desconto
    print(f"Desconto de 10% aplicado, tivemos R${desconto:.2f} de desconto")

# Exibição formatada


print("\n----RESUMO COMPRA----")
print(f"")







# Verificação de estoque





