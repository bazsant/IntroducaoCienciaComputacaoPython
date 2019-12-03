def encontra_impares(lista, indice = 0, impares = []):
    if len(lista) == indice:
        return impares
    else:
        if lista[indice] % 2 != 0:
            impares.append(lista[indice])
        
        return encontra_impares(lista, indice + 1, impares)

