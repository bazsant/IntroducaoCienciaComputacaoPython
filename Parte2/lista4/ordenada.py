def ordenada(lista):
    crescente = True

    for item in range(1,len(lista)):
        if lista[item] < lista[item-1]:
            crescente = False
            break
    return crescente

def test_ordenada_true():
    assert ordenada([2,3,5,7,8]) == True

def test_ordenada_false():
    assert ordenada([2,3,5,9,8]) == False
