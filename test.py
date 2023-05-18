import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gráfica")
ventana.geometry("400x300")

# Crear un widget Canvas
canvas = tk.Canvas(ventana, width=400, height=300)
canvas.pack()

# Datos de la gráfica (ejemplo)
datos = [10, 20, 30, 40, 50]

# Calcular las coordenadas de los puntos de la gráfica
coordenadas = []
x = 50
ancho_barra = 50
for dato in datos:
    y = 300 - dato
    coordenadas.append((x, y, x + ancho_barra, 300))
    x += ancho_barra + 10

# Dibujar las barras de la gráfica en el Canvas
for coordenada in coordenadas:
    canvas.create_rectangle(coordenada, fill="blue")

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
