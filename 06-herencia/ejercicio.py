
""" 
======================================================================

======================================================================
"""

class Vehiculo:
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)
    
    
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
    
class Camioneta(Coche):
    
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + ", carga de {} kg".format(self.carga)
    
class Bicicleta(Vehiculo):
    
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ", tipo: {}".format(self.tipo)
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
    
coche = Coche("Azul", 4, 150, 1200)
camioneta =  Camioneta("Rojo", 4, 300, 1500, 1000)
bicicleta = Bicicleta("Blanco", 2, "Urbano")
motocicleta = Motocicleta("Verde", 2, "Deportivo", 180, 700)

vehiculos = [coche, camioneta, bicicleta, motocicleta]
    
def catalogar(vehiculos, ruedas):
    ct = 0
    for v in vehiculos:
        if( v.ruedas == ruedas):
            ct += 1
            
    print("Se han encontrado {} vehículos con {} ruedas.".format(ct, ruedas))
    print("=============================================")
    for v in vehiculos:
        if( v.ruedas == ruedas):
            print(type(v).__name__, v)
            
        
catalogar(vehiculos, 4)
    
    
    
