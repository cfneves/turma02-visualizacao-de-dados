# EXERCICIO 2 - Refinado

# Coleta de dados
nome = input("Digite o nome do funcionário: ")
salario_bruto = float(input("Digite o salário bruto do funcionário: "))
horas_extras = int(input("Digite o número de horas extras trabalhadas: "))

# Cálculos
valor_hora_comum = salario_bruto / 220
valor_hora_extra = valor_hora_comum * 1.5
total_horas_extras = horas_extras * valor_hora_extra

# Novo salário bruto (Base + Extras)
salario_total_bruto = salario_bruto + total_horas_extras

# Desconto do INSS (11% sobre o total recebido)
desconto_inss = salario_total_bruto * 0.11

# Salário Final (Líquido)
salario_final = salario_total_bruto - desconto_inss

# Comparações Lógicas
salario_final_maior_3000 = salario_final > 3000
condicao_especial = (horas_extras > 10) and (salario_final > 2000)

# Exibir relatório formatado
print("\n" + "="*30)
print("     RELATÓRIO DE PAGAMENTO     ")
print("="*30)
print(f"Funcionário: {nome}")
print(f"Salário Base:    R$ {salario_bruto:>10.2f}")
print(f"Horas Extras:    R$ {total_horas_extras:>10.2f} ({horas_extras}h)")
print(f"Desconto INSS:   R$ {desconto_inss:>10.2f}")
print("-" * 30)
print(f"SALÁRIO LÍQUIDO: R$ {salario_final:>10.2f}")
print("-" * 30)
print(f"Salário > R$ 3.000,00? {salario_final_maior_3000}")
print(f"Bônus Especial (10h+ e R$ 2k+)? {condicao_especial}")
print("="*30)