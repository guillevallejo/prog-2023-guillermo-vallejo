import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow
from PyQt5.QtGui import QPixmap, QFont
import os

# Crear la aplicación y la ventana principal
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Registro de Usuario')

# Establecer el tamaño de la ventana
#window.resize(800, 600)

# determina el tamaño del texto para los label
font = QFont()
font.setPointSize(14)

# Crear los widgets
label_titulo = QLabel('*** registro de usuario ***', parent=window)
label_titulo.setFont(font)
label_nombre = QLabel('Nombre:', parent=window)
input_nombre = QLineEdit(parent=window)
label_email = QLabel('Email:', parent=window)
input_email = QLineEdit(parent=window)
label_password = QLabel('Contraseña:', parent=window)
input_password = QLineEdit(parent=window)
input_password.setEchoMode(QLineEdit.Password)
button_registrar = QPushButton('Registrar', parent=window)
label_mensaje = QLabel(parent=window)

# Definir la disposición de los widgets en la ventana
layout = QVBoxLayout()
layout.addWidget(label_titulo)
layout.addWidget(label_nombre)
layout.addWidget(input_nombre)
layout.addWidget(label_email)
layout.addWidget(input_email)
layout.addWidget(label_password)
layout.addWidget(input_password)
layout.addWidget(button_registrar)
layout.addWidget(label_mensaje)
window.setLayout(layout)

# Definir la función que se ejecutará al hacer clic en el botón de registrar
def registrar_usuario():
    nombre = input_nombre.text().strip()
    email = input_email.text().strip()
    password = input_password.text().strip()
    usuario = {"nombre": nombre, "email": email, "password": password}

    # Cargar usuarios existentes del archivo JSON
    try:
        with open("data/usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, se crea una lista vacía
        usuarios = []

    # Validar que los campos no estén vacíos
    if not nombre or not email or not password:
        label_mensaje.setText('Todos los campos son obligatorios.')
        return

    # Validar si el email ya está registrado
    for u in usuarios:
        if u["email"] == email:
            mensaje = "El email ya está registrado."
            label_mensaje.setText(mensaje)
            return

    # Agregar el nuevo usuario a la lista de usuarios
    usuarios.append(usuario)

    # Guardar la lista de usuarios en el archivo JSON
    with open("data/usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo)

    mensaje = "Usuario registrado correctamente."
    label_mensaje.setText(mensaje)

# Conectar la función registrar_usuario() con el evento de clic en el botón de registrar
button_registrar.clicked.connect(registrar_usuario)

# Mostrar la ventana
window.show()

# Iniciar el ciclo de eventos de la aplicación
sys.exit(app.exec_())
