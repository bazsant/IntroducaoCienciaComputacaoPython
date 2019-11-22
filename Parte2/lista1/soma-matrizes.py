def soma_matrizes(m1,m2):
    matriz = []
    if len(m1) == len(m2):
        for index in range(len(m1)):
            linha = []
            if len(m1[index]) != len(m2[index]):
                return False
            else:
                for jindex in range(len(m1[index])):
                    linha.append(m1[index][jindex] + m2[index][jindex])

            matriz.append(linha)
        return matriz
    else:
        return False


                
