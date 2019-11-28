import matrz

def soma_matrizes(matA, matB):
    numLinhas=len(matA)
    numCols=len(matA[0])

    matC = matrz.cria_matriz(numLinhas, numCols, 0)

    for i in range(numLinhas):
        for j in range(numCols):
            matC[i][j] = matA[i][j] + matB[i][j]
    return matC

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[7,8,9]]
    B = [[10,20,30],[40,50,60],[70,80,90]]
    print(soma_matrizes(A,B))
