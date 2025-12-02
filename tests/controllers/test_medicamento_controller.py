


from PythonVidaPlus1.controllers.medicamento_controller import MedicamentoController

def test_criar_medicamento_controller():
    controller = MedicamentoController()
    med = controller.criar_medicamento("M1", "Ibuprofeno", 200, 3.0)
    assert med.nome == "Ibuprofeno"

def test_adicionar_retirar_controller():
    controller = MedicamentoController()
    med = controller.criar_medicamento("M1", "Ibuprofeno", 200, 3.0)
    controller.adicionar_estoque(med, 50)
    assert med.quantidade == 250
    assert controller.retirar_estoque(med, 100) is True
    assert med.quantidade == 150
