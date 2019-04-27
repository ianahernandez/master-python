##Una tupla es una colección  parecida a la lista pero es inmutable ( no se pueden
# modificar sus elementos), se utilizan para asegurarse que los datos no se pueden modificar
#  (no necesariamente los elementos son del mismo tipo)

# =================================
# ======== Declaracion ============
# =================================

tupla = (100,'Hola', [1,2,3,4], -50)

# ==================================
## ==== Acceso a los elemetos ======
# ==================================

# Mediante su índice comenzando desde cero

# el índice '-1' corresponde al ultimo elemento de la colección
tupla[-1]
# >> -50

# Si uno de los elementos es otra tupla se accede tambien mediante el índice,
# por ejemplo, accedemos a:
tupla[2][-1] 
# >> 4 

# ==================================
# ==== Asignacion de valores =======
# ==================================

# No se permite asignar valores a una posicion especifica
# tupla[1] = 20
# >> TypeError: 'tuple' object does not support item assignment


# =================================
# ==== Tamaño de la tupla =========
# =================================

len(tupla)
# >> 4


# ===========================================
#===== Buscar un elemento en la tupla =======
# ===========================================

tupla.index(100) #Devuelve la posicion donde se encuentra el elemento con valor 100 (si hay varios
# devuelve solo el primero, si no se encuentra devuelve error)
# >> 0


# ========================================================
# ==== Contar ocurrencias de un elemento en una tupla ====
# ========================================================

tupla = (100,'Hola', [1,2,3,4], -50,100, -50, 100, 100, 'Hola', 50)
tupla.count('Hola') #Devuelve la cantidad de 'Hola' dentro de la  tupla
# >> 2
tupla.count(100)
# >> 4
tupla.count(3)
# >> 0   (La tupla no contiene un elemento co el valor 3)
