# ==============================================================================
#          Funciones Lambda
# ==============================================================================
# Son funciones anonimas que intentan simplificar el codigo de una funcion, cuyo
# contenido es una UNICA expresion y no un bloque de acciones,
# debe ser guardada en una variable para ser utlizada 

# Funcion normal que dobla un numero
def doblar(numero):
    return numero * 2
# o, ya que la funcion tiene una unica instruccion se puede simplificar en una sola linea
def doblar(numero): return numero * 2

# Funcion lambda que dobla un numero
doblar = lambda num : num * 2
print(doblar(3))
# 6

# Funcion lambda que verificar si un numero es impar
es_impar = lambda num : num % 2 != 0
print(es_impar(28))
# False

# Funcion lambda que revierte una  cadena
revertir = lambda cadena: cadena[::-1]
print(revertir("Hola como estas"))
# satse omoc aloH

# Funcino lambda que suma dos numeros
sumar = lambda a,b : a + b
print(sumar(3,5))
# 8

