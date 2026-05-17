# 1. Repetir 5 vezes
for i in range(5):
    print("Número: ", i)    # Saída: 0, 1, 2, 3, 4

# 2. Iterar sobre lista
frutas = ["Banana", "Kiwi", "Abacate"]
for fruta in frutas:
    print("Eu gosto de ", fruta)

# 3. Range com início e fim
for num in range(1,11):     # 1 até 10 (11 não inclui)
    if num < 10:
        print(num, end=" - ")
    else:
        print(num)
print()

