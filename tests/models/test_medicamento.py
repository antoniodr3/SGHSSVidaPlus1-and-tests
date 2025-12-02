


from PythonVidaPlus1.models.medicamento import Medicamento

def test_criar_medicamento():
    med = Medicamento("M1", "Paracetamol", 100, 2.5)
    assert med.validar() is True

def test_adicionar_retirar_medicamento():
    med = Medicamento("M1", "Paracetamol", 100, 2.5)
    med.adicionar(50)
    assert med.quantidade == 150
    assert med.retirar(30) is True
    assert med.quantidade == 120
    assert med.retirar(200) is False
