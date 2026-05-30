print("CAIXA DA LOJA\n")

# Cadastro dos produtos
produto1 = input("Nome do 1º produto: ")
preco1   = float(input(f"Preço do {produto1}: R$ "))

produto2 = input("\nNome do 2º produto: ")
preco2   = float(input(f"Preço do {produto2}: R$ "))

produto3 = input("\nNome do 3º produto: ")
preco3   = float(input(f"Preço do {produto3}: R$ "))

# Cálculo do total
total = preco1 + preco2 + preco3

# Aplicar desconto se total > R$ 100
if total > 100:
    desconto    = total * 0.10
    total_final = total - desconto
    tem_desconto = True
else:
    desconto     = 0
    total_final  = total
    tem_desconto = False

# Exibição do cupom

print("         CUPOM FISCAL")

print(f"  {produto1:<15} R$ {preco1:>7.2f}")
print(f"  {produto2:<15} R$ {preco2:>7.2f}")
print(f"  {produto3:<15} R$ {preco3:>7.2f}")
print(f"  {'Subtotal':<15} R$ {total:>7.2f}")

if tem_desconto:
    print(f"  {'Desconto 10%':<15} R$ -{desconto:>6.2f}")


print(f"  {'TOTAL FINAL':<15} R$ {total_final:>7.2f}")

if tem_desconto:
    print(f"\n🎉 Desconto de 10% aplicado! Você economizou R$ {desconto:.2f} ")
else:
    print(f"\n💡 Gaste mais R$ {100 - total:.2f} para ganhar 10% de desconto!")