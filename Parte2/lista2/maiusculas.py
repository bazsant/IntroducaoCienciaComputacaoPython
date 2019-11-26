def maiusculas(frase):
    ret=""
    for letra in frase:
        if ord(letra) >= 65 and ord(letra) <=90:
            ret += letra
    return ret

def test_maiusculas():
    assert maiusculas("a Ds ASfdd Qassdq sasaSkk") == "DASQS"
