# Iniciando antes do loop
total_cadastros = 0
qnt_aprovados = 0
recuperacao = 0
reprovados = 0
soma_medias_turma = 0
maior_media = 0
nome_maior_media = ""

# Número de alunos
qnt_alunos = int(input("Quantos alunos serão cadastrados? "))

# Cadastro de alunos
for i in range(qnt_alunos):
    # Pedindo os dados
    nome = input(f"\nDigite o nome do {i+1}º aluno: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Validar nota negativa
    if nota1 < 0 or nota2 < 0 or nota3 < 0:
        print("Nota inválida! Pulando processamento deste aluno.")
        continue

    # Cálculos
    media = (nota1 + nota2 + nota3) / 3
    total_cadastros += 1
    soma_medias_turma += media

    # Classificação
    if media >= 7:
        print(f"O aluno {nome} foi aprovado com média {media:.2f}.")
        qnt_aprovados += 1
    elif 5 <= media < 7:
        print(f"O aluno {nome} está em recuperação com média {media:.2f}.")
        recuperacao += 1
    else:
        print(f"O aluno {nome} foi reprovado com média {media:.2f}.")
        reprovados += 1

    # Verificar destaque
    if idade < 15 and media >= 7:
        print(f"Aluno destaque. Parabéns!")

    # Maior média da turma
    if media > maior_media:
        maior_media = media
        nome_maior_media = nome

# Cálculo da média da turma
if total_cadastros > 0:
    media_turma = soma_medias_turma / total_cadastros
else:
    media_turma = 0

# RELATÓRIO
print("\n" + "="*30)
print("          RELATÓRIO         ")
print("="*30)
print(f"Total de alunos cadastrados: {total_cadastros}")
print(f"Quantidade de alunos aprovados: {qnt_aprovados}")
print(f"Quantidade de alunos em recuperação: {recuperacao}")
print(f"Quantidade de alunos reprovados: {reprovados}")
print(f"Média da turma: {media_turma:.2f}")
print(f"Aluno com maior média: {nome_maior_media} com média {maior_media:.2f}")

# Alerta Risco
if media_turma < 6 and total_cadastros > 0:
    print(f"\n⚠️ ATENÇÃO: Turma em risco!")