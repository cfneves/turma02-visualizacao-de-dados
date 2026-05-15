# nome, cidade, profissão, idade e salário

nome = input("Digite o seu nome: ")

cidade = input("Digite a sua cidade: ")

profissao = input("Digite a sua profissão: ")

idade = int(input("Digite a sua idade: "))

salario = float(input("Digite o seu salário: "))

# tipos de dados

print(f"o tipo da variável 'nome' é: {type(nome)}")

print(f"o tipo da variável 'cidade' é: {type(cidade)}")

print(f"o tipo da variável 'profissão' é: {type(profissao)}")

print(f"o tipo da variável 'idade' é: {type(idade)}")

print(f"o tipo da variável 'salário' é: {type(salario)}")

# ficha cadastral com f-string

print(f"Olá, {nome}! Você mora em {cidade} e tem {idade} anos. Sua profissão atual é {profissao}, e recebe o salário de {salario: .2f}R$.  ")

# Cálculo do salário em três anos

salario_futuro = salario + (300 * 3)

print(f"Daqui há três anos, seu salário será de : {salario_futuro:.2f}")