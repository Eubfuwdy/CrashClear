def exibir_menu():
    print("\n💀 === Crash Clear === 💀")
    print("============================")
    print("[1] - Limpar arquivos temporarios")
    print("[2] - Limpar navegadores")
    print("[3] - Esvaziar lixeira")
    print("[4] - Verificar uso de CPU e RAM")
    print("[5] - Gerenciar processos (Listar e Finalizar)")
    print("[0] - Sair")


def escolher_opcao():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            from limpeza.limpar_temporarios import limpar_temporarios
            limpar_temporarios()
        elif opcao == "2":
            from limpeza.limpar_navegadores import limpar_navegadores
            limpar_navegadores()
        elif opcao == "3":
            from limpeza.esvaziar_lixeira import esvaziar_lixeira
            esvaziar_lixeira()
        elif opcao == "4":
            print("📈 Verificando uso de CPU e RAM...")
            from desempenho.uso_sistema import exibir_monitoramento
            exibir_monitoramento()
        elif opcao == "5":
            print("📋 Listando processos e permitindo finalizacao...")
            from desempenho.gerenciar_processos import gerenciar_processos
            gerenciar_processos()
        elif opcao == "0":
            print("Saindo do Crash Clear...")
            break
        else:
            print("Opcao invalida. Tente novamente.")