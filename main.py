import wx
from gui import VideoDownloaderFrame

def main():
    app = wx.App(False)
    frame = VideoDownloaderFrame(None, title="Descargador de Videos")
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
