# Declarando variáveis de diferentes tipos de dados

idade = 25  # Variável do tipo inteiro
altura = 1.75  # Variável do tipo float
nome = "João"  # Variável do tipo string
estudante = True  # Variável do tipo booleano


# Verificar tipo da variável
print(type(idade))  # Saída: <class 'int'>
print(type(altura))  # Saída: <class 'float'>
print(type(nome))  # Saída: <class 'str'>
print(type(estudante))  # Saída: <class 'bool'>

# Conversão entre tipos de dados (casting)

numero_texto = "123"
numero_inteiro = int(numero_texto)  # Convertendo string para inteiro
print(numero_inteiro)  # Saída: 123