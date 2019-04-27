# Guiones con instrucciones en código fuente que se ejecutan de arriba a abajo, guardados en un 
# fichero con un nombre ùnico y ejecutados desde el intérprete
# Pueden tomar datos (Argumentos) en el momento de la ejecución.

import sys

#Instruccion que sera ejecuta desde el exterior

print("Hola, este es el primer script")

texto = sys.argv[1]
repeticiones = int(sys.argv[2])


for i in range(repeticiones):
    print(texto)