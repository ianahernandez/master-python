# ==============================================================================
#          Funcion locals y globals
# ==============================================================================

 #locals() : retorna las funciones y variables definidas en un bloque de codigo especifico, 
 #           una clase o una funcion.
 #globals(): retorna todas los espacios de memoria dedicado a las variables y funciones 
 #           declaradas globalmente.

print(globals())
 #>> {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fb5d6ae0a90>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'funciones-decoradoras.py', '__cached__': None}
print(locals())
 #>> {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fb5d6ae0a90>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'funciones-decoradoras.py', '__cached__': None}
 
# ==============================================================================
#          Funciones Decoradoras
# ==============================================================================
# Es una funcion que envuelve la ejecucion de otra funcion y permite extender su comportamiento
# estan pensandas para reutilizarlas gracias a una sintaxis de ejecucion mucho mas simple.

# Funcion decoradora 

def op_decorador( funcion ):
    def decorar( *args, **kwargs ):
        print("\t Se va a ejecutar la funcion: ", funcion.__name__)
        funcion(*args, **kwargs)
        print("\t Finalizó la ejecucion de la funcion: ", funcion.__name__)
    return decorar

# Funciones 
@op_decorador
def suma(a,b):
    print("{} + {} = {}".format(a,b,a+b))
    
@op_decorador
def resta(a,b):
    print("{} - {} = {}".format(a,b,a-b))
    
@op_decorador    
def multiplicacion(a,b):
    print("{} * {} = {}".format(a,b,a*b))
    
@op_decorador   
def division(a,b):
    print("{} / {} = {}".format(a,b,a/b))
    

print(suma(2,3))
#>>          Se va a ejecutar la funcion:  suma
#2 + 3 = 5
#        Finalizó la ejecucion de la funcion:  suma
print(multiplicacion(3,5))
#         Se va a ejecutar la funcion:  multiplicacion
#3 * 5 = 15
#         Finalizó la ejecucion de la funcion:  multiplicacion