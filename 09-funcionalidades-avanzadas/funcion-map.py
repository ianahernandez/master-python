#!/usr/bin/python
# -*- coding: utf-8 -*-

# ==============================================================================
#          Funcion MAP
# ==============================================================================
# Recibe una funcion, y una lista y se encarga de aplicar la funcion a todos los elementos 
# de la lista, y retorna un iterable de tipo map.

#EJemplo: Tenemos una lista de numeros
numeros = [2,5,10,23,50,33]

#Creamos una funcion que dobla todos los elementos de la lista

def doblar (numero):
    return numero*2

# Ahora aplicamos la funcion a todos los numeros de la lista
dobles = map(doblar,numeros)
print(map(doblar,numeros))
# >> <map object at 0x7f129bb47cf8>

# Iteramos con la funcion next
print(next(dobles))
# >> 4
print(next(dobles))
# >> 10
print(next(dobles))
# >> 20
print(next(dobles))
# >> 46
print(next(dobles))
# >> 100
print(next(dobles))
# >> 66

# O hacemos cast a una lista
print(list(map(doblar,numeros)))
# >> [4, 10, 20, 46, 100, 66]

# ==============================================================================
#          Funcion MAP con lambda
# ==============================================================================
dobles = map(lambda numero : numero * 2, numeros)
print(list(dobles))
# >> [4, 10, 20, 46, 100, 66]

# ==========   La funcion map, puede aplicar las operciones de una funcion a varias lista siempre que estas tengan la misma longitud ======================

# Por ejemplo
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = [11,12,13,14,15]
#Multiplicamos todos los elementos de a por los de b
print(list(map(lambda a,b : a*b, a,b)))
# >> [6, 14, 24, 36, 50]

#Multiplicamos todos los elementos de a por los de b y por los de c
print(list(map(lambda a,b,c : a*b*c, a,b,c)))
# >> [66, 168, 312, 504, 750]


# ==============================================================================
#          Funcion MAP con objetos
# ==============================================================================

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return "{}, de {} annos".format(self.nombre, self.edad) 

personas = [
    Persona("Juan",35),
    Persona("Marta",16),
    Persona("Eduardo",12),
    Persona("Manuel", 78)
]
# Incrementamos en 1 la edad de todas las personas de la lista
def incrementar(persona):
    persona.edad += 1
    return persona

personas= map(incrementar,personas)
for p in personas:
    print(p)

# Juan, de 36 annos
# Marta, de 17 annos
# Eduardo, de 13 annos
# Manuel, de 79 annos


# Incrementamos en 1 la edad de todas las personas de la lista usando funcion lambda

personas = map(lambda persona: Persona(persona.nombre, persona.edad + 1), personas)
for p in personas:
    print(p)

# Juan, de 36 annos
# Marta, de 17 annos
# Eduardo, de 13 annos
# Manuel, de 79 annos