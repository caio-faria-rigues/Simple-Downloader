import tkinter as tk
import customtkinter as ctk

version = "0.2.1"
download_frame = None
"""
functions
"""


def change_tabs_2(tabview, button):
    tabview.set(button)


# Melhorias: usar pack() ao invés de place()

main_screen = ctk.CTk(fg_color="#1e0d6b")
main_screen.geometry("900x525")
main_screen.minsize(900, 525)
main_screen.maxsize(900, 525)
main_screen.title(f"Simple Downloader ver {version}")
main_screen.wm_iconbitmap(r"src\logo-simple-downloader.ico")

side_frame = ctk.CTkFrame(main_screen, width=180, height=526, fg_color="#423290", corner_radius=10)
side_frame.place(x=0, y=0)



ctk.CTkLabel(main_screen, text="Simple Downloader", font=("Bahnschrift SemiBold SemiConden", 40)).place(x=200, y=12)

download_frame = ctk.CTkTabview(main_screen, width=700, height=465)
download_frame.place(x=200, y=60)
download_frame.add("Download Video")
download_frame.add("Download Audio")
download_frame.add("Download Video from Youtube")
download_frame.add("Download Audio from Youtube")

side_button_download_video = ctk.CTkButton(main_screen, fg_color="#0f0a37", text="Download Video",
                                           font=("Bahnschrift SemiBold SemiConden", 20),
                                           command=change_tabs_2(download_frame, "Download Video"))
side_button_download_audio = ctk.CTkButton(main_screen, fg_color="#0f0a37", text="Download Audio",
                                           font=("Bahnschrift SemiBold SemiConden", 20))
side_button_download_video_youtube = ctk.CTkButton(main_screen, fg_color="#0f0a37", text="Download Video from YouTube",
                                           font=("Bahnschrift SemiBold SemiConden", 20))
side_button_download_audio_youtube = ctk.CTkButton(main_screen, fg_color="#0f0a37", text="Download Audio from YouTube",
                                           font=("Bahnschrift SemiBold SemiConden", 20))

side_button_download_video.place(x=10, y=20)
side_button_download_audio.place(x=10, y=70)
side_button_download_video_youtube.place(x=10, y=120)
side_button_download_audio_youtube.place(x=10, y=170)

label = ctk.CTkLabel(download_frame.tab("Download Video"), text="oiiiiii")
label.pack()

main_screen.mainloop()
