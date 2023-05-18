import json
import tkinter as tk
from tkinter import ttk, messagebox, Tk, PhotoImage, Label
import menu
from sesion import sesion


# Crear la ventana principal
ventana = Tk()
ventana.title('Bienvenido')
# ventana.geometry("521x430")
ventana.resizable(False, False)
menu.crear_menu(ventana)  # Inserta el menú

# Crear un widget de etiqueta para el logo
logo = PhotoImage(file='data/logo.png')
logo_label = Label(ventana, image=logo)
logo_label.grid(row=0, column=0, columnspan=2)

# Crear un widget de etiqueta para el título
label_titulo = Label(ventana, text='*** Lista de gastos ***', font=('Arial', 12, 'bold'))
label_titulo.grid(row=1, column=0, columnspan=2)


# Crear el árbol para mostrar las categorías
lista_categorias = ttk.Treeview(ventana, columns=("nombre", "descripcion"))
lista_categorias.heading("#0", text="ID")
lista_categorias.column("#0", width=50)
lista_categorias.heading("nombre", text="Nombre")
lista_categorias.column("nombre", width=150)
lista_categorias.heading("descripcion", text="Descripción")
lista_categorias.grid(row=2, column=0, columnspan=5, sticky='nsew')

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
    if not seleccion:
        messagebox.showerror("Error", "Seleccione una categoría para eliminar.")
        return
    categoria_seleccionada = lista_categorias.item(seleccion)
    nombre = categoria_seleccionada["values"][0]

    # Cargar las categorías del archivo JSON
    try:
        with open("data/categorias.json", "r") as archivo:
            categorias = json.load(archivo)
    except FileNotFoundError:
        categorias = []

    # Verificar si la categoría seleccionada tiene gastos asociados
    with open("data/gastos.json", "r") as archivo:
        gastos = json.load(archivo)
    for gasto in gastos:
        if gasto["categoria"] == nombre:
            messagebox.showerror("Error", "No se puede eliminar una categoría con gastos asociados.")
            return

    # Confirmar la eliminación de la categoría
    if not messagebox.askyesno("Confirmar", "¿Está seguro de eliminar la categoría seleccionada?"):
        return

    # Eliminar la categoría de la lista
    categorias = [c for c in categorias if c["nombre"] != nombre]

    # Guardar las categorías actualizadas en el archivo JSON
    with open("data/categorias.json", "w") as archivo:
        json.dump(categorias, archivo)

    # Volver a cargar las categorías en el árbol
    cargar_categorias()



# Botón para cargar las categorías
boton_cargar = tk.Button(ventana, text="Cargar Categorías", command=cargar_categorias)
boton_cargar.grid(row=4, column=0)

# Botón para eliminar una categoría
boton_eliminar = tk.Button(ventana, text="Eliminar Categoría", command=eliminar_categoria)
boton_eliminar.grid(row=4, column=1)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()