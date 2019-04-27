# =======================================================================
# ======================= FORMATEO DE PALABRAS ==========================
# =======================================================================

v = "otro texto"
n = 10

#Formato para imprimir datos, cuando se necesita concatenar datos variables 

c = "Un numero, {} y un numero: {}".format(v,n)

print(c)

# Para cambiar el orden en que se toman los argumentos utilizando posiciones

c = "Un numero, {1} y un numero: {0}".format(v,n)

print(c)

# Para cambiar el orden en que se toman los argumentos utilizando alias

texto = "otro texto"
numero = 10

c = "Un numero, {texto} y un numero: {numero}".format(texto = texto ,numero= numero)


# =======================================================================
# ======================= Alineacion ====================================
# =======================================================================

# Derecha
# Linea de tamaño n = 30 y una palabra al extremo derecho
print("{:>30}".format("palabra"))
#>>                        palabra


# Izquierda
# Linea de tamaño n = 30 y una palabra al extremo izquiera
print("{:30}".format("palabra"))
#>> palabra       


# Centro
# Linea de tamaño n = 30 y una palabra al centro
print("{:^30}".format("palabra"))
#>>            palabra    

# =======================================================================
# ======================= Trucamiento ===================================
# =======================================================================  

#Truncamiento a 5 caracteres

print('{:.5}'.format('palabra'))
#>> palab


#Truncamiento a 3 caracteres

print('{:.3}'.format('palabra'))
#>> pal

# =======================================================================
# ======================= FORMATEO DE NUMEROS ===========================
# =======================================================================

#Números enteros formateados a 4 digitos

print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

""" 
  10
 100
1000
"""
#numeros enteros formateados a 4 digitos con ceros

print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

""" 
0010
0100
1000
"""

#Números flotantes formateados a 4 digitos

print("{:.3f}".format(3.1415926))

#numeros flotantes formateados a 4 digitos con espacios

print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))

#numeros flotantes formateados a 4 digitos con ceros

print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))
