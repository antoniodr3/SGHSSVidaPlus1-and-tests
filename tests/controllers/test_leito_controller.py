


from PythonVidaPlus1.controllers.leito_controller import LeitoController

def test_criar_e_ocupar_leito_controller():
    controller = LeitoController()
    leito = controller.criar_leito("L1")
    assert controller.validar(leito) is True
    controller.ocupar(leito)
    assert leito.ocupado is True
    controller.liberar(leito)
    assert leito.ocupado is False
