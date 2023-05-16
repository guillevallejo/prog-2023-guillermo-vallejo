from tkinter import Tk, Label, Button, font, messagebox
from PIL import Image, ImageTk
import json
import subprocess
import menu
from sesion import sesion

#######################################################################
# trae el usuario en sesion activa.
try:
    with open("data/sesion.json", "r") as archivo_sesion:
        datos_sesion = json.load(archivo_sesion)
        usuario_sesion = datos_sesion["usuario"]
except (FileNotFoundError, json.JSONDecodeError):
    messagebox.showerror("Error", "No se pudo cargar la sesión.")
#######################################################################

# Crear la ventana de bienvenida
ventana = Tk()
ventana.title('Bienvenido')
ventana.geometry("521x430")
ventana.resizable(False,False)
menu.crear_menu(ventana) # Inserta el menu

# Cargar la imagen del logo
logo_image = Image.open('data/logo.png')
logo_photo = ImageTk.PhotoImage(logo_image)

# Crear una etiqueta para el logo
logo = Label(ventana, image=logo_photo)
logo.grid(row=0, column=0, columnspan=5)

# Configurar la fuente
fuente = font.Font(family='Arial', size=24, weight='bold')

# Crear el widget de etiqueta
label = Label(ventana, text=f"Hola, {usuario_sesion}!", font=fuente)
label.grid(row=1, column=0, columnspan=5, sticky='nsew')

# Mostrar la ventana de bienvenida
ventana.mainloop()
