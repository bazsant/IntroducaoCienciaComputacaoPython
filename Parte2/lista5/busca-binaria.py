import pytest

def busca(lista, elemento):
    inicio = 0
    fim = len(lista)-1

    while inicio <= fim:
        meio = ((fim-inicio)//2)+inicio
        print(meio)

        if lista[meio] == elemento:
            return meio
        else:
            if elemento < lista[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1
    return False

@pytest.mark.parametrize("lista, elemento, saida",[
    (['a','e','i'],'e',1),
    ([1,2,3,4,5],4,3),
    ([1,2,3,4,5],6,False)
    ])

def test_busca(lista, elemento, saida):
    assert busca(lista, elemento) == saida
