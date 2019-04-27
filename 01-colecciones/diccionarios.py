# Son (junto a las listas) las coleccion mas usadas en python, se basa en una estructura mapeada
# (mapping) donde cada elemento de la coleccion se encuentra indentificado con una clave unica


# =========================================
# ========== Declaracion ==================
# =========================================

# vacío
vacio = {}
type(vacio)
# >> dict

# Con elementos
colores = {
    'amarillo':'yellow',
    'azul':'blue',
    'verde':'green'
}

numeros = {
    0: 'cero',
    1: 'uno',
    2: 'dos',
    3: 'tres'
}


# =========================================
# ======  Acceso a los elementos ==========
# =========================================
colores['amarillo']
# >> 'yellow'

numeros[2]
# >> 'dos'


# =========================================
# ======  Modificar los elementos =========
# =========================================

colores['amarillo'] = 'new yellow'
colores['amarillo']
# >> 'new yellow'

# =========================================
# ======  Eliminar un elemento  ===========
# =========================================
del(colores['amarillo'])
colores
#>> {'azul': 'blue', 'verde': 'green'}

# =======================================================
# ======  Recorrer elementos del diccionario  ===========
# =======================================================


#Imprime solo las claves 
for clave in colores:
    print(clave)
    
""" 
azul
verde 
"""

#Imprime clave con valor
for clave in colores:
    print(clave +':'+colores[clave])
    
""" 
azul:blue
verde:green
"""
#Imprimir clave y valor utilizando la funcion 'items'

for c,v in colores.items():
    print(c,v)

""" 
azul blue
verde green 
"""

# =======================================================
# ======  Combinando Listas con Diccionarios ============
# =======================================================

#Lista
personajes = []

# >>>> Elemento (diccionario) Personaje Gandalf
personaje = {
    'nombre' : 'Gandalf',
    'clase' : 'Mago',
    'raza' : 'Humano'
}
# Agregamos a la lista
personajes.append(personaje)

# >>>>>> Elemento (diccionario) Personaje Legolas
personaje = {
    'nombre' : 'Legolas',
    'clase' : 'Arquero',
    'raza' : 'Elfo'
}
# Agregamos a la lista
personajes.append(personaje)

# >>>>>> Elemento (diccionario) Personaje Gimli
personaje = {
    'nombre' : 'Gimli',
    'clase' : 'Guerrero',
    'raza' : 'Enano'
}
# Agregamos a la lista
personajes.append(personaje)

# >>>>>>> Mostramos los personajes

for p in personajes:
    print(p['nombre'], p['clase'], p['raza'])
    
""" 
Gandalf Mago Humano
Legolas Arquero Elfo
Gimli Guerrero Enano
"""