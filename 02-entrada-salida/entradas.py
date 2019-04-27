""" 
Las entradas se capturan con la funcion input y pueden ser convertidas en otro tipo de dato
"""
# === Entrada float
decimal = float ( input("Introduzca un numero decimal con punto: ") )

# Entradas para llenar una lista
valores = []

print("Introduce 3 valores")
for i in range(3):
    valores.append(input('Valor '+  str(i+1) +': '))
    
valores



