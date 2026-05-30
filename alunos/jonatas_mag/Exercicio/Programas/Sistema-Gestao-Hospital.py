print("=== SISTEMA DE GESTÃO HOPITALAR ===\n")

atendimentos = int(input("Atendimentpo do dia"))

total_atendimentos = 0
emergencia = 0
uti_cti = 0
clinico = 0
cirurgico = 0
pediatra = 0
abstetra = 0
soma_atendimentos = 0
paciente_mais_grave = ""
soma_graves = uti_cti + emergencia
soma_normal = clinico + cirurgico + pediatra + abstetra


print("\n--- CADASTRO DE PACIENTE ---")

for i in range(1, atendimentos + 1):
  print(f"\nAtendimento {i}:")

  nome = input(" Nome: ")
  idade = int(input("Idade: "))
  endereço = input(" Endereço: ")
  altura = float(input("Altura: "))
  peso = float(input(" Peso: "))
  doença = input(" Doença: ")
  sintomas = input(" Sintomas: ")
  pressao = float(input(" Pressão: "))
  glicemia = float(input(" Glicemia: "))
  imc = peso / (altura ** 2)

  if pressao <= 12.8 or glicemia <= 120:
    print(f"Paciente {nome}. Paciente normal. ")
    continue

  total_atendimentos += 1

  situacao_pressao = ""
  if pressao >= 8.6 and pressao < 12.8:
    situacao_pressao = "Normal"
    clinico += 1
  elif pressao >= 12.8 and pressao < 14.10:
    situacao_pressao = "EMERGÊNCIA"
    emergencia += 1
  elif pressao >= 14.10 and pressao < 22.13:
    situacao_pressao = "URGÊNCIA"
    emergencia += 1
  else:
    situacao_pressao = "INTERVENÇÃO"
    uti_cti += 1
  print(f" Condições da Pressão: {pressao:.1f} - {situacao_pressao}")

  situacao_glicemia = ""
  if glicemia >= 80 and glicemia < 130:
    situacao_glicemia = "Normal"
    clinico += 1
  elif glicemia >= 130 and glicemia < 240:
    situacao_glicemia = "DIABETICO"
    clinico += 1
  elif glicemia >= 240 and glicemia < 400:
    situacao_glicemia = "URGÊNCIA"
    emergencia += 1
  else:
    situacao_glicemia = "INTERNAÇÃO"
    uti_cti += 1
  print(f" Condições da glicemia: {glicemia:.1f} - {situacao_glicemia}")

  idoso_ou_jovem = idade < 65
  falecimento_glicemia = glicemia >= 600

  if idoso_ou_jovem and falecimento_glicemia:
    print(f" PESSOA FALECIDA: {nome} ENCAMINHADO AO IML!")

  idoso_ou_jovem = idade < 50
  falecimento_pressao = pressao >= 23.14

  if idoso_ou_jovem and falecimento_pressao:
    print(f" PESSOA FALECIDA: {nome} ENCAMINHADO AO IML!")

print("\n ------- RESUMO --------")

if total_atendimentos == 0:
  print("Nenhum atendimento válido foi processado.")

else:
  print(f"Total de atendimentos processados: {total_atendimentos}")
  print(f"Emegência: {emergencia}")
  print(f"UTI ou CTI: {uti_cti}")
  print(f"Para o Clínico: {clinico}")
  print(f"Para Cirúrgia: {cirurgico}")
  print(f"Para Pedriatra: {pediatra}")
  print(f"Para Abstetração: {abstetra}")
  print(f"\nPaciente mais grave: {nome} Doença: {doença} Pressão: {pressao:.1f} Glicemia: {glicemia:.1f}")

print("=========== OBRIGADO ==========")