


from PythonVidaPlus1.controllers.leito_controller import LeitoController

def test_criar_leito_controller():
    controller = LeitoController()
    leito = controller.criar_leito("L1", "UTI")
    assert leito.tipo == "UTI"

def test_ocupar_liberar_leito_controller():
    controller = LeitoController()
    leito = controller.criar_leito("L1", "UTI")
    controller.ocupar_leito(leito)
    assert leito.ocupado is True
    controller.liberar_leito(leito)
    assert leito.ocupado is False

def test_validar_leito_controller():
    controller = LeitoController()
    leito = controller.criar_leito("L1", "UTI")
    assert controller.validar(leito) is True
