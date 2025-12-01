


class Paciente:
    def __init__(self, id_, nome, idade, genero, contato):
        self.id = id_
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.contato = contato

    def validar(self):
        return all([self.id, self.nome, self.idade, self.genero, self.contato])
