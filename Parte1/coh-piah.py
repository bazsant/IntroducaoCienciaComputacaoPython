import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0

    for indice in range(0,6):
        calc = as_a[indice] - as_b[indice]
        if calc < 0:
            calc = calc * -1

        soma = soma + calc

    #print('soma:',soma)
    
    valor = soma / 6

    #print('valor:',valor)
    
    if valor < 0:
        valor = valor * -1
    
    return valor

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    palavras = []
    tamanhoPalavras = 0
    frases = []
    
    for sentenca in sentencas:
        frases = frases + separa_frases(sentenca)        

    for frase in frases:
        palavras = palavras + separa_palavras(frase)
            
    for pal in palavras:
        tamanhoPalavras = tamanhoPalavras + len(pal)

    palavrasDiferentes = n_palavras_diferentes(palavras)
    palavrasUnicas = n_palavras_unicas(palavras)

    qtCaracteresSent = len(re.sub('[.!?]', '', texto))
    qtCaracteresFras = len(re.sub('[,:;.!?]', '', texto))
    
    wal = tamanhoPalavras / len(palavras)
    ttr = palavrasDiferentes / len(palavras)
    hlr = palavrasUnicas / len(palavras)
    sal = qtCaracteresSent / len(sentencas)
    sac = len(frases) / len(sentencas)
    pal = qtCaracteresFras / len(frases)

    #print('texto:', [wal, ttr, hlr, sal, sac, pal])
    
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    probCopia = []
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        probCopia.append(compara_assinatura(assinatura, ass_cp))
        
    print('probCopia:',probCopia)
    sabMenor =  probCopia[0]
    textoEscolhido = 1
    for indice in range(1, len(probCopia)):
        if probCopia[indice] < sabMenor:
            textoEscolhido = indice + 1

    return textoEscolhido

def main():
    assinaturaPadrao = le_assinatura()    
    textos = le_textos()
    print('O autor do texto', avalia_textos(textos, assinaturaPadrao),'está infectado com COH-PIAH')
    
def mock():
    #ass1 = [4.34, 0.05, 0.02, 12.81, 2.16, 0.0]
    #ass2 = [3.96, 0.05, 0.02, 22.22, 3.41, 0.0]

    #print(compara_assinatura(ass1, ass2))
    
    #assinaturaPadrao = [4.5,0.60,0.35,85.0,2.0,40.5]
    #assinaturaPadrao = [4.79,0.72,0.56,80.5,2.5,31.6]
    #assinaturaPadrao = [5.0, 0.75, 0.6, 465.0, 10.0, 45.0]

    #print('ass_padrao:', assinaturaPadrao)

    #textos = ['Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.',
    #         'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.',
    #          'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.']
    #print('O autor do texto', avalia_textos(textos, assinaturaPadrao),'está infectado com COH-PIAH')
    pass

main()

