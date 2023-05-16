import json
from tkinter import Tk, Label, Entry, Button, PhotoImage
import menu
from sesion import sesion

# Creamos la ventana
ventana = Tk()
ventana.title('Buscar Usuario')
ventana.geometry("521x430")
ventana.resizable(False,False)
menu.crear_menu(ventana) # Inserta el menu

# Crear un widget de etiqueta para el logo
logo = PhotoImage(file='data/logo.png')
logo_label = Label(ventana, image=logo)
logo_label.grid(row=0, column=0, columnspan=5)

# Determinar el tamaño del texto para los label
font = ('Arial', 14)

# Creamos los widgets
label_email = Label(ventana, text='usuario (email):')
campo_email = Entry(ventana)
boton_buscar = Button(ventana, text='Buscar')
label_mensaje = Label(ventana)

# Configuramos los widgets utilizando grid
label_email.grid(row=1, column=0, padx=10, pady=10)
campo_email.grid(row=1, column=1, padx=10, pady=10)
boton_buscar.grid(row=2, column=1, padx=10, pady=10)
label_mensaje.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Función para buscar al usuario
def buscar_usuario():
    with open('data/usuarios.json') as archivo:
        usuarios = json.load(archivo)

    # Buscamos el usuario
    email = campo_email.get()
    encontrado = False
    for usuario in usuarios:
        if usuario['email'] == email:
            mensaje = f"Usuario encontrado:\nNombre: {usuario['nombre']}\nEmail: {usuario['email']}"
            label_mensaje.config(text=mensaje, fg='green')
            encontrado = True
            break

    # Si no se encuentra el usuario
    if not encontrado:
        mensaje = f"No se encontró el usuario con email {email}"
        label_mensaje.config(text=mensaje, fg='red')

# Conectamos la función al botón
boton_buscar.config(command=buscar_usuario)

# Mostramos la ventana
ventana.mainloop()
