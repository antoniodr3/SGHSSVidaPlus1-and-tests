


from PythonVidaPlus1.models.unidade_hospitalar import UnidadeHospitalar
from PythonVidaPlus1.models.leito import Leito
from PythonVidaPlus1.models.internacao import Internacao
from PythonVidaPlus1.models.paciente import Paciente
from PythonVidaPlus1.models.profissional import Profissional

def test_criar_unidade():
    unidade = UnidadeHospitalar("U1", "Hospital Central", "Rua A, 123")
    assert unidade.validar() is True
    assert unidade.nome == "Hospital Central"

def test_adicionar_leito_unidade():
    unidade = UnidadeHospitalar("U1", "Hospital Central", "Rua A, 123")
    leito = Leito("L1", "UTI")
    unidade.adicionar_leito(leito)
    assert leito in unidade.listar_leitos()

def test_adicionar_internacao_unidade():
    unidade = UnidadeHospitalar("U1", "Hospital Central", "Rua A, 123")
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("Dr. Ana", "Clínico Geral", "CRM123")
    leito = Leito("L1", "UTI")
    internacao = Internacao(paciente, profissional, leito, "2025-12-01")
    unidade.adicionar_internacao(internacao)
    assert internacao in unidade.listar_internacoes()
