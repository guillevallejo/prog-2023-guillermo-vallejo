import json
from datetime import datetime
from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu, messagebox, font
from PIL import Image, ImageTk
import subprocess
import menu
from sesion import sesion


#######################################################################
# trae el usuario en sesion activa.
try:
    with open("data/sesion.json", "r") as archivo_sesion:
        datos_sesion = json.load(archivo_sesion)
        email_sesion = datos_sesion["usuario"]
except (FileNotFoundError, json.JSONDecodeError):
    messagebox.showerror("Error", "No se pudo cargar la sesión.")

# Obtener el nombre de usuario correspondiente al email de la sesión activa
try:
    with open("data/usuarios.json", "r") as archivo_usuarios:
        usuarios = json.load(archivo_usuarios)
        for usuario in usuarios:
            if usuario["email"] == email_sesion:
                nombre_usuario = usuario["nombre"]
                break
        else:
            nombre_usuario = "Usuario Desconocido"
except (FileNotFoundError, json.JSONDecodeError):
        nombre_usuario = "Usuario Desconocido"
#######################################################################

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
    categoria = var_categoria.get()
    monto = entry_monto.get()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Validar que el usuario exista
    usuario_encontrado = False
    with open("data/usuarios.json", "r") as usuarios_file:
        usuarios = json.load(usuarios_file)
        for usuario in usuarios:
            if usuario["email"] == email_sesion:
                usuario_encontrado = True
                email = usuario["email"]
                break

    if not usuario_encontrado:
        messagebox.showerror("Error", "El usuario no existe.")
        return
    
      # Validar que los campos no estén vacíos
    if not monto:
        messagebox.showerror("Error", "El campo monto no puede ser vacio.")
        return
    
    try:
        monto = int(monto)  # Convertir el monto a entero
    except ValueError:
        messagebox.showerror("Error", "El campo monto debe ser un número entero.")
        return
    
    # Guardar el gasto en el archivo "gastos.json"
    gasto = {
        "email": email,
        "fecha": fecha,
        "categoria": categoria,
        "monto": monto
    }

    # Cargar los gastos existentes del archivo JSON
    try:
        with open("data/gastos.json", "r") as archivo:
            gastos_existentes = json.load(archivo)
    except FileNotFoundError:
        gastos_existentes = []

    # Agregar el nuevo gasto a la lista existente
    gastos_existentes.append(gasto)

    # Guardar los gastos actualizados en el archivo JSON
    with open("data/gastos.json", "w") as archivo:
        json.dump(gastos_existentes, archivo, indent=4)

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

# Crear el widget de etiqueta
label = Label(ventana, text='*** Registra gastos ***', font=fuente)
label.grid(row=1, column=0, columnspan=5, sticky='nsew')

# Crear etiquetas y campos de entrada
label_usuario = Label(ventana, text="Nombre del usuario:")
label_usuario.grid(row=2, column=0, padx=1, pady=1)

label_n_usuario = Label(ventana, text=f"{nombre_usuario}", font=fuente)
label_n_usuario.grid(row=2, column=1, padx=1, pady=1)

label_categoria = Label(ventana, text="Categoría:")
label_categoria.grid(row=3, column=0, padx=1, pady=1)
categorias = cargar_categorias()
var_categoria = StringVar(ventana)
var_categoria.set(categorias[0])
dropdown_categoria = OptionMenu(ventana, var_categoria, *categorias)
dropdown_categoria.grid(row=3, column=1, padx=1, pady=1)

label_monto = Label(ventana, text="Monto:")
label_monto.grid(row=4, column=0, padx=1, pady=1)
entry_monto = Entry(ventana)
entry_monto.grid(row=4, column=1, padx=1, pady=1)

# Crear botón para guardar el gasto
boton_guardar = Button(ventana, text="Guardar", command=guardar_gasto, width=16, height=2)
boton_guardar.grid(row=5, column=1, columnspan=2, padx=1, pady=1)

# Mostrar la ventana
ventana.mainloop()
