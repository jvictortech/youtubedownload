from tkinter import *
from tkinter import messagebox, filedialog
import tkinter 
from pytube import YouTube

#Interface
def Widgets():

    #Campos de entrada

    entrada_1 = Label(root, text = "Link do Youtube:", bg="#E8D579")
    entrada_1.grid(row= 1, column=0, pady=5, padx=5)
    root.linkText= Entry(root, width=55, textvariable= link_youtube)
    root.linkText.grid(row=1,column=1, pady=5, padx=5, columnspan=2)

    entrada_2 = Label(root, text="Pasta de Destino:", bg="#E8D579")
    entrada_2.grid(row=2, column=0, pady= 5, padx = 5)
    root.destinoText = Entry(root, width=40, textvariable= caminho_baixar)
    root.destinoText.grid(row=2, column=1, pady=5, padx=5)

    #Botões 

    procura = Button(root, text='Procurar', command=Diretorio, width=10, bg="#05E8E0")
    procura.grid(row=2, column=2, pady=1, padx=1)

    baixar = Button(root, text="Baixar", command= Iniciar, width=20, bg="#05e8e0")
    baixar.grid(row=3, column=1, pady=3, padx=3)

def Diretorio():
    local_donwload = filedialog.askdirectory(initialdir="Escolha aonde quer salvar o vídeo")
    caminho_baixar.set(local_donwload)
 
def Iniciar():

    YouTube_link = link_youtube.get()
    pasta_salvar = caminho_baixar.get()

    getVideo = YouTube(YouTube_link)
    videoStream = getVideo.streams.first()
    videoStream.download(pasta_salvar)

    messagebox.showinfo("Video Baixado com Sucesso!!", "Seu video está salvo em:" + pasta_salvar)

#Janela Principal
root = tkinter.Tk()
root.geometry("600x120")
root.resizable(False, False)
root.title("Baixar Vídeo do Youtube")
root.config(background="#000000")

link_youtube = StringVar()
caminho_baixar = StringVar()

Widgets()
root.mainloop()