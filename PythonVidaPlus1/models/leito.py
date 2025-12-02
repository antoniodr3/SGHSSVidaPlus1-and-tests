


class Leito:
    def __init__(self, id_: str, tipo: str, ocupado: bool = False):
        self.id = id_
        self.tipo = tipo  # Ex: "UTI", "Enfermaria", "Apartamento"
        self.ocupado = ocupado

    def ocupar(self):
        self.ocupado = True

    def liberar(self):
        self.ocupado = False

    def validar(self) -> bool:
        return bool(self.id and self.tipo)
