from pytube import YouTube
from pytube import Playlist
p=Playlist('https://www.youtube.com/watch?v=v6O0l7IAfU8&list=PLhg-xN-ojp302wvIHs6_DstBrUieJYfm6')
#creamos un objeto yt


for video in p.videos:
    print("descargando:",video.title)
    stream=video.streams.filter(only_audio=True).first()                                                                                                    
    stream.download(r"G:\Banda xxi")
