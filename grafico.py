import json
import matplotlib.pyplot as plt
from sesion import sesion

def mostrar_graficas():
    # Cargar el archivo JSON
    with open('data/gastos.json') as f:
        data = json.load(f)
        email = data[0]['email']  # Obtener el email del primer gasto del archivo JSON
        
    # Filtrar los gastos por el usuario activo de la sesión
    usuario_activo = sesion()
    gastos_filtrados = [gasto for gasto in data if gasto["email"] == usuario_activo]

    # Obtener todos los gastos del usuario especificado
    gastos_usuario = [gasto['monto'] for gasto in data if gasto['email'] == usuario_activo]

    # Obtener el total de gastos del usuario
    total_gastos = sum(gastos_usuario)

    # Obtener los nombres de las categorías
    categorias = list(set([gasto['categoria'] for gasto in data]))

    # Calcular el total de gastos por categoría del usuario
    gastos_por_categoria = [sum([gasto['monto'] for gasto in data if gasto['categoria'] == categoria and gasto['email'] == usuario_activo]) for categoria in categorias]

    # Graficar la gráfica de torta
    plt.pie(gastos_por_categoria, labels=categorias, autopct='%1.1f%%')
    plt.title('Gastos por categoría de {}'.format(usuario_activo))
    plt.show()

mostrar_graficas()
