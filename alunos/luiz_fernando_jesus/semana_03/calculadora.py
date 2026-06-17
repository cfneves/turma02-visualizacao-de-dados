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
# Crie um programa que pede dois números ao usuário e exibe:
# • Soma
# • Subtração
# • Multiplicação
# • Divisão

print('=== Programa de Calculadora ===')
print()
valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))

print(f'\nA Soma desses valores é:        {valor1} + {valor2} = {valor1+valor2}')
print(f'A Subtração desses valores é:     {valor1} - {valor2} = {valor1-valor2}')
print(f'A Multiplacação desses valores é: {valor1} * {valor2} = {valor1*valor2}')
print(f'A Divisão desses valores é:       {valor1} / {valor2} = {valor1/valor2}')

# Exercício 2: Par ou Ímpar
# Peça um número ao usuário e informe se é par ou ímpar.

# Dica: Use o operador % (módulo)
# Se numero % 2 == 0 é par!

print('=== Número PAR ou IMPAR ===')

print()
numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'\nO número {numero} que você digitou é par.')
else:
    print(f'\nO número {numero} que voce digitou  é impar.')
print()

# Exercício 3: Média de Notas
# Peça 3 notas ao usuário, calcule a média e informe:
# • Média >= 7: "Aprovado"
# • Média < 7: "Reprovado"

print("=== Média do aluno ===")

print()
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

nota_total = (nota1 + nota2 + nota3) / 3

if nota_total >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")

# Exercício 4: Tabuada
# Peça um número e exiba a tabuada dele de 1 a 10.
# Use um loop for com range(1, 11)

print('=== Tabuada ===')

print()
numero_n = int(input('Digite um número: '))

i = 0
for tabuada in range(11):
    print(f'{numero_n} X {i} = {numero_n * i}')
    i += 1