# EXCERCIO 1 ----- Ficha Cadastral
nome_do_Candidato = input ('porfavor digite seu nome: ')
cidade_do_Candidato = input('digite sua cidade onde reside')
profissao_do_Candidato = input('digite a suaprofissao')
idade_do_Candidato = int(input('digite a sua idade'))
salario_atual_do_Candidato = float(input('digite seu salario'))

print(type(nome_do_Candidato))
print(type(cidade_do_Candidato))
print(type(profissao_do_Candidato))
print(type(idade_do_Candidato))
print(type(salario_atual_do_Candidato))

print(f'obrigado pelas informacoes {nome_do_Candidato} {cidade_do_Candidato} {profissao_do_Candidato} {idade_do_Candidato}')
salario_atual_do_Candidato += 300.00
print(f'Voce vai receber {salario_atual_do_Candidato} por seus esforcoes ao longo dos anos')