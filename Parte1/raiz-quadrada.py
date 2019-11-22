import math

def obterDelta(a,b,c):
    return b**2 - (4 * a * c)

def obterRaiz(a,b,delta,positiva):
    if positiva:
        return ((-b) + math.sqrt(delta))/ (2*a)
    else:
        return ((-b) - math.sqrt(delta))/ (2*a)

def mostrarRaizes(a,b,delta):
    raizPosit = obterRaiz(a,b,delta,True)
    if delta == 0:
        print("a raiz desta equação é", raizPosit)
    else:    
        raizNegat = obterRaiz(a,b,delta,False)
        if(raizPosit>raizNegat):
            print("as raízes da equação são", raizPosit, "e", raizNegat)
        else:
            print("as raízes da equação são", raizNegat, "e", raizPosit)

def bhaskara(a,b,c):    
    delta = obterDelta(a,b,c)
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        mostrarRaizes(a,b,delta)    

def main():
    a=float(input())
    b=float(input())
    c=float(input())

    bhaskara(a,b,c)

main()
