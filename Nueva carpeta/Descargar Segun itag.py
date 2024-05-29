from pytube import YouTube
from pytube import Playlist
p=Playlist('https://www.youtube.com/watch?v=zlbCOD_-8Ik&list=PLyfdsEDOtz3IdarUQR8Up-06uxB209hv9')
#creamos un objeto yt


for video in p.videos:
    print("descargando:",video.title)
    stream=video.streams.get_by_itag(249)
    stream.download(r"E:\Musica\Hugo Flores")
