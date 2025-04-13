from gestor import *
if __name__ == "__main__":
    tareas = cargar_tareas()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Guardar y salir")
        op = input("Elegí una opción: ")

        if op == "1":
            mostrar_tareas(tareas)
        elif op == "2":
            agregar_tarea(tareas)
        elif op == "3":
            completar_tarea(tareas)
        elif op == "4":
            guardar_tareas(tareas)
            print("Tareas guardadas. ¡Hasta la próxima!")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")