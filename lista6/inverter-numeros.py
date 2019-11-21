def inverter():
    sair = False
    numeros = []
    while not sair:
        numero=int(input("Digite um número: "))
        if numero != 0:
            numeros.append(numero)
        else:
            sair = True

    for item in range(len(numeros) - 1, -1, -1):
        print(numeros[item])

inverter()
