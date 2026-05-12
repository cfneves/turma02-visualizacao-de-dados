"""
Exercício 1: Calculadora
Crie um programa que pede dois números ao usuário e exibe:
• Soma
• Subtração
• Multiplicação
• Divisão

"""
# criar uma variável com input para indicar as operações aritméticas:
operacao = input("Selecione a operação aritmética: (1) Soma / (2) Subtração / (3) Multiplicação / (4) Divisão")

#selecionar os números:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

#determinar as condicionais:
if operacao == '1':
    print(num1 + num2)
elif operacao == '2':
    print(num1 - num2)
elif operacao == '3':
    print(num1 * num2)
elif operacao == '4':
    print(num1 / num2)
else:
    print("Opção inválida")         
        

"""""=========================================================================================================
Exercício 2: Par ou Ímpar
Peça um número ao usuário e informe se é par ou ímpar.

Dica: Use o operador % (módulo)
Se numero % 2 == 0 é par!
"""
#solicitar um número ao usuário:
numero = float(input("Digite um número: "))

#determinar as condicionais:
if numero % 2 == 0:
    print(f"O número é par!")
else:
    print(f"O número é impar!")

"""============================================================================================================

Exercício 3: Média de Notas
Peça 3 notas ao usuário, calcule a média e informe:
• Média >= 7: "Aprovado"
• Média < 7: "Reprovado"

"""
""""""
#solicitar um número ao usuário:
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

#calcular a média:
resultado = (nota1 + nota2 + nota3) / 3

#determinar as condicionais:
if resultado >= 7:
    print(f"Aluno Aprovado!")
elif resultado < 7:
    print(f"Aluno Reprovado!")


"""==============================================================================================================
Exercício 4: Tabuada
Peça um número e exiba a tabuada dele de 1 a 10.
Use um loop for com range(1, 11)
    
"""
#pedir para o usuário inserir o número da tabuada desejada:
tabuada = int(input("Insira o número da tabuada: "))

#gerando a tabuada:
for i in range(1, 11):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}\n")

