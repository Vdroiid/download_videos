import yt_dlp
import subprocess

"""
    Este Script descarga un video de YouTube y luego lo procesa con ffepeg para convertirlo en cualquier formato.
    En este caso, en mp4.
"""

# Configuración de yt_dlp para descargar el video
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'downloaded_video.%(ext)s',  # Plantilla para el nombre del archivo
    'noplaylist': True,  # No descargar listas de reproducción
}

def download_video(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(rl, download=True)
        return info_dict

def process_video(input_file, output_file):
    # Aquí puedes usar cualquier comando de FFmpeg
    # Ejemplo: Convertir el video a MP4
    command = [
        'ffmpeg',
        '-i', input_file,  # Archivo de entrada
        '-vf', 'scale=1280:720',  # Escalar video a 1280x720
        '-c:a', 'aac',  # Codificar audio en AAC
        '-b:a', '192k',  # Bitrate de audio
        '-c:v', 'libx264',  # Codificar video en H.264
        '-crf', '23',  # Calidad del video (23 es un buen punto de partida)
        output_file  # Archivo de salida
    ]
    subprocess.run(command, check=True)

def main():
    url = 'https://youtu.be/y_sRNLlGsM4'  # URL del video a descargar
    info_dict = download_video(url)
    print(f"Descargado: {info_dict['title']}")

    # Procesar el video descargado
    input_file = 'downloaded_video.webm'  # Ajusta la extensión a .webm
    output_file = 'processed_video.mp4'
    process_video(input_file, output_file)
    print(f"Procesado y guardado en: {output_file}")

if __name__ == "__main__":
    main()