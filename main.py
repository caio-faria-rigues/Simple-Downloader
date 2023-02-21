from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Label
from tkinter import PhotoImage
from pytube import YouTube
import threading
import os

caminho = ''
options_list = ['1080p', '720p', '480p', '360p', '240p', '144p']
index = 0
res = ''
message = ''


def path_download():
    global caminho
    origem = filedialog.askdirectory()
    caminho = origem
    return origem


def hidenseek():
    global index
    index = index + 1
    if index % 2 == 0:
        options.place_forget()
    else:
        options.place(x=365, y=186)


def video_download():
    global index
    global res
    global message
    try:
        link = search.get()
        yt = YouTube(link)
        mp4_files = yt.streams.filter(file_extension="mp4")

        new_file_name = file_name.get()
        path = path_download()
        if index % 2 == 0:
            res = '720p'
        if index % 2 != 0:
            res = options.get(options.curselection())
        # print(res)

        mp4_files_hd = mp4_files.get_by_resolution(res)

        try:
            if new_file_name == '':
                mp4_files_hd.download(path)
            else:
                mp4_files_hd.download(path, filename=new_file_name + ".mp4")
        except:
            messagebox.showerror('Simple Downloader - Oops...',
                                 'Algo deu errado! :(\nTente novamente em outra resolução!')
    except:
        pass


def audio_download():
    try:
        new_file_name = file_name.get()
        path = path_download()
        link = search.get()

        yt = YouTube(link)
        mp3_files = yt.streams.filter(only_audio=True).first()

        if new_file_name == '':
            audio = mp3_files.download(path)
        else:
            audio = mp3_files.download(path, filename=new_file_name + ".mp3")

        base, ext = os.path.splitext(audio)
        new_file = base + '.mp3'
        os.rename(audio, new_file)
    except:
        pass


def video_threading():
    threading1 = threading.Thread(target=video_download()).start()
    return threading1


def info():
    messagebox.showinfo('Simple Downloader - Info', """Versão 0.1.2 de 02/10/2022\nVersão beta: podem haver diversos 
    erros.\nSinta-se a vontade para avaliar e\\ou reportar erros.\nCriado por Caio Faria Rigues.""")


root = Tk()
root.title("Simple Downloader")
icon = PhotoImage(file=r"src\logo simple downloader.png")
root.iconphoto(False, icon)

background = PhotoImage(file=r"src\900 x 525 background.png")
input_bar = PhotoImage(file=r"src\input bar 510 x 64.png")

logo = PhotoImage(file=r"src\logo simple downloader transparent.png")
header = PhotoImage(file=r"src\Simple downloader header.png")

# download
frm = ttk.Frame(root, padding=10)
root.minsize(898, 525)
root.maxsize(898, 525)
background_label = Label(root, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

logo_canva = Canvas(root, width=470, height=70)
logo_canva.create_image((0, 0), anchor="nw", image=logo)
logo_canva.create_image((70, 0), anchor="nw", image=header)
logo_canva.grid(column=0, row=0)

# Label(root, text="\nYoutube Downloader\n\n\n", background='#BADEFC').grid(column=0, row=0)
# Label(root, text="Insira o link abaixo:\n", background='#BADEFC').grid(column=0, row=1)
search = Entry(root, width=100, borderwidth=0, highlightthickness=0, background="white")
search.grid(column=0, row=2)

# nome do arquivo
Label(root, text="\nNomeie o arquivo(opcional):\n", background='#BADEFC').grid(column=0, row=3)
file_name = Entry(root, width=20)
file_name.grid(column=0, row=4)

# botoes
botao = ttk.Button(root, text="Baixar Audio", command=audio_download).grid(column=0, row=5)
botao2 = ttk.Button(root, text="Baixar Video", command=video_threading).grid(column=0, row=6)

botao_info = Button(root, text="    ℹ️", width=1, height=1, command=info).place(y=1, x=1)

options = Listbox(master=root, selectmode='single', heigh=6, width=7, selectbackground='#B5446E')
for iten in options_list:
    options.insert(END, iten)

botaoconfig = Button(root, text="⚙️", width=1, height=1, command=hidenseek).place(x=340, y=231)

root.mainloop()
