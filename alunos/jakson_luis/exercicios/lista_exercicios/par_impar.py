"""Peça um número ao usuário e informe se é par ou ímpar.

Dica: Use o operador % (módulo)
Se numero % 2 == 0 é par!
"""

numero = int(input("Digite um número para verificar se é par ou ímpar: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")