


from PythonVidaPlus1.models.usuario import Usuario

def test_criar_usuario_valido():
    usuario = Usuario("u1", "João", "paciente")
    assert usuario.validar() is True

def test_criar_usuario_invalido():
    usuario = Usuario("", "", "")
    assert usuario.validar() is False
