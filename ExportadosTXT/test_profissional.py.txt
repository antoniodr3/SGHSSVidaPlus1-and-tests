


from PythonVidaPlus1.models.profissional import Profissional

def test_profissional_assinatura(profissional_cardio):
    assinatura = profissional_cardio.assinatura()
    assert "Dra. Ana" in assinatura
    assert "Cardiologia" in assinatura
    assert "CRM123" in assinatura
