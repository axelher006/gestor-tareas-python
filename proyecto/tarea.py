from datetime import datetime

class Tarea:
    def __init__(self, descripcion, fecha_str):
        self.descripcion = descripcion
        self.fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def to_dict(self):
        return {
            "descripcion": self.descripcion,
            "fecha": self.fecha.strftime("%Y-%m-%d"),
            "completada": self.completada
        }

    @staticmethod
    def from_dict(data):
        tarea = Tarea(data["descripcion"], data["fecha"])
        tarea.completada = data["completada"]
        return tarea
