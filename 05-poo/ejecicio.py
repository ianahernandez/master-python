# Preparacion
# Crea una clase llamada Punto con sus dos coordenadas X e Y
# Añadir un metodo constructor para crear puntos facilmente si no se reciben, su valor sera 0
# Sobreescribe el metodo string para que al imprimir por pantalla un punto aparezca: (x,y)
# Añade un metodo llama cuadrante que indique a que cuadrante pertenece el punto, o si es el origen
# Añade un metodo llamado vector que tome otro punto y calcule el vector resultante entre los puntos
# Añade un metodo llamado distancia que tome otro punto y calcule la distancia entre los puntos y la 
#   muestre por pantalla

#===================================================
#==================== PUNTO ========================
#===================================================
import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print("Se ha creado el punto '({},{})'".format(x,y))
    
    def __str__(self):
        return "({},{})".format(self.x,self.y)
    
    def cuadrante(self):
        x = self.x
        y = self.y
        if( x == 0 and y == 0):
            return "El punto corresponde al origen"
        if( x > 0 and y > 0):
            return "Primer cuadrante"
        if( x > 0 and y < 0):
            return "Segundo Cuadrante"
        if( x < 0 and y < 0):
            return "Tercer cuadrante"
        else:
            return "Cuarto cuadrante"
        
    def vector(self, punto):
        x = punto.x - self.x
        y = punto.y - self.y
        vector = Punto(x,y)
        return vector
    
    def distancia(self, punto):
        dx = punto.x - self.x
        dy = punto.y - self.y
        distancia = math.sqrt( dx**2 + dy**2 )
        print ("La distancia entre los puntos {} y {} es de: {} unidades".format(punto,self,distancia))
        return distancia
    
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)
O = Punto(0,0)

""" print(A.cuadrante())
print(B.cuadrante())
print(C.cuadrante())
print(D.cuadrante())

print(A.vector(B))
print(B.vector(A))
print(A.distancia(B))
print(B.distancia(A)) """

#Crea una clase llamada Rectangulo con dos puntos (inicial, final) que formaran la diagonal del rectangulo
#Añade un metodo contructor para crear ambos puntos facilmente, si no se envian son cero
# Añade al rectangulo el metodo llamado base, que muestre la base
# Añade al rectangulo un metodo llamado altura
# Añade un metodo llamado area que muestre el area

class Rectangulo:
    def __init__(self, inicial=Punto(), final=Punto()):
        self.inicial = inicial
        self.final = final
        
    def base(self):
        p = Punto(self.final.x, self.inicial.y)
        return self.inicial.distancia(p)
    
    def altura(self):
        p = Punto(self.final.x, self.inicial.y)
        return self.final.distancia(p)
    
    def area(self):
        return self.base()*self.altura()
    
    def imprimir(self):
        for y in range(10):
            print(10-y,"-",end="")
            for x in range(10):
                if( (10-x+1) in range(self.inicial.x, self.final.x) and (10-y) in range (self.inicial.y, self.final.y)):
                    """ if( x == self.inicial.x):
                        print(" * ",end="")
                    else:  """                           
                    print("* ",end="")
                else:
                    print(" ",end="")
            print("")
        print('  0 1 2 3 4 5 6 7 8 9 10')

 
r = Rectangulo(A,B)
r2 = Rectangulo(Punto(2,2),Punto(8,8))
print(r.base())
print(r.altura())
print(r.area())
r2.imprimir()