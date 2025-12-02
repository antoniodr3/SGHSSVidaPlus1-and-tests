


from PythonVidaPlus1.models.auditoria import Auditoria

def test_registrar_log():
    auditoria = Auditoria()
    auditoria.registrar("João", "Login no sistema")
    logs = auditoria.listar_logs()
    assert len(logs) == 1
    assert logs[0]["usuario"] == "João"
    assert "Login no sistema" in logs[0]["acao"]

def test_validar_auditoria():
    auditoria = Auditoria()
    assert auditoria.validar() is True
