"""

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

print("Calculadora Simples")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")


if num2 != 0:
    print(f"Divisão: {num1 / num2}")
else:
    print("Divisão: Erro (não é possível dividir por zero)")


# Exercício 2: Par ou Ímpar

print("\nVerificador de Par ou Ímpar")
num = int(input("Digite um número para verificar se é par ou ímpar: "))

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")   



# Exercício 3: Média de Notas

print("\nCalculadora de Média de Notas")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Sua média: {media:.2f}")

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")  


# Exercício 4: Tabuada

print("\nTabuada")
num = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
