from tkinter import Tk, Label
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = Tk()
ventana.title('Bienvenido')
ventana.resizable(False, False)
# menu.crear_menu(ventana)  # Comentado ya que no tengo acceso al código de la función crear_menu

# Cargar la imagen del logo
logo_image = Image.open('data/logo.png')
logo_photo = ImageTk.PhotoImage(logo_image)

# Crear una etiqueta para el logo
logo = Label(ventana, image=logo_photo)
logo.grid(row=0, column=0, columnspan=2)

# Crear un widget de etiqueta para el título
label_titulo = Label(ventana, text='*** Acerca de ***', font=('Arial', 12, 'bold'))
label_titulo.grid(row=1, column=0, columnspan=2)

# Crear un widget de etiqueta para el mensaje
mensaje = "Esta app fue desarrollada en el lenguaje de programación Python mediante la aplicación Visual Studio Code, usando la librería tkinter para crear su interfaz y demás funciones de la misma y está diseñada para el ahorro del usuario. Los desarrolladores de Control Total son Guillermo Vallejo, Juan Vanegas y Juan José Zafra."
label_mensaje = Label(ventana, text=mensaje, padx=20, pady=20, wraplength=400)
label_mensaje.grid(row=2, column=0, columnspan=2)

# Mostrar la ventana principal
ventana.mainloop()
