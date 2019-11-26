def menor_nome(nomes):
    menorNome = nomes[0].strip()
    
    for item in nomes:
        nome = item.strip()
        if len(nome.strip().lower()) < len(menorNome.strip().lower()):
            menorNome = nome
    return menorNome.capitalize()

def test_menor_nome():
    assert menor_nome([' claudio','enzo','   ana ', ' jefferson', 'rafael   ']) == 'Ana'
