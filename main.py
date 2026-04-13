from modelos import ClienteRegular, ClientePremium
from validaciones import validar_email, validar_telefono, ErrorValidacion
import logging

# Configuración básica
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def iniciar_sistema_prueba():
    print("--- Bienvenido al gestor de clientes (Modo Test 1) ---\n")
    
    dni_input = "12345678A"
    nombre_input = "Ana Gómez"
    email_input = "ana.gomez@empresa.com" 
    telefono_input = "987654321"         
    
    print("Registrando nuevo cliente...")
    
    try:
        validar_email(email_input)
        validar_telefono(telefono_input)
        
        nuevo_cliente = ClientePremium(dni_input, nombre_input, email_input, telefono_input, puntos=500)
        
        print("\n¡Éxito! Cliente creado:")
        print(nuevo_cliente) 
        print(f"Tipo registrado: {nuevo_cliente.obtener_tipo()}") 
        
        logging.info(f"Cliente {nuevo_cliente.nombre} registrado correctamente.")

    except ErrorValidacion as e:
        # Si falla
        print(f"\n[ATENCIÓN] No se pudo crear el cliente: {e}")
        logging.error(f"Fallo de validación: {e}")

if __name__ == "__main__":
    iniciar_sistema_prueba()