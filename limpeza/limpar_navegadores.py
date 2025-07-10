import os
import shutil
import psutil

def navegador_aberto(nome_processo):
    nome_processo = nome_processo.lower()
    for proc in psutil.process_iter(['name']): 
        try:
            nome = proc.info['name']
            if nome and nome.lower() == nome_processo:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

def limpar_pasta(caminho):
    arquivos_removidos = 0
    if not os.path.exists(caminho):
        return arquivos_removidos
    
    for item in os.listdir(caminho):
        item_path = os.path.join(caminho, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
                arquivos_removidos += 1
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                arquivos_removidos += 1
        except Exception as e:
            print(f"Erro ao remover {item_path}: {e}")

    return arquivos_removidos

def limpar_chrome():
    if navegador_aberto("chrome.exe"):
        print("⚠️ O Chrome está aberto. Feche o navegador antes de limpar o cache.\n")
        return
    
    caminho = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache")
    print(f"Limpando cache do Chrome...")
    removidos = limpar_pasta(caminho)
    print(f"chrome: {removidos} itens removidos.\n")

def limpar_firefox():
    if navegador_aberto("firefox.exe"):
        print("⚠️ O Firefox está aberto. Feche o navegador antes de limpar o cache.\n")
        return
    
    base = os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles")
    if not os.path.exists(base):
        print("Firefox nao encontrado.\n")
        return
    
    for perfil in os.listdir(base):
        caminho = os.path.join(base, perfil, "cache2")
        print(f"Limpando cache do firefox (perfil: {perfil})...")
        removidos = limpar_pasta(caminho)
        print(f"Firefox: {removidos} itens removidos.\n")

def limpar_edge():
    if navegador_aberto("edge.exe"):
        print("⚠️ O Edge está aberto. Feche o navegador antes de limpar o cache.\n")
        return
    
    caminho = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cache")
    print(f"Lipando cache do Edge...")
    removidos = limpar_pasta(caminho)
    print(f"Edge: {removidos} itens removidos.\n")

def limpar_navegadores():
    print("\n🌐 Limpando cache dos navegadores...\n")
    limpar_chrome()
    limpar_firefox()
    limpar_edge()
    print("✅ Limpeza de navegadores completa.")