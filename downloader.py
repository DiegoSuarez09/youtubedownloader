from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MesageBox




def accion():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

def popup():
    MesageBox.showinfo("Sobre mi", "Autor: Diego Suarez")
    
    
root = Tk()
root.config(bd=15)
root.title('Descargar')

imagen = PhotoImage(file='youtube-logo.png')
imagen = imagen.subsample(2) 

foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)
menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar)
menubar.add_cascade(label='Para mas informacion', menu=helpmenu)
helpmenu.add_command(label='Informacion del autor', command=popup)
menubar.add_command(label="Salir", command=root.destroy)

instrucciones = Label(root, text="Por favor ingresa la URL del video que desea descargar\n")
instrucciones.grid(row=0, column=1)
videos = Entry(root)
videos.grid(row=1, column=1)

boton= Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)

root.mainloop()
