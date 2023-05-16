import json
import tkinter as tk
from tkinter import ttk, PhotoImage, Label, messagebox

#######################################################################
# trae el usuario en sesion activa.
def sesion():
    try:
        with open("data/sesion.json", "r") as archivo_sesion:
            datos_sesion = json.load(archivo_sesion)
            usuario_sesion = datos_sesion["usuario"]
            return usuario_sesion
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror("Error", "No se pudo cargar la sesión.")

#######################################################################

