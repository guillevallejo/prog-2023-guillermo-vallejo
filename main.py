from tkinter import Tk, Label, Button, font
from PIL import Image, ImageTk
import subprocess

# Crear la ventana de bienvenida
ventana_main = Tk()
ventana_main.title('Bienvenido')
ventana_main.geometry("521x430")
ventana_main.resizable(False,False)

# Cargar la imagen del logo
logo_image = Image.open('data/logo.png')
logo_photo = ImageTk.PhotoImage(logo_image)

# Crear una etiqueta para el logo
logo = Label(ventana_main, image=logo_photo)
logo.grid(row=0, column=0, columnspan=5)

# Configurar la fuente
fuente = font.Font(family='Arial', size=12, weight='bold')

# Crear el widget de etiqueta
label = Label(ventana_main, text='*** Login ***', font=fuente)
label.grid(row=1, column=0, columnspan=5, sticky='nsew')

# Crear botones
boton_login = Button(ventana_main, text='ENTRAR', width=16, height=2)
boton_registro = Button(ventana_main, text='REGISTRO', width=16, height=2)


# Ubicar los botones utilizando grid
boton_login.grid(row=2, column=2, padx=1, pady=0)
boton_registro.grid(row=3, column=2, padx=1, pady=0)

# Funciones para los botones
def ventana_login():
    # Cerrar la ventana de bienvenida
    ventana_main.destroy()
    subprocess.run(["python", "login.py"])

def ventana_registro():
    # Cerrar la ventana de bienvenida
    ventana_main.destroy()
    subprocess.run(["python", "usu_reg.py"])

# Conectar las funciones con los botones
boton_login.config(command=ventana_login)
boton_registro.config(command=ventana_registro)

# Mostrar la ventana de bienvenida
ventana_main.mainloop()
