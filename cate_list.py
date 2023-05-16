import json
import tkinter as tk
from tkinter import ttk
import menu
from sesion import sesion

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Lista de Categorías')
menu.crear_menu(ventana) # Inserta el menu

# Determinar el tamaño de la fuente para los labels
font = ('Arial', 14)

# Crear un widget de etiqueta para el logo
logo = tk.PhotoImage(file='data/logo.png')
logo_label = tk.Label(ventana, image=logo)
logo_label.grid()

# Crear un widget de etiqueta para el título
label_titulo = tk.Label(ventana, text='*** Listado de Categorías ***', font=font, justify=tk.CENTER)
label_titulo.grid()

# Crear un widget de caja de texto para mostrar la lista de categorías
output_categorias = tk.Text(ventana, width=50, height=10)
output_categorias.grid()

# Crear un botón para cargar la lista de categorías
button_cargar = tk.Button(ventana, text='Cargar')
button_cargar.grid()

# Definir la función que se ejecutará al hacer clic en el botón de cargar
def cargar_categorias():
    # Cargar la lista de categorías del archivo JSON
    try:
        with open("data/categorias.json", "r", encoding="utf8") as archivo:
            categorias = json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, mostrar un mensaje en la caja de texto de salida
        output_categorias.delete(1.0, tk.END)
        output_categorias.insert(tk.END, 'No hay categorías registradas.')
        return

    # Crear una lista de cadenas para almacenar las categorías y sus descripciones
    categorias_str = []
    for categoria in categorias:
        categoria_str = f"{categoria['nombre']}: {categoria['descripcion']}\n"
        categorias_str.append(categoria_str)

    # Concatenar todas las cadenas de categorías y sus descripciones en una sola cadena
    categorias_str_concat = '\n'.join(categorias_str)

    # Mostrar la lista de categorías y sus descripciones en la caja de texto de salida
    output_categorias.delete(1.0, tk.END)
    output_categorias.insert(tk.END, categorias_str_concat)
    
# Conectar la función cargar_categorias() con el evento de clic en el botón de cargar
button_cargar.config(command=cargar_categorias)

# Mostrar la ventana principal
ventana.mainloop()
