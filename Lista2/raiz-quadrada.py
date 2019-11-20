import math

a=float(input())
b=float(input())
c=float(input())

delta = b**2 - (4 * a * c)
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    raizPosit = ((-b) + math.sqrt(delta))/ (2*a)
    if delta == 0:
        print("a raiz desta equação é", raizPosit)
    else:    
        raizNegat = ((-b) - math.sqrt(delta))/ (2*a)
        if(raizPosit>raizNegat):
            print("as raízes da equação são", raizNegat, "e", raizPosit)
        else:
            print("as raízes da equação são", raizPosit, "e", raizNegat)
    
    
