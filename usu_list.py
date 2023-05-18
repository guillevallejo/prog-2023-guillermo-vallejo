import json
import tkinter as tk
from tkinter import ttk, PhotoImage, Label, messagebox
import menu
from sesion import sesion

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Lista y Eliminación de Usuarios')
#ventana.geometry("521x430")
ventana.resizable(False,False)
menu.crear_menu(ventana) # Inserta el menu

# Crear un widget de etiqueta para el logo
logo = PhotoImage(file='data/logo.png')
logo_label = Label(ventana, image=logo)
logo_label.grid(row=0, column=0, columnspan=2)

# Crear un widget de etiqueta para el título
label_titulo = Label(ventana, text='*** Lista de usuario ***', font=('Arial', 12, 'bold'))
label_titulo.grid(row=1, column=0, columnspan=2)

# Crear el árbol para mostrar los usuarios
lista_usuarios = ttk.Treeview(ventana, columns=("nombre", "email"))
lista_usuarios.heading("#0", text="ID")
lista_usuarios.column("#0", width=50)
lista_usuarios.heading("nombre", text="Nombre")
lista_usuarios.column("nombre", width=150)
lista_usuarios.heading("email", text="Email")
lista_usuarios.grid(row=2, column=0, columnspan=5, sticky='nsew')

def cargar_usuarios():
    # Cargar los usuarios del archivo JSON
    try:
        with open("data/usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        usuarios = []

    # Limpiar el árbol antes de cargar los usuarios
    lista_usuarios.delete(*lista_usuarios.get_children())

    # Insertar los usuarios en el árbol
    for usuario in usuarios:
        nombre = usuario["nombre"]
        email = usuario["email"]
        lista_usuarios.insert("", tk.END, values=(nombre, email))


# Botón para cargar los usuarios
boton_cargar = tk.Button(ventana, text="Cargar Usuarios", command=cargar_usuarios)
boton_cargar.grid(row=3, column=0)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
