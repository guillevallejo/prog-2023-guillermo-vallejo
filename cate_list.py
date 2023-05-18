import json
import tkinter as tk
from tkinter import ttk, PhotoImage, Label, messagebox
import menu
from sesion import sesion

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Lista de Categorías')
menu.crear_menu(ventana)  # Inserta el menú

# Determinar el tamaño de la fuente para los labels
font = ('Arial', 14)

# Crear un widget de etiqueta para el logo
logo = tk.PhotoImage(file='data/logo.png')
logo_label = tk.Label(ventana, image=logo)
logo_label.grid()

# Crear un widget de etiqueta para el título
label_titulo = tk.Label(ventana, text='*** Listado de Categorías ***', font=font, justify=tk.CENTER)
label_titulo.grid()

# Crear el árbol para mostrar las categorías
lista_categorias = ttk.Treeview(ventana, columns=("descripcion",))
lista_categorias.heading("#0", text="Categoría")
lista_categorias.column("#0", width=150)
lista_categorias.heading("descripcion", text="Descripción")
lista_categorias.grid(row=2, column=0, columnspan=5, sticky='nsew')

def cargar_categorias():
    # Cargar la lista de categorías del archivo JSON
    try:
        with open("data/categorias.json", "r", encoding="utf8") as archivo:
            categorias = json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, mostrar un mensaje de error
        messagebox.showerror("Error", "No hay categorías registradas.")
        return

    # Limpiar el árbol antes de cargar las categorías
    lista_categorias.delete(*lista_categorias.get_children())

    # Insertar las categorías en el árbol
    for categoria in categorias:
        nombre = categoria["nombre"]
        descripcion = categoria["descripcion"]
        lista_categorias.insert("", tk.END, text=nombre, values=(descripcion,))

# Botón para cargar las categorías
boton_cargar = tk.Button(ventana, text="Cargar Categorías", command=cargar_categorias)
boton_cargar.grid()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
