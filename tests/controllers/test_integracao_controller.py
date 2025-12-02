


from PythonVidaPlus1.controllers.integracao_controller import IntegracaoController

def test_criar_integracao_controller():
    controller = IntegracaoController()
    integracao = controller.criar_integracao("Laboratório XYZ", "laboratorio", "https://labxyz.com/api")
    assert integracao.sistema == "Laboratório XYZ"

def test_conectar_controller():
    controller = IntegracaoController()
    integracao = controller.criar_integracao("Convênio ABC", "convenio", "https://convenioabc.com/api")
    controller.conectar(integracao)
    assert integracao.status == "conectado"

def test_desconectar_controller():
    controller = IntegracaoController()
    integracao = controller.criar_integracao("API Externa", "api", "https://apiexterna.com")
    controller.conectar(integracao)
    controller.desconectar(integracao)
    assert integracao.status == "desconectado"

def test_validar_integracao_controller():
    controller = IntegracaoController()
    integracao = controller.criar_integracao("Laboratório XYZ", "laboratorio", "https://labxyz.com/api")
    assert controller.validar(integracao) is True
