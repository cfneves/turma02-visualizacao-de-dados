"""

Exercício 1: Calculadora
Crie um programa que pede dois números ao usuário e exibe:
• Soma
• Subtração
• Multiplicação
• Divisão


Exercício 2: Par ou Ímpar
Peça um número ao usuário e informe se é par ou ímpar.

Dica: Use o operador % (módulo)
Se numero % 2 == 0 é par!

Exercício 3: Média de Notas
Peça 3 notas ao usuário, calcule a média e informe:
• Média >= 7: "Aprovado"
• Média < 7: "Reprovado"


Exercício 4: Tabuada
Peça um número e exiba a tabuada dele de 1 a 10.
Use um loop for com range(1, 11)

"""

# Exercício 1: Calculadora
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Erro: divisão por zero"

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

# Exercício 2: Par ou Ímpar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par!")
else:
    print("O número é ímpar!")  

# Exercício 3: Média de Notas
notas = []  
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")  

# Exercício 4: Tabuada
num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")   

