import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

# Creamos la ventana
app = QApplication([])
window = QMainWindow()
window.setWindowTitle('Buscar Usuario')
window.setFixedSize(200, 200)

# Creamos los widgets
label_email = QLabel('usuario (email):', parent=window)
campo_email = QLineEdit(parent=window)
boton_buscar = QPushButton('Buscar', parent=window)
label_mensaje = QLabel('', parent=window)

# Configuramos los widgets
label_email.move(20, 50)
campo_email.move(80, 50)
campo_email.setFixedSize(200, 20)
boton_buscar.move(150, 100)
boton_buscar.setFixedSize(100, 30)
label_mensaje.move(20, 150)

# función para buscar al usuario
def buscar_usuario():
    with open('data/usuarios.json') as archivo:
        usuarios = json.load(archivo)

    # Buscamos el usuario
    email = campo_email.text()
    encontrado = False
    for usuario in usuarios:
        if usuario['email'] == email:
            mensaje = f"Usuario encontrado:\nNombre: {usuario['nombre']}\nEmail: {usuario['email']}"
            label_mensaje.setStyleSheet('color: green')
            label_mensaje.setText(mensaje)
            encontrado = True
            break

    # Si no se encuentra el usuario
    if not encontrado:
        mensaje = f"No se encontró el usuario con email {email}"
        label_mensaje.setStyleSheet('color: red')
        label_mensaje.setText(mensaje)

# Conectamos la función al botón
boton_buscar.clicked.connect(buscar_usuario)

# Agregamos los widgets al layout y lo configuramos en la ventana
layout = QVBoxLayout()
layout.addWidget(label_email)
layout.addWidget(campo_email)
layout.addWidget(boton_buscar)
layout.addWidget(label_mensaje)

widget = QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)

# Mostramos la ventana
window.show()
app.exec()
