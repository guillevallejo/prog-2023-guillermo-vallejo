import json
import tkinter as tk
from tkinter import ttk
import menu
from sesion import sesion

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Lista y Eliminación de Categorías')
menu.crear_menu(ventana) # Inserta el menu

# Crear el árbol para mostrar las categorías
lista_categorias = ttk.Treeview(ventana, columns=("nombre", "descripcion"))
lista_categorias.heading("#0", text="ID")
lista_categorias.column("#0", width=50)
lista_categorias.heading("nombre", text="Nombre")
lista_categorias.column("nombre", width=150)
lista_categorias.heading("descripcion", text="Descripción")
lista_categorias.grid(row=0, column=0, columnspan=2)

def cargar_categorias():
    # Cargar las categorías del archivo JSON
    try:
        with open("data/categorias.json", "r") as archivo:
            categorias = json.load(archivo)
    except FileNotFoundError:
        categorias = []

    # Limpiar el árbol antes de cargar las categorías
    lista_categorias.delete(*lista_categorias.get_children())

    # Insertar las categorías en el árbol
    for categoria in categorias:
        nombre = categoria["nombre"]
        descripcion = categoria["descripcion"]
        lista_categorias.insert("", tk.END, values=(nombre, descripcion))

def eliminar_categoria():
    # Obtener la categoría seleccionada
    seleccion = lista_categorias.focus()
    if seleccion:
        categoria_seleccionada = lista_categorias.item(seleccion)
        nombre = categoria_seleccionada["values"][0]

        # Cargar las categorías del archivo JSON
        try:
            with open("data/categorias.json", "r") as archivo:
                categorias = json.load(archivo)
        except FileNotFoundError:
            categorias = []

        # Eliminar la categoría de la lista
        categorias = [c for c in categorias if c["nombre"] != nombre]

        # Guardar las categorías actualizadas en el archivo JSON
        with open("data/categorias.json", "w") as archivo:
            json.dump(categorias, archivo)

        # Volver a cargar las categorías en el árbol
        cargar_categorias()


# Botón para cargar las categorías
boton_cargar = tk.Button(ventana, text="Cargar Categorías", command=cargar_categorias)
boton_cargar.grid(row=1, column=0)

# Botón para eliminar una categoría
boton_eliminar = tk.Button(ventana, text="Eliminar Categoría", command=eliminar_categoria)
boton_eliminar.grid(row=1, column=1)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
