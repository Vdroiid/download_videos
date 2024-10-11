import os
import shutil

def clear_chrome_cache():
    # Ruta a la caché de Chrome en Linux
    chrome_cache_path = os.path.expanduser("~/.cache/google-chrome/Default/Cache")

    if os.path.exists(chrome_cache_path):
        shutil.rmtree(chrome_cache_path)
        print("Caché de Chrome eliminada.")
    else:
        print("Ruta de caché de Chrome no encontrada.")

clear_chrome_cache()
