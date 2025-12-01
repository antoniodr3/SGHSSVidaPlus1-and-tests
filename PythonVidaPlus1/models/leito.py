


class Leito:
    def __init__(self, id_, ocupado=False):
        self.id = id_
        self.ocupado = ocupado

    def ocupar(self):
        self.ocupado = True

    def liberar(self):
        self.ocupado = False

    def validar(self):
        return self.id is not None
