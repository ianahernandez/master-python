# Simuladas con listas


#================================================================================================
# ================================== P I L A S ==================================================
#================================================================================================

# Pila: coleccion de elementos ordenas que permite dos acciones: Añadir, sacar un elemento
# push, pop. Estrutura LIFO

#==========================
# ===== Declaracion =======
#==========================

pila = [3,4,5]

#===================================
# === Añadir (push | append)========
#===================================

pila.append(7)

pila.append(6)

pila

# >> [3,4,5,7,6]

#==========================
# ===== Sacar (pop) =======
#==========================

#Elimina el último elemento de la pila y devuelve su valor

pila.pop()

# >> 6
pila.pop()

# >> 7
pila.pop()

# >> 5

# *** No se puede utilizar pila.pop() si la misma se encuentra vacía.

#================================================================================================
# ================================== C O L A S ==================================================
#================================================================================================

# Colas: coleccion de elementos con estructura FIFO.

#================================
# ===== Importar librería =======
#================================

from collections import deque

#==========================
# ===== Declaracion =======
#==========================

cola = deque()

# Recibe una lista

cola = deque(['Hector', 'Ana', 'Andres', 'Carmen'])

#===================================
# === Añadir (push | append)========
#===================================

cola.append('Maria')

cola.append('Pedro')

cola

# >> deque(['Hector', 'Ana', 'Andres', 'Carmen', 'Maria', 'Pedro'])

#==========================
# === Sacar (popleft) =====
#==========================

#cola.popleft() elimina el primer elemento de la cola y devuelve su valor
# .popleft() es propio de la librería deque

cola.popleft()
# >> 'Hector

cola
#>> deque(['Ana', 'Andres', 'Carmen', 'Maria', 'Pedro'])

# *** No se puede utilizar cola.pop() si la misma se encuentra vacía.
