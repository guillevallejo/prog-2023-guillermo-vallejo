import sys
import json
from PyQt5.QtWidgets import * #QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QWidget, QAction, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


def buscar_usuarios():
    with open('data/usuarios.json', 'r') as archivo:
        try:
            usuarios = json.load(archivo)
        except:
            usuarios = []
    
    mensaje = ''
    
    for u in usuarios:
        mensaje += f"{u['nombre']}: {u['email']}\n"
    
    if mensaje:
        mensaje_box = QMessageBox()
        mensaje_box.setText(mensaje)
        mensaje_box.exec_()
    else:
        mensaje = 'No hay usuarios registrados'
        label_mensaje.setText(mensaje)

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('Buscar usuarios')

# Widget central
widget_central = QWidget()

# Layout vertical
layout_vertical = QVBoxLayout(widget_central)

# Mensaje
label_mensaje = QLabel(parent=widget_central)
layout_vertical.addWidget(label_mensaje, 0, alignment=Qt.AlignCenter)

# Botón buscar usuarios
button_buscar_usuarios = QPushButton('Buscar usuarios', parent=widget_central)
button_buscar_usuarios.clicked.connect(buscar_usuarios)
layout_vertical.addWidget(button_buscar_usuarios, 0, alignment=Qt.AlignCenter)

window.setCentralWidget(widget_central)
window.setGeometry(100, 100, 400, 300)
window.show()

sys.exit(app.exec_())
