
# 1) Realiza un programa que siga las siguientes instrucciones

    # Crea un conjunto llamado usuarios con Marta, David, Elvira, Juan y Marcos

usuarios = {'Marta', 'David', 'Elvira', 'Juan', 'Marcos'}
    
    # Crear un conjunto llamado administradores con Juan y Marta
    
administradores = {'Juan', 'Marta'}
    
    # Borra al administrador Juan del conjunto administradores

administradores.discard('Juan')

    # Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios

administradores.add('Marcos')
    
    # Muestra todos los usuarios por pantalla de forma dinamica, ademas debes indicar si cada 
    # usuario es administrador o no  
    
for usuario in usuarios:
    if(usuario in administradores):
        print(usuario,'es admin')
    else:
        print(usuario,'no es admin')
        
# 2) Durante el desarrollo de un videojuego se te encarga configurar y balancear cada clase de personaje
#    jugable. 

caballero = {
    'vida' : 2,
    'ataque': 2,
    'defensa': 2,
    'alcance': 2
}

guerrero = {
    'vida' : 2,
    'ataque': 2,
    'defensa': 2,
    'alcance': 2
}

arquero = {
    'vida' : 2,
    'ataque': 2,
    'defensa': 2,
    'alcance': 2
}

# Partiendo que la estadistica base es 2, debes cumplir con las siguientes condiciones:

    # El caballero tiene el doble de vida y defensa que un guerrero

caballero['vida'] = 2*guerrero['vida']
caballero['defensa'] = 2*guerrero['defensa']
    
    # El guerrero tiene el doble de ataque y alcance de un caballero
    
guerrero['ataque'] = 2*caballero['ataque']
guerrero['alcance'] = 2*caballero['alcance']
    
    # El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble 
    # de su alcance
arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = 0.5*guerrero['defensa']
arquero['alcance'] = 2*guerrero['alcance']

    # Muestra como quedan las propiedades de los tres personajes

print(caballero)
#{'vida': 4, 'ataque': 2, 'defensa': 4, 'alcance': 2}
print(guerrero)
#{'vida': 2, 'ataque': 4, 'defensa': 2, 'alcance': 4}
print(arquero)
#{'vida': 2, 'ataque': 4, 'defensa': 1.0, 'alcance': 8}


# 3) Durante la planificacion de un proyecto se han acordado una lista de tareas. Para cada una de
#    estas tareas se ha asignado un orden de prioridad (cuanto menor es el numero de orden, mas 
#    prioridad)

# ¿Eres capaz de crear una estructura de tipo cola con todas las tareas ordenadas pero sin los numeros
# de orden?

# Pista: para ordenar una lista, usaremos 'sort'

tareas = [
    [6, 'Distribucion'],
    [2, 'Diseño'],
    [1, 'Concepcion'],
    [7, 'Mantenimiento'],
    [4, 'Produccion'],
    [3, 'Planificacion'],
    [5, 'Pruebas']
]

from collections import deque

tareas.sort()

# Cola de tareas

cola_tareas = deque()

#Agregar a la cola e imprimir

for tarea in tareas:
    cola_tareas.append(tarea[1])
    print(tarea[1])
