import json
from tarea import Tarea
from validar_fecha import *

def guardar_tareas(tareas, archivo="tareas.json"):
    with open(archivo, "w") as f:
        json.dump([t.to_dict() for t in tareas], f, indent=4)

def cargar_tareas(archivo="tareas.json"):
    try:
        with open(archivo, "r") as f:
            data = json.load(f)
            return [Tarea.from_dict(d) for d in data]
    except FileNotFoundError:
        return []

def aplicar_tachado(texto):
    return ''.join(char + '\u0336' for char in texto)

def mostrar_tareas(tareas):
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
    # Creamos una copia ordenada solo para mostrar
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
