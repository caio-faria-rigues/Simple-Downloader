from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import Label
from tkinter import PhotoImage
from pytube import YouTube
import os


caminho = ''


def path_download():
    global caminho
    origem = filedialog.askdirectory()
    caminho = origem
    return origem


def video_download():
    path = path_download()
    link = search.get()

    yt = YouTube(link)
    mp4_files = yt.streams.filter(file_extension="mp4")
    mp4_files_hd = mp4_files.get_by_resolution("720p")
    mp4_files_hd.download(path)


def audio_download():
    path = path_download()
    link = search.get()

    yt = YouTube(link)
    mp3_files = yt.streams.filter(only_audio=True).first()
    audio = mp3_files.download(path)

    base, ext = os.path.splitext(audio)
    new_file = base + '.mp3'
    os.rename(audio, new_file)


root = Tk()
root.title("Youtube Downloader")
icon = PhotoImage(file='C:\\Users\\Cliente\\PycharmProjects\\guppe\\Projetos\\music downloader\\youtube-icon.png')
root.iconphoto(False, icon)

frm = ttk.Frame(root, padding=10)
root.minsize(600, 300)
root.configure(background='#dde')
Label(root, text="\nYoutube Downloader\n\n\n", background='#dde').grid(column=0, row=0)
Label(root, text="Insira o link abaixo:\n", background='#dde').grid(column=0, row=1)
search = Entry(root, width=100)
search.grid(column=0, row=2)
botao = ttk.Button(root, text="Baixar Audio", command=audio_download).grid(column=0, row=3)
botao2 = ttk.Button(root, text="Baixar Video", command=video_download).grid(column=0, row=4)
root.mainloop()
