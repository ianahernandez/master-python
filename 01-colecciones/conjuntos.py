# Un conjunto es una colección desordenada de elementos únicos, se utilizan normalmente para 
# hacer pruebas de pertenencia a grupos y eliminacion de elementos duplicados, tambien soportan operaciones 
# matematicas avanzadas

#==========================
# ===== Declaracion =======
#==========================

# vacío
conjunto = set()
# Con elementos
conjunto = {1,2,3}


#============================
# ==== Añadir elementos =====
#============================

conjunto.add(4)
conjunto
#>> {1,2,3,4}

conjunto.add(0)
conjunto
#>> {0,1,2,3,4}

conjunto.add('H')
conjunto
#>> {1,2,3,4,'H'}


#=====================================
# === Pertenecia en la coleccion =====
#=====================================

grupo = {'Ana', 'Jose', 'Carmen', 'Pedro'}
#Podemos verificar si alguien pertenece al grupo d la siguiente manera:
'Ana' in grupo
# >> True

'Maria' in grupo
# >> False


#=====================================
# === No pertenecia en la coleccion ==
#=====================================

grupo = {'Ana', 'Jose', 'Carmen', 'Pedro'}
#Podemos verificar si alguien NO pertenece al grupo d la siguiente manera:
'Ana' not in grupo
# >> False

'Maria' not in grupo
# >> True


#=====================================
# === Unicidad de los elementos ======
#=====================================

#Intentamos agregar el mismo elemento varias veces en la coleccion
prueba = {'elemento','elemento','elemento','elemento'}
prueba
#>> 'elemento'


#=========================================
# === Transformacion de colecciones ======
#=========================================

# Podemos estar interesados en transformar una lista a un conjunto con el fin de eliminar los
# elementos repetidos
#Lista
l = [1,2,2,2,3,3,3,1]
# Transformamos la lista 'l' a un conjunto 'c'
#Conjunto c
c = set(l)
c
# >> {1,2,3}

# Una vez eliminados los elementos repetidos transformamos la coleccion nuevamente a una lista
# para seguir operando con normalidad

l = list(c)
l
# >> [1,2,3]

# ********** Todo esto se puede hacer con la instruccion
l = list (set(l))

# ******** Cadena de caracteres a conjunto *************
s = "Al pan pan y al vino vino"
set(s)
# >> {'n', 'i', 'o', 'v', 'A', 'p', 'a', ' ', 'y', 'l'}