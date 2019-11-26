def primeiro_lex(lista):
    menor = lista[0].strip()
    for item in lista:
        if ord(item[0].strip()) < ord(menor[0]):
            menor = item.strip()

    return menor

def test_primeiro_lex():
    assert primeiro_lex(['oĺá', 'A', 'a', 'casa']) == 'A'
    assert primeiro_lex(['AAAAAA', 'b']) == 'AAAAAA'
