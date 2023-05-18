from tkinter import Tk, Label, Button, font, messagebox
from PIL import Image, ImageTk
import json
import subprocess
import menu
from sesion import sesion

#######################################################################
# trae el usuario en sesion activa.
try:
    with open("data/sesion.json", "r") as archivo_sesion:
            datos_sesion = json.load(archivo_sesion)
            email_sesion = datos_sesion["usuario"]
except (FileNotFoundError, json.JSONDecodeError):
    messagebox.showerror("Error", "No se pudo cargar la sesión.")


# Obtener el nombre de usuario correspondiente al email de la sesión activa
try:
    with open("data/usuarios.json", "r") as archivo_usuarios:
        usuarios = json.load(archivo_usuarios)
        for usuario in usuarios:
            if usuario["email"] == email_sesion:
                nombre_usuario = usuario["nombre"]
                break
            else:
                nombre_usuario = "Usuario Desconocido"
except (FileNotFoundError, json.JSONDecodeError):
    nombre_usuario = "Usuario Desconocido"
#######################################################################

# Crear la ventana de bienvenida
ventana = Tk()
ventana.title('Bienvenido')
#ventana.geometry("521x430")
ventana.resizable(False,False)
menu.crear_menu(ventana) # Inserta el menu

# Cargar la imagen del logo
logo_image = Image.open('data/logo.png')
logo_photo = ImageTk.PhotoImage(logo_image)

# Crear una etiqueta para el logo
logo = Label(ventana, image=logo_photo)
logo.grid(row=0, column=0, columnspan=5)

# Configurar la fuente
fuente = font.Font(family='Arial', size=24, weight='bold')

# Crear el widget de etiqueta
label = Label(ventana, text=f"Hola, {nombre_usuario}!", font=fuente)
label.grid(row=1, column=0, columnspan=5, sticky='nsew')

  # Crear una etiqueta con el texto de bienvenida
texto_bienvenida = """¡Bienvenido a la aplicación de Gestión de Gastos!
Aquí podrás llevar un registro de tus gastos, listarlos, eliminarlos y ver gráficos 
de tus gastos para tener un mejor control de tus finanzas."""
etiqueta_bienvenida = Label(ventana, text=texto_bienvenida, padx=1, pady=1)
etiqueta_bienvenida.grid(row=2, column=0, padx=1, pady=1,columnspan=5, sticky='nsew')

# Funciones para los botones
def ventana_registro():
    # Cerrar la ventana de bienvenida
    ventana.destroy()
    subprocess.run(["python", "gas_reg.py"])

def ventana_busqueda():
    # Cerrar la ventana de bienvenida
    ventana.destroy()
    subprocess.run(["python", "gas_list.py"])

def ventana_elimina():
    # Cerrar la ventana de bienvenida
    ventana.destroy()
    subprocess.run(["python", "gas_del.py"])

def ventana_grafico():
    ventana.destroy()
    # Cerrar la ventana de bienvenida
    subprocess.run(["python", "grafico.py"])



# Crear botones
boton_r_gasto = Button(ventana, text='Registrar Gasto', width=16, height=2)
boton_l_gasto = Button(ventana, text='Listar Gastos', width=16, height=2)
boton_d_gasto = Button(ventana, text='Borrar Gastos', width=16, height=2)
boton_grafico = Button(ventana, text='Ver Grafico', width=16, height=2)

# Ubicar los botones utilizando grid
boton_r_gasto.grid(row=3, column=0, padx=1, pady=5)
boton_l_gasto.grid(row=3, column=2, padx=1, pady=5)
boton_d_gasto.grid(row=3, column=3, padx=1, pady=5)
boton_grafico.grid(row=3, column=4, padx=1, pady=5)

# Conectar las funciones con los botones
boton_r_gasto.config(command=ventana_registro)
boton_l_gasto.config(command=ventana_busqueda)
boton_d_gasto.config(command=ventana_elimina)
boton_grafico.config(command=ventana_grafico)

# Mostrar la ventana de bienvenida
ventana.mainloop()
