#1) Localice el error en el siguiente bloque. Crea una excepcion para evitar que el prgama se bloquee
# y ademas explica en un mensaje a l usuario la causa y/o solucion

""" 
resultado = 10/0
"""

try:
    resultado = 10/0
except ZeroDivisionError:
    print("Error: la división entre cero no esta definida")
    
#2) Localice el error en el siguiente bloque. Crea una excepcion para evitar que el prgama se bloquee
# y ademas explica en un mensaje a l usuario la causa y/o solucion

""" 
lista = [1,2,3,4,5]
lista[10]
"""

lista = [1,2,3,4,5]

try:
    lista[10]
except IndexError:
    print("El índice indicado está fuera de rango, seleccione uno inferior a 5")
    
#3) Localice el error en el siguiente bloque. Crea una excepcion para evitar que el prgama se bloquee
# y ademas explica en un mensaje a l usuario la causa y/o solucion

""" 
colores = {
    'rojo':'red',
    'verde': 'green',
    'negro': 'black'
}

colores['blanco']
"""
colores = {
    'rojo':'red',
    'verde': 'green',
    'negro': 'black'
}
try:
    colores['blanco']
except KeyError:
    print('El color indicada no existe en el diccionario')
    
#4) Localice el error en el siguiente bloque. Crea una excepcion para evitar que el prgama se bloquee
# y ademas explica en un mensaje a l usuario la causa y/o solucion

""" 
resultado = "20"+15
"""
try:
    resultado = "20" + 15
except TypeError:
    print("Error: no se pueden realizar operaciones sobre datos de distinto tipo")
    print("Introduzca 'cadena' + 'cadena2' o num1 + num2 ")
else:
    print(resultado)
    
#5) Realizar una funcion llamada agregar_una_vez que reciba una lista y un elemento.
# La funcion debe añadir el elemento al final de la lista con la condicion de no repetir ningun elemento
# ademas si este elemento se encuentra en la lista, debe invocar un error de tipo: ValueError
# que debes capturar y mostrar este mensaje en su lugar
# Error: imposible añadir elementos duplicados => [elemento]

elementos = [1,5,-2]

def agregar_una_vez(elementos, elemento):
    try:
        if(elemento in elementos):
            raise ValueError("Error: imposible añadir elementos duplicados => {}".format(elemento))
    except ValueError as e:
        print(e)
    else:
        elementos.append(elemento)
        print("Elemento ",elemento," añadido a la lista")
        
agregar_una_vez(elementos,10)
agregar_una_vez(elementos,-2)
agregar_una_vez(elementos,"Hola")