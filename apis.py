import requests

def enviar_notificacion_bienvenida(nombre, email):
    """
    Simula el envío de un correo de bienvenida usando una API gratuita.
    Cumple con el requerimiento de integración con APIs externas.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    datos = {
        "title": f"Mensaje de Bienvenida para {nombre}",
        "body": "Gracias por registrarte en nuestra plataforma de Solution Tech.",
        "email_destino": email
    }
    
    try:
        respuesta = requests.post(url, json=datos, timeout=5)
        
        if respuesta.status_code == 201:
            return True, f"Notificación enviada a {email}"
        else:
            return False, f"El servidor respondió con código: {respuesta.status_code}"
            
    except requests.exceptions.RequestException as e:
        return False, f"Sin conexión a la API."