
class ErrorValidacion(Exception):
    """Excepción, dato del cliente no válido."""
    pass

def validar_email(email):
    if "@" not in email or "." not in email:
        raise ErrorValidacion("El email no es válido. Debe contener '@' y un punto ('.').")
    return True


def validar_telefono(telefono):
    if not telefono.isdigit():
        raise ErrorValidacion("El teléfono es inválido. Solo debe contener números, sin espacios ni letras.")
    
    if len(telefono) < 8:
        raise ErrorValidacion("El teléfono es muy corto. Debe tener al menos 8 números.")
    return True