#1) Realiza una funcion llamada area_rectangulo que devuelva el area a partir de una 
# base y una altura. Calcula el area d eun rectangulo de 15 de base y 10 de altura

def area_rectangulo(base, altura):
    return base*altura;

area = area_rectangulo(base=15, altura = 10)

print(area)

# 2) Realiza una funcion llamada area_circulo que devuela el area de un circulo a partir de un radio
# calcula el area de un circulo de radio 5

import math

def area_circulo(radio):
    return math.pi*radio**2

area2 = area_circulo(5)
print(area2)

#3) Realiza una funcion llamada relacion que a partir de dos numeros cumpla lo siguiente:
#   -Si el primer numero es mayor que el segundo: devuelve 1
#   -Si el primer numero es menor que el segundo: devuelve -1
#   -Si ambos son iguales: devuelve 0
#   -Comprueba la relacion de: 6y10 , 10y5 , 5y5

def relacion(a,b):
    if(a>b):
        return 1
    elif (a<b):
        return -1
    else:
        return 0

print(relacion(6,10))
print(relacion(10,5))
print(relacion(5,5))

# 4) realiza una funcion llamada intermedio que a partir de dos numeros devuelva su punto medio
#    Compruebe el punto medio de: -12y24

def intermedio(a,b):
    return (a+b)/2

print((intermedio(-12,24)))

# 5) realiza una funcion llamada recortar que reciba 3 parametros. El primero es el numero a recortar
#el segundo es el limite inferior y el tercero es el limite superior
# La funcion tentra que cumplir lo siguiente:
# - Devolver el limite inferior, si el numero ees menor que este
# - Devolver el limite superior si el numero es mayor que este
# - Devolver el numero sin cambios si no se superan los limites

def recortar(num,li,ls):
    if(num<li):
        return li
    elif(num>ls):
        return ls
    else:
        return num
    
print(recortar(15,0,10))

#6) Realice una funcion llamada separada que tome una lista de numeros enteros y devuelva dos listas
# ordenas. La primera con los numeros pares y la segunda con los impares

def separada(lista):
    pares = []
    impares = []
    for numero in lista:
        if(numero%2 == 0):
            pares.append(numero)
        else:
            impares.append(numero)
    pares.sort()
    impares.sort()
    return pares,impares

pares,impares = separada([-12,84,13,20,-33,101,9])
print(pares)
print(impares)