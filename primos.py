def eh_primo(numero):
    primo=True
    variante=numero
    while variante > 2 and primo:    
        if(numero%(variante-1)==0):
            primo=False
        else:
            variante=variante-1

    return primo

def main():
    numero=int(input("Digite um número inteiro > 0:"))
    while numero > 0:        
        print("primo:", eh_primo(numero))
        numero=int(input("Digite o próximo número inteiro > 0:"))

main()
