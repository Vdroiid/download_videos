# downloader.py
import yt_dlp

def download_video(url, video_format, quality):
    ydl_opts = {
        'format': f'{quality}[ext={video_format}]+bestaudio[ext=m4a]/best[ext={video_format}]',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': video_format,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': video_format,
        }],
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
