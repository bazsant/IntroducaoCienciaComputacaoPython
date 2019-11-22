def eh_primo(numero):
    primo=True
    index=2
    while index < numero and primo:
        if numero % index == 0:
            primo = False
        index = index + 1
    return primo

def n_primos(numero):
    contador = 0
    
    while numero >= 2:
        if eh_primo(numero):
            contador = contador + 1
        numero = numero - 1
    return contador
