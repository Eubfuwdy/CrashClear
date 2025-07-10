import winshell

def esvaziar_lixeira():
    print("\n🗑️\tEsvaziando a lixeira...")

    try:
        itens = list(winshell.recycle_bin())

        if not itens:
            print("⚠️\tA lixeira esta vazia.")
            return

        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        print("✅\tLixeira esvaziada com sucesso!")

    except Exception as e:
        print(f"❌\tErro ao esvaziar lixeira: {e}")