def é_hipotenusa(n):
    eh_hipot=False
    i = 1
    while not eh_hipot and i < n:
        j = 1
        while not eh_hipot and j < n:            
            eh_hipot = n**2 == (i**2+j**2)
            j = j + 1
        i = i + 1
    return eh_hipot

def soma_hipotenusas(numero):
    i = 1
    soma = 0
    while i <= numero:
        if é_hipotenusa(i):
            soma = soma + i
        i = i + 1
    return soma
