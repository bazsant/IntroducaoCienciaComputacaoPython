def ordem_inversa():
    numero = 1
    lista=[]
    while numero > 0:
        numero = int(input())
        lista.append(numero)

    i = len(lista) - 1
    while i >= 0:
        print(lista[i], end=" ")
        i = i - 1
