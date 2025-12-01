


from PythonVidaPlus1.models.consulta import Consulta

def test_consulta_campos():
    consulta = Consulta("Maria", "Dr. Carlos", "2025-12-01", "Dor de cabeça")
    assert consulta.paciente == "Maria"
    assert consulta.profissional == "Dr. Carlos"
    assert consulta.data == "2025-12-01"
    assert consulta.motivo == "Dor de cabeça"

def test_consulta_resumo():
    consulta = Consulta("Maria", "Dr. Carlos", "2025-12-01", "Dor de cabeça")
    resumo = consulta.resumo()
    assert "Maria" in resumo
    assert "Dr. Carlos" in resumo
    assert "2025-12-01" in resumo
    assert "Dor de cabeça" in resumo
