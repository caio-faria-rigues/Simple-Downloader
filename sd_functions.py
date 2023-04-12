import tkinter as tk
import customtkinter as ctk
import requests
import bs4
from pytube import YouTube
import os

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

    def generic_video_download(self, link, name):
        if link.split("/")[2] == "twitter.com":
            print("eba")
        else:
            print("affr")

    def generic_audio_download(self):
        pass

    def youtube_video_download(self, link, name, resolution, extension):
        print("chegou aqui" + link + " " + name)
        try:
            yt = YouTube(link)
            default_name = yt.title
            mp4_files = yt.streams.filter(file_extension="mp4")

            path = self.path_download()

            res = resolution if resolution else '1080p'

            ext = extension if extension else '.mp4'

            print(res + ext)

            mp4_files_hd = mp4_files.get_by_resolution(res)

            try:
                if name:
                    mp4_files_hd.download(path, filename=name + ext)
                else:
                    mp4_files_hd.download(path, filename=default_name + ext)
            except:
                print('Simple Downloader - Oops...',
                      'Algo deu errado! :(\nTente novamente em outra resolução!')
        except:
            pass

    def youtube_audio_download(self, link, name, extension):
        try:
            path = self.path_download()

            yt = YouTube(link)
            mp3_files = yt.streams.filter(only_audio=True).first()
            default_name = yt.title

            ext = extension if extension else ".mp3"

            if name:
                audio = mp3_files.download(path, filename=name + ext)

            else:
                audio = mp3_files.download(path, filename=default_name + ext)

            base, ext = os.path.splitext(audio)
            new_file = base + ext
            os.rename(audio, new_file)
        except:
            pass


sla = downloads()
sla.generic_video_download(link="https://twitter.com/i/status/1641974620776722433", name="jao")
