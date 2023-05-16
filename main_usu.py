import sys
import json
from tkinter import Tk, Label, Button, font
from PIL import Image, ImageTk
import menu
from sesion import sesion

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
fuente = font.Font(family='Arial', size=12, weight='bold')

# Crear el widget de etiqueta
label = Label(ventana, text='*** Gestion de usuarios ***', font=fuente)
label.grid(row=1, column=0, columnspan=5, sticky='nsew')

# Crear botones
boton_entrar = Button(ventana, text='Iniciar Registro', width=16, height=2)
boton_modificar = Button(ventana, text='Modificar Usuario', width=16, height=2)
boton_buscar = Button(ventana, text='Buscar Usuario', width=16, height=2)
boton_eliminar = Button(ventana, text='Eliminar Usuario', width=16, height=2)

# Ubicar los botones utilizando grid
boton_entrar.grid(row=2, column=0, padx=1, pady=5)
boton_modificar.grid(row=2, column=2, padx=1, pady=5)
boton_buscar.grid(row=2, column=3, padx=1, pady=5)
boton_eliminar.grid(row=2, column=4, padx=1, pady=5)

# Funciones para los botones
def ventana_registro():
    # Cerrar la ventana de bienvenida
    ventana.destroy()

def ventana_busqueda():
    # Cerrar la ventana de bienvenida
    ventana.destroy()

def ventana_elimina():
    # Cerrar la ventana de bienvenida
    ventana.destroy()

def ventana_modifica():
    # Cerrar la ventana de bienvenida
    ventana.destroy()

# Conectar las funciones con los botones
boton_entrar.config(command=ventana_registro)
boton_modificar.config(command=ventana_modifica)
boton_buscar.config(command=ventana_busqueda)
boton_eliminar.config(command=ventana_elimina)

# Mostrar la ventana de bienvenida
ventana.mainloop()
