arancel = 12000

pago = input('efectivo? (S/N): ').lower() == 'si'

if pago() == 'si':
    arancel = arancel * 15/100
else:
    print('No descuento')


print('Arancel de python normal: ', arancel)

print('Arancel de python con descuento: ', pago)