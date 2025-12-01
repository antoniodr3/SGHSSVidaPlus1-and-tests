


from PythonVidaPlus1.models.profissional import Profissional

class ProfissionalController:
    def criar_profissional(self, nome: str, especialidade: str, registro: str) -> Profissional:
        return Profissional(nome, especialidade, registro)

    def validar(self, profissional: Profissional) -> bool:
        return all([profissional.nome, profissional.especialidade, profissional.registro])
