import os
import shutil

def clear_edge_cache():
    # Ruta a la caché de Edge en Windows
    edge_cache_path = os.path.expanduser("C:/Users/YourUsername/AppData/Local/Microsoft/Edge/User Data/Default/Cache")

    if os.path.exists(edge_cache_path):
        shutil.rmtree(edge_cache_path)
        print("Caché de Edge eliminada.")
    else:
        print("Ruta de caché de Edge no encontrada.")

clear_edge_cache()
