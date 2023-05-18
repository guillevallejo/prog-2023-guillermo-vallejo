import tkinter as tk
from tkinter import messagebox, Label, font
from PIL import Image, ImageTk
import json
import subprocess

# Crear la ventana de bienvenida
ventana_inicio = tk.Tk()
ventana_inicio.title('Bienvenido')
ventana_inicio.geometry("521x430")
ventana_inicio.resizable(False,False)

# Cargar la imagen del logo
logo_image = Image.open('data/logo.png')
logo_photo = ImageTk.PhotoImage(logo_image)

# Crear una etiqueta para el logo
logo = Label(ventana_inicio, image=logo_photo)
logo.grid(row=0, column=0, columnspan=5)

# Configurar la fuente
fuente = font.Font(family='Arial', size=12, weight='bold')


def iniciar_sesion():
    email = entry_email.get()
    contraseña = entry_contraseña.get()

    # Cargar la base de datos de usuarios desde el archivo JSON
    try:
        with open("data/usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró la base de datos de usuarios.")
        return

    # Verificar las credenciales de inicio de sesión
    for u in usuarios:
        if u["email"] == email and u["password"] == contraseña:
            # Guardar la sesión en un archivo JSON
            datos_sesion = {"usuario": email}
            try:
                with open("data/sesion.json", "w") as archivo_sesion:
                    json.dump(datos_sesion, archivo_sesion)
            except IOError:
                messagebox.showerror("Error", "No se pudo guardar la sesión.")
                return

            # Mostrar mensaje de inicio de sesión exitoso
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")

            # Cerrar la ventana de inicio de sesión
            ventana_inicio.destroy()

            # Abrir la ventana principal
            abrir_ventana_principal()
            return

    # Mostrar mensaje de error de inicio de sesión
    messagebox.showerror("Inicio de Sesión", "Credenciales inválidas.")

def abrir_ventana_principal():
    # Crear la ventana principal
    ventana_principal = tk.Tk()

    # Cargar la sesión desde el archivo JSON
    try:
        with open("data/sesion.json", "r") as archivo_sesion:
            datos_sesion = json.load(archivo_sesion)
            usuario_sesion = datos_sesion["usuario"]
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror("Error", "No se pudo cargar la sesión.")
        return

    # Configurar la ventana principal
    label_bienvenida = tk.Label(ventana_principal, text=f"Bienvenido, {usuario_sesion}!")
    label_bienvenida.grid(row=0, column=0)

    # Mostrar la ventana principal
    ventana_principal.mainloop()

# Crear la ventana de inicio de sesión

# Configurar la ventana de inicio de sesión
label_email = tk.Label(ventana_inicio, text="Email:")
label_email.grid(row=1, column=0)
entry_email = tk.Entry(ventana_inicio)
entry_email.grid(row=1, column=1)

label_contraseña = tk.Label(ventana_inicio, text="Contraseña:")
label_contraseña.grid(row=2, column=0)
entry_contraseña = tk.Entry(ventana_inicio, show="*")
entry_contraseña.grid(row=2, column=1)

button_iniciar = tk.Button(ventana_inicio, text="Iniciar Sesión", command=iniciar_sesion, width=16, height=2)
button_iniciar.grid(row=3, column=1, columnspan=2)

def ventana_registro():
    # Cerrar la ventana de bienvenida
    ventana_inicio.destroy()
    subprocess.run(["python", "usu_reg.py"])

button_registrar = tk.Button(ventana_inicio, text="Registrar", command=ventana_registro, width=16, height=2)
button_registrar.grid(row=4, column=1, columnspan=2)

# Mostrar la ventana de inicio de sesión
ventana_inicio.mainloop()
