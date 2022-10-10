#Funcion base

# Nombre
# Argumentos
# Codigo
# Retorno

"""
def sumar(a, b):

    resultado = a + b

    return resultado


resultado_sumar = sumar(2, 3)
print(resultado_sumar)
print(sumar(2, 3))

# Funcion 2
def resta():
    resultado = 2 - 3

    return resultado

print(resta())

# Funcion 3
def resta_2():

    print(2-3)


resta_2()

# Funcion saludo

def saludo(nombre):
    print('Hola')

saludo('Juan')


def saludo_dos(nombre):
    print('Hola', nombre)

nombre = input('Ingrese su nombre: ')
saludo_dos(nombre)
nombre = input('Ingrese su nombre: ')
saludo_dos(nombre)

#Funcion Hola DON PEPITO



def saludo_don_pepito(hola_don_pepito):
    print('Hola Don Jose!',hola_don_pepito )

hola_don_pepito = input()
saludo_don_pepito(hola_don_pepito) 






def prueba(a, b, c):
    print(a, b, c)

a = 420
b = 3
c = 5
prueba(b, c, a)

#hay que pasar los parametros en orden

def prueba(a, b, c):
    print(a, b, c)

a = 420
b = 3
c = 5
prueba(a=a, b=b, c=c)

def prueba(a, b, c):
    print(a, b, c)

a = 420
b = 3
c = 5
prueba(b=a, c=b, a=c)

"""

def saludo(cantidad_saludos):

    lista_nombres = []

    # Bucle Ingreso de nombres
    for i in range(cantidad_saludos):

        nombre = input('Ingrese su nombre: ')
        print('Hola', nombre)

        lista_nombres.append(nombre)

    print(lista_nombres)
    return lista_nombres


#cambia el orden
def orden(lista, sentido):

    lista.sort(reverse=sentido)

    return lista

nombres = saludo(int(input('Ingrese la cantidad de saludos a efectuar: ')))
print(
    orden(nombres, True)
)

#no cambia el orden
def orden(lista, sentido):

    lista.sort(reverse=sentido)

    return lista

nombres = saludo(int(input('Ingrese la cantidad de saludos a efectuar: ')))

print(
    orden(nombres, False)
)

