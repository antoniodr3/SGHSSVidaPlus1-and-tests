


from tabela_hash import TabelaHash
from estados_bb import estados

def main():
    tabela = TabelaHash()  #Cria a tabela vazia
    print("Tabela Hash (inicialmente vazia):") #imprime a tabela vazia antes de inserção de dados
    tabela.imprimir()

    for sigla, nome in estados:  # Insere todos os estados na tabela
        tabela.inserir(sigla, nome)
    print("\nTabela Hash (com dados inseridos):")
    tabela.imprimir()

if __name__ == "__main__": #Garante que o main será executado apenas ao rodar o arquivo
    main()