# Revisão de Lógica de Programação em Python 
# Ministrado pelo professor Claudio F Neves
print("  ")
print(" ---------------- ----------------- ----------------- ")
print("  ")

print("Bloco 1 - Revisão")
# Inicial - Bloco 1
print("Olá, turma de Análise de Dados do SENAI!")
print("Bem-vindos ao mundo do Python! 🐍")

print("  ")
print(" ---------------- ----------------- ----------------- ")
print("  ")


print("Bloco 2 - Variáveis e Tipos de Dados")
print("  ")

#Variáeis e Tipos de Dados - Bloco 2
# =============================================
# 🏭 CENÁRIO: Dados de uma linha de produção
# =============================================

# Variáveis do tipo int (inteiro)
pecas_produzidas = 1500
pecas_com_defeito = 37
numero_operadores = 8

# Variáveis do tipo float (decimal)
temperatura_forno = 182.5
velocidade_esteira = 0.75  # metros por segundo

# Variáveis do tipo str (texto)
nome_produto = "Engrenagem Tipo A"
turno = "Manhã"
data_producao = "2025-05-19"

# Variáveis do tipo bool (verdadeiro ou falso)
linha_ativa = True
manutencao_pendente = False

# Exibindo os dados
print("=== RELATÓRIO DA LINHA DE PRODUÇÃO ===")
print(f"Produto: {nome_produto}")
print(f"Turno: {turno}")
print(f"Data: {data_producao}")
print(f"Peças produzidas: {pecas_produzidas}")
print(f"Peças com defeito: {pecas_com_defeito}")
print(f"Temperatura do forno: {temperatura_forno}°C")
print(f"Linha ativa: {linha_ativa}")

print("...")

# Descobrindo o TIPO de uma variável com type()
print(type(pecas_produzidas))   # int
print(type(temperatura_forno))  # float
print(type(nome_produto))       # str
print(type(linha_ativa))        # bool

print("  ")
print(" ---------------- ----------------- ----------------- ")
print("  ")

# ✏️ ATIVIDADE ACOMPANHADA 1
# Preencha as variáveis com dados de uma linha de produção fictícia

meu_produto = "Pizza Quatro Queijos"    # TODO: coloque o nome de um produto industrial
meu_turno = "Noturno"                   # TODO: "Manhã", "Tarde" ou "Noite"
minhas_pecas = 20                       # TODO: coloque uma quantidade de peças produzidas
minha_temperatura = 400.5               # TODO: coloque uma temperatura em graus Celsius
linha_funcionando = True                # TODO: a linha está ativa? True ou False

print(f"Produto: {meu_produto}")
print(f"Turno: {meu_turno}")
print(f"Peças: {minhas_pecas}")
print(f"Temperatura: {minha_temperatura}°C")
print(f"Linha funcionando: {linha_funcionando}")

print("  ")
print(" ---------------- ----------------- ----------------- ")
print("  ")

print("Bloco 3 - Operadores e Expressões")
print("  ")

# =============================================
# 🏭 CENÁRIO: Calculando indicadores de produção
# =============================================

pecas_produzidas = 1500
pecas_com_defeito = 37
horas_trabalhadas = 8
numero_operadores = 6
custo_por_peca = 12.50  # reais

# Peças boas
pecas_boas = pecas_produzidas - pecas_com_defeito
print(f"Peças boas: {pecas_boas}")

# Taxa de defeito (em %)
taxa_defeito = (pecas_com_defeito / pecas_produzidas) * 100
print(f"Taxa de defeito: {taxa_defeito:.2f}%")

# Produtividade por operador
produtividade = pecas_produzidas / numero_operadores
print(f"Peças por operador: {produtividade:.1f}")

# Produção por hora
pecas_por_hora = pecas_produzidas / horas_trabalhadas
print(f"Peças por hora: {pecas_por_hora:.1f}")

# Faturamento do turno
faturamento = pecas_boas * custo_por_peca
print(f"Faturamento do turno: R$ {faturamento:,.2f}")


print(" ---------------- ----------------- ----------------- ")


# Operadores de comparação — retornam True ou False
print("=== COMPARAÇÕES ===")
print(f"1500 > 1000? {1500 > 1000}")    # Maior que
print(f"37 < 50? {37 < 50}")            # Menor que
print(f"taxa_defeito <= 5? {taxa_defeito <= 5.0}")  # Menor ou igual
print(f"turno == 'Tarde'? {'Manhã' == 'Tarde'}")   # Igual
print(f"turno != 'Tarde'? {'Manhã' != 'Tarde'}")   # Diferente

print("  ")
print(" ---------------- ----------------- ----------------- ")
print("  ")

print("Bloco 4 - Input")
print("  ")

# =============================================
# 🏭 CENÁRIO: Coletor de dados de produção
# =============================================

print("=== REGISTRO DE PRODUÇÃO ===")

operador = input("Nome do operador: ")
produto = input("Nome do produto: ")
pecas = int(input("Quantidade de peças produzidas: "))    # convertendo para int
defeitos = int(input("Quantidade de peças com defeito: "))

taxa = (defeitos / pecas) * 100

print("\n--- RESUMO DO REGISTRO ---")
print(f"Operador: {operador}")
print(f"Produto: {produto}")
print(f"Total produzido: {pecas}")
print(f"Defeituosos: {defeitos}")
print(f"Taxa de defeito: {taxa:.2f}%")

# 🔷 Bloco 5 — Estruturas Condicionais (`if`, `elif`, `else`)

