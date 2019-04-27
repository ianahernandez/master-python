#=======================================================
#=================== Conversiones ======================
#=======================================================

# String -> entero
n = int("10")
n
#>>10

# Entero -> string
cadena = str(10)
cadena
#>>"10"

# String -> Flotante
n = float("3.14")
n
#>>3.14

# Flotante -> string
cadena = str(3.14)
cadena
#>>"3.14"


# Decimal -> binario
bin(10)
#0b1010   ------> 0b indica que esta expresado en binario

#Decimal -> Hexadecimal
hex(10)
#>> 0xa   -------> 0x indica que esta expresado en hexadecimal

# binario -> decimal
#Se debe indicar cual es la base del numero, en este caso 2
int('0b1010',2)
#10 

#hexadecimal -> decimal
#Se debe indicar cual es la base del numero, en este caso 16
int('0xa',16)
#>> 0xa   -------> 0x indica que esta expresado en hexadecimal

#Valor absoluto
abs(-10)
#>>10


#Redondeo
round(5.5)
#>>6
round(5.4)
#>>5


#Evaluar una expresion en una cadena
eval("2+5")
#>>7
n = 10
eval("n*2")
#>>20
eval("2==2")
#>>True
