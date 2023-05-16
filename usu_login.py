import json
from tkinter import Tk, Button, Entry, Label, PhotoImage, END

# Crear la ventana de inicio de sesión
ventana = Tk()
ventana.title('Inicio de Sesión')
ventana.geometry("521x430")
ventana.resizable(False,False)


# Crear un widget de etiqueta para el logo
logo = PhotoImage(file='data/logo.png')
logo_label = Label(ventana, image=logo)
logo_label.grid(row=0, column=0, columnspan=2)

# Crear los widgets
label_titulo = Label(ventana, text='*** Inicio de Sesión ***', font=('Arial', 14,'bold'),)
label_titulo.grid(row=1, column=0, columnspan=2)
label_email = Label(ventana, text='Email:')
input_email = Entry(ventana)
label_password = Label(ventana, text='Contraseña:')
input_password = Entry(ventana, show='*')
button_ingresar = Button(ventana, text='Ingresar')
label_mensaje = Label(ventana)

# Posicionar los widgets usando grid
label_email.grid(row=2, column=0)
input_email.grid(row=2, column=1)
label_password.grid(row=3, column=0)
input_password.grid(row=3, column=1)
button_ingresar.grid(row=4, column=0, columnspan=2)
label_mensaje.grid(row=5, column=0, columnspan=2)

# Definir la función que se ejecutará al hacer clic en el botón de ingresar
def iniciar_sesion():
    email = input_email.get().strip()
    password = input_password.get().strip()

    # Cargar usuarios existentes del archivo JSON
    try:
        with open("data/usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, se crea una lista vacía
        usuarios = []

    # Validar si el usuario existe
    for u in usuarios:
        if u["email"] == email and u["password"] == password:
            mensaje = "Inicio de sesión exitoso."
            label_mensaje.config(text=mensaje)
            return

    mensaje = "El email o la contraseña es incorrecta."
    label_mensaje.config(text=mensaje)

# Conectar la función iniciar_sesion() con el evento de clic en el botón de ingresar
button_ingresar.config(command=iniciar_sesion)

# Mostrar la ventana de inicio de sesión
ventana.mainloop()

