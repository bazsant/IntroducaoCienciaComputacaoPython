
def ordenacao_insercao(lista):
    for j in range(1,len(lista)):
        x = lista[j]
        i = j - 1
        while i >= 0 and lista[i] > x:
            lista[i+1] = lista[i]
            i = i-1
        lista[i+1] = x
    return lista
        
