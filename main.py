import tkinter as tk
import customtkinter as ctk

version = "0.2.1"

# Melhorias: usar pack() ao invés de place()

main_screen = ctk.CTk(fg_color="#1e0d6b")
main_screen.geometry("900x525")
main_screen.minsize(900, 525)
main_screen.maxsize(900, 525)
main_screen.title(f"Simple Downloader ver {version}")
main_screen.wm_iconbitmap(r"src\logo-simple-downloader.ico")

ctk.CTkLabel(main_screen, text="Simple Downloader", font=("Bahnschrift SemiBold SemiConden", 40)).place(y=10, x=10)

side_frame = ctk.CTkFrame(main_screen, width=180, height=526, fg_color="#423290", corner_radius=10)
side_frame.place(y=0, x=0)


main_screen.mainloop()
