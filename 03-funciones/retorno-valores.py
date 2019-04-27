#=== ==========================Retorno de cadena
def test():
    return "Una cadena retornada"

p = test()

print(p)
#=============================Retorno de colecciones

#=============Lista
def lista():
    return [1,2,3,4,5]

print(lista())

l = lista()

print(l[1:4])

#============Tupla
def tupla():
    return "Una cadena",20,[1,2,3,4,5]

c,n,l = tupla()
c
#>>>'Una cadena'
n
#>>>20
l
#>>>[1, 2, 3, 4, 5]
