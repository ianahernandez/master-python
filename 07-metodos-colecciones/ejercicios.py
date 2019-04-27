# Utilizando todo sobre cadenas, listas, sus metodos internos, transforma este texto:

"""
un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un
monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el
viento, lo que se mueve son vuestras mentes -dijo el maestro

"""
#en este otro:
"""
Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
"""

texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
print(texto)
lista = texto.split('#')

lista2 = []

for i,sub in enumerate(lista):
    sub = sub.capitalize()
    sub = list(sub)
    if(i == 0):
        sub.append("...\n")
    else:
        sub.insert(0,'- ')
        sub.append(".\n")
    sub = "".join(sub)
    lista2.append(sub)

texto =  "".join(lista2)

print(texto)
#print(lista)

#2) Crea una funcion que a partir de una lista de numeros, realice las siguientes tareas sin modificar
# el original

# Borrar los elementos duplicados
# Ordenar las lista de mayor a menor
# Eliminar todos los numeros impares
# Realizar una suma de todos los numeros que quedan
# Devolver la lista modificada
# Finalmente, despues de ejecutar la funcion, comprueba que la suma de todos los numeros a partir
# del segundo, concuerda con el primer numero de la lista, tal que asi:
import copy

lista = [29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]

def modificar_lista(lista):
    lista2 = copy.copy(lista)
    lista2 = list(set(lista2))
    lista2.sort(reverse=True)
    aux = []
    for numero in lista2:   
        if(numero%2 == 0):
            aux.append(numero)
    lista2 = aux
    print("Suma de los elementos restantes: ", sum(lista2[:]))
    lista2.insert(0,sum(lista2[:]))
    return lista2

print(lista)
nueva_lista = modificar_lista(lista)
print(nueva_lista)
print(nueva_lista[0] == sum(nueva_lista[1:]))

