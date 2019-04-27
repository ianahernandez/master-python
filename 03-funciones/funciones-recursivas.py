#=======================================================
#=================== RECURSIVIDAD ======================
#=======================================================

#Es una tecnica muy utilizada que se basa en dividir un problema en partes mas pequeñas
# para poder solucionarlo de forma mas simple. Una funcion recursiva es aquellla que se llama a sí misma

def cuenta_atras(num):
    num -=1
    if(num > 0):
        print(num)
        cuenta_atras(num)
    else:
        print("BOOOOOM!")
    print("Fin recursion: ",num)

#cuenta_atras(10)

def factorial(num):
    print("Valor inicial ",num)
    if(num > 1):
        num = num*factorial(num-1)
    print("Valor final ", num)
    return num

print(factorial(5))