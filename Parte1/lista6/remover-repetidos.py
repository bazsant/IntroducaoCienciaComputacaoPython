def remove_repetidos(lista):
    aux=[]
    for item in lista:
        if item not in aux:
            aux.append(item)
    return sorted(aux)
