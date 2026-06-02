# Exemplo 1: Contador simples

contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Exemplo 2: Validanção de entrada do usuário

senha = ""

while senha != "1234":
    senha = input("Digite a senha correta: ")
if senha  != "1234":
        print("Senha incorreta. Tente novamente.")
print("Senha correta! Acesso concedido.")   