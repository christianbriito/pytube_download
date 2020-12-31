#Importação da biblioteca

import tkinter as tk 
from tkinter import *
from pytube import YouTube 
from tkinter import messagebox, filedialog 

program = tk.Tk()

program.geometry("600x200")
program.resizable(True, True)
program.title("Download youtube")
program.config(background="#000000")

def Widgets(): 
	link_label = Label(program, 
					text="Link: ", 
					bg="#000000") 
	link_label.grid(row=1, 
					column=0, 
					pady=5, 
					padx=5) 

	program.linkText = Entry(program, 
						width=55, 
						textvariable=video_Link) 
	program.linkText.grid(row=1, 
					column=1, 
					pady=5, 
					padx=5, 
					columnspan = 2) 

	destination_label = Label(program, 
							text="Destino:", 
							bg="#000000") 
	destination_label.grid(row=2, 
						column=0, 
						pady=5, 
						padx=5) 

	program.destinationText = Entry(program, 
								width=40, 
								textvariable=download_Path) 
	program.destinationText.grid(row=2, 
							column=1, 
							pady=5, 
							padx=5) 

	browse_B = Button(program, 
					text="Buscar", 
					command=Browse, 
					width=10, 
					bg="#000000") 
	browse_B.grid(row=2, 
				column=2, 
				pady=1, 
				padx=1) 

	Download_B = Button(program, 
						text="Baixar", 
						command=Download, 
						width=20, 
						bg="#000000") 
	Download_B.grid(row=3, 
					column=1, 
					pady=3, 
					padx=3) 


def Browse():
    download_Directory = filedialog.askdirectory(initialdir="Seu diretorio PATH")

    download_Path.set(download_Directory)

def Download():

    Youtube_link = video_Link.get()

    download_Folder = download_Path.get()

    getVideo = YouTube(Youtube_link) 

    VideoStream = getVideo.streams.first()
    
    VideoStream.download(download_Folder)

    messagebox.showinfo("Sucesso!",
                        "Download Salvo na pasta selecionada.")




video_Link = StringVar()
download_Path = StringVar()

Widgets()

program.mainloop()