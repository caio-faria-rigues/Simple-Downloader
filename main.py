import tkinter as tk
from abc import ABC

import customtkinter as ctk
from PIL import Image
from sd_functions import tabs, downloads

version = "0.2.1"
resolution = ""
extension = ""
download_frame = None
downloads = downloads()

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

        self.downloadframe()
        self.sideframe()

        ctk.CTkLabel(self,
                     text="Simple Downloader",
                     font=("Bahnschrift SemiBold SemiConden", 60)) \
            .place(x=200, y=12)

    def downloadframe(self):
        global download_frame
        download_frame = ctk.CTkTabview(self,
                                        width=700,
                                        height=466,
                                        fg_color=pallete["background_1"],
                                        bg_color=pallete["background_1"])
        download_frame.grid(row=1, column=2)
        download_frame.add("Download Video")
        download_frame.add("Download Audio")
        download_frame.add("Download Video from Youtube")
        download_frame.add("Download Audio from Youtube")

        def download_youtube_video_tab():
            ctk.CTkLabel(download_frame.tab("Download Video"),
                         text="Download a video of any site besides YouTube\nPaste your link below:",
                         font=("Bahnschrift SemiBold SemiConden", 20), justify="left"). \
                grid(in_=download_frame.tab("Download Video"),
                     row=0,
                     column=0,
                     pady=20)

            link_video_entry = ctk.CTkEntry(download_frame.tab("Download Video"),
                                            placeholder_text="Insert link",
                                            width=400,
                                            height=25)
            link_video_entry.grid(in_=download_frame.tab("Download Video"),
                                  row=1,
                                  column=0,
                                  pady=20,
                                  padx=10)

            video_extension = ctk.CTkOptionMenu(download_frame.tab("Download Video"),
                                                values=[".mp4", ".avi", ".wmv", ".asf", ".m4v"],
                                                # command=video_extension_optionmenu_callback,
                                                height=25,
                                                fg_color=pallete["button_1"],
                                                button_color=pallete["button_2"],
                                                button_hover_color=pallete["hover_2"]
                                                )
            video_extension.grid(in_=download_frame.tab("Download Video"),
                                 row=1,
                                 column=1,
                                 pady=20,
                                 padx=10)

            ctk.CTkLabel(download_frame.tab("Download Video"),
                         text="Name your file (optional)",
                         font=("Bahnschrift SemiBold SemiConden", 20),
                         justify="left").grid(in_=download_frame.tab("Download Video"),
                                              row=2,
                                              column=0)

            name_entry = ctk.CTkEntry(download_frame.tab("Download Video"), placeholder_text="Insert Name",
                                      width=400,
                                      height=25)
            name_entry.grid(in_=download_frame.tab("Download Video"),
                            row=3,
                            column=0,
                            pady=0)

            download_buton_video = ctk.CTkButton(download_frame.tab("Download Video"),
                                                 font=("Bahnschrift SemiBold SemiConden", 30),
                                                 fg_color="#3C2862", bg_color="#2F2542", text="Download ↓",
                                                 height=50,
                                                 width=200,
                                                 hover_color="#9669ad",
                                                 # command=downloads.youtube_video_download(link=link_video_entry.get()
                                                 #                                         , name=name_entry.get(),
                                                 #                                         resolution=resolution,
                                                 #                                         extension=extension)
                                                 )
            download_buton_video.grid(in_=download_frame.tab("Download Video"),
                                      row=4,
                                      column=0,
                                      pady=20)

        download_youtube_video_tab()

    def sideframe(self):
        global download_frame
        side_frame = ctk.CTkFrame(self,
                                  width=180,
                                  height=526,
                                  fg_color="#211726",
                                  corner_radius=15)
        side_frame.place(x=0, y=0)

        logo_image = ctk.CTkImage(Image.open(r"src\logo simple downloader transparent .png"), size=(80, 80))
        logo = ctk.CTkLabel(side_frame, image=logo_image, text='')
        logo.grid(row=0, column=0, padx=50, pady=10)

        def change_tabs_1():
            download_frame.set("Download Video")

        def change_tabs_2():
            download_frame.set("Download Audio")

        def change_tabs_3():
            download_frame.set("Download Video from Youtube")

        def change_tabs_4():
            download_frame.set("Download Audio from Youtube")

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
                                          fg_color="#3C2862",
                                          text="Download Audio",
                                          bg_color="#211726",
                                          font=("Bahnschrift SemiBold SemiConden", 20),
                                          command=change_tabs_2,
                                          hover_color="#9669ad").grid(row=2,
                                                                      column=0,
                                                                      pady=10,
                                                                      ipady=5,
                                                                      ipadx=2)
        sb_download_video_youtube = ctk.CTkButton(side_frame,
                                                  fg_color="#3C2862",
                                                  text="Download Video \nfrom YouTube",
                                                  font=("Bahnschrift SemiBold SemiConden", 20),
                                                  command=change_tabs_3,
                                                  bg_color="#211726",
                                                  hover_color="#9669ad").grid(row=3,
                                                                              column=0,
                                                                              pady=10,
                                                                              ipady=5,
                                                                              ipadx=2)
        sb_download_audio_youtube = ctk.CTkButton(side_frame,
                                                  fg_color="#3C2862",
                                                  text="Download Audio \nfrom YouTube",
                                                  font=("Bahnschrift SemiBold SemiConden", 20),
                                                  command=change_tabs_4,
                                                  bg_color="#211726",
                                                  hover_color="#9669ad").grid(row=4,
                                                                              column=0,
                                                                              pady=10,
                                                                              ipady=5,
                                                                              ipadx=2)
        config_image = ctk.CTkImage(Image.open(r"src\Gear.png"), size=(40, 40))
        config_button = ctk.CTkButton(side_frame,
                                      image=config_image,
                                      text="",
                                      fg_color="#211726",
                                      hover_color="#9669ad")
        config_button.grid(row=5, column=0, padx=10, pady=45)


if __name__ == "__main__":
    app = App()
    app.mainloop()
