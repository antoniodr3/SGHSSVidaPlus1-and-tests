


from PythonVidaPlus1.controllers.seguranca_controller import SegurancaController

def test_criar_usuario_controller():
    controller = SegurancaController()
    usuario = controller.criar_usuario("u1", "Maria", "admin")
    assert usuario.perfil == "admin"

def test_validar_usuario_controller():
    controller = SegurancaController()
    usuario = controller.criar_usuario("u2", "Carlos", "profissional")
    assert controller.validar_usuario(usuario) is True

def test_registrar_acao_controller():
    controller = SegurancaController()
    usuario = controller.criar_usuario("u3", "Ana", "paciente")
    controller.registrar_acao(usuario, "Agendamento criado")
    logs = controller.listar_logs()
    assert any("Agendamento criado" in log["acao"] for log in logs)
