#  ATIVIDADE ACOMPANHADA 3

temperaturas = [182.5, 179.3, 185.1, 183.8, 180.0, 178.5, 184.2]

# TODO: Complete o código abaixo
soma = 0
leituras_altas = 0  # temperaturas acima de 183°C

for temp in temperaturas:
    soma += temp  # TODO: acumule a soma
    if temp > 183:
        leituras_altas += 1  # TODO: conte leituras acima de 183°C

media = 0  # TODO: calcule a média

print(f"Total de leituras: {len(temperaturas)}")
print(f"Soma: {soma:.1f}°C")
print(f"Média: {media:.2f}°C")
print(f"Leituras acima de 183°C: {leituras_altas}")