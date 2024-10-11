# gui.py
import wx
from downloader import download_video

class VideoDownloaderFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(VideoDownloaderFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)

        # Crear controles
        self.url_label = wx.StaticText(panel, label="URL del video:", pos=(10, 10))
        self.url_text = wx.TextCtrl(panel, pos=(150, 10), size=(300, 25))

        self.format_label = wx.StaticText(panel, label="Formato de video:", pos=(10, 50))
        self.format_choice = wx.Choice(panel, choices=['mp4', 'webm', 'mkv'], pos=(150, 50))
        self.format_choice.SetSelection(0)

        self.quality_label = wx.StaticText(panel, label="Calidad:", pos=(10, 90))
        self.quality_choice = wx.Choice(panel, choices=['best', 'bestaudio', 'worst'], pos=(150, 90))
        self.quality_choice.SetSelection(0)

        self.download_button = wx.Button(panel, label="Descargar", pos=(150, 130))
        self.download_button.Bind(wx.EVT_BUTTON, self.on_download)

        self.result_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY, pos=(10, 170), size=(500, 200))

        self.SetSize((540, 450))
        self.Centre()

    def on_download(self, event):
        url = self.url_text.GetValue()
        video_format = self.format_choice.GetStringSelection()
        quality = self.quality_choice.GetStringSelection()

        if not url:
            wx.MessageBox('Por favor, introduce una URL.', 'Error', wx.OK | wx.ICON_ERROR)
            return

        self.result_text.AppendText(f"Descargando video de {url}\nFormato: {video_format}\nCalidad: {quality}\n")

        try:
            download_video(url, video_format, quality)
            self.result_text.AppendText("Descarga completada.\n")
        except Exception as e:
            self.result_text.AppendText(f"Error: {e}\n")
            wx.MessageBox(f'Error al descargar el video: {e}', 'Error', wx.OK | wx.ICON_ERROR)
