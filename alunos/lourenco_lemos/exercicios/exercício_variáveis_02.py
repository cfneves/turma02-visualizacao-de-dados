# 2. Concatenação de String
#É possivel concatenar (juntar) strings usando o operador de adição (+).

nome = "Lourenço"
sobrenome = "Lemos"

nome_completo = nome + " " + sobrenome # O espaço entre as aspas é para adicionar um espaço entre o nome e o sobrenome
print(nome_completo)  # Saída: Lourenço Lemos

#Melhorando
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_completo = nome + " " + sobrenome
print(nome_completo)  # Saída: <nome> <sobrenome>
