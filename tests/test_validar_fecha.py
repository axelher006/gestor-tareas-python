import unittest
from proyecto.validar_fecha import validar_fecha

class TestValidarFecha(unittest.TestCase):
    def test_fecha_valida(self):
        self.assertTrue(validar_fecha("2025-04-12"))

    def test_fecha_invalida(self):
        self.assertFalse(validar_fecha("2025-04-32")) 
        self.assertFalse(validar_fecha("texto"))
        self.assertFalse(validar_fecha("12/04/2025"))
