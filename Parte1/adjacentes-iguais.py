numero=int(input())
adjacentesIguais = False
ultimoNumero = numero%10

while not adjacentesIguais and numero!=0:
    numero=numero//10
    adjacentesIguais=ultimoNumero==numero%10
    ultimoNumero = numero%10
if adjacentesIguais:
    print("sim")
else:
    print("não")
    
