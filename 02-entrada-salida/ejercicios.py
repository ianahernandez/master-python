# 1) Formatear los siguientes valores para mostrar el resultado indicado
 # "Hola mundo" alineado a la derecha en 20 caracteres
print("{:>20}".format("Hola mundo"))

 # "Hola mundo" truncamiento en el cuarto caracter indice 3
print("{:.3}".format("Hola mundo"))

 # "Hola mundo" alineado al centro en 20 caracteres con truncamiento en el segundo caracter indice 1
print("{:^20.1}".format("Hola mundo"))

 # 150 -> formateo a cinco numeros enteros rellenados con ceros
print("{:05d}".format(150))

 # 7887 -> formateo a 7 numeros enteros rellenados con espacio
print("{:7d}".format(7887))

 # 7887 -> formateo a 7 numeros enteros rellenados con cero
print("{:07d}".format(7887))

# 20.02 -> formateo a 3 numeros enteros y 3 decimales rellenado con cero
print("{:07.3f}".format(20.02))
