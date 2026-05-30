# 1. If simples
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# 2. If-Else
nota = float(input("Digite sua nota: "))
if nota >= 7.0:
    print("Parabéns! Você foi aprovado!")
else:
    print("Você não foi aprovado.")

# If-Elif-Else (múltiplas condições)
nota = float(input("Digite sua nota: "))
if nota >= 9.0:
    print("Excelente!")
elif nota >= 7.0:
    print("Bom Trabalho!")
elif nota >= 5.0:
    print("Regular.")
else:
    print("Insuficiente.")
