print("=== SISTEMA DE GESTÃO ESCOLAR ===\n")

quantos_alunos = int(input("Quantos alunos serão cadastrados? "))

total_alunos = 0
aprovados = 0
recuperados = 0
reprovados = 0
soma_medias = 0
maior_media = 0
nome_destaque = ""

print("\n--- Cadastro Aluno ---")

for i in range(1, quantos_alunos + 1):
  print(f"\tAluno {i}:")

  nome = input(" Nome: ")
  idade = int(input("Idade: "))

  nota1 = float(input(" Trimrdtre 1: "))
  nota2 = float(input(" Trimrdtre 2: "))
  nota3 = float(input(" Trimrdtre 3: "))
  nota4 = float(input(" Trimrdtre 4: "))

  if nota1 < 0 or nota2 < 0 or nota3 < 0:
    print(f"Nota inválida para {nome}. Aluno ignorado. ")
    continue

  total_alunos += 1

  media = (nota1 + nota2 + nota3 + nota4) / 4

  soma_medias += media

  if media > maior_media:
    maior_media = media
    nome_destaque = nome

  if media >= 7:
    situacao = "APROVADO"
    aprovados += 1

  elif media >= 5:
    situacao = "RECUPERAÇÃO"
    recuperados += 1

  else:
    situacao = "RECUPERAÇÃO"
    reprovados += 1

  print(f" Média: {media:.1f} - {situacao}")

  jovem = idade < 15
  esta_aprovado = media >= 7

  if jovem and esta_aprovado:
    print(f" DESTAQUE JOVEM: {nome} APROVADO COM EXCELENCIA!")


print("\n ------- RESUMO --------")

if total_alunos == 0:
  print("Nenhum aluno válido foi processado.")

else:
  print(f"Total de alunos processados: {total_alunos}")
  print(f"Aprovados: {aprovados}")
  print(f"Em recuperação: {recuperados}")
  print(f"Reprovado: {reprovados}")
  print(f"\nAluno destaque: {nome_destaque} (Média: {maior_media:.1F})")

  print("\n === MÉDIA GERAL DA TURMA === ")

  media_geral = soma_medias / total_alunos
  print(f"Média geral da turma: {media_geral:.1f}")

  if media_geral < 6:
    print("\n ALERTA: Média geral a baixo de 6:")
    print("Aturma representa risco - reconmenda-se intervenção pedagógica")
  else:
    print("\n Turma com desempenho satisfatória.")

    taxa_aprovacao = (aprovados / total_alunos) * 100
    print(f"Taxa de aprovação: {taxa_aprovacao:.1f}")

print("=========== OBRIGADO ===========")