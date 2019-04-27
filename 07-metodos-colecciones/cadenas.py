# Manipulacion de mayusculas y minusculas

#Convertir todo a mayusculas
print("cadena de texto".upper())
#>> "CADENA DE TEXTO"

#Convertir todo a minusculas
print("CADENA DE TEXTO".lower())
#>>cadena de texto

#Convertir a la primera letra en mayuscula
print("CADENA DE TEXTO".capitalize())
#>>Cadena de texto

#Convertir a la primera letra de cada palabra en mayuscula
print("CADENA DE TEXTO".title())
#>>Cadena De Texto

#Contar las ocurrencias de una cadena dentro del texto
print("CADENA DE TEXTO".count('A'))
#>>2

#Buscar el indice de la ultima aparicion de una subcadena: Reverse find
print("CADENA DE TEXTO".find('DE'))
#>>2  ---> CA (DE) NA      #Primera aparicion

print("CADENA DE TEXTO".rfind('DE'))
#>>7  ---> DE     #Ultima aparicion


# ==============================================================================
#           Otras comprobaciones
# ==============================================================================
c = "100"
c2 = "ABC1003Apo"
c3 = "ABC$%&?1000"
 
 #Comprobar si la cadena contiene solo numeros
print(c.isdigit())
 #>> True
 #Comprobar si la cadena contiene solo caracteres alfanumericos
print(c2.isalnum())
 #>> True
print(c3.isalnum())
 #>>False
 
 
 
 #Comprobar si la cadena contiene solo letras
print("Hola mundo".isalpha())
 #>> False   ------> Porque contiene un espacio
print("Holamundo".isalpha())
 #>> True
 
 
 
#Comprobar si la cadena esta en minusculas, mayusculas o titulo
print("hola mundo".islower())
#>>True
print("Hola mundo".isupper())
#>>False
print("Hola mundo".istitle())
 #>> False 
 
 
 #Comprobar si la cadena cmpuesta de puros espacios
print("        ".isspace())
 #>> True
print("    a    ".isspace())
 #>> False
 
 
#Comprobar el comienzo de una cadena
print("hola mundo".startswith("h"))
#>>True
print("hola mundo".startswith("hola"))
#>>True
print("hola mundo".startswith("m"))
#>>False


#Comprobar el fin de una cadena
print("hola mundo".endswith("o"))
#>>True
print("hola mundo".endswith("mundo"))
#>>True
print("hola mundo".endswith("m"))
#>>False


# ==============================================================================
#          Operaciones en cadenas
# ==============================================================================
# Separar cada token 
print("Hola mundo mundo hola".split())
#>> ['Hola', 'mundo', 'mundo', 'hola']

# Separar en subcadenas delimitadas por comas
print("Hola,mundo,mundo,hola".split(','))
#>> ['Hola', 'mundo', 'mundo', 'hola']

# Separar cada token y mostrar uno en especifico
print("Hola mundo mundo hola".split()[2])
#>> mundo

# Insertar separadores  una cadena
print(",".join("Hola mundo"))
#>> H,o,l,a, ,m,u,n,d,o

# Insertar separadores  una cadena
print(" ".join("Hola"))
#>> H o l a

# Suprimir espacios o simbolos de una cadena
print("      Hola     ".strip())
#>> Hola

print("-------Hola-----------".strip('-'))
#>> Hola


#Reemplazar cadena  o subcadena
print("Hola mundo".replace('Hola','Hello'))

#Suprimir ocurrencias de una cadena
print("Hola mundo mundo hola mundo otro mundo hola".replace('mundo', '',3))