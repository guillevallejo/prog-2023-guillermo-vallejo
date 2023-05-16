import tkinter as tk
from tkinter import messagebox
import subprocess

def mostrar_mensaje(mensaje):
    messagebox.showinfo("Mensaje", mensaje)

def menu_opcion1():
    mostrar_mensaje("Opción 1 seleccionada")

def menu_opcion2():
    mostrar_mensaje("Opción 2 seleccionada")

def m_cat_reg():
    subprocess.run(["python", "cate_reg.py"])

def m_cat_list():
    subprocess.run(["python", "cate_list.py"])

def m_cat_del():
    subprocess.run(["python", "cate_del.py"])

def m_usu_list():
    subprocess.run(["python", "usu_list.py"])

def m_usu_del():
    subprocess.run(["python", "usu_del.py"])

def m_gas_reg():
    subprocess.run(["python", "gas_reg.py"])

def m_gas_list():
    subprocess.run(["python", "gas_list.py"])

def menu_opcion9():
    mostrar_mensaje("Opción 9 seleccionada")    

def crear_menu(ventana):
    # Crear la ventana principal
    # ventana = tk.Tk()
    # ventana.title("Ejemplo de Menú")
    # ventana.geometry("800x600")
    # ventana.resizable(False,False)

    # Crear la barra de menú
    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)

    # Crear el menú Archivo
    menu_archivo = tk.Menu(barra_menu, tearoff=False)
    menu_archivo.add_command(label="Opción 1", command=menu_opcion1)
    menu_archivo.add_command(label="Opción 2", command=menu_opcion2)
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", command=ventana.quit)
    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

    # Crear el menú Categoria
    menu_cat = tk.Menu(barra_menu, tearoff=False)
    menu_cat.add_command(label="Registrar", command=m_cat_reg)
    menu_cat.add_command(label="Listar", command=m_cat_list)
    menu_cat.add_command(label="Elimnar", command=m_cat_list)
    barra_menu.add_cascade(label="Categorias", menu=menu_cat)

    # Crear el menú Usuario
    menu_usu = tk.Menu(barra_menu, tearoff=False)
    menu_usu.add_command(label="Listar", command=m_usu_list)
    menu_usu.add_command(label="Eliminar", command=m_usu_del)
    barra_menu.add_cascade(label="Usuarios", menu=menu_usu)

    # Crear el menú gastos
    menu_tmp = tk.Menu(barra_menu, tearoff=False)
    menu_tmp.add_command(label="Registrar", command=m_gas_reg)
    menu_tmp.add_command(label="Listar", command=m_gas_list)
    barra_menu.add_cascade(label="Gastos", menu=menu_tmp)

    # Crear el menú Ayuda
    menu_ayuda = tk.Menu(barra_menu, tearoff=False)
    menu_ayuda.add_command(label="Opción 9", command=menu_opcion9)
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)


def crear_menu_inicio(ventana):
    # Crear la barra de menú
    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)

    # Crear el menú Archivo
    menu_archivo = tk.Menu(barra_menu, tearoff=False)
    menu_archivo.add_command(label="Opción 1", command=menu_opcion1)
    menu_archivo.add_command(label="Opción 2", command=menu_opcion2)
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", command=ventana.quit)
    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)