import tkinter as tk
import customtkinter as ctk
import requests
import bs4

download_frame = None


class tabs:
    def change_tab_DV(self, frame):
        download_frame = frame
        download_frame.set("Download Video")

    def change_tab_DA(self):
        download_frame.set("Download Audio")

    def change_tab_DVY(self):
        download_frame.set("Download Video from Youtube")

    def change_tab_DAY(self):
        download_frame.set("Download Audio from Youtube")


class downloads:
    caminho = ''

    def path_download(self):
        global caminho
        origem = ctk.filedialog.askdirectory()
        caminho = origem
        return origem

    def generic_video_download(self, link):
        if link.split("/")[2] == "twitter.com":
            print("eba")
        else:
            print("affr")

    def generic_audio_download(self):
        pass

    def youtube_video_download(self):
        pass

    def youtube_audio_download(self):
        pass


sla = downloads()
sla.generic_video_download(link="https://twitter.com/i/status/1641974620776722433")
