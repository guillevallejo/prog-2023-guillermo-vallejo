import json
from tkinter import Tk, Label, Button, font, Entry, PhotoImage
import subprocess
import re

# Crear la ventana de bienvenida
ventana = Tk()
ventana.title('Bienvenido')
#ventana.geometry("521x430")
ventana.resizable(False,False)

# Crear un widget de etiqueta para el logo
logo = PhotoImage(file='data/logo.png')
logo_label = Label(ventana, image=logo)
logo_label.grid()

# Determinar el tamaño del texto para los label
font = ('Arial', 14)

# Crear los widgets
label_titulo = Label(ventana, text='*** registro de usuario ***', font=font)
label_nombre = Label(ventana, text='Nombre:')
input_nombre = Entry(ventana)
label_email = Label(ventana, text='Email:')
input_email = Entry(ventana)
label_password = Label(ventana, text='Contraseña:')
input_password = Entry(ventana, show='*')
button_registrar = Button(ventana, text='Registrar',  width=16, height=2)
button_entrar = Button(ventana, text='Entrar',  width=16, height=2)
label_mensaje = Label(ventana)

# Definir la disposición de los widgets en la ventana
logo_label.grid()
label_titulo.grid()
label_nombre.grid()
input_nombre.grid()
label_email.grid()
input_email.grid()
label_password.grid()
input_password.grid()
button_registrar.grid()
button_entrar.grid()
label_mensaje.grid()

# Definir la función que se ejecutará al hacer clic en el botón de registrar
def registrar_usuario():
    nombre = input_nombre.get().strip()
    email = input_email.get().strip()
    password = input_password.get().strip()
    usuario = {"nombre": nombre, "email": email, "password": password}

    # Cargar usuarios existentes del archivo JSON
    try:
        with open("data/usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        
        usuarios = []

    # Validar que los campos no estén vacíos
    if not nombre or not email or not password:
        label_mensaje.config(text='Todos los campos son obligatorios.')
        return
    
     # Validar el formato del correo electrónico
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        label_mensaje.config(text='Ingrese un correo electrónico válido.')
        return

    # Validar si el email ya está registrado
    if email in usuarios:
        mensaje = "El email ya está registrado."
        label_mensaje.config(text=mensaje)
        return

    # Agregar el nuevo usuario al diccionario de usuarios
    #usuarios[email] = usuario
    usuarios.append(usuario)
    
    # Guardar el diccionario de usuarios en el archivo JSON
    with open("data/usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)
        
     # Limpiar las cajas de texto
    input_nombre.delete(0, 'end')
    input_email.delete(0, 'end')
    input_password.delete(0, 'end')

    mensaje = "Usuario registrado correctamente."
    label_mensaje.config(text=mensaje)

def ventana_inicio_s():
    # Cerrar la ventana de bienvenida
    ventana.destroy()
    subprocess.run(["python", "login.py"])

# Conectar la función registrar_usuario() con el evento de clic en el botón de registrar
button_registrar.config(command=registrar_usuario)
button_entrar.config(command=ventana_inicio_s)

# Mostrar la ventana
ventana.mainloop()
