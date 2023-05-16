import json
import tkinter as tk
from tkinter import Tk, ttk, PhotoImage, Label, END
import menu
from sesion import sesion

# Crear la ventana principal
ventana = Tk()
ventana.title('Lista de gastos')
menu.crear_menu(ventana) # Inserta el menu

# Crear un widget de etiqueta para el logo
logo = PhotoImage(file='data/logo.png')
logo_label = Label(ventana, image=logo)
logo_label.grid(row=0, column=0, columnspan=2)

# Crear un widget de etiqueta para el título
label_titulo = Label(ventana, text='*** Lista de gastos ***', font=('Arial', 12, 'bold'))
label_titulo.grid(row=1, column=0, columnspan=2)

# Crear el árbol para mostrar los gastos
lista_gastos = ttk.Treeview(ventana, columns=("email", "fecha", "categoria", "monto"))
lista_gastos.heading("#0", text="ID")
lista_gastos.column("#0", width=50)
lista_gastos.heading("email", text="Email")
lista_gastos.column("email", width=120)
lista_gastos.heading("fecha", text="Fecha")
lista_gastos.column("fecha", width=100)
lista_gastos.heading("categoria", text="Categoría")
lista_gastos.column("categoria", width=80)
lista_gastos.heading("monto", text="Monto")
lista_gastos.column("monto", width=60)
lista_gastos.grid(row=2, column=0, columnspan=5, sticky='nsew')

def cargar_gastos():
    # Cargar los gastos del archivo JSON
    try:
        with open("data/gastos.json", "r") as archivo:
            gastos = json.load(archivo)
    except FileNotFoundError:
        gastos = []

    # Limpiar el árbol antes de cargar los gastos
    lista_gastos.delete(*lista_gastos.get_children())

    # Insertar los gastos en el árbol
    for i, gasto in enumerate(gastos, start=1):
        email = gasto["email"]
        fecha = gasto["fecha"]
        categoria = gasto["categoria"]
        monto = gasto["monto"]
        lista_gastos.insert("", tk.END, text=str(i), values=(email, fecha, categoria, monto))


# Botón para cargar los gastos
boton_cargar = tk.Button(ventana, text="Cargar Gastos", command=cargar_gastos)
boton_cargar.grid(row=3, column=0, sticky='nsew')

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
