


from PythonVidaPlus1.models.governanca import Governanca

def test_registrar_backup():
    g = Governanca()
    g.registrar_backup("Backup diário")
    assert len(g.listar_backups()) == 1
    assert "Backup diário" in g.listar_backups()[0]["descricao"]

def test_registrar_atualizacao():
    g = Governanca()
    g.registrar_atualizacao("Atualização de segurança")
    assert len(g.listar_atualizacoes()) == 1
    assert "Atualização de segurança" in g.listar_atualizacoes()[0]["descricao"]

def test_registrar_suporte():
    g = Governanca()
    g.registrar_suporte("Chamado técnico")
    assert len(g.listar_suporte()) == 1
    assert "Chamado técnico" in g.listar_suporte()[0]["descricao"]

def test_validar_governanca():
    g = Governanca()
    assert g.validar() is True
