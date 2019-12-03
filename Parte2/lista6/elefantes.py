def incomodam(n):
    if n == 0:
        return ""
    else:
        return "incomodam " + incomodam(n-1)

def elefantes(n, indice = 1):
    prefixo = "\n" + str(indice) + " elefantes incomodam muita gente\n"
    sufixo = str(indice+1) + " elefantes " + incomodam(indice+1) + " muito mais"

    if indice == n:
        return ""
    elif indice == 1:
        return "Um elefante incomoda muita gente\n"  + sufixo + elefantes(n, indice + 1)
    else:
        return prefixo  + sufixo + elefantes(n, indice + 1)
