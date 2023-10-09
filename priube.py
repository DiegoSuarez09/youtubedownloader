from pytube import YouTube
import tkinter as tk


video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Ejemplo de URL de un video de YouTube
yt = YouTube(video_url)


stream = yt.streams.get_highest_resolution()
stream.download()
