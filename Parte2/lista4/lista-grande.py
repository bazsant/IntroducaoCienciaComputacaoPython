import random

def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(n**2*-1, n**2))
    return lista

        
