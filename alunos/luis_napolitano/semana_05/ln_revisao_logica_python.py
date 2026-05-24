# Meu arquivo somente irá tratar as ativades da ln_revisao)logica_python.ipynb
# Os exercícios jpá realizados em aula serão reescritos, para pratica da digitação e aprendizado do conteúdo.

print("       -- ATIVIDADE - #01 ACOMPANHADA --     ")
print("\n")

# ATIVIDADE ACOMPANHADA 1
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

print("\n")
print("       -- ATIVIDADE - #02 ACOMPANHADA --     ")  
print("\n")


# ATIVIDADE ACOMPANHADA 2
# O forno deve operar entre 160°C e 200°C
# Classifique a temperatura como: Baixa / Normal / Alta

temperatura_forno = 360.5  # Mude esse valor para testar!

# TODO: Complete as condições abaixo
if temperatura_forno < 160:       # TODO: condição para BAIXA
    print("🔵 Temperatura BAIXA — aquecer forno")
elif temperatura_forno <= 200:    # TODO: condição para NORMAL
    print("✅ Temperatura NORMAL — produção liberada")
else:
    print("🔴 Temperatura ALTA — risco de queima das peças")

print("\n")
print("       -- ATIVIDADE - #03 ACOMPANHADA --     ")  
print("\n")

# ATIVIDADE ACOMPANHADA 3

temperaturas = [182.5, 179.3, 185.1, 183.8, 180.0, 178.5, 184.2, 246.0, 362.5, 192, 100]

                                    # TODO: Complete o código abaixo
soma = 0
leituras_altas = 0                  # temperaturas acima de 184°C

for temp in temperaturas:
    soma += temp                    # TODO: acumule a soma
    if temp > 184:
        leituras_altas += 1         # TODO: conte leituras acima de 184°C

media = soma / len(temperaturas)    # TODO: calcule a média

print(f"Total de leituras: {len(temperaturas)}")
print(f"Soma: {soma:.1f}°C")
print(f"Média: {media:.2f}°C")


print("\n")
print("       -- ATIVIDADE - #04 ACOMPANHADA --     ")  
print("\n")


# ATIVIDADE ACOMPANHADA 4
# OEE = Disponibilidade × Performance × Qualidade × 100
# Cada fator vai de 0 a 1 (ex: 0.85 = 85%)

def calcular_oee(disponibilidade, performance, qualidade):
    """
    Calcula o OEE (Overall Equipment Effectiveness)
    
    Parâmetros:
        disponibilidade: tempo disponível / tempo planejado (0 a 1)
        performance: velocidade real / velocidade ideal (0 a 1)
        qualidade: peças boas / total produzido (0 a 1)
    """
    # TODO: calcule o OEE
    oee = disponibilidade * performance * qualidade * 100
    return oee


# Testando a função
oee_resultado = calcular_oee(
    disponibilidade=0.90,       # máquina disponível 90% do tempo
    performance=0.95,           # operando a 95% da velocidade ideal
    qualidade=0.98              # 98% de peças boas
)

print(f"OEE calculado: {oee_resultado:.1f}%")

# OEE de classe mundial é ≥ 88%
if oee_resultado >= 88:
    print("🏆 Equipamento de CLASSE MUNDIAL!")
else:
    print("📈 Há oportunidade de melhoria")

print("\n")
print("       -- ATIVIDADE - #01 INDIVIDUAL --     ")  
print("\n")

# ============================================================
# ATIVIDADE INDIVIDUAL 1 — Calculadora de Salário
# ============================================================
# 
# ENUNCIADO:
# Um operador recebe R$ 18,50 por hora normal.              # (ht = 18.50)
# Horas extras (acima de 44h semanais) valem 50% a mais.    # (he = ht * 1.5)
#
# Crie um programa que:
# 1. Peça o nome do funcionário                             # input - string para nome do funcionário
# 2. Peça as horas trabalhadas na semana                    # input - float para horas trabalhadas semanais
# 3. Calcule o salário semanal (com horas extras se houver) # criar condicional para he se ht > 44
# 4. Exiba um comprovante formatado                         # exibir saida
#
# DICA:
# - Salário normal = horas normais x R$ 18,50
# - Horas extras = horas trabalhadas - 44 (se > 44)
# - Valor hora extra = 18,50 x 1,5
# ============================================================

# SEU CÓDIGO AQUI:

#informações fixadas pelo exercicio

"""
vlr_hr = 18.50
vlr_hr_extra = vlr_hr * 1.5

# Informações prestadas pelo usuário

nome_func = input("Nome do funcionário: ")
hr_trab_sem = float(input("Horas trabalhadas na semana: "))
"""


"""
# ============================================================
# 📝 ATIVIDADE INDIVIDUAL 1 — Calculadora de Salário
# ============================================================

# Pedindo o nome do funcionário
nome = input("Digite o nome do funcionário: ")

# Pedindo as horas trabalhadas
horas_trabalhadas = float(input("Digite as horas trabalhadas na semana: "))

# Valor da hora normal
valor_hora = 18.50

# Limite semanal sem hora extra
limite_horas = 44

# Verificando se houve hora extra
if horas_trabalhadas > limite_horas:
    
    # Calculando horas normais
    horas_normais = limite_horas
    
    # Calculando horas extras
    horas_extras = horas_trabalhadas - limite_horas
    
    # Calculando valor da hora extra
    valor_hora_extra = valor_hora * 1.5
    
    # Calculando salário normal
    salario_normal = horas_normais * valor_hora
    
    # Calculando salário extra
    salario_extra = horas_extras * valor_hora_extra
    
    # Calculando salário total
    salario_total = salario_normal + salario_extra

else:
    
    # Quando não existe hora extra
    horas_normais = horas_trabalhadas
    horas_extras = 0
    
    # Calculando salário total
    salario_total = horas_normais * valor_hora

# Exibindo comprovante
print("\n========== COMPROVANTE ==========")
print(f"Funcionário: {nome}")
print(f"Horas trabalhadas: {horas_trabalhadas:.1f}h")
print(f"Horas extras: {horas_extras:.1f}h")
print(f"Salário semanal: R$ {salario_total:.2f}")
print("=================================")

"""


# Pedindo o nome do funcionário
nome = input("Digite o nome do funcionário: ")

# Pedindo as horas trabalhadas
horas_trabalhadas = float(input("Digite as horas trabalhadas na semana: "))

# Valor da hora normal
valor_hora = 18.50

# Valor da hora extra
valor_hora_extra = valor_hora * 1.5

# Limite semanal sem hora extra
limite_horas = 44

if horas_trabalhadas < 0:
    print("Você deve digitar um valor válido.")
    horas_extras = 0

elif horas_trabalhadas <= limite_horas:
    salario_total = horas_trabalhadas * valor_hora
    horas_extras = 0
else:
    horas_extras = horas_trabalhadas - limite_horas
    salario_total = (limite_horas * valor_hora) + ((horas_trabalhadas - limite_horas) * valor_hora_extra)
    

# Exibindo comprovante
print("\n========== COMPROVANTE ==========")
print(f"Funcionário: {nome}")
print(f"Horas trabalhadas: {horas_trabalhadas:.1f}h")
print(f"Horas extras: {horas_extras:.1f}h")
print(f"Salário semanal: R$ {salario_total:.2f}")
print("=================================")


print("\n")
print("       -- ATIVIDADE - #02 INDIVIDUAL --     ")  
print("\n")

## Atividade Individual 2 — Verificador de Lote

# ============================================================
# ATIVIDADE INDIVIDUAL 2 — Verificador de Lote
# ============================================================
#
# ENUNCIADO:
# Um lote de peças passa pelo controle de qualidade.
# Você tem a lista de medições de diâmetro (em mm) abaixo.
# A especificação permite entre 49.8mm e 50.2mm.
#
# Crie um programa que:
# 1. Percorra a lista de medições                               # encontrar funçao para percorrer a lista de medições
# 2. Conte quantas peças estão DENTRO e FORA da especificação   # criar contador de peças len
# 3. Calcule o percentual de aprovação                          # calcular percentual de aprovação  
# 4. Classifique o lote:                                        # criar a condicional para classificar o lote (peça a peça)
#    - Aprovado: aprovação >= 98%
#    - Aprovado c/ ressalvas: entre 95% e 97.9%
#    - Reprovado: < 95%
# ============================================================

# medicoes = [50.1, 49.9, 50.0, 50.3, 49.7, 50.2, 50.1, 49.8,
#            50.0, 50.1, 49.6, 50.2, 50.0, 49.9, 50.1, 50.4,
#            49.8, 50.0, 50.1, 49.9]

# especificacao_min = 49.8
# especificacao_max = 50.2

medicoes = [50.1, 49.9, 50.0, 50.3, 49.7, 50.2, 50.1, 49.8,
            50.0, 50.1, 49.6, 50.2, 50.0, 49.9, 50.1, 50.4,
            49.8, 50.0, 50.1, 49.9]

especificacao_min = 49.8
especificacao_max = 50.2

dentro_especif = 0
fora_especif = 0
 

for diametro in medicoes:
    if especificacao_min <= diametro <= especificacao_max:
        dentro_especif += 1
    else:
        fora_especif += 1

total_pecas = len(medicoes)
perc_aprovadas = (dentro_especif / total_pecas) * 100



if perc_aprovadas >= 98:
    classificacao = "APROVADO"
elif perc_aprovadas >= 95:
    classificacao = "APROVADO COM RESSALVAS"
else:
    classificacao = "REPROVADO"

print("============== RELATORIO DE LOTE ==============")
print(f"Peças aprovadas: {dentro_especif}")
print(f"Peças não aprovadas: {fora_especif}")
print(f"Percentual de aprovação: {perc_aprovadas:.2f}%")
print(f"Classificação do lote: {classificacao}")


print("\n")
print("       -- ATIVIDADE - #03 INDIVIDUAL --     ")  
print("\n")

##  Atividade Individual 3 — Função de Conversão

# ============================================================
# ATIVIDADE INDIVIDUAL 3 — Funções de Conversão de Unidades
# ============================================================
#
# ENUNCIADO:
# Na indústria trabalhamos com diferentes unidades de medida.
# Crie um programa com FUNÇÕES para converter:
#
# a) Temperatura: Celsius ↔ Fahrenheit                          # criar funcoes para conversao de C-> f e f ->C
#    F = (C × 9/5) + 32
#    C = (F - 32) × 5/9
#
# b) Pressão: bar → PSI e PSI → bar                             # criar funcoes para conversao de b-> P e P -> b
#    1 bar = 14.504 PSI
#
# c) Velocidade: m/s → km/h e km/h → m/s                        # criar funcoes para conversao de m-> K e K -> m
#    1 m/s = 3.6 km/h
#
# Depois crie um menu simples com while para o usuário
# escolher qual conversão fazer.
# ============================================================

# Criando as funcões para conversão 

def celsius_p_fahrenheit(cels):
    fahrenheit = (cels * 9/5) + 32
    return fahrenheit

def fahrenheit_p_celsius(fahr):
    celsius = (fahr - 32) * 5/9
    return celsius

def bar_p_psi(bar):
    psi = bar * 14.504
    return psi

def psi_p_bar(psi):
    bar = psi / 14.504
    return bar

def m_s_p_km_h(metsgund):
    km_h = metsgund * 3.6
    return km_h

def km_h_p_m_s(kmhora):
    m_s = kmhora / 3.6
    return m_s

# Após definidas as funcoes de conversao criaremos o "while" par criacao das opcoes de ecolha

while True:
    print("\nEscolha a conversão que deseja realizar:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Bar para PSI")
    print("4. PSI para Bar")
    print("5. m/s para km/h")
    print("6. km/h para m/s")
    print("0. Sair")

    opcao = input("Digite o número da opção de conversão: ")

    if opcao == "1":
        c = float(input("Insira a temperatura em Celsius (0.00): "))
        f = celsius_p_fahrenheit(c)
        print(f"{c}°C é igual a {f:.2f}°F")

    elif opcao == "2":
        f = float(input("Insira a temperatura em Fahrenheit (0.00): "))
        c = fahrenheit_p_celsius(f)
        print(f"{f}°F é igual a {c:.2f}°C")

    elif opcao == "3":
        bar = int(input("Insira a pressão em Bar (0): "))
        psi = bar_p_psi(bar)
        print(f"{bar} Bar é igual a {psi:.2f} PSI")

    elif opcao == "4":
        psi = float(input("Insira a pressão em PSI (0.00): "))
        bar = psi_p_bar(psi)
        print(f"{psi} PSI é igual a {bar:.0f} Bar")

    elif opcao == "5":
        m_s = float(input("Insira a velocidade em m/s (0.00): "))
        km_h = m_s_p_km_h(m_s)
        print(f"{m_s} m/s é igual a {km_h:.2f} km/h")

    elif opcao == "6":
        km_h = float(input("Insira a velocidade em km/h (0.00): "))
        m_s = km_h_p_m_s(km_h)
        print(f"{km_h} km/h é igual a {m_s:.2f} m/s")

    elif opcao == "0":
        print("Encerrando o programa.")
        break

    else:
        print("Opção NÃO válida. Por favor, tente novamente.")

input("\n Pressione 'Enter' para finalizar")


print("\n")
print("       -- ATIVIDADE - #01 GRUPO - MAS FOI INDIVIDUAL --     ")  
print("\n")

# ============================================================
# 👥 ATIVIDADE EM GRUPO 1 — Sistema de Registro de Produção
# ============================================================
#
# ENUNCIADO:
# Vocês devem criar um mini-sistema de registro de produção.
# O sistema deve:
#
# 1. Usar um while para manter o programa rodando
# 2. Apresentar um menu com as opções:
#    [1] Registrar produção de um turno
#    [2] Ver todos os registros
#    [3] Ver estatísticas (total, maior, menor, média)
#    [4] Sair
#
# 3. Armazenar os registros em uma lista de dicionários
# 4. Cada registro deve conter:
#    - nome do operador
#    - turno (Manhã/Tarde/Noite)
#    - quantidade produzida
#    - quantidade com defeito
#    - taxa de defeito (calculada automaticamente)
#
# DICA: Dividam as tarefas! Uma pessoa faz o menu,
#       outra faz o registro, outra faz as estatísticas.
# ============================================================

# CÓDIGO DO GRUPO AQUI:
"""
registros = []

def registrar_produtos():
	nome = input("Digite o nome do usuário: ")
	
	while True:
		turno = input("Escreva o turno ('Matutino', 'Vespertino', 'Noturno')").strip().capitalize()
		
        if turno in ["Matutino", "Vespertino", "Noturno"]:
            break
        else:
        	print("Turno NÃO válido. Redigite corretamente.")
	try:
		qtde_produzida = int(input("Qtde produzida: "))
		qtde_defeito = int(input("Qtde com defeito"))
	except ValueError:
		print("Erro: Insira números inteiros válidos.")
		return
	
	if qtde_produzida > 0:
		tx_defeito = (qtde_defeito / qtde_produzida) * 100
	else:
		tx_defeito = 0.0
          
"""

# ============================================================
# 👥 ATIVIDADE EM GRUPO 1 — Sistema de Registro de Produção
# ============================================================

registros = []  # lista para armazenar os registros

def reg_producao():
    nome = input("Insira o nome do operador: ").strip()
    
    while True:
        turno = input("Turno (Manhã/Tarde/Noite): ").strip().capitalize()
        if turno in ["Manhã", "Tarde", "Noite"]:
            break
        print("Turno inválido! Digite Manhã, Tarde ou Noite.")
    
    try:
        qtde_produzida = int(input("Insira a qtde produzida: "))
        qtde_defeito = int(input("Insira a qtde com defeito: "))
    except ValueError:
        print("Erro: Por favor, insira números inteiros válidos para as quantidades.")
        return

    if qtde_produzida > 0:
        taxa_defeito = (qtde_defeito / qtde_produzida) * 100
    else:
        taxa_defeito = 0.0

    # Criação do dicionário e armazenamento na lista
    novo_registro = {
        "operador": nome,
        "turno": turno,
        "quantidade_produzida": qtde_produzida,
        "quantidade_defeito": qtde_defeito,
        "taxa_defeito": taxa_defeito
    }
    
    registros.append(novo_registro)
    print("\n✅ Registro adicionado com sucesso!")


def ver_registros():
    print("\n--- TODOS OS REGISTROS ---")
    if not registros:
        print("Nenhum registro encontrado.")
        return

    # Cabeçalho formatado para parecer uma tabela no terminal
    print(f"{'Operador':<15} | {'Turno':<8} | {'Produzido':<10} | {'Defeito':<8} | {'Taxa Defeito':<12}")
    print("-" * 62)
    
    for r in registros:
        print(f"{r['operador']:<15} | {r['turno']:<8} | {r['quantidade_produzida']:<10} | {r['quantidade_defeito']:<8} | {r['taxa_defeito']:.2f}%")


def ver_estatisticas():
    print("\n--- ESTATÍSTICAS DA PRODUÇÃO ---")
    if not registros:
        print("Sem dados suficientes para calcular estatísticas.")
        return

    # Criando listas auxiliares para facilitar os cálculos matemáticos
    producoes = [r['quantidade_produzida'] for r in registros]
    defeitos = [r['quantidade_defeito'] for r in registros]
    
    total_produzido = sum(producoes)
    total_defeito = sum(defeitos)
    maior_producao = max(producoes)
    menor_producao = min(producoes)
    media_producao = total_produzido / len(registros)
    
    # Taxa de defeito global da fábrica
    taxa_global_defeito = (total_defeito / total_produzido * 100) if total_produzido > 0 else 0

    print(f"Total produzido (geral): {total_produzido} unidades")
    print(f"Total com defeito (geral): {total_defeito} unidades")
    print(f"Média de produção por turno: {media_producao:.2f} unidades")
    print(f"Maior produção registrada: {maior_producao} unidades")
    print(f"Menor produção registrada: {menor_producao} unidades")
    print(f"Taxa de defeito global: {taxa_global_defeito:.2f}%")


# Menu principal
while True:
    print("\n" + "="*40)
    print("      SISTEMA DE REGISTRO DE PRODUÇÃO")
    print("="*40)
    print("[1] Registrar produção de um turno")
    print("[2] Ver todos os registros")
    print("[3] Ver estatísticas (total, maior, menor, média)")
    print("[4] Sair")
    print("="*40)
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
        reg_producao()
    elif opcao == '2':
        ver_registros()
    elif opcao == '3':
        ver_estatisticas()
    elif opcao == '4':
        print("\nEncerrando o sistema de produção. Bom trabalho!")
        break
    else:
        print("\n Opção inválida! Escolha um número de 1 a 4.")
    
    # Pausa para o usuário ler o resultado antes do menu reaparecer
    input("\nPressione Enter para continuar...")