import psutil
import os
import sys
import time
import threading

# Variavel de controle
parar_monitoramento = False

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def barra(valor, total=100, tamanho=25):
    proporcao = min(valor / total, 1)
    preenchido = int(proporcao * tamanho)
    vazio = tamanho - preenchido
    return '[' + '#' * preenchido + '-' * vazio + f'] {valor:.1f}%'

def pressionar_enter():
    global parar_monitoramento
    input()
    parar_monitoramento = True

def formatar_gb(valor_bytes):
    return round(valor_bytes / (1024 ** 3), 1)

def exibir_monitoramento():
    global parar_monitoramento
    parar_monitoramento = False

    threading.Thread(target=pressionar_enter, daemon=True).start()

    try:
        while not parar_monitoramento:
            limpar_tela()

            uso_cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory()
            swap = psutil.swap_memory()
            disco = psutil.disk_usage('/')

            print("Monitoramento do Sistema")
            print("========================\n")
            print(f"🧠 CPU  | {barra(uso_cpu)}")
            print(f"💾 RAM  | {barra(ram.percent)} - Usado: {formatar_gb(ram.used)} GB / Total: {formatar_gb(ram.total)} GB")
            print(f"📂 SWAP | {barra(swap.percent)}")
            print(f"💽 DISCO| {barra(disco.percent)} - Usado: {formatar_gb(disco.used)} GB / Total: {formatar_gb(disco.total)} GB")
            print("\nLegenda: '#' = uso | '-' = livre")
            print("Aperte Enter para sair...") 

            time.sleep(1)

    except KeyboardInterrupt:
        parar_monitoramento = True
        print("Retornando ao menu...")