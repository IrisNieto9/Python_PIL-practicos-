# Clase

class Animal:

    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self, sonido):
        print(sonido)



class Perro(Animal):

    #Atributos de clase == global
    #especie = 'mamiferos'

    def __init__(self, nombre, raza, especie, edad):
        #Atributos de instancias == locales
        self.nombre = nombre
        self.raza = raza
        super().__init__(especie, edad)
    #Metodos
    """
    def ladrar(self):
       print('Guau')

    def jugar(self, objeto):
        print('El perro esta jugando con ', objeto)

    def saludar(self):
        print('Guau, mi nombre es', self.nombre)
    """

    def saludar(self):
        print(f'{self.nombre} dio la pata')


"""
perro_1 = Perro('Rex', 'Collie')
print(f'Perro_1 -> {perro_1.nombre}, {perro_1.raza}, {perro_1.especie}')
perro_1.ladrar()
perro_1.jugar('Pelota')
perro_1.saludar()



perro_2 = Perro('Ana', 'Collie')
print(f'Perro_2 -> {perro_2.nombre}, {perro_2.raza}, {perro_2.especie}')
perro_2.saludar()
"""

perro_1 = Perro('Firulais', 'Salchicha', 'Perro', '5')
print(f'Perro_1 -> {perro_1.nombre}, {perro_1.raza}, {perro_1.especie}, {perro_1.edad}')
perro_1.saludar()
