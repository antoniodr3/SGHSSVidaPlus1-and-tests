

# Cartão de triagem (paciente na fila)
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero   # Número do cartão
        self.cor = cor         # Cor do cartão ___ A = Amarelo , V = Verde
        self.proximo = None    # Ponteiro para próximo da fila
