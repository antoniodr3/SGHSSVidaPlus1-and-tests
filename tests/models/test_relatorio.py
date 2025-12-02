


from PythonVidaPlus1.models.relatorio import Relatorio
from PythonVidaPlus1.models.leito import Leito
from PythonVidaPlus1.models.internacao import Internacao
from PythonVidaPlus1.models.paciente import Paciente
from PythonVidaPlus1.models.profissional import Profissional

def test_relatorio_leitos():
    leito1 = Leito("L1", "UTI", ocupado=True)
    leito2 = Leito("L2", "Enfermaria", ocupado=False)
    relatorio = Relatorio([leito1, leito2], [])
    assert relatorio.total_leitos() == 2
    assert relatorio.leitos_ocupados() == 1
    assert relatorio.leitos_disponiveis() == 1

def test_relatorio_pacientes_internados():
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("Dr. Ana", "Clínico Geral", "CRM123")
    leito = Leito("L1", "UTI", ocupado=True)
    internacao = Internacao(paciente, profissional, leito, "2025-12-01")
    relatorio = Relatorio([leito], [internacao])
    assert paciente in relatorio.pacientes_internados()

def test_validar_relatorio():
    relatorio = Relatorio([], [])
    assert relatorio.validar() is True
