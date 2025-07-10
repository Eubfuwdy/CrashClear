import os 
import shutil

def limpar_pasta(caminho):
    arquivos_removidos = 0
    tamanho_total = 0

    for item in os.listdir(caminho):
        item_path = os.path.join(caminho, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                tamanho_total += os.path.getsize(item_path)
                os.remove(item_path)
                arquivos_removidos += 1
            elif os.path.isdir(item_path):
                tamanho_total += get_tamanho_dir(item_path)
                shutil.rmtree(item_path)
                arquivos_removidos += 1 
        except Exception as e:
            print(f"Erro ao remover {item_path}: {e}")
    
    return arquivos_removidos, tamanho_total

def get_tamanho_dir(pasta):
    tamanho = 0
    for dirpath, dirnames, filenames in os.walk(pasta):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                tamanho += os.path.getsize(fp)
            except:
                continue
    return tamanho

def limpar_temporarios():
    print("\nArquivos pasta temp\n")

    temp_usuario = os.environ.get("TEMP")

    removidos, tamanho = limpar_pasta(temp_usuario)
    
    print(f"\n✅ Total removidos: {removidos} itens ({round(tamanho / (1024*1024), 2)} MB)")