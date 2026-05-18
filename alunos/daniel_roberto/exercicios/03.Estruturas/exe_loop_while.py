# 1. Contador simples
contador = 0
while contador < 5:
    print(f'Contador: {contador}')
    contador += 1

# 2. Validação de login do usuário (TUDO ENCOSTADO NA ESQUERDA)
senha = ""

while senha != "1234":
    senha = input("Digite a senha correta: ")
    if senha != "1234":
        print("SENHA INCORRETA! Tente Novamente.")

print("SENHA CORRETA! Acesso concedido.")