# La Herencia: es la capacidad de una clase de heredar atributos y métodos de otra, ademàs
#              de agregar nuevos o modificar los heredados

""" class Producto:
    def __init__(self, ref, tipo, nombre, pvp, descripcion, productor=None, distribuidor=None, isbn=None, autor=None):
        self.ref = ref
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn 
        self.autor = autor """
        
""" adorno = Producto('000A', 'ADORNO','Vaso adornado',15,'Vaso de porcelana')

print(adorno)
print(adorno.tipo) """

#Superclase
class Producto:
    def __init__(self, ref, nombre, pvp, descripcion):
        self.ref = ref
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
    def __str__(self):
        return """\
        Referencia:\t{}
        Nombre:\t\t{}
        Pvp:\t\t{}
        Descripcion:\t{}""".format(self.ref, self.nombre,self.pvp, self.descripcion)
        
#Subclases

class Adorno(Producto):
    pass

class Alimento(Producto):
    productor = ""
    distribuidor = ""
    def __str__(self):
        return """\
        Referencia:\t{}
        Nombre:\t\t{}
        Pvp:\t\t{}
        Descripcion:\t{}
        Productor:\t{}
        Distribuidor:\t{}""".format(self.ref, self.nombre,self.pvp, self.descripcion,self.productor,self.distribuidor)

class Libro(Producto):
    isbn = ""
    autor = ""
    def __str__(self):
        return """\
        Referencia:\t{}
        Nombre:\t\t{}
        Pvp:\t\t{}
        Descripcion:\t{}
        ISBN:\t\t{}
        Autor:\t\t{}""".format(self.ref, self.nombre,self.pvp, self.descripcion,self.isbn,self.autor)
    


adorno = Adorno('000A','Vaso adornado',15,'Vaso de porcelana')

al = Alimento('2035','Aceite de oliva', 5, '250 ml')
al.productor = "La aceitera"
al.distribuidor = "Distri S.A"

li = Libro('2036','Cocina Mediterránea',9,'Recetas sanas')
li.isbn = "0-123456-78-9"
li.autor = "Doña Juana"


productos = [adorno,al,li]

""" for p in productos:
    print(p,"\n")

for p in productos:
    print(p.ref,p.nombre) """
    
for p in productos:
    if( isinstance(p, Adorno) ):
        print("\t========= ADORNO ==============")
    elif( isinstance(p, Libro)):
        print("\t========= LIBRO ===============")
    else:
        print("\t========= ALIMENTO ============")
    print(p,"\n")

# Funcion externa para rebajar el precio de un producto

def rebajar_producto(p, rebaja):
    """ Devuelve el producto con un pocentaje de rebaja en su perecio"""
    p.pvp -= (p.pvp/100*rebaja)
    return p

#print(li)
""" 
Referencia:     2036
Nombre:         Cocina Mediterránea
Pvp:            9       <===== Precio actual
Descripcion:    Recetas sanas
ISBN:           0-123456-78-9
Autor:          Doña Juana 
"""
        
#rebajar_producto(li,10)
#print(li)
""" 
Referencia:     2036
Nombre:         Cocina Mediterránea
Pvp:            8.1     <======= Nuevo precio con rebaja
Descripcion:    Recetas sanas
ISBN:           0-123456-78-9
Autor:          Doña Juana 

"""

#********* Los objetos son parametros que se pasan por referencia, es decir que cuando son manipulados
# desde una funcion externa, el objeto original conserva los cambios
# Este enefecto NO se puede evitar intentando hacer una copia del objeto.
# En este caso, para realizar una copia de un objeto, importamos la librería externa copy y modificamos
# la copia, manteniendo intacto el objeto original

""" 
import copy

copia_objeto = copy.copy(al)
"""

import copy
copia_libro = copy.copy(al)


print(li)
""" 
Referencia:     2036
Nombre:         Cocina Mediterránea
Pvp:            9       <===== Precio actual
Descripcion:    Recetas sanas
ISBN:           0-123456-78-9
Autor:          Doña Juana 
"""
        
rebajar_producto(copia_libro,10)
print(li)
""" 
Referencia:     2036
Nombre:         Cocina Mediterránea
Pvp:            9     <======= Precio igual, ya que se modifico solo la copia
Descripcion:    Recetas sanas
ISBN:           0-123456-78-9
Autor:          Doña Juana 

"""

""" 
======================================================================
    Polimorfia
======================================================================
"""
# Propiedad de la herencia en que objetos de distintas subclases pueden responder una misma accion
# En Python todas las clases sona  su vez subclases de la superclase Object, es decir, son polimorficas
# por defecto

""" 
======================================================================
    Herencia múltiple
======================================================================
"""
class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este es un metodo heredado de A")
        
        
class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este es un metodo heredado de B")
        
class C(B,A):
    def c(self):
        print("Este es un metodo solo de C")

c = C()
c.a()
c.b()
c.c()