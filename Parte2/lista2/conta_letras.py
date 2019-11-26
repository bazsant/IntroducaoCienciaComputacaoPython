def conta_letras(frase, contar="vogais"):
    qtd = 0
    vogais = "aAeEiIoOuU"
    if contar == "vogais":
        for letra in frase:
            if letra in vogais:
                qtd += 1
    else:
        for letra in frase:
            if letra not in vogais and letra.isalpha():
                qtd += 1

    return qtd

def test_conta_letras():
    assert conta_letras("Algumas coisas") == 6
    assert conta_letras("Vamos ver quale", "vogais") == 6
    assert conta_letras("Habemus Sabadus", "consoantes") == 8
