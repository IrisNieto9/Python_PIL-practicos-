# For
lista = [True, False, 1, 2, 3, 4, 'Hola']

for i in lista:
    print(i)

for i  in 'Python':
    print(i)

lista = []

for i in range(0, 10):
    print(i)

for i in range(5, 10):
    print(i)
#primer parametro marcamos el inicio, segundo parametro el largo y el tercer parametro como queremos que los de a los saltos
for i in range(0, 10, 2):
    print(i)

lista =  []

for i in range(10):
    lista.append(i)

print(lista)

for i in range(3):
    numero_usuario = int(input('Ingrese un numero: '))
    lista.append(numero_usuario)

print(lista)

# Es lo mismo que :

for i in range(3):
    lista.append(int(input('Ingrese un numero: ')))

print(lista)

#que pasa si queremos poner palabras con letras

for i in range(3):

    #Ingreso de datos
    dato_ingreso = input('Ingrese un numero: ')

    #Validacion
    if dato_ingreso.isnumeric():
        lista.append(int(dato_ingreso))

print(lista)

for i in range(3):

    #Ingreso de datos
    dato_ingreso = input('Ingrese un numero: ')

    #Validacion
    if dato_ingreso.isnumeric():
        lista.append(int(dato_ingreso))
    else:
        print('No es un numero')
        break
print(lista)

#While
x = 10

while x > 0:
    print(x)

    x -= 1

#CAJERO

print('\n\n### Hola Amigo ###\n\n')
print('### ¿En que lo puedo ayudar? ###\n\n')
print('### Elija una opcion ###\n\n')
while True:
    print('  1 - DEPOSITO \n')
    print('  2 - EXTRACCION \n')
    print('  3 - TRANSFERENCIA \n')
    print('  4 - SALIR \n')
    opcion = int(input('Ingrese el número de la opción deseada: '))

    if opcion == 1:
        x = int(input('Ingrese el monto a Depositar: '))
    elif opcion == 2:
        x = int(input('Ingrese el monto a Extraer: '))
    elif opcion == 3:
        x = int(input('Ingrese el monto a Transferir: '))
    elif opcion == 4:
        print('Usted Salió')
        break
    else:
        print("El número ingresado no es una opcion")