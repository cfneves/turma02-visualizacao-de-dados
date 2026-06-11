##############################################################################
# EXERCÍCIO 1 — CALCULADORA
# Autor: Professor Especialista Cláudio Ferreira Neves
##############################################################################

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print(f"Soma:           {numero1 + numero2}")
print(f"Subtração:      {numero1 - numero2}")
print(f"Multiplicação:  {numero1 * numero2}")

if numero2 != 0:
    print(f"Divisão:        {numero1 / numero2}")
else:
    print("Divisão:        não é possível dividir por zero")


##############################################################################
# EXERCÍCIO 2 — PAR OU ÍMPAR
##############################################################################

numero = int(input("\nDigite um número: "))

if numero % 2 == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")


##############################################################################
# EXERCÍCIO 3 — MÉDIA DE NOTAS
##############################################################################

nota1 = float(input("\nDigite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3
print(f"Média: {media:.2f}")

if media >= 7:
    print("Resultado: Aprovado")
else:
    print("Resultado: Reprovado")


##############################################################################
# EXERCÍCIO 4 — TABUADA
##############################################################################

numero = int(input("\nDigite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
