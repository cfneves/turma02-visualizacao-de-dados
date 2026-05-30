#Exercício 1: Calculadora
#Crie um programa que pede dois números ao usuário e exibe:
#• Soma
#• Subtração
#• Multiplicação
#• Divisão

print("Olá, bem-vindo!")
calculadora1 = float(input("Digite um número: "))
calculadora2 = float(input("Digite outro número: "))

soma = calculadora1 + calculadora2
print(soma)

subtracao = calculadora1 - calculadora2
print(subtracao)

divisao = calculadora1 / calculadora2
print(divisao)

multiplicacao = calculadora1 * calculadora2
print(multiplicacao)


#Exercício 2: Par ou Ímpar
#Peça um número ao usuário e informe se é par ou ímpar.

#Dica: Use o operador % (módulo)
#Se numero % 2 == 0 é par!

print("Olá, bem-vindo!")
numero = int(input("Digite um número: "))
par_ou_impar = numero%2
if par_ou_impar == 0:
    print("O número é par!")
else:
    print("O número é ímpar!")


# Exercício 3: Média de Notas
# Peça 3 notas ao usuário, calcule a média e informe:
#• Média >= 7: "Aprovado"
#• Média < 7: "Reprovado"

print("Olá, bem-vindo!")
nota1 = float(input("Vamos lançar as notas, coloque a primeira nota: "))
nota2 = float(input("Coloque a segunda nota: "))
nota3 = float(input("Agora coloque a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"{media:.2f}")
if media >= 7:
    print("aprovado")
else:
    print("reprovado")


# Exercício 4: Tabuada
# Peça um número e exiba a tabuada dele de 1 a 10.
# Use um loop for com range(1, 11)
print("Olá, bem-vindo!\nVamos aprender a tabuada!")
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")