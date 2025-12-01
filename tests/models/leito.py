


from PythonVidaPlus1.models.leito import Leito

def test_criar_leito():
    leito = Leito("L1")
    assert leito.id == "L1"
    assert leito.ocupado is False

def test_ocupar_e_liberar_leito():
    leito = Leito("L2")
    leito.ocupar()
    assert leito.ocupado is True
    leito.liberar()
    assert leito.ocupado is False

def test_validar_leito():
    leito = Leito("L3")
    assert leito.validar() is True
