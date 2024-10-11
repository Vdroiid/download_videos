import os
import shutil
def clear_firefox_cache():
    # Ruta a la caché de Firefox en Linux
    firefox_cache_path = os.path.expanduser("~/.cache/mozilla/firefox")

    if os.path.exists(firefox_cache_path):
        shutil.rmtree(firefox_cache_path)
        print("Caché de Firefox eliminada.")
    else:
        print("Ruta de caché de Firefox no encontrada.")

clear_firefox_cache()
