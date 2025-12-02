


from PythonVidaPlus1.controllers.governanca_controller import GovernancaController

def test_registrar_backup_controller():
    c = GovernancaController()
    c.registrar_backup("Backup semanal")
    assert any("Backup semanal" in b["descricao"] for b in c.listar_backups())

def test_registrar_atualizacao_controller():
    c = GovernancaController()
    c.registrar_atualizacao("Patch de correção")
    assert any("Patch de correção" in a["descricao"] for a in c.listar_atualizacoes())

def test_registrar_suporte_controller():
    c = GovernancaController()
    c.registrar_suporte("Atendimento remoto")
    assert any("Atendimento remoto" in s["descricao"] for s in c.listar_suporte())

def test_validar_governanca_controller():
    c = GovernancaController()
    assert c.validar() is True
