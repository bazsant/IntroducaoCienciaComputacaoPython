def soma_lista(lista, indice = 0, soma = 0):
    if len(lista) == indice:
        return soma
    else:
        return lista[indice] + soma_lista(lista, indice + 1, soma)


    
