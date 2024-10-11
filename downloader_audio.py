import yt_dlp

def download_and_convert_to_mp3(url):
    # Opciones de ydl
    ydl_opts = {
        'format': 'bestaudio',  # Descarga el mejor audio disponible
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convierte a MP3
            'preferredquality': '192',  # Calidad del MP3
        }],
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Iniciando descarga de audio...")
            ydl.download([url])
            print("Descarga y conversión a MP3 completadas.")
    except Exception as e:
        print(f"Ocurrió un error durante la descarga: {e}")

download_and_convert_to_mp3('https://youtu.be/WP6-pjcmqi4')
