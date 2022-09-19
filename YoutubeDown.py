from ast import Str
from pickletools import string1
from pydoc import text
from tkinter import *
from turtle import width
from unittest import result 

from pytube import YouTube


#INTERFACE
janela = Tk()

janela.geometry('400x300')
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

texto_tela = Label(janela, text= '')
texto_tela.grid(column=0, row=7)

texto_tela2 = Label(janela, text= '')
texto_tela2.grid(column=0, row=8)

texto_tela3 = Label(janela, text='')
texto_tela3.grid(column=0, row=9)

caixa_texto= Entry(janela)
caixa_texto.grid(column=0, row=3)
caixa_texto2= Entry(janela)
caixa_texto2.grid(column=0, row=5)
 

var = str(caixa_texto) 


def iniciar():

    yt = YouTube(caixa_texto.get())
    
    result = {
        'Titulo': yt.title,
        'Número de views': yt.views,
        'Tamanho': yt.length,
        'Avaliação': yt.rating,
    }


    ys = yt.streams.get_highest_resolution()

    texto1 = f'O video escolhido foi: {result}'
    texto2 = f'Aguarde Seu vídeo está sendo baixado..'

    texto_tela['text'] = texto1
    texto_tela2['text'] = texto2


    def baixar(): 
        ys.download(str (caixa_texto2.get()))
        texto3 = f'Seu Donwload foi concluído com sucesso'
        texto_tela3['text'] = texto3

    baixar()

botao = Button(janela,text='DONWLOAD', command= iniciar)
botao.grid(column=0, row=6)

janela.mainloop()