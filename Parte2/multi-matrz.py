def retornaValor(linha, coluna, matA, matB):
    qtd = len(matB)
    valor = 0
    for i in range(qtd):
        valor += matA[linha][i]*matB[i][coluna]

    return valor

def mult_matriz(matA, matB):
    matC = []    
    for linha in range(len(matA)):
        linhas = []
        for coluna in range(len(matB[0])):
            linhas.append(retornaValor(linha, coluna, matA, matB))
        matC.append(linhas)
        

    return matC

if __name__ == '__main__':
    A = [[2,3],[0,1],[-1,4]]
    B = [[1,2,3],[-2,0,4]]
    C = [[1,2,3,4,5],[2,3,4,5,6]]
    D = [[2,3],[2,5],[5,2],[5,7],[6,8]]
    E = [[2,3,1],[-1,0,2]]
    F = [[1,-2],[0,5],[4,1]]
    print(mult_matriz(A,B))
    print(mult_matriz(B,A))
    print(mult_matriz(C,D))
    print(mult_matriz(E,F))
