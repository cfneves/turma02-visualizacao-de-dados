# Declarando variáveis de diferentes tipos de dados
idade = 47      # variável tipo int
preco = 59.90   # variável tipo float
cidade = "Blumenau"     # variável tipo string
estudante = True        # variável tipo bool

# Verificar tipo de variável
print(type(idade))      # Saída: <class 'int'>
print(type(preco))      # Saída: <class 'float'>
print(type(cidade))     # Saída: <class 'str'>
print(type(estudante))  # Saída: <class 'bool'>

# Conversão entre tipos de dados (casting)
numero_texto = "1979"
numero_inteiro = int(numero_texto) # Convertendo str para int
print(numero_inteiro)   # Saída: 1979