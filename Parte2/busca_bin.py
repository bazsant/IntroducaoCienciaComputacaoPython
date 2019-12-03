def busca_bin(lista, elem, min=0, max=None):
    print('entrou ', min, max)
    if max == None:
        max = len(lista) - 1
    if max < min:
        return False
    else:
        meio = min + (max-min)//2
    if lista[meio] > elem:
        return busca_bin(lista, elem, min, meio-1)
    elif lista[meio] < elem:
        return busca_bin(lista, elem, meio + 1, max)
    else:
        return meio


lista = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875,934]
print(busca_bin(lista, 99))
        
