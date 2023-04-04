import tkinter as tk
import customtkinter as ctk
from PIL import Image

version = "0.2.1"
download_frame = None
logo_png = Image.open(r"src\logo simple downloader transparent .png")
"""
functions
"""


def change_tabs_1():
    download_frame.set("Download Video")


def change_tabs_2():
    download_frame.set("Download Audio")


def change_tabs_3():
    download_frame.set("Download Video from Youtube")


def change_tabs_4():
    download_frame.set("Download Audio from Youtube")


# Melhorias: usar pack() ao invés de place()

main_screen = ctk.CTk(fg_color="#2F2542")
main_screen.geometry("900x525")
main_screen.minsize(900, 525)
main_screen.maxsize(900, 525)
main_screen.title(f"Simple Downloader ver {version}")
main_screen.wm_iconbitmap(r"src\logo-simple-downloader.ico")

side_frame = ctk.CTkFrame(main_screen, width=180, height=526, fg_color="#554079", corner_radius=10)
side_frame.place(x=0, y=0)

ctk.CTkLabel(main_screen, text="Simple Downloader", font=("Bahnschrift SemiBold SemiConden", 40)).place(x=200, y=12)

download_frame = ctk.CTkTabview(main_screen, width=700, height=466)
download_frame.place(x=200, y=60)
download_frame.add("Download Video")
download_frame.add("Download Audio")
download_frame.add("Download Video from Youtube")
download_frame.add("Download Audio from Youtube")

side_button_download_video = ctk.CTkButton(main_screen, fg_color="#3C2862", text="Download Video", bg_color="#423290",
                                           font=("Bahnschrift SemiBold SemiConden", 20), command=change_tabs_1)
side_button_download_audio = ctk.CTkButton(main_screen, fg_color="#3C2862", text="Download Audio", bg_color="#423290",
                                           font=("Bahnschrift SemiBold SemiConden", 20), command=change_tabs_2)
side_button_download_video_youtube = ctk.CTkButton(main_screen, fg_color="#3C2862", text="Download Video \nfrom YouTube"
                                                   , font=("Bahnschrift SemiBold SemiConden", 20), command=change_tabs_3
                                                   , bg_color="#423290")
side_button_download_audio_youtube = ctk.CTkButton(main_screen, fg_color="#3C2862", text="Download Audio \nfrom YouTube"
                                                   , font=("Bahnschrift SemiBold SemiConden", 20), command=change_tabs_4
                                                   , bg_color="#423290")
logo_image = ctk.CTkImage(Image.open(r"src\logo simple downloader transparent .png"), size=(80, 80))
logo = ctk.CTkLabel(side_frame, image=logo_image, text='')
logo.place(x=50, y=0)

side_button_download_video.place(x=18, y=100)
side_button_download_audio.place(x=18, y=150)
side_button_download_video_youtube.place(x=18, y=200)
side_button_download_audio_youtube.place(x=18, y=275)

link_video_entry = ctk.CTkEntry(download_frame.tab("Download Video"), placeholder_text="Insert link", width=400,
                                height=20)
link_video_entry.place(x=0, y=0)

main_screen.mainloop()
