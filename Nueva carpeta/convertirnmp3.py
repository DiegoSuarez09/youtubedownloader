import os
from moviepy.editor import *

# Ruta de la carpeta con los archivos de audio
folder_path = r'E:\Musica\que Lokura y la Konga'

# Ruta donde se guardarán los archivos MP3
save_path = r'E:\Musica\que Lokura y la Konga\Nueva carpeta'

# Recorrer los archivos en la carpeta
for file_name in os.listdir(folder_path):
    # Ruta completa del archivo
    file_path = os.path.join(folder_path, file_name)
    
    # Verificar si es un archivo de audio
    if file_name.endswith('.mp4') or file_name.endswith('.wav') or file_name.endswith('.flac'):
        # Nombre del archivo sin extensión
        name, ext = os.path.splitext(file_name)
        
        # Ruta de destino del archivo MP3
        mp3_path = os.path.join(save_path, name + '.mp3')
        
        # Convertir a MP3
        audio = AudioFileClip(file_path)
        audio.write_audiofile(mp3_path, bitrate='320k')
        audio.close()

print("La conversión ha finalizado.")
