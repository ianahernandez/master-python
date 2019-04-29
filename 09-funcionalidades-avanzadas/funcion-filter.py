#!/usr/bin/python
# -*- coding: utf-8 -*-

# ==============================================================================
#          Funcion filter
# ==============================================================================
# A partir de una lista o iterador y una funcion condicional es capaz de devolver una
# nueva coleccion con los elementos filtrados, es decir los que cumplen la condicion.
# El tipo de retorno es un objeto filter la cual es iterable.

#Por ejemplo: partiendo de una lista de numeros:
numeros = [2,5,10,23,50,33]

# Filtrar los multiplos de 5
#Funcion condicional

def multiplo_cinco(numero):
    if(numero % 5 == 0):
        return True

# Cuando un numero pase por la funcion y esta devuelva True, el mismo persistira en la lista
# es dcir, se devolvera para que forme parte de la nueva lista filtrada

print(filter(multiplo_cinco,numeros)) # El tipo de retorno es filter, pero es posible hacer un cast para
# convertirlo en una lista

print(list(filter(multiplo_cinco,numeros))) 
#>> [5, 10, 50]

# ======== Con funcion anonima ===============
#Permite realizar la misma funcion, sin declarar nuevas funciones condicionales, que solo ocupan espacio
# en memoria

print(list(filter(lambda numero : numero % 5 == 0, numeros)))
#>> [5, 10, 50]
#
#
# ==============================================================================
#          Filtral Objetos
# ==============================================================================
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return "{}, de {} años".format(self.nombre, self.edad) 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return "{}, de {} años".format(self.nombre, self.edad) 

personas = [
    Persona("Juan",35),
    Persona("Marta",16),
    Persona("Eduardo",12),
    Persona("Manuel", 78)
]

personas = [
    Persona("Juan",35),
    Persona("Marta",16),
    Persona("Eduardo",12),
    Persona("Manuel", 78)
]

print(personas)
#>> [<__main__.Persona instance at 0x7fdeca63f830>, <__main__.Persona instance at 0x7fdeca63f878>, <__main__.Persona instance at 0x7fdeca63f8c0>, <__main__.Persona instance at 0x7fdeca63f908>]

# Filtrar las personas, obteniendo solo las menores de edad

menores = filter(lambda persona : persona.edad < 18, personas)
for menor in menores:
    print(menor)

#Marta, de 16 annos
#Eduardo, de 12 annos