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
numero1 = float(input("Primeiro número: "))
numero2 = float(input("Segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2 if numero2 != 0 else "Erro: Divisão por zero não é permitida."#Para a divisão é necessário trabalhar com um condicional, para evitar a divisão por zero.

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

# Exercício 2: Par ou Ímpar
numero = int(input("\nDigite um número: "))
if numero % 2 == 0:  # O operador % (módulo) retorna o resto da divisão. Se o número for divisível por 2, o resultado será 0, indicando que é par.
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")

# Exercício 3: Média de Notas
nota1 = float(input("\nNota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Média: {media:.2f}")  # O :.2f formata a média para mostrar apenas 2 casas decimais.
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

# Exercício 4: Tabuada
numero = int(input("\nDigite um número para ver a tabuada: "))# O input é convertido para inteiro, pois a tabuada é feita com números inteiros.
for i in range(1, 11): # O loop for percorre os números de 1 a 10 (inclusive) usando a função range(1, 11). O número 11 é exclusivo, então o loop termina em 10.
    print(f"{numero} x {i} = {numero * i}")