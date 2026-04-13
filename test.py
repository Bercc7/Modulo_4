import unittest

from modelos import ClienteRegular, ClientePremium
from validaciones import validar_email, validar_telefono, ErrorValidacion

class TestGestorClientes(unittest.TestCase):

    def test_creacion_cliente_regular(self):
        cliente = ClienteRegular("1111", "Juan", "juan@mail.com", "12345678")
        self.assertEqual(cliente.nombre, "Juan")
        self.assertEqual(cliente.obtener_tipo(), "Regular")

    def test_validar_email_correcto(self):
        resultado = validar_email("correo@valido.com")
        self.assertTrue(resultado)

    def test_validar_email_incorrecto(self):
        with self.assertRaises(ErrorValidacion):
            validar_email("correosin_arroba.com")

    def test_validar_telefono_letras(self):
        with self.assertRaises(ErrorValidacion):
            validar_telefono("1234abcd") 

if __name__ == '__main__':
    unittest.main()