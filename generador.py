# Ejemplo generador en Python

#no utiliza generador
def gerenarPares(limite):
    lista=[]
    for i in range(2,limite,2):
        lista.append(i)
    return lista

#con generador
def gerenarParesConGenerador(limite):

    for i in range(2,limite,2):
        yield i

devuelvePares=gerenarParesConGenerador(20)

print(next(devuelvePares))
pass
pass
print(next(devuelvePares))
pass
pass
print(next(devuelvePares))
pass
pass
print(next(devuelvePares))

