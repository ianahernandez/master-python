# Clase galleta

class Galleta():
    chocolate = False
    # __init__ es una funcion especial que se ejecuta al crear un objeto, permite enviar argumentos
    # durante la instanciación. El parametro self hace referencia al propio objeto, y se coloca para
    # diferenciar entre el ambito de clase y un metodo
    def __init__(self, sabor=None,color=None):
        self.sabor = sabor
        self.color = color
        print("Se ha instanciado una galleta")
    def chocolatear(self):
        self.chocolate = True
    def tiene_chocolate(self):
        if(self.chocolate):
            print("Soy una galleta chocolateada")
        else:
            print("Soy una galleta sin chocolate :(")

#Objetos: instancias de la clases
""" una_galleta = Galleta()
g = Galleta(sabor="Vainilla", color="Amarillo")
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()
 """
#>> <class '__main__.Galleta'>

#===================================================
#============= METODOS ESPECIALES ==================
#===================================================

class Pelicula:
    #Constructor de la clase:
    def __init__(self, titulo, duracion, anno):
        self.titulo = titulo
        self.duracion = duracion
        self.anno = anno
        print("Se ha creado la pelicula: ",titulo)
    
    # Destructor de la clase
    def __del__(self):
        print("Se esta borrando la pelicula ", self.titulo)
        
    #Redefinimos el metodo string de la clase
    def __str__(self):
        return "{} lanzada en el año {} con una duracion de {} minutos.".format(self.titulo, self.anno,self.duracion)
    
    #Redefinimos el metodo len() para que retorne la duracion de la pelicula
    def __len__(self):
        return self.duracion

         
""" print(str(p))
print(len(p)) """

#===================================================
#========== OBJETOS DENTRO DE OBJETOS ==============
#=================================================== 

class Catalogo():
    peliculas = []
    
    def __init__(self, peliculas= []):
        self.peliculas = peliculas
        
    def agregar(self, p):
        self.peliculas.append(p)
        
    def mostrar(self):
        for p in self.peliculas:
            print(p)
            
p = Pelicula("El padrino", 175,1972)
c = Catalogo([p])


c.agregar(Pelicula("El padrino parte II", 202,1974))
c.agregar(Pelicula("La cita perfecta", 90,2019))
c.mostrar()

#===================================================
#================ ENCAPSULACION ====================
#===================================================
#Evita acceder a un atributo o metodo desde el exterior, python no ofrece esta opcion, pero se puede simular

class Ejemplo:
    __atributo_privado = "Atributo privado"
    
    def __metodo_privado(self):
        print("Este es un metodo privado")
    
    def atributo_publico(self):
        return self.__atributo_privado
    
e = Ejemplo()
print(e.atributo_publico())
