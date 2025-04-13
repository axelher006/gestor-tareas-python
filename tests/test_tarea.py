import unittest
from proyecto.tarea import Tarea

class TestTarea(unittest.TestCase):
    def test_marcar_completada(self):
        tarea = Tarea("Probar método", "2025-04-15")
        self.assertFalse(tarea.completada)
        tarea.marcar_completada()
        self.assertTrue(tarea.completada)

    def test_to_dict_and_from_dict(self):
        original = Tarea("Guardar tarea", "2025-05-01")
        original.marcar_completada()
        data = original.to_dict()
        nueva = Tarea.from_dict(data)
        self.assertEqual(nueva.descripcion, "Guardar tarea")
        self.assertEqual(nueva.fecha.strftime("%Y-%m-%d"), "2025-05-01")
        self.assertTrue(nueva.completada)

