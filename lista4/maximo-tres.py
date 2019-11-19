def maximo(n1, n2, n3):
    if n1 > n2 :
        if n1 > n3:
            return n1
        else:
            return n3
    elif n2 > n3:
        return n2
    else:
        return n3

def test_maximo():
    assert maximo(3,2,1) == 3
    assert maximo(2,3,1) == 3
    assert maximo(1,2,3) == 3
    