


from PythonVidaPlus1.controllers.exame_controller import ExameController

def test_criar_exame():
    ctrl = ExameController()
    exame = ctrl.criar_exame("João", "Dra. Ana", "Hemograma")
    assert exame.tipo == "Hemograma"

def test_validar_exame_ok():
    ctrl = ExameController()
    exame = ctrl.criar_exame("João", "Dra. Ana", "Hemograma")
    assert ctrl.validar(exame) is True

def test_validar_exame_falha():
    ctrl = ExameController()
    exame = ctrl.criar_exame("", "Dra. Ana", "Hemograma")
    assert ctrl.validar(exame) is False
