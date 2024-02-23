from pytube import YouTube
from pytube import Playlist
p=Playlist('https://www.youtube.com/watch?v=cyBEcIW7aiw&list=PLNM4Hm5ilXqjnRVT6Je4LnTiFTurkmy41')
#creamos un objeto yt


for video in p.videos:
    print("descargando:",video.title)
    stream=video.streams.filter(only_audio=True).first()
    stream.download(r"E:\Musica\Lucas sugo y mas")
