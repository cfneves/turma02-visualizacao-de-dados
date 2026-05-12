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

#----------Exercício 1: Calculadora----------

# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Cálculos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"

# Exibição dos resultados
print(f"Soma: {soma}")  
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

#----------Exercício 2: Par ou Ímpar----------

# Entrada de dados
numero = int(input("\nDigite um número para verificar se é par ou ímpar: "))

# Verificação
if numero % 2 == 0:
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")

#----------Exercício 3: Média de Notas----------

# Entrada de dados
nota1 = float(input("\nDigite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Verificação do resultado
if media >= 7:
    print(f"Média: {media:.2f} - Aprovado")
else:
    print(f"Média: {media:.2f} - Reprovado")

#----------Exercício 4: Tabuada----------

# Entrada de dados
num = int(input("\nDigite um número para exibir a tabuada: "))

# Exibição da tabuada
print(f"Tabuada de {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
