def eh_primo(numero):
    primo = True
    contador = numero - 1
    while primo and contador > 2:
        primo = numero % (contador) != 0
        contador = contador - 1
    return primo

def maior_primo(numero):
    primo = 0
    while primo == 0 and numero > 2:
        if(eh_primo(numero)):
            primo = numero
        numero = numero - 1
    return primo
