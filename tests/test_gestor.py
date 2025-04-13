import unittest
import os
from proyecto.tarea import Tarea
from proyecto import gestor

class TestGestor(unittest.TestCase):

    def setUp(self):
        self.tareas = [
            Tarea("Tarea 1", "2025-04-15"),
            Tarea("Tarea 2", "2025-05-01")
        ]
        self.archivo_prueba = "tareas_test.json"

    def tearDown(self):
        if os.path.exists(self.archivo_prueba):
            os.remove(self.archivo_prueba)

    def test_guardar_y_cargar_tareas(self):
        gestor.guardar_tareas(self.tareas, self.archivo_prueba)
        cargadas = gestor.cargar_tareas(self.archivo_prueba)
        self.assertEqual(len(cargadas), 2)
        self.assertEqual(cargadas[0].descripcion, "Tarea 1")
        self.assertEqual(cargadas[1].fecha.strftime("%Y-%m-%d"), "2025-05-01")

    def test_aplicar_tachado(self):
        texto = "Probando"
        tachado = gestor.aplicar_tachado(texto)
        self.assertIn('\u0336', tachado)
        self.assertEqual(len(tachado), len(texto)*2)

if __name__ == '__main__':
    unittest.main()
