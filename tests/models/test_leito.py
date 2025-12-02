


from PythonVidaPlus1.models.leito import Leito

def test_criar_leito():
    leito = Leito("L1", "UTI")
    assert leito.id == "L1"
    assert leito.tipo == "UTI"
    assert leito.ocupado is False

def test_ocupar_liberar_leito():
    leito = Leito("L1", "UTI")
    leito.ocupar()
    assert leito.ocupado is True
    leito.liberar()
    assert leito.ocupado is False

def test_validar_leito_valido():
    leito = Leito("L1", "UTI")
    assert leito.validar() is True

def test_validar_leito_invalido():
    leito = Leito("", "")
    assert leito.validar() is False
