import json
import tkinter as tk
import menu
from sesion import sesion

ventana = tk.Tk()
ventana.title('Registro de Categorías')
menu.crear_menu(ventana) # Inserta el menu

logo = tk.PhotoImage(file='data/logo.png')
logo_label = tk.Label(ventana, image=logo)
logo_label.grid()

font = ('Arial', 14)

label_titulo = tk.Label(ventana, text='*** Registro de Categorías ***', font=font, justify=tk.CENTER)
label_titulo.grid()

label_nombre = tk.Label(ventana, text='Nombre de la categoría:')
label_nombre.grid()
input_nombre = tk.Entry(ventana)
input_nombre.grid()

label_descripcion = tk.Label(ventana, text='Descripción de la categoría:')
label_descripcion.grid()
input_descripcion = tk.Entry(ventana)
input_descripcion.grid()

def registrar_categoria():
    # Obtener el nombre y la descripción de la categoría ingresados en los campos de entrada
    nombre = input_nombre.get().strip()
    descri = input_descripcion.get().strip()

    try:
        # Cargar categorías existentes del archivo JSON
        with open("data/categorias.json", "r") as archivo:
            categorias = json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, se crea una lista vacía
        categorias = []

    if not nombre:
        # Validar que el campo nombre no esté vacío
        mensaje = 'El campo nombre es obligatorio.'
        label_mensaje.config(text=mensaje)
        return

    for c in categorias:
        if c["nombre"] == nombre:
            # Validar si la categoría ya existe
            mensaje = "La categoría ya existe."
            label_mensaje.config(text=mensaje)
            return

    # Crear un diccionario con el nombre y la descripción de la nueva categoría
    categoria = {"nombre": nombre, "descripcion": descri}
    categorias.append(categoria)

    # Guardar la lista de categorías actualizada en el archivo JSON
    with open("data/categorias.json", "w") as archivo:
        json.dump(categorias, archivo)

    # Limpiar los campos de entrada
    input_nombre.delete(0, tk.END)
    input_descripcion.delete(0, tk.END)

    mensaje = "Categoría registrada correctamente."
    label_mensaje.config(text=mensaje)

    
button_registrar = tk.Button(ventana, text='Registrar', command=registrar_categoria)
button_registrar.grid()

label_mensaje = tk.Label(ventana)
label_mensaje.grid()

ventana.mainloop()
