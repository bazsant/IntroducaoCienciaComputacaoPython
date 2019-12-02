import pytest

def bubble_sort(lista):
    
    for i in range(len(lista)-1,-1,-1):
        alterou = False
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                alterou = True
                print(lista)
        if not alterou:
            return lista
    return lista

@pytest.mark.parametrize("entrada, saida", [
    ([5,1,4,2], [1,2,4,5])
    ])

def test_bubble(entrada, saida):
    assert bubble_sort(entrada) == saida
        
            
            
