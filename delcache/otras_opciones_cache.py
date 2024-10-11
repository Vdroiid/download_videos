import subprocess

def clear_browser_cache():
    # Ejemplo para Windows
    subprocess.run(["ipconfig", "/flushdns"], check=True)
    print("Caché de DNS eliminada.")

clear_browser_cache()
