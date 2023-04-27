import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow
from PyQt5.QtGui import QPixmap
import os

# Crear la aplicación y la ventana de bienvenida
app = QApplication(sys.argv)
ventana_bienvenida = QWidget()
ventana_bienvenida.setWindowTitle('Bienvenido')

# Crear un widget de etiqueta para el logo
logo = QLabel()
logo.setPixmap(QPixmap('data/logo.png'))

# Crear un botón de "Entrar"
boton_entrar = QPushButton('Iniciar Registro')
boton_entrar.setFixedSize(100, 30) # se define alto y ancho del boton
boton_modificar = QPushButton('Modifcar Usuario')
boton_modificar.setFixedSize(100, 30)
boton_buscar = QPushButton('Buscar Usuario')
boton_buscar.setFixedSize(100, 30)
boton_eliminar = QPushButton('Eliminar Usuario')
boton_eliminar.setFixedSize(100, 30)


# Crear un diseño vertical para la ventana de bienvenida y agregar los widgets
layout = QVBoxLayout()  #crea una capa vertical
layout.addWidget(logo)
layout.addWidget(boton_entrar)
layout.addWidget(boton_modificar)
layout.addWidget(boton_buscar)
layout.addWidget(boton_eliminar)

# Establecer el diseño vertical como el diseño de la ventana de bienvenida
ventana_bienvenida.setLayout(layout)

# Funciónes para los botones
def ventana_registro():
    # Cerrar la ventana de bienvenida
    ventana_bienvenida.close()
def ventana_busqueda():
    # Cerrar la ventana de bienvenida
    ventana_bienvenida.close()
def ventana_elimina():
    # Cerrar la ventana de bienvenida
    ventana_bienvenida.close()
def ventana_modifica():
    # Cerrar la ventana de bienvenida
    ventana_bienvenida.close()

# Conectar las funciones con los botones
boton_entrar.clicked.connect(ventana_registro)
boton_buscar.clicked.connect(ventana_busqueda)
boton_eliminar.clicked.connect(ventana_elimina)
boton_modificar.clicked.connect(ventana_modifica)

# Mostrar la ventana de bienvenida
ventana_bienvenida.show()
sys.exit(app.exec_())
