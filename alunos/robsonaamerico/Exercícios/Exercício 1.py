#Criando os inputs para o usuário preencher as informações solicitadas
(input("Digite seu nome: "))
(input("Digite sua cidade: ")) 
(input("Digite sua profissão: "))
(input("Digite seu idade: "))
(input("Digite seu salaário: "))

#Criando os types de variáveis para cada informação solicitada
nome = str (input("Digite seu nome: "))
cidade = str (input("Digite sua cidade: "))
profissão = str (input("Digite sua profissão: "))
idade = int (input("Digite sua idade: "))
salário = float (input("Digite seu salário: "))

#Criando as f-strings para exibir as informações do usuário
f-string = f(("Olá, {nome}! Você é de {cidade} e trabalha como {profissão}. Você tem {idade} anos e ganha R${salário:.2f} por mês."))
f-string = f("Daqui a 3 anos seu salario será de R${salário + 900:.2f}.")