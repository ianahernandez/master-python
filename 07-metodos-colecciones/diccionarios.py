colores = {
    'amarillo':'yellow',
    'azul':'blue',
    'verde':'green'
}

#Acceso por clave
print(colores['amarillo'])

print(colores.get('amarillo', 'Mensaje si no se encuentra'))

print(colores.get('negro', 'Mensaje si no se encuentra'))

# Verificar si un elemento existe en el diccionario
print('negro' in colores)
#>> False
print('amarillo' in colores)
#>> True

# Claves de un diccionario
print(colores.keys())
#>> dict_keys(['amarillo','azul','verde'])

# Valores de un diccionario
print(colores.values())
#>> dict_values(['yellow','blue','green'])

# Claves y valores
print(colores.items())
#>> dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')])
for c,v in colores.items():
    print(c,v)
    
    
# ELiminar elemento de un diccionario
print(colores.pop('amarillo','mensaje si no se ha encontrado'))
#>> yellow
print(colores)
#>> {'azul': 'blue', 'verde': 'green'}
print(colores.pop('negro','mensaje si no se ha encontrado'))
#>> mensaje si no se ha encontrado

#Vaciar diccinario
colores.clear()
print(colores)
#>> {}