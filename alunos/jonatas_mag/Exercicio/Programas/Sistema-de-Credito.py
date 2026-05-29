# - SISTEMA COMPLETO COM TODAS AS CONDICIONAIS

print (" === Sistema de aprovação de crédito === ")
# Regras:
# 1. idade deve ser entre 18 e 75 anos
# 2. renda mínima de R$ 1.900,00
# 3. Score de crédito: acima de 700 = aprovado, 500-700 = análise, abaixo = negado
# 4. se aprovado, o limite é 1/3 da renda

nome = input("Digite seu nome: ")
idade = int(input("Idade: "))
renda = float(input("Renda mensal: R$ "))
score = int(input("Score de crédito (0-1000): "))

# verificando requisitos básicos primeiro
idade_ok = 18 <= idade <=75
renda_ok = renda >= 1900

# Verificando se passa nos requisitos básicos
if not idade_ok:
  print(f"\n{nome}, sua solicitação foi NEGADA. ")
  print(f"Motivo: Idade fora do permito (18-75 anos)")

elif not renda_ok:
  print(f"\n{nome}, sua solicitação foi NEGADA. ")
  print(f"Motivo: Renda de R$ {renda:.2f} abaixo do minimo de R$ 1.900,00")

# passou nos requisitos básicos - agora avaliamos o score
else:
  print(f"\n{nome}, requisitos básicos verificados.")

  if score > 700:
    limite = renda * 1/3
    print("Status: APROVADO")
    print(f"Seu limite de crédito é: R$ {limite:.2f}")

  elif score > 500:
    limite = renda * 2
    print("Status: EM ANÁLISE - Aprovação parcial")
    print(f"Limite reduzido: R$ {limite:.2f}")
    print("Nossa equipe entrará em contato em até 24h. ")

  else:
    print("Status: NEGADO por score insuficiente.")
    print(f"Score atual: {score} (mínimo necessário: 500)")
    print("Dica: quite suas dívidas para melhorar o score. ")
