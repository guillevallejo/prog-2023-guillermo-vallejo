import json
import locale
import tkinter as tk
from tkinter import Tk, ttk, PhotoImage, Label, END
import menu
from sesion import sesion

# Crear la ventana principal
ventana = Tk()
ventana.title('Bienvenido')
#ventana.geometry("521x430")
ventana.resizable(False, False)
menu.crear_menu(ventana) # Inserta el menú

# Crear un widget de etiqueta para el logo
logo = PhotoImage(file='data/logo.png')
logo_label = Label(ventana, image=logo)
logo_label.grid(row=0, column=0, columnspan=2)

# Crear un widget de etiqueta para el título
label_titulo = Label(ventana, text='*** Lista de gastos ***', font=('Arial', 12, 'bold'))
label_titulo.grid(row=1, column=0, columnspan=2)

# Crear el árbol para mostrar los gastos
lista_gastos = ttk.Treeview(ventana, columns=("fecha", "email", "categoria", "monto"))
lista_gastos.heading("#0", text="ID")
lista_gastos.column("#0", width=5)
lista_gastos.heading("fecha", text="Fecha")
lista_gastos.column("fecha", width=20)
lista_gastos.heading("email", text="Usuario")
lista_gastos.column("email", width=20)
lista_gastos.heading("categoria", text="Categoría")
lista_gastos.column("categoria", width=20)
lista_gastos.heading("monto", text="Monto")
lista_gastos.column("monto", width=20)
lista_gastos.grid(row=2, column=0, columnspan=5, sticky='nsew')

def cargar_gastos():
    # Cargar los gastos del archivo JSON
    # Configurar el formato de moneda
    locale.setlocale(locale.LC_ALL, '')  # Configurar la configuración regional actual

    
    try:
        with open("data/gastos.json", "r") as archivo:
            gastos = json.load(archivo)
    except FileNotFoundError:
        gastos = []

    # Limpiar el árbol antes de cargar los gastos
    lista_gastos.delete(*lista_gastos.get_children())

    # Filtrar los gastos por el usuario activo de la sesión
    usuario_activo = sesion()
    gastos_filtrados = [gasto for gasto in gastos if gasto["email"] == usuario_activo]

    # Insertar los gastos filtrados en el árbol
    for gasto in gastos_filtrados:
        fecha = gasto["fecha"]
        email = gasto["email"]
        categoria = gasto["categoria"]
        monto = gasto["monto"]
        monto_con_signo = locale.currency(monto)  # Obtener el monto con signo de moneda
        lista_gastos.insert("", tk.END, values=(fecha, email, categoria, monto_con_signo))

# Botón para cargar los gastos
boton_cargar = tk.Button(ventana, text="Cargar gastos", command=cargar_gastos)
boton_cargar.grid(row=3, column=0, sticky='nsew')

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
