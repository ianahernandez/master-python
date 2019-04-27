lista = [1,2,3,4,5]

# Agregar un elemento
#Al final
lista.append(6)
print(lista)
#>> [1,2,3,4,5,6]
#En una posicion especifica
lista.insert(2, 2.5)
print(lista)
#>> [1,2,2.5,3,4,5,6]
#Penúltimo
lista.insert(-1,5.5)
print(lista)
#>> [1,2,2.5,3,4,5.5,6]
#**************** Si se indica una posicion mucho mayor a la longitud, lo inserta al final


# Vaciar
lista.clear()
print(lista)
#>> []

#Unir dos listas
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)
#>> [1,2,3,4,5,6]


# Contar ocurrencias en una lista
print([1,2,3,4,1,2,3,'a',1,'a',1].count(1))
#>> 4

#Encontrar el indice de un elemento en una lista
print([1,2,3,4,1,2,3,'a',1,'a',1].index('a'))
#>>7


#Eliminar elementos de la lista
#Al final
lista = [1,2,3,4,5]
lista.pop()
print(lista)
#>> [1,2,3,4]
#En una posicion especifica
lista.pop(0)
print(lista)
#>> [2,3,4]
#Por un valor especifico
lista.remove(3)
print(lista)
#>> [2,4]
lista = [1,2,3,3,3,3,3,4,5]
lista.remove(3)
print(lista)
#>> [1,2,3,3,3,3,4,5]  Solo elimina el primero


# Dar vuelta a una lista
lista.reverse()
print(lista)
#>> [1,2,3,3,3,3,3,4,5]

#Dar vuelta a una cadena
cadena = list("Hola mundo")
cadena.reverse()
print(cadena)
#>> ['o', 'd', 'n', 'u', 'm', ' ', 'a', 'l', 'o', 'H']
cadena = "".join(cadena)
print(cadena)
#>> odnum aloH


# Ordenar elementos de una cadena
numero = [100,2,1,-10,9,4,3]
numero.sort()
print(numero)
#>> [-10, 1, 2, 3, 4, 9, 100]

#Descendente
numero.sort(reverse=True)
print(numero)
#>> [100, 9, 4, 3, 2, 1, -10]