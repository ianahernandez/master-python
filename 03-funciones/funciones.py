#=======================================================
#=============== FUNCIONES =============================
#=======================================================
"""
Son fragmentos de codigo que se puede ajecutar múltiples veces. Puede recibir y devolver
información para comunicarse con el proceso principal.
"""

#=======================================================
#=================== Definicion ========================
#=======================================================

def saludar():
    print("Hola desde la funcion saludar")


# saludar()

def dibujar_tabla_de_5():
    for x in range(11):
        print("5 x",x," = ",5*x)

# dibujar_tabla_de_5()
n = 10
def test():
    print(n)

test()