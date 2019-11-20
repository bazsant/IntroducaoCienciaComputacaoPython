numero=int(input("Digite um número inteiro: "))
primo=True
variante=numero
while variante>2 and primo:    
    if(numero%(variante-1)==0):
        primo=False
    else:
        variante=variante-1
if primo:
    print("primo")
else:
    print("não primo")
