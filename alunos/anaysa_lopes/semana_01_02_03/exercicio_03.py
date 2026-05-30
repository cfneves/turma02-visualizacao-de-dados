# Criar programa que calcule IMC

# Nome, peso,  altura e idade

nome = str(input('Qual o seu nome? '))
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
idade = int(input('Qual a sua idade? '))


# Calculo do IMC: peso / (altura ** 2)

imc = peso / (altura ** 2)

print(f"O IMC de {nome} é: {imc:.2f}")

#Classificação usando elif:

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc <= 24.9:
    classificacao = "Peso normal"
elif imc <= 29.9:
    classificacao = "Sobrepeso"
elif imc <= 34.9:
    classificacao = "Obesidade grau 1"
elif imc <= 39.9:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3"

print(f"Classificação: {classificacao}")

# Se o IMC é normal e a pessoa tem mais de 60 anos, exibir mensagem epecial de atenção á saúde;

if (imc >= 18.5 and imc <= 24.9) and idade > 60:
  print("Atenção redobrada à saúde")



# Verificar se o IMC está acima de 25

acima_25 = imc > 25

print(f"O IMC está acima de 25? {acima_25}")