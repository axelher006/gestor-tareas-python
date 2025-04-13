from datetime import datetime

class Tarea:
    """
    Representa una tarea con descripción, fecha y estado de completada.
    """
    def __init__(self, descripcion, fecha_str):
        """
         Inicializa una nueva tarea.

        :param descripcion: Texto que describe la tarea.
        :param fecha_str: Fecha límite en formato 'YYYY-MM-DD'.
        """
        self.descripcion = descripcion
        self.fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        self.completada = False

    def marcar_completada(self):
        """
        Marca la tarea como completada.
        """
        self.completada = True

    def to_dict(self):
        """
        Convierte la tarea en un diccionario para guardarla en JSON.

        :return: Diccionario con los datos de la tarea.
        """
        return {
            "descripcion": self.descripcion,
            "fecha": self.fecha.strftime("%Y-%m-%d"),
            "completada": self.completada
        }

    @staticmethod
    def from_dict(data):
        """
        Crea una instancia de Tarea a partir de un diccionario.

        :param data: Diccionario con los datos de la tarea.
        :return: Objeto Tarea.
        """
        tarea = Tarea(data["descripcion"], data["fecha"])
        tarea.completada = data["completada"]
        return tarea
