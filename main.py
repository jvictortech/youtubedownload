
from unittest import result
from pytube import YouTube


linkurl = input('Cole a URL do vídeo que deseja baixar: ')
save = input('Cole o caminho da pasta em que deseja salvar o video: ')

yt = YouTube(linkurl)

result = {
    'Titulo': yt.title,
    'Número de views': yt.views,
    'Tamanho': yt.length,
    'Avaliação': yt.rating,
}


ys = yt.streams.get_highest_resolution()

print('Seu vídeo está sendo baixado...')

ys.download(save)
print('Donwload concluído com sucesso!')

