import random

class Ordenador:

    def __init__(self):
        self.lista = []
        pass

    def appendRange(self, lista):
        self.lista = lista[:]
    
    def ordenar(self, crescente):
        final = len(self.lista)

        for i in range(final):
            menorValor = i

            for j in range(i+1,final):
                if (crescente and self.lista[menorValor] > self.lista[j]) or (not crescente and self.lista[menorValor] < self.lista[j]):
                    menorValor = j

            self.lista[i], self.lista[menorValor] = self.lista[menorValor], self.lista[i]
        self.lista

    def criarLista(self, tamanho):
        lista = []
        for i in range(tamanho):
            lista.append(random.randint(1,10000))
        return lista

    def isCrescente(self):
        crescente = True

        for item in range(1,len(self.lista)):
            if self.lista[item] < self.lista[item-1]:
                crescente = False
                break

        return crescente

    def isDecrescente(self):
        decrescente = True

        for item in range(1,len(self.lista)):
            if self.lista[item] > self.lista[item-1]:
                decrescente = False
                break

        return decrescente
            
