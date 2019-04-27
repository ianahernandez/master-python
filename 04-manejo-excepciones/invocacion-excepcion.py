def funcion(algo = None):
    try:
        if (algo is None):
            raise ValueError("No se permite un valor nulo")
    except ValueError as e:
        print(e)
        
funcion()