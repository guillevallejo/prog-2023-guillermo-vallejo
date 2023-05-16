import json
from datetime import datetime
from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu, messagebox, font
from PIL import Image, ImageTk
import subprocess
import menu
from sesion import sesion

def cargar_categorias():
    with open("data/categorias.json", "r") as categorias_file:
        categorias = json.load(categorias_file)
        nombres_categorias = [categoria["nombre"] for categoria in categorias]
        return nombres_categorias

def cargar_usuarios():
    with open("data/usuarios.json", "r") as usuarios_file:
        usuarios = json.load(usuarios_file)
        nombres_usuarios = [usuario["nombre"] for usuario in usuarios]
        return nombres_usuarios

def guardar_gasto():
    # Obtener los valores ingresados por el usuario
    usuario_nombre = var_usuario.get()
    categoria = var_categoria.get()
    monto = entry_monto.get()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Validar que el usuario exista
    usuario_encontrado = False
    with open("data/usuarios.json", "r") as usuarios_file:
        usuarios = json.load(usuarios_file)
        for usuario in usuarios:
            if usuario["nombre"] == usuario_nombre:
                usuario_encontrado = True
                email = usuario["email"]
                break

    if not usuario_encontrado:
        messagebox.showerror("Error", "El usuario no existe.")
        return

    # Guardar el gasto en el archivo "gastos.json"
    gasto = {
        "email": email,
        "fecha": fecha,
        "categoria": categoria,
        "monto": monto
    }

    with open("data/gastos.json", "a") as gastos_file:
        gastos_file.write(json.dumps(gasto, separators=(",", ":")) + "\n")

    messagebox.showinfo("Éxito", "El gasto se ha guardado correctamente.")

# Crear la ventana
ventana = Tk()
ventana.title('Registro de Gastos')
ventana.geometry("521x460")
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


# Crear etiquetas y campos de entrada
label_usuario = Label(ventana, text="Nombre del usuario:")
label_usuario.grid(row=1, column=0, padx=1, pady=1)
usuarios = cargar_usuarios()
var_usuario = StringVar(ventana)
var_usuario.set(usuarios[0])
dropdown_usuario = OptionMenu(ventana, var_usuario, *usuarios)
dropdown_usuario.grid(row=1, column=1, padx=1, pady=1)

label_categoria = Label(ventana, text="Categoría:")
label_categoria.grid(row=2, column=0, padx=1, pady=1)
categorias = cargar_categorias()
var_categoria = StringVar(ventana)
var_categoria.set(categorias[0])
dropdown_categoria = OptionMenu(ventana, var_categoria, *categorias)
dropdown_categoria.grid(row=2, column=1, padx=1, pady=1)

label_monto = Label(ventana, text="Monto:")
label_monto.grid(row=3, column=0, padx=1, pady=1)
entry_monto = Entry(ventana)
entry_monto.grid(row=3, column=1, padx=1, pady=1)

# Crear botón para guardar el gasto
boton_guardar = Button(ventana, text="Guardar", command=guardar_gasto, width=16, height=2)
boton_guardar.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

# Mostrar la ventana
ventana.mainloop()
