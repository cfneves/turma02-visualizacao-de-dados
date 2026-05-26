# O forno deve operar entre 160ºC e 200ºC. Escreva um programa que leia a temperatura do forno e informe se ela está dentro da faixa ideal ou não.
# Classifique a temperatura como: BAIXA / NORMAL /ALTA

temperatura_forno = 175.0

if temperatura_forno < 160:
    print("Temperatura BAIXA - aquecer forno")

elif temperatura_forno <= 200:
    print("Temperatura NORMAL - produção liberada")

else:
    print("Temperatura ALTA - risco de queima de peças")

