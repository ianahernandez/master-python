# 3) Crea un script que realice las siguientes tareas:
#       -Debe tomar un argumento que sera un numero entero positivo.
#       -En caso de no recibir un argumento, mostrat informacion de como utilizar el script
#       -El objetivo del script es descomponer el numero en unidades, decenas, centenas y miles ...
#       tal que si se introduce el numero 3647 el programa deberá devolver una descomposicion como 
#       la siguiente utilizando tecnicas de formateo
"""
3000
0600
0040
0007 
"""

import sys

if(len(sys.argv) < 2):
    print("ERROR: faltan argumentos, debe introducir un numero entero")
    print("Ejemplo: python ejercicio-tabla.py 3647")  
else:
    
    if(sys.argv[1].isdigit()):
        digitos = len(sys.argv[1])
        numero_str = sys.argv[1]
        numero = int(sys.argv[1])
        for x in range(digitos):
            unidad = int(numero_str[digitos-x-1])*10**x
            print("{:0{digitos}d}".format(unidad, digitos = digitos))
    else:
        print("ERROR: el argumento deben ser numérico entero")