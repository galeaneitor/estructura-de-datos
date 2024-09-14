nombre = input('Ingrese su nombre completo: ')
edad = input('Ingrese su edad: ')
nacimiento = input('Ingrese su fecha de nacimiento: ')
matricula = int(input('Ingrese monto de la matrícula: '))
titulo = True

cuota = matricula + 1000

arancel = 12000 - ((12000 * 15) / 100)

print('')

print('Su nombre completo es:', nombre)
print('Su edad ingresada es:', edad)
print('Nació el: ', nacimiento)
print('El monto de la matrícula es: ', matricula)
print('La cuota mensual es: ', cuota)
print('¿Posee título?: ', titulo)
print('El valor del arancel es 12000, y con un descuento del 15%, es de: ', arancel)