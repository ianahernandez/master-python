# 2) Crear un script que realioce las siguientes tareas:

        # Debe tomar 2 argumentos, ambos numeros positivos del 1 - 9, sino mostrar un error
                
        # El primero argumento hara referencia a las filas de una tabla, el seguntos las columnas
        
        # En caso de no recibir uno o ambos argumentos debe mostrar infomacion acerca de como utilizar el script
        
        # El script contendrá un bucle for que itere el numero de veces del primer argumento
        
        # Dentro de for añade un segundo for que itere el numero de veces del segundo argumento
        
        # Dentro del segundo for  ejecuta una instruccion print("+",end="), (end=" evita el salto de linea)
        
        # Ejecuta el codigo y observa el resultado
         
 # ======== Solución =============

import sys

if(len(sys.argv) < 3):
    print("ERROR: faltan argumentos, debe introducir dos numeros")
    print("Ejemplo: python ejercicio-tabla.py 2 4")
    
else:
    
    if(sys.argv[1].isdigit() and sys.argv[2].isdigit()):
        filas = int(sys.argv[1])
        columnas = int(sys.argv[2])
        if(filas>0 and filas <10 and columnas>0 and columnas<10):
            
            for x in range(filas):
                for y in range(columnas):
                    print(" *",end="") 
                print("")         
              
        else:
            print("ERROR: los argumentos deben ser numéricos (enteros del 1 al 9)")
    else:
        print("ERROR: los argumentos deben ser numéricos (enteros del 1 al 9)")