#Metodos simploes

conjunto = set()

#Agregar elementos
conjunto.add(2)
conjunto.add(1)
conjunto.add(3)

print(conjunto)
#>> {1,2,3}

#Eliminar un elemento
conjunto.discard(1)
print(conjunto)
#>> {2,3}
conjunto.add(1)

#Copiar un conjunto en otro
c2 = conjunto.copy()
print(c2)
#>> {1,2,3}

#Vaciar
c2.clear()
print(c2)
#>> set()

# ==============================================================================
#           Otras comprobaciones
# ==============================================================================
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

# Verificar si son disjuntos
print(c1.isdisjoint(c3))
#>> True -----> Ya que no hay elementos comunes
print(c1.isdisjoint(c2))
#>> False -----> Ya que hay un elemento comun

# Verificar si un conjunto es subconjunto de otro
print(c2.issubset(c4))
#>> True -----> Ya que todos los elementos de c2 estan contenidos en c4
print(c1.issubset(c4))
#>> True -----> Ya que todos los elementos de c1 estan contenidos en c4
print(c3.issubset(c4))
#>> False -----> Ya que ningun elemento de c3 esta contenido en c4

# Verificar si un conjunto contiene a otro
print(c4.issuperset(c1))
#>> True -----> Ya que c4 contiene a todos elementos de c1
print(c4.issuperset(c2))
#>> True -----> Ya que c4 contiene a todos elementos de c2
print(c4.issuperset(c3))
#>> False ----->  Ya que c4 NO contiene a todos elementos de c3

# ==============================================================================
#           Operacines avanzadas
# ==============================================================================
# Union de conjuntos SIN MODIFICAR ORIGINALES
print(c1.union(c2))
#>> {1,2,3,4,5}
print(c1.union(c2) == c4)
#>> True

# Union de conjuntos  MODIFICANDO EL PRIMER CONJUNTO ORIGINAL
c1.update(c2)
print(c1)
#>> {1,2,3,4,5}

c1 = {1,2,3}

#Encontrar elementos no comunes de dos conjuntos
print(c1.difference(c2))
#>> {1,2}

#Encontrar elementos no comunes de dos conjuntos y reemplazarlo en el primer conjunto
c1.difference_update(c2)
print(c1)
#>> {1,2}
c1 = {1,2,3}


#Encontrar elementos comunes de dos conjuntos
print(c1.intersection(c2))
#>> {3}

#Encontrar elementos comunes de dos conjuntos y reemplazarlo en el primer conjunto
c1.intersection_update(c2)
print(c1)
#>> {3}
c1 = {1,2,3}

#Diferencia simetrica
#c1 unido con c2, menos c1 intersectado con c2
print(c1.symmetric_difference(c2))
#>> {1,2,4,5}