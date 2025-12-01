


from estado import Estado
class ListaEncadeada:
    def __init__(self):
        self.head = None  #Ponteiro pro inicio da lista

    def inserir(self, sigla, nome):
        novo_estado = Estado(sigla, nome)  #Cria novo nodo
        novo_estado.proximo = self.head   #move o head
        self.head = novo_estado     # Inseri no inicio

    def imprimir(self):
        atual = self.head   #Percorre a lista e coleta as siglas
        siglas = []
        while atual:
            siglas.append(atual.sigla)
            atual = atual.proximo

        # Retorna as siglas separadas por "->" ou "Vazia"
        return ' -> '.join(siglas) if siglas else 'Vazia'

