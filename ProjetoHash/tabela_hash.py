

from lista_encadeada import ListaEncadeada

class TabelaHash:
    def __init__(self):
        self.tabela = [ListaEncadeada() for _ in range(10)] #cria tabela com 10 listas

    def funcao_hash(self, sigla):
        if sigla.upper() == 'DF':
            return 7
        ascii_soma = ord(sigla[0].upper()) + ord(sigla[1].upper()) #Calcula a soma ASCII das letras
        return ascii_soma % 10  #Aplica o MOD 10

    def inserir(self, sigla, nome):
        indice = self.funcao_hash(sigla)   # Usa a função hash
        self.tabela[indice].inserir(sigla, nome) # Insere o estado na lista

    def imprimir(self):
        # Exibe cada posição da tabela e sua lista encadeada
        for i, lista in enumerate(self.tabela):
            print(f'[{i}] {lista.imprimir()}')

