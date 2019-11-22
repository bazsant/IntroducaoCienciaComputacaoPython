largura=int(input("Digite a largura: "))
altura=int(input("Digite a altura: "))
i = 1
while i <= altura:
    j = 1
    while j <= largura:
        print("#", end="")
        j = j + 1
    print()
    i = i + 1
    
