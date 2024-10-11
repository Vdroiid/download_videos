import yt_dlp
import subprocess

"""
    Este Script descarga un video de YouTube y luego lo procesa con ffepeg para convertirlo en cualquier formato.
    En este caso, en mp4.
"""
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'downloaded_video.%(ext)s',  # Nombre del archivo
    'noplaylist': True,  # Para que no descargue la lista de reporducción
}

def download_video(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        return info_dict


"""
En este función se utiliza comandos de FFmpeg para hacer conversiones de un formato 
a otro formato (Necesario tener FFmpeg instaldo.)
"""
def process_video(input_file, output_file):
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

"""
Función principal
"""
def main():
    url = input("Pega en enlace: ")
    info_dict = download_video(url)
    print(f"Descargado: {info_dict['title']}")

    # Procesar el video descargado
    input_file = 'downloaded_video.webm'  # Ajusta la extensión a .webm
    output_file = 'processed_video.mp4'
    process_video(input_file, output_file)
    print(f"Procesado y guardado en: {output_file}")

if __name__ == "__main__":
    main()