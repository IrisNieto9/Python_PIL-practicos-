# CONDICIONALES PYTHON
a = 1
b = 2
r = a + b
type(r)
print(r)

if a >= 0:
    print(a)

if a < b:
    print('A es menor a B')
else:
    print('B es menor a A')

print('final del codigo')

a = 1
b = 2

if a > b:
    print('Ingreso al if')
else:
    print('Ingreso al else')

a = 3
b = 2
c = 5

if a > b:
    print('A > B')

    if a > c:
        print('A es mayor ')

    else:
        print('C > A & C > B')
else:
    print('Ingreso al else')

if a == 3:
    print('a es igual a 3')
else:
    print('A no es igual')

edad_juan = 16

if edad_juan >= 16 and edad_juan >= 18:
    print('Juan puede votar y es mayor de edad')
else:
    print('No se cumple alguna de las condiciones')

if edad_juan >= 16 or edad_juan >= 18:
    print('Juan puede votar y es mayor de edad')
else:
    print('No se cumple alguna de las condiciones')

#Elif
a = 5

if a == 3:
    print('A es igual a 3')
elif a == 4:
    print('A es igual a 4')
elif a == 5:
    print('A es igual a 5')
else:
    print('A no es igual a nada')

# es lo mismo que decir

if a == 3:
    print('A es igual a 3')
if a == 4:
    print('A es igual a 4')
if a == 5:
    print('A es igual a 5')




