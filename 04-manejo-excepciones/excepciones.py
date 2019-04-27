 # Manejode excepciones
 
while(True):
    try:
        n = float(input("Introduce un numero: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error")
    else:
        print("Todo ha funcionado correctamete")
        break
    finally:
        print("Fin de la iteracion")
        
# Mostrando las excepciones

try:
    n = float(input("Introduce un numero: "))
    5/n
except TypeError:
    print("Error: no se puede dividir un numero entre una cadena")
except ValueError:
    print("Error: debes introducir un numero")
except ZeroDivisionError:
    print("Error: la división entre cero no esta deficina")
except Exception as error:
    print(type(error).__name__)
