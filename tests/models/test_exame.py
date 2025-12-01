


from PythonVidaPlus1.models.exame import Exame

def test_exame_campos():
    exame = Exame("João", "Dra. Ana", "Hemograma")
    assert exame.paciente == "João"
    assert exame.solicitante == "Dra. Ana"
    assert exame.tipo == "Hemograma"

def test_exame_descricao():
    exame = Exame("João", "Dra. Ana", "Hemograma")
    desc = exame.descricao()
    assert "Hemograma" in desc
    assert "João" in desc
    assert "Dra. Ana" in desc
