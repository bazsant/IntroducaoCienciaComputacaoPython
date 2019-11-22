largura=int(input("Digite a largura: "))
altura=int(input("Digite a altura: "))
i = 1
while i <= altura:
    j = 1
    while j <= largura:
        if j == 1 or j == largura or i == 1 or i == altura:
            print("#", end="")
        else:
            print(" ", end="")
        j = j + 1
    print()
    i = i + 1
    
