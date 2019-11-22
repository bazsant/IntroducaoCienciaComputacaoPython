def fatorial(numero):
    fat = 1
    while numero > 1:
        fat = fat * numero
        numero = numero - 1
    return fat

def main():
    numero=0
    while numero >= 0:
        numero=int(input("Digite um número para calcular fatorial. Termine com -1: "))
        if numero >= 0:        
            print("O fatorial de", numero, "é:", fatorial(numero))
    
main()
