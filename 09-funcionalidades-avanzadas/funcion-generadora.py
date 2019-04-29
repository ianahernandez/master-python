# ==============================================================================
#          Funciones Generadoras
# ==============================================================================
# Devuelven un objeto generador con caracteristicas particulares, por ejemplo son
# iterables, contrario al resto de las colecciones

def generar_pares(n):
    for numero in range(n+1):
        if(numero %2 == 0):
            yield numero  #yield agregar el elemento al objeto generador
            
print(generar_pares(10))
#>> <generator object generar_pares at 0x7f8d9c1976d8>

# Se puede recorrer la lista
for par in generar_pares(10):
    print(par)
""" 
0
2
4
6
8
10 
"""

# Asignamos el iterador generado a una variable y la iteramos con la funcion integrada next

pares = generar_pares(20)

print(next(pares))
print(next(pares))

# ==============================================================================
#          Convertir colecciones en iteradores
# ==============================================================================
# En algunos casos podría ser de interés, convertir una coleccion a un iterador
# generado, para ello se hace uso de la funcion iter que recibe la funcion que
# deseamos convertir ejemplo

cadena_iterable = iter("cadena de texto iterable")
print(next(cadena_iterable))
lista_iterable = iter(['l','i','s','t','a',2,'iterable'])
print(next(lista_iterable))
