import psutil
from collections import defaultdict

def gerenciar_processos():
    print("\n🔍\tAgrupando processos por aplicativo:\n")

    apps_destaque = ['chrome.exe', 'spotify.exe', 'Code.exe', 'notepad.exe', 'explorer.exe', 'msedge.exe', 'WhatsApp.exe', 'ChatGPT.exe']

    grupos = defaultdict(list)

    # Agrupar por nome
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            nome = proc.info['name']
            grupos[nome].append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processos_ativos = list(grupos.keys())

    # Separar em duas categorias
    apps_visiveis = []
    processos_fundo = []

    for nome in processos_ativos:
        if nome.lower() in [a.lower() for a in apps_destaque]:
            apps_visiveis.append(nome)
        else:
            processos_fundo.append(nome)

    indice_total = 0
    mapa_indices = {}

    print("🟦\tAplicativos abertos:\n")
    for nome in apps_visiveis:
        print(f"[{indice_total}] - {nome} ({len(grupos[nome])} processos)")
        mapa_indices[str(indice_total)] = nome
        indice_total += 1

    print("\n⚙️\tProcessos em segundo plano:\n")
    for nome in processos_fundo:
        print(f"[{indice_total}] - {nome} ({len(grupos[nome])} processos)")
        mapa_indices[str(indice_total)] = nome
        indice_total += 1

    print("\nDigite oo numero do grupo que deseja finalizar ou pressione Enter para voltar.")
    escolha = input("Escolha: ")

    if escolha in mapa_indices:
        nome_escolhido = mapa_indices[escolha]
        confirm = input(f"Tem certeza que deseja finalizar todos os processos de '{nome_escolhido}'? (S/N): ")
        if confirm == 's':
            for proc in grupos[nome_escolhido]:
                try:
                    proc.terminate()
                except Exception as e:
                    print(f"Erro ao finalizar PID {proc.pid}: {e}")
            print(f"✅\tProcessos de '{nome_escolhido}' finalizados.")
        else:
            print("❌\tCancelado")
    else:
        print("Retornando ao menu...")