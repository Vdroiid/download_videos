import yt_dlp
import re
"""
Este Script descarga un video de YouTube,
eligiendo la mejor calidad en MP4. Además,
agarra el título del video como nombre de este archivo descargado.
"""
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Descargar el mejor video y audio combinados en MP4
    'outtmpl': '%(title)s.%(ext)s',  # Usar el título del video como nombre del archivo
    'noplaylist': True,  # No descargar listas de reproducción
    'merge_output_format': 'mp4',  # Asegurarse de que la salida sea en formato MP4 si se descargan por separado
    'postprocessors': [{  # Usar un postprocesador para ajustar el nombre del archivo
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Convertir a MP4 si es necesario
    }],
}

def sanitize_filename(filename):
    # Limpiar el nombre del archivo para evitar caracteres no permitidos
    return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', filename)

def download_video(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        # Obtener el nombre del archivo descargado
        filename = ydl.prepare_filename(info_dict)
        # Limpiar el nombre del archivo para que sea válido en todos los sistemas operativos
        sanitized_filename = sanitize_filename(filename)
        return sanitized_filename

def main(url):
    filename = download_video(url)
    print(f"Descargado y renombrado como: {filename}")

url = str(input("Pega el enlace del video: ")).strip()
main(url)