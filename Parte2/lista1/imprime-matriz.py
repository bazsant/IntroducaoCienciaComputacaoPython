def imprime_matriz(matriz):
    for lin in matriz:
        for col in range(len(lin)):
            if col == len(lin)-1:
                print(lin[col])
            else:
                print(lin[col], end=" ")

imprime_matriz([[1, 2], [3, 4]])
