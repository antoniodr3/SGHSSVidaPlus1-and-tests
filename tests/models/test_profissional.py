


from PythonVidaPlus1.models.profissional import Profissional

def test_profissional_campos():
    prof = Profissional("Dr. Pedro", "Cardiologia", "CRM12345")
    assert prof.nome == "Dr. Pedro"
    assert prof.especialidade == "Cardiologia"
    assert prof.registro == "CRM12345"

def test_profissional_resumo():
    prof = Profissional("Dr. Pedro", "Cardiologia", "CRM12345")
    resumo = prof.resumo()
    assert "Dr. Pedro" in resumo
    assert "Cardiologia" in resumo
    assert "CRM12345" in resumo
