"""Peça 3 notas ao usuário, calcule a média e informe:
• Média >= 7: "Aprovado"
• Média < 7: "Reprovado"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado, media: {:.2f}".format(media))
else:
    print("Reprovado, media: {:.2f}".format(media))