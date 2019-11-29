import ordenador
import pytest

class TestaOrdenador:
    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()

    def test_ordenar_cresc(self, o):
        lista = o.criarLista(10)
        o.appendRange(lista)
        o.ordenar(True)
        assert o.isCrescente()

    def test_ordenar_descresc(self, o):
        lista = o.criarLista(10)
        o.appendRange(lista)
        o.ordenar(False)
        assert o.isDecrescente()
