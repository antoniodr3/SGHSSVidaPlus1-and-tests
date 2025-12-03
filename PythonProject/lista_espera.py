


from nodo import Nodo
from cores import AMARELO, VERDE, RESET


# Classe Usando lista encadeada que gerencia a fila de espera
class ListaEspera:
    def __init__(self):
        self.head = None   #inicio
        self.contador_verde = 1   # Contado cartão verde ( < para > )
        self.contador_amarelo = 201   # Contado cartão amarelo ( > para < )

        #Insere paciente ao final da fila ( sem prioridade )
    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo   # Fila livre
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo    # Adiciona ao fim da fila

        # Insere paciente com prioridade antes do Verdes
    def inserirComPrioridade(self, nodo):
        if not self.head or self.head.cor == "V":
            nodo.proximo = self.head   #Insere do inicio se estiver livre
            self.head = nodo
        else:
            atual = self.head   #Insere depois do ultimo Amarelo
            while atual.proximo and atual.proximo.cor == "A":
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

        # Inserir pacientes
    def inserir(self):
        cor = input("Informe a cor do cartão (A/V): ").strip().upper()
        if cor == "A":
            numero = self.contador_amarelo
            self.contador_amarelo += 1
        elif cor == "V":
            numero = self.contador_verde
            self.contador_verde += 1
        else:
            print("Cor inválida.")
            return

        nodo = Nodo(numero, cor)
        if not self.head:
            self.head = nodo
        elif cor == "V":
            self.inserirSemPrioridade(nodo)
        else:
            self.inserirComPrioridade(nodo)

        # Imprime pacientes na ordem
    def imprimirListaEspera(self):
        if not self.head:
            print("Fila vazia.")
            return
        atual = self.head
        print("\n--- Lista de Espera ---")
        while atual:
            cor_nome = f"{AMARELO}Amarelo{RESET}" if atual.cor == "A" else f"{VERDE}Verde{RESET}"
            print(f"Cartão {cor_nome} - Número {atual.numero}")
            atual = atual.proximo
        print("------------------------")

        #Remove primeiro da lista e o indica
    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila.")
            return
        atendido = self.head
        self.head = self.head.proximo  #segue para prox nodo.
        cor = f"{AMARELO}Amarelo{RESET}" if atendido.cor == "A" else f"{VERDE}Verde{RESET}"
        print(f"Chamando paciente do cartão {cor} número {atendido.numero} para atendimento.")
