from base_datos import inicializar_bd
from interfaz import iniciar_interfaz

def main():
    inicializar_bd()
    
    iniciar_interfaz()

if __name__ == "__main__":
    main()