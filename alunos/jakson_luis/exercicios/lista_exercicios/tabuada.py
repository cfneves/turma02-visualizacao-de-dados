# Peça um número e exiba a tabuada dele de 1 a 10.

# Use um loop for com range(1, 11)
numero = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do número {numero}:")
for i in range (1 ,11):
    #print(f'{numero} x {i} = {numero * i}')

    #print("%d x %d = %d" % (numero, i, numero * i))

    print('{} x {} = {}'.format(numero, i, numero * i))


"""
    Usei três formas de fazer a impressão da tabuada, 
    a primeira usando f-string, 
    a segunda usando o operador de formatação % 
    e a terceira usando o método format() da string. 
    Todas as três formas produzem o mesmo resultado.
"""