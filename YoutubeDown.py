from ast import Str
from pickletools import string1
from pydoc import text
from tkinter import *
from turtle import width
from unittest import result 

from pytube import YouTube


#INTERFACE
janela = Tk()

janela.geometry('320x300')
janela.configure(background='#dde')

janela.title('Download Youtube')

texto_inicial = Label(janela,text= 'Baixe Vídeos na Melhor Qualidade Direto do Youtube',background='#dde', foreground='#009')
texto_inicial.grid(column= 0, row=0)

texto_inicial2 = Label(janela, text= 'Sem anúcios, gratuito e seguro',background='#dde', foreground='#009')
texto_inicial2.grid(column= 0, row=1)

texto_orientacao = Label(janela, text= 'Insira a URL do vídeo que deseja baixar aqui:',background='#dde', foreground='#009')
texto_orientacao2 = Label(janela, text= 'Insira o caminho da pasta onde deseja salvar o video aqui:' ,background='#dde', foreground='#009')
texto_orientacao.grid(column=0 ,row=2)
texto_orientacao2.grid(column=0, row=4)

caixa_texto= Entry(janela)
caixa_texto.grid(column=0, row=3)
caixa_texto2= Entry(janela)
caixa_texto2.grid(column=0, row=5)
 

var = str(caixa_texto) 


def iniciar():

    yt = YouTube(caixa_texto.get())

    #print(caixa_texto.get('1.0', 'end-1c'))

    result = {
        'Titulo': yt.title,
        'Número de views': yt.views,
        'Tamanho': yt.length,
        'Avaliação': yt.rating,
    }


    ys = yt.streams.get_highest_resolution()

    print(result)
    print('Seu vídeo está sendo baixado...')

    def baixar(): 
        ys.download(str (caixa_texto2.get()))
        print('Donwload concluído com sucesso!')

    baixar()

botao = Button(janela,text='DONWLOAD', command= iniciar)
botao.grid(column=0, row=6)

janela.mainloop()