def resta(a,b):
    return(a-b)

print(resta(2,1))


def resta_v(a=None,b=None):
    if(a==None or b==None):
        print("Error debe introducir dos numeros")
        return
    return(a-b)

print(resta_v(b=2,a=8))

#=======================================================
#=================== POR VALOR =========================
#=======================================================
"""
La variable solo vive dentro de la funcion y no afecta al exterior
"""
def doblar_valor(numero):
    numero*=2

n =10
doblar_valor(n)
print(n)
#>>10    No cambia su valor porque la operacion se hizo dentro de la funcion

# Si se desea manipular como si fuera por referencia:

def doblar_valor(numero):
    return numero*2

n =10
n = doblar_valor(n)
print(n)
#>> 20


#=======================================================
#=================== POR REFERENCIA =========================
#=======================================================
"""
hacen referencia a variables externas, que si se modifican permanecen los cambios
"""
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *=2

ns = [10,50,100]
doblar_valores(ns)
print(ns)

# Si se desea manipular como si fuera or valor y no modificatr la collecio original:

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *=2

ns = [10,50,100]
print(doblar_valores(ns[:]))
print(ns)

#=======================================================
#=================== INDETERMINADOS ====================
#=======================================================
""" 

"""
def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

indeterminados_posicion("Hola",3,[1,2,3,4])

def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg," = ", kwargs[kwarg])

indeterminados_nombre(c="Hola",n=3,l=[1,2,3,4])

def super_funcion(*args,**kwargs):
    suma = 0
    for arg in args:
        suma += arg
    print("suma = ",suma)
    
    for kwarg in kwargs:
        print(kwarg," = ", kwargs[kwarg])
        
super_funcion(3,2,10,8,90,23.4, nombre = 'Ana', edad = 23, carrera= 'Informatica')