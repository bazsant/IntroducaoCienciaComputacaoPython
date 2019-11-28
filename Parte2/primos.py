import pytest

def eh_primo(numero):
    primo=True
    variante=numero
    while variante > 2 and primo:    
        if(numero%(variante-1)==0):
            primo=False
        else:
            variante=variante-1

    return primo


@pytest.mark.parametrize('entrada, esperado', [
    (1, True),
    (2, True),
    (4, False),
    (7, True),
    (8, False)
    ])

def test_primo(entrada, esperado):
    assert eh_primo(entrada) == esperado
