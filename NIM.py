def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("Você começa!")
    else:
        print("Computador começa!")
        n = n - computador_escolhe_jogada(n, m)
        pecasRestante(n)

    while n > 0:
        n = n - usuario_escolhe_jogada(n, m)
        pecasRestante(n)
        n = n - computador_escolhe_jogada(n, m)
        pecasRestante(n)

    print("Fim do jogo! O computador ganhou!")


def pecasRestante(n):
    if n > 1:
        print("Agora restam", n, "peças no tabuleiro.")
    elif n == 1:
        print("Agora resta apenas uma peça no tabuleiro.")


def usuario_escolhe_jogada(n, m):
    valido = False
    jogada = 0
    while not valido:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada > m:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            if jogada > 1:
                print("Você tirou", jogada, "peças.")
            else:
                print("Você tirou", jogada, "peça.")
            valido = True
    return jogada


def computador_escolhe_jogada(n, m):
    pecasTiradas = m

    multiplo = False

    while not multiplo and m > 0:
        if (n-m)%(m+1)==0:
            pecasTiradas = m
            multiplo=True
        else:
            m = m - 1

    if pecasTiradas > 1:
        print("O computador retirou", pecasTiradas, "peças.")
    else:
        print("O computador retirou", pecasTiradas, "peça.")

    return pecasTiradas


def campeonato():

    quantidadeRodadas = 3
    rodada = 1

    while rodada <= quantidadeRodadas:
        print("**** Rodada", rodada, "****")
        partida()
        rodada = rodada + 1

    print("**** Final do campeonato ****")

    print("Placar: Você 0 X", quantidadeRodadas,"Computador")


def main():
    print("Bem vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))

    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    else:
        print("Você escolheu um campeonato!")
        campeonato()

main()
