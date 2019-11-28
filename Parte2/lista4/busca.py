def busca(lista, elemento):    
    for indice in range(len(lista)):
        if lista[indice] == elemento:
            return indice
    return False


def test_busca_true():
    assert busca([1,'44',4], '44') == 1

def test_busca_true2():
    assert busca([1,'44',4], 4) == 2

def test_busca_true3():
    assert busca([1,'44',4], (3+1)) == 2

def test_busca_false():
    assert busca([1,'44',4], 2) == False
        
