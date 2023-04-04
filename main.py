import tkinter as tk
import customtkinter as ctk
from PIL import Image
from sd_functions import tabs

version = "0.2.1"
download_frame = None
"""
functions
"""


def video_extension_optionmenu_callback(choice):
    print(choice)


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

ctk.CTkLabel(main_screen, text="Simple Downloader", font=("Bahnschrift SemiBold SemiConden", 60)).place(x=200, y=12)

download_frame = ctk.CTkTabview(main_screen, width=700, height=466, fg_color="#2F2542", bg_color="#2F2542")
download_frame.place(x=200, y=80)
download_frame.add("Download Video")
download_frame.add("Download Audio")
download_frame.add("Download Video from Youtube")
download_frame.add("Download Audio from Youtube")

side_button_download_video = ctk.CTkButton(main_screen, fg_color="#3C2862", text="Download Video", bg_color="#554079",
                                           font=("Bahnschrift SemiBold SemiConden", 20), command=change_tabs_1)
side_button_download_audio = ctk.CTkButton(main_screen, fg_color="#3C2862", text="Download Audio", bg_color="#554079",
                                           font=("Bahnschrift SemiBold SemiConden", 20), command=change_tabs_2)
side_button_download_video_youtube = ctk.CTkButton(main_screen, fg_color="#3C2862", text="Download Video \nfrom YouTube"
                                                   , font=("Bahnschrift SemiBold SemiConden", 20), command=change_tabs_3
                                                   , bg_color="#554079")
side_button_download_audio_youtube = ctk.CTkButton(main_screen, fg_color="#3C2862", text="Download Audio \nfrom YouTube"
                                                   , font=("Bahnschrift SemiBold SemiConden", 20), command=change_tabs_4
                                                   , bg_color="#554079")
logo_image = ctk.CTkImage(Image.open(r"src\logo simple downloader transparent .png"), size=(80, 80))
logo = ctk.CTkLabel(side_frame, image=logo_image, text='')
logo.place(x=50, y=8)

side_button_download_video.place(x=18, y=100)
side_button_download_audio.place(x=18, y=150)
side_button_download_video_youtube.place(x=18, y=200)
side_button_download_audio_youtube.place(x=18, y=275)

# start tab download video
ctk.CTkLabel(download_frame.tab("Download Video"),
             text="Download a video of any site besides YouTube\nPaste your link below:",
             font=("Bahnschrift SemiBold SemiConden", 20), justify="left").place(x=0, y=0)

link_video_entry = ctk.CTkEntry(download_frame.tab("Download Video"), placeholder_text="Insert link", width=400,
                                height=25)
link_video_entry.place(x=0, y=60)

video_extension = ctk.CTkOptionMenu(download_frame.tab("Download Video"), values=[".mp4", ".avi", ".wmv", ".asf", ".m4v"],
                                    command=video_extension_optionmenu_callback, height=25)
video_extension.place(x=420, y=60)

ctk.CTkLabel(download_frame.tab("Download Video"),
             text="Name your file (optional)",
             font=("Bahnschrift SemiBold SemiConden", 20), justify="left").place(x=0, y=85)

name_entry = ctk.CTkEntry(download_frame.tab("Download Video"), placeholder_text="Insert Name", width=400,
                          height=25)
name_entry.place(x=0, y=120)

download_buton_video = ctk.CTkButton(download_frame.tab("Download Video"), font=("Bahnschrift SemiBold SemiConden", 30),
                                     fg_color="#554079", bg_color="#2F2542", text="Download ↓", height=50, width=200)
download_buton_video.place(x=0, y=170)
# end tab download video

back_side_frame = ctk.CTkFrame(main_screen, width=10, height=526, fg_color="#554079", corner_radius=0)
back_side_frame.place(x=0, y=0)
secret_frame = ctk.CTkFrame(main_screen, fg_color="#2F2542", width=700, height=27)
secret_frame.place(x=180, y=90)

main_screen.mainloop()
