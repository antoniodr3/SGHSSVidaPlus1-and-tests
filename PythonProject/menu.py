


from lista_espera import ListaEspera

    #  Função principal
def menu():
    fila = ListaEspera()
    while True:  #Loop principal com escolhas ao usuário
        print("\nMenu: \nEscolha umas das opções abaixo:")
        print("1 - Adicionar paciente na fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()
        # Ações de encolha do usuário
        if opcao == "1":
            fila.inserir()
        elif opcao == "2":
            fila.imprimirListaEspera()
        elif opcao == "3":
            fila.atenderPaciente()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")
