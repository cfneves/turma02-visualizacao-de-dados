
# 2. Input - Receber Dados do Usuário
# Pede o nome do usuário e guarda em uma variável
nome = input("Digite seu nome: ")
print("Olá,", nome)
# IMPORTANTE: input() sempre retorna STRING (texto)
# Se precisar de número, precisa converter:
idade = int(input("Digite sua idade: "))
print("Você tem", idade, "anos")