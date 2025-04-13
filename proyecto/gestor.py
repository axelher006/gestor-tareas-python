import json
from tarea import Tarea
from validar_fecha import *

def guardar_tareas(tareas, archivo="tareas.json"):
    """
    Guarda la lista de tareas en un archivo JSON.

    :param tareas: Lista de objetos Tarea.
    :param archivo: Nombre del archivo donde guardar.
    """
    with open(archivo, "w") as f:
        json.dump([t.to_dict() for t in tareas], f, indent=4)

def cargar_tareas(archivo="tareas.json"):
    """
    Carga tareas desde un archivo JSON si existe.

    :param archivo: Nombre del archivo a cargar.
    :return: Lista de objetos Tarea.
    """
    try:
        with open(archivo, "r") as f:
            data = json.load(f)
            return [Tarea.from_dict(d) for d in data]
    except FileNotFoundError:
        return []

def aplicar_tachado(texto):
    """
    Devuelve el texto con cada letra tachada usando un carácter unicode.

    :param texto: Texto a modificar.
    :return: Texto con tachado.
    """
    return ''.join(char + '\u0336' for char in texto)

def mostrar_tareas(tareas):
    """
    Muestra todas las tareas ordenadas por fecha.
    Si están completadas, se muestran con tachado.

    :param tareas: Lista de objetos Tarea.
    """
    if not tareas:
        print("\n------------------\n")
        print("No hay tareas.")
        print("\n------------------\n")
        return
    print("\n \n Tareas:\n------------------\n")

    for i, t in enumerate(sorted(tareas, key=lambda x: x.fecha)):
        desc = aplicar_tachado(t.descripcion) if t.completada else t.descripcion
        print(f"{i+1}. {desc} (Para: {t.fecha.strftime('%Y-%m-%d')})")

    print("\n------------------\n")


def agregar_tarea(tareas):
    """
    Pide al usuario una nueva tarea, valida la fecha y la agrega a la lista.

    :param tareas: Lista de tareas existente.
    """
    desc = input("Descripción de la tarea: ")
    while True:
        fecha = input("Fecha (YYYY-MM-DD): ")
        if validar_fecha(fecha):
            tareas.append(Tarea(desc, fecha))
            print("Tarea agregada.")
            break
        else:
            print("Fecha inválida. Intentá nuevamente")


def completar_tarea(tareas):
    """
    Permite al usuario marcar una tarea como completada.

    :param tareas: Lista de tareas existente.
    """
    tareas_ordenadas = sorted(tareas, key=lambda x: x.fecha)
    mostrar_tareas(tareas)

    try:
        idx = int(input("Número de la tarea a marcar como completada: ")) - 1
        if 0 <= idx < len(tareas_ordenadas):
            tarea_seleccionada = tareas_ordenadas[idx]
            tarea_seleccionada.marcar_completada()
            print("Tarea marcada como completada.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")
