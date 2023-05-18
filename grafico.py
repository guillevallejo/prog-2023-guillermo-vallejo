import json
from tkinter import Tk, ttk, PhotoImage, Label, END, messagebox, Button
import menu
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar_barras(canvas):
    # Cargar los datos del archivo JSON
    with open('data/gastos.json') as archivo:
        datos = json.load(archivo)

    # Calcular la suma de los montos por categoría
    categorias = {}
    for registro in datos:
        categoria = registro['categoria']
        monto = float(registro['monto'])
        categorias[categoria] = categorias.get(categoria, 0) + monto

    # Crear el gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(categorias.keys(), categorias.values())
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Suma de montos')
    ax.set_title('Gastos por categoría')
    ax.tick_params(axis='x', rotation=45)

    # Mostrar el gráfico en el Canvas
    canvas.figure = fig
    canvas.draw()

def graficar_torta(canvas):
    # Cargar los datos del archivo JSON
    with open('data/gastos.json') as archivo:
        datos = json.load(archivo)

    # Calcular la suma de los montos por categoría
    categorias = {}
    for registro in datos:
        categoria = registro['categoria']
        monto = float(registro['monto'])
        categorias[categoria] = categorias.get(categoria, 0) + monto

    # Crear el gráfico de torta
    fig, ax = plt.subplots()
    ax.pie(categorias.values(), labels=categorias.keys(), autopct='%1.1f%%')
    ax.set_title('Distribución de gastos por categoría')

    # Mostrar el gráfico en el Canvas
    canvas.figure = fig
    canvas.draw()

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
label_titulo = Label(ventana, text='*** Graficos ***', font=('Arial', 12, 'bold'))
label_titulo.grid(row=1, column=0, columnspan=2)

# Crear el Canvas
canvas = FigureCanvasTkAgg(plt.figure())
canvas.get_tk_widget().grid()

# Botones para generar los gráficos
btn_barras = Button(ventana, text='Gráfico de Barras', command=lambda: graficar_barras(canvas))
btn_barras.grid(pady=10)

btn_torta = Button(ventana, text='Gráfico de Torta', command=lambda: graficar_torta(canvas))
btn_torta.grid()

# Ejecutar la ventana principal
ventana.mainloop()
