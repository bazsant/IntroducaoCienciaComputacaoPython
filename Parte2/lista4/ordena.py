def ordena(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i+1,len(lista)):
            if lista[menor] > lista[j]:
                menor = j
        lista[menor], lista[i] = lista[i], lista[menor]
    return lista

def test_ordena_certo():
    assert ordena([4, 1, 3, 6, 2, 7, 9, 8]) == [1, 2, 3, 4, 6, 7, 8, 9]

def test_ordena_certo_com_neg():
    assert ordena([5, 1, 3, 6, 2, 7, 4, -1, 10]) == [-1, 1, 2, 3, 4, 5, 6, 7, 10]
