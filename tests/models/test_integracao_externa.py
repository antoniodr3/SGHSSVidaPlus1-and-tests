


from PythonVidaPlus1.models.integracao_externa import IntegracaoExterna

def test_criar_integracao_externa():
    integracao = IntegracaoExterna("Laboratório XYZ", "laboratorio", "https://labxyz.com/api")
    assert integracao.validar() is True
    assert integracao.status == "desconectado"

def test_conectar_desconectar_integracao():
    integracao = IntegracaoExterna("Convênio ABC", "convenio", "https://convenioabc.com/api")
    integracao.conectar()
    assert integracao.status == "conectado"
    integracao.desconectar()
    assert integracao.status == "desconectado"

def test_validar_integracao_invalida():
    integracao = IntegracaoExterna("", "", "")
    assert integracao.validar() is False
