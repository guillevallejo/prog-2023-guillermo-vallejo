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
label_titulo = Label(ventana, text='*** Ahorra ***', font=('Arial', 12, 'bold'))
label_titulo.grid(row=1, column=0, columnspan=2)

# Crear un widget de etiqueta para el mensaje
mensaje = "Control Total te invita ahorrar y que mejores tu responsabilidad financiera, usar tecnología como método de seguimiento de finanzas va más allá, no solo colocar montos e ir restándolos o sumándolos, se trata de ayudarte a lograr un mejor manejo del dinero. Sabías que el 77.4% de los colombianos no cuenta con el sueldo mensual suficiente para comenzar a ahorrar y el 6.2% comenta que ni siquiera tiene ingresos para poder hacerlo, es alarmante conocer estos datos ya que, ahorrar es una ventaja para problemas del futuro. Es por esto a que te invitamos a que aproveches al máximo nuestra app y mejore tu vida financiera."
label_mensaje = Label(ventana, text=mensaje, padx=20, pady=20, wraplength=400)
label_mensaje.grid(row=2, column=0, columnspan=2)

# Mostrar la ventana principal
ventana.mainloop()
