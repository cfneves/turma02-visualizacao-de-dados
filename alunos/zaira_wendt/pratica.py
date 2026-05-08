 print("=== Exercício 1: Calculadora ===")

continuar = "sim"

while continuar != "sair":

    num1 = float(input("Digite o número: ")) 
    num2 = float(input("Digite o número: "))

    print("\nEscolha a operação")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicaçao")
    print("4 - Divisão")

    opcao = input("Digite o número da operação: ")

    if opcao == "1":
        print(num1 + num2)

    elif opcao == "2":
        print(num1 - num2)

    elif opcao == "3":
        print(num1 * num2)

    elif opcao == "4": 
        if num2 != 0:
            print(num1 / num2) 
        else:
            print("ERRO: Não é possivel dividir por zero!")
    else:
        print("Opção inválida")

    continuar = input("\nDigite 'sair' para encerrar ou qualquer tecla para continuar: ")

print("Calculadora encerrada")




print("=== Exercício 2: Par ou ímpar ===")

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par!")
else: 
    print("O número é ímpar!")




print("=== Exercício 3: Média de notas ===")

nota1 = float(input("Digite a primeira nota: ."))
nota2 = float(input("Digite a segunda nota: ."))
nota3 = float(input("Digite a terceira nota: ."))

media = (nota1 + nota2 + nota3) / 3

print("Média: ", media )

if media >= 7:
    print("Aprovado!")

elif media < 7:
    print("Reprovado!")



print("=== Exercício 4: Tabuada ===")

numero = float(input("Escolha um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")




