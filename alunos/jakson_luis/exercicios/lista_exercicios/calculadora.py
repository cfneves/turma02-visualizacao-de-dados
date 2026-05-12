"""
Crie um programa que pede dois números ao usuário e exibe:
• Soma
• Subtração
• Multiplicação
• Divisão

"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

# divisao = num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"


print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")

if num2 !=0:
    print(f"Divisão: {divisao}")
else:
    print("Divisão por zero não é permitida")