nombre = input('Ingrese su nombre completo: ')
edad = input('Ingrese su edad: ')
fecha = input('Ingrese su fecha de nacimiento: ')
titulo = True

cuota = 35000 - ((35000 * 15) / 100) 
matricula= int(input('Ingrese monto de la matrícula: '))
matricula = matricula + 1000

print('--------------------------------------------------')

print('Nombre completo:', nombre)
print('Edad y fecha de nacimiento: ', '(', edad, ')', ' / ', fecha)
print('¿Posee título?: ', titulo)
print('Valor de la matrícula: ', matricula)
print('Valor de la cuota: ', '35000')
print('Valor de la cuota con 15 por ciento de descuento: ', cuota)

