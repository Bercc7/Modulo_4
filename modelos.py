
class Cliente:
    def __init__(self, dni, nombre, email, telefono):
        # Atributos básicos
        self.dni = dni
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"DNI: {self.dni} | Nombre: {self.nombre} | Email: {self.email}"

    def obtener_tipo(self):
        return "Cliente Base"

class ClienteRegular(Cliente):
    def __init__(self, dni, nombre, email, telefono):
        super().__init__(dni, nombre, email, telefono)

    def obtener_tipo(self):
        return "Regular"

class ClientePremium(Cliente):
    def __init__(self, dni, nombre, email, telefono, puntos=0):
        super().__init__(dni, nombre, email, telefono)
        self.puntos = puntos

    def obtener_tipo(self):
        return "Premium"

    def __str__(self):
        return super().__str__() + f" | Puntos: {self.puntos}"


class ClienteCorporativo(Cliente):
    def __init__(self, dni, nombre, email, telefono, nombre_empresa):
        super().__init__(dni, nombre, email, telefono)
        self.nombre_empresa = nombre_empresa

    def obtener_tipo(self):
        return "Corporativo"

    def __str__(self):
        return super().__str__() + f" | Empresa: {self.nombre_empresa}"