


import pytest
from PythonVidaPlus1.models.consulta import Consulta
from PythonVidaPlus1.models.exame import Exame
from PythonVidaPlus1.models.profissional import Profissional

@pytest.fixture
def consulta_basica():
    return Consulta("João", "Dra. Ana", "2025-12-01 10:00")

@pytest.fixture
def exame_basico():
    return Exame("João", "Dra. Ana", "Hemograma")

@pytest.fixture
def profissional_cardio():
    return Profissional(
        id_="p1",
        nome="Dra. Ana",
        registro="CRM123",
        especialidade="Cardiologia",
        cargo="Médica",
    )
