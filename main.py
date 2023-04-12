import tkinter as tk
from abc import ABC

import customtkinter as ctk
from PIL import Image
from sd_functions import tabs, downloads

version = "0.2.1"
resolution = ""
extension = ""
link = ""
name = ""
download_frame = None
downloads = downloads()

name_entry = None
link_entry = None

pallete = {"background_1": "#2F2542", "background_2": "#211726",
           "button_1": "#3C2862", "hover_1": "#9669ad",
           "button_2": "#28164a", "hover_2": "#44365c"}

"""
functions
"""


class App(ctk.CTk):
    global pallete

    def __init__(self):
        super().__init__()

        self.configure(fg_color=pallete["background_1"])
        self.geometry("900x525")
        self.resizable(False, False)
        self.title(f"Simple Downloader ver {version}")
        self.wm_iconbitmap(r"src\logo-simple-downloader.ico")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.link_entry = None
        self.name_entry = None
        self.video_extension = None
        self.video_resolution = None
        self.audio_extension = None

        self.downloadframe()
        self.sideframe()

        ctk.CTkLabel(self,
                     text="Simple Downloader",
                     font=("Bahnschrift SemiBold SemiConden", 60)) \
            .place(x=200, y=12)

    def downloadframe(self):
        global download_frame
        download_frame = ctk.CTkFrame(self,
                                      width=900,
                                      height=466,
                                      fg_color=pallete["background_1"],
                                      bg_color=pallete["background_1"])
        download_frame.grid(row=0, column=1, pady=45, ipadx=30)

        def download_tab():
            ctk.CTkLabel(download_frame,
                         text="Download Videos and Audios from Web\nPaste your link below:",
                         font=("Bahnschrift SemiBold SemiConden", 20), justify="left"). \
                place(x=10, y=10)

            self.link_entry = ctk.CTkEntry(download_frame,
                                           placeholder_text="Insert link",
                                           width=400,
                                           height=25)
            self.link_entry.grid(in_=download_frame,
                                 row=1,
                                 column=0,
                                 pady=(80, 0),
                                 padx=10)

            self.video_extension = ctk.CTkOptionMenu(download_frame,
                                                     values=[".mp4", ".avi", ".wmv", ".asf", ".m4v"],
                                                     # command=video_extension_optionmenu_callback,
                                                     height=25,
                                                     width=80,
                                                     fg_color=pallete["button_1"],
                                                     button_color=pallete["button_2"],
                                                     button_hover_color=pallete["hover_2"]
                                                     )
            self.video_extension.place(x=420, y=80)

            ctk.CTkLabel(download_frame,
                         text="Name your file (optional)",
                         font=("Bahnschrift SemiBold SemiConden", 20),
                         justify="left").grid(in_=download_frame,
                                              row=2,
                                              column=0,
                                              pady=10,
                                              padx=(0, 209))

            self.name_entry = ctk.CTkEntry(download_frame,
                                           placeholder_text="Insert Name",
                                           width=400,
                                           height=25)
            self.name_entry.grid(in_=download_frame,
                                 row=3,
                                 column=0,
                                 pady=0)

            self.video_resolution = ctk.CTkOptionMenu(download_frame,
                                                      values=["1080p", "720p", "480p", "360p", "240p", "144p"],
                                                      height=25,
                                                      fg_color=pallete["button_1"],
                                                      button_color=pallete["button_2"],
                                                      button_hover_color=pallete["hover_2"]
                                                      )
            self.video_resolution.grid(in_=download_frame,
                                       row=3,
                                       column=1,
                                       pady=0)

            self.audio_extension = ctk.CTkOptionMenu(download_frame,
                                                     values=[".mp3", ".m4a", ".wav", ".wma", ".webm", ".opus"],
                                                     height=25,
                                                     width=80,
                                                     fg_color=pallete["button_1"],
                                                     button_color=pallete["button_2"],
                                                     button_hover_color=pallete["hover_2"]
                                                     )
            self.audio_extension.place(x=510, y=80)

            download_buton_video = ctk.CTkButton(download_frame,
                                                 font=("Bahnschrift SemiBold SemiConden", 26),
                                                 fg_color=pallete["button_1"],
                                                 bg_color=pallete["background_1"],
                                                 text="Show more options",
                                                 height=50,
                                                 width=200,
                                                 hover_color=pallete["hover_1"],
                                                 # command=downloads.youtube_video_download(link=link_video_entry.get()
                                                 #                                         , name=name_entry.get(),
                                                 #                                         resolution=resolution,
                                                 #                                         extension=extension)
                                                 )
            download_buton_video.grid(in_=download_frame,
                                      row=4,
                                      column=0,
                                      pady=20,
                                      padx=(0, 190))

        download_tab()

    def sideframe(self):
        global download_frame
        side_frame = ctk.CTkFrame(self,
                                  fg_color=pallete["background_2"],
                                  corner_radius=15)
        side_frame.place(x=0, y=0)

        logo_image = ctk.CTkImage(Image.open(r"src\logo simple downloader transparent .png"), size=(80, 80))
        logo = ctk.CTkLabel(side_frame, image=logo_image, text='')
        logo.grid(row=0, column=0, padx=50, pady=10)

        def change_tabs_1():
            download_frame.set("Download Video")

        def change_tabs_2():
            download_frame.set("Download Audio")

        def download_vd_yt_callback():
            link2 = self.link_entry.get()
            print(link2)
            name2 = self.name_entry.get()
            print(name2)
            resolution = self.video_resolution.get()
            print(resolution)
            extension = self.video_extension.get()
            print(extension)

            print("nice")

            downloads.youtube_video_download(link2, name2, resolution, extension)

        def download_ad_yt_callback():
            link2 = self.link_entry.get()
            print(link2)
            name2 = self.name_entry.get()
            print(name2)
            extension2 = self.audio_extension.get()
            print(extension2)

            print("nice")

            downloads.youtube_audio_download(link2, name2, extension2)

        sb_download_video = ctk.CTkButton(side_frame,
                                          fg_color=pallete["button_1"],
                                          text="Download Video",
                                          bg_color=pallete["background_2"],
                                          font=("Bahnschrift SemiBold SemiConden", 20),
                                          command=change_tabs_1,
                                          hover_color=pallete["hover_1"]).grid(row=1,
                                                                               column=0,
                                                                               pady=10,
                                                                               ipady=5,
                                                                               ipadx=2)
        sb_download_audio = ctk.CTkButton(side_frame,
                                          fg_color=pallete["button_1"],
                                          text="Download Audio",
                                          bg_color=pallete["background_2"],
                                          font=("Bahnschrift SemiBold SemiConden", 20),
                                          command=change_tabs_2,
                                          hover_color=pallete["hover_1"]).grid(row=2,
                                                                               column=0,
                                                                               pady=10,
                                                                               ipady=5,
                                                                               ipadx=2)
        sb_download_video_youtube = ctk.CTkButton(side_frame,
                                                  fg_color=pallete["button_1"],
                                                  text="Download Video \nfrom YouTube",
                                                  font=("Bahnschrift SemiBold SemiConden", 20),
                                                  command=download_vd_yt_callback,
                                                  bg_color=pallete["background_2"],
                                                  hover_color=pallete["hover_1"]).grid(row=3,
                                                                                       column=0,
                                                                                       pady=10,
                                                                                       ipady=5,
                                                                                       ipadx=2)
        sb_download_audio_youtube = ctk.CTkButton(side_frame,
                                                  fg_color=pallete["button_1"],
                                                  text="Download Audio \nfrom YouTube",
                                                  font=("Bahnschrift SemiBold SemiConden", 20),
                                                  command=download_ad_yt_callback,
                                                  bg_color=pallete["background_2"],
                                                  hover_color=pallete["hover_1"]).grid(row=4,
                                                                                       column=0,
                                                                                       pady=10,
                                                                                       ipady=5,
                                                                                       ipadx=2)
        config_image = ctk.CTkImage(Image.open(r"src\Gear.png"), size=(40, 40))
        config_button = ctk.CTkButton(side_frame,
                                      image=config_image,
                                      text="",
                                      fg_color=pallete["background_2"],
                                      hover_color=pallete["hover_1"])
        config_button.grid(row=5, column=0, padx=10, pady=45)


if __name__ == "__main__":
    app = App()
    app.mainloop()
