class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return 'equilátero'
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return 'isósceles'
        else:
            return 'escaleno'

    def retangulo(self):
        return self.a**2 == self.b**2 + self.c**2 or self.b**2 == self.a**2 + self.c**2 or self.c**2 == self.b**2 + self.a**2

    def semelhantes(self, triangulo):
        return self.a/triangulo.a == self.b/triangulo.b and self.b/triangulo.b == self.c/triangulo.c

def test_perimetro():
    t = Triangulo(1,2,3)
    assert t.perimetro() == 6

def test_equilatero():
    t = Triangulo(4,4,4)
    assert t.tipo_lado() == 'equilátero'

def test_isosceles():
    t = Triangulo(4,1,4)
    assert t.tipo_lado() == 'isósceles'

def test_isosceles_2():
    t = Triangulo(4,4,1)
    assert t.tipo_lado() == 'isósceles'

def test_isosceles_3():
    t = Triangulo(1,4,4)
    assert t.tipo_lado() == 'isósceles'

def test_escaleno():
    t = Triangulo(2,1,4)
    assert t.tipo_lado() == 'escaleno'

def test_triangulo_retangulo_true1():
    t = Triangulo(5,3,4)
    assert t.retangulo() == True

def test_triangulo_retangulo_true():
    t = Triangulo(3,4,5)
    assert t.retangulo() == True
    
def test_triangulo_retangulo_false():
    t = Triangulo(1,3,5)
    assert t.retangulo() == False

def test_semelhantes_true():
    t1 = Triangulo(2, 2, 2)
    t2 = Triangulo(4, 4, 4)
    assert t1.semelhantes(t2) == True

def test_semelhantes_false():
    t1 = Triangulo(2, 2, 2)
    t2 = Triangulo(3, 4, 3)
    assert t1.semelhantes(t2) == False
