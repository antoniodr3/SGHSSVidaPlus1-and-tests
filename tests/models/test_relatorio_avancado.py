


from PythonVidaPlus1.models.relatorio_avancado import RelatorioAvancado
from PythonVidaPlus1.models.unidade_hospitalar import UnidadeHospitalar
from PythonVidaPlus1.models.leito import Leito
from PythonVidaPlus1.models.financeiro import Financeiro

def test_taxa_ocupacao_media():
    unidade = UnidadeHospitalar("U1", "Hospital Central", "Rua A, 123")
    unidade.adicionar_leito(Leito("L1", "UTI", ocupado=True))
    unidade.adicionar_leito(Leito("L2", "Enfermaria", ocupado=False))
    financeiro = Financeiro()
    relatorio = RelatorioAvancado([unidade], [], [], financeiro)
    assert relatorio.taxa_ocupacao_media() == 50.0

def test_total_consultas():
    financeiro = Financeiro()
    relatorio = RelatorioAvancado([], [], ["Consulta1", "Consulta2"], financeiro)
    assert relatorio.total_consultas() == 2

def test_custos_totais():
    financeiro = Financeiro()
    financeiro.registrar_transacao("Exame", 200.0)
    financeiro.registrar_transacao("Internação", 500.0)
    relatorio = RelatorioAvancado([], [], [], financeiro)
    assert relatorio.custos_totais() == 700.0

def test_validar_relatorio_avancado():
    financeiro = Financeiro()
    relatorio = RelatorioAvancado([], [], [], financeiro)
    assert relatorio.validar() is True
