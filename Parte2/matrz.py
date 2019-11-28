def cria_matriz(lin, col, val):
    matrz = []

    for l in range(lin):
        newLine = []

        for c in range(col):
            newLine.append(val)

        matrz.append(newLine)
    return matrz
