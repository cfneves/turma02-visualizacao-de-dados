def preco_final(preco, **adicionais):
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1- adicionais ['desconto'])
        print(f'Você teve um desconto de {adicionais["desconto"]*100}%')
    if 'garantia_extra' in adicionais:
            preco += adicionais['garantia_extra']
            print(f'Você adicionou uma garantia extra de R${adicionais["garantia_extra"]}')
    if 'imposto' in adicionais:
        preco *= (1+ adicionais['imposto'])
        print(f'Você pagou {adicionais["imposto"]*100}% de imposto')
        return preco
print(preco_final(1000, desconto=0.1, garantia_extra=200, imposto=0.3))