# 2. Input - Receber Dados do Usuário
# Com o comando input, podemos pedir informações ao usuário. O valor digitado é armazenado em uma variável. Exemplo:
nome = input("Digite seu nome: ")
print("Olá,", nome)
# IMPORTANTE: input() sempre retorna STRING (texto)
# Para armazenar um número, precisamos converter a string para o tipo numérico desejado. Exemplo:
idade = int(input("Digite sua idade: "))
print("Você tem", idade, "anos")