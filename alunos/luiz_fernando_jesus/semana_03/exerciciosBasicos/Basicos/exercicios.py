"""
Exercicios da semana 03.

Decidi colocar tudo em um arquivo só,
sei quem alguns momentos pode ser que algo sobreescreve outra variável,
mas entendi o conceito dos exercicios.

"""

# 01 Exibindo mensagens - jeito simples:

# String - Textos que estão entre as aspas.
print("Olá! Meu nome é Luiz Fernando e estou aprendendo Python.")

# Números - Porque não está dentro das aspas.
print(25)

# Imprimir tipos de valores diferentes, requer o uso de virgula para separar Strings e Números.
print("Meu nome é, Luiz Fernando, e tenho", 25, "anos.")

# 02 Recebendo os dados que o usuário digite: input()

nome = input("Digite seu nome: ")
print("Olá,", nome)

# int(input()) int= para converter o valor fornecido do usuário para números inteiros.
# Por padrão, o input() recebe os dados como String.
idade = int(input("Digite a sua idade: "))
print("Você tem", idade, "anos.")

# 03 Comentando o código

# Comentando de uma linha (Usamos o #)

# Comentario de multiplas linhas (""" ou ''') Exemplo:

"""
Tudo aqui dentro está comentado e o python irá ignorar complemtamente.

"""

nome = "Luiz Fernando" # Comentario no final da linha.

# 04 Variáveis do tipo booleano

ativo = True # True ou False (Primeira letra sempre Maiúscula)
print(ativo)

pago = False
print(pago)

maior_idade = True
print(maior_idade)

# 05 Números com casas decimais (10,00).

preço = 9.99
print(preço)

altura = 1.65
print(altura)

nota = 8.4
print(nota)

# (Float 9.99) (Int 9.)

# 06 Números inteiros (10, 20, 100 -4, -50)

idade = 25
temperatura = -10
ano = 2026

print(idade)
print(temperatura)
print(ano)

# números inteiros podem ser feitos para fazer cálculos.
soma = idade + ano
print(soma)

# 07 Concatenação de Strings

nome = "Luiz"
sobrenome = "Jesus"

# + " " + Adiciona um espaço entre as variáveis.
nome_completo = nome + " " + sobrenome 
print(nome_completo)

# 08 Variáveis do tipo String

nome = "Luiz Fernando"
cidade = "São José"
mensagem = "Olá!"

# Declarando variáveis de diferentes tipos de dados.

idada = 25             # Variável do tipo inteiro
altura = 1.65          # Variável do tipo float
nome = "Luiz Fernando" # Variável do tipo string
estudante = True       # Variável do tipo booleano

# Verificando o tipo das variáveis.
# Função type().

print(type(idade))     # Saída: <class 'int'>
print(type(altura))    # Saída: <class 'float'>
print(type(nome))      # Saída: <class 'str'>
print(type(estudante)) # Saída: <class 'bool'>

# Convertendo tipos de dados (casting)

numero_texto = "987"
numero_inteiro = int(numero_texto) # Converte o str para int
print(numero_inteiro) # Saída: 987

# 09 Condicionais - if, elif e else.

# Exemplo 1: if simples
idade = 18
if idade >= 18:
    print("Você é maior de idade.")

# Exemplo 2: if-else
nota = 7.5
if nota >= 7.0:
    print("Você foi aprovado.")
else:
    print("Você não foi aprovado.")

# Exemplo 3: if-elif-else (multiplas condições)

notas = 8.0
if notas >= 9.0:
    print("Exelente!")
elif notas >= 7.0:
    print("Bom trabalho!")
else:
    print("Estude mais.")

# 10 Estruturas de repetição - loop for.

# Exemplo 1: repertir 5 vezes.

for i in range(5):
    print("Número:", i)
# Saída: 0, 1, 2, 3, 4

# Exemplo 2: Iterar sobre lista
frutas = ["maça", "banana", "laranja"]

for fruta in frutas:
    print('Eu gosto dessas frutas:', fruta)

# Exemplo 3: Range com início e fim
for num in range(1, 10): # 1 até 10 (11 não
    print(num)

# 11 Estruturas de repetição - loop while.

# Exemplo 1: Contador simples.

contador = 0
while contador < 5:
    print(f'Contador: {contador}')
    contador += 1

# Exemplo 2: Validanção de entrada do usuário.

senha = ""

while senha != "4321":
    senha = input("Digite a senha correta: ")
    
if senha != "4321":
    print("Senha incorreta. Tente novamente.")
print("Senha correta! Acesso concedido.")
