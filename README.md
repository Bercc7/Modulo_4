Gestor Inteligente de Clientes

Es una plataforma integral desarrollada en Python para la gestión eficiente de clientes. El sistema resuelve problemas de duplicación de datos e ineficiencia mediante una arquitectura robusta basada en Programación Orientada a Objetos (POO).


🎯 Objetivos del Proyecto

Desarrollar una solución escalable que permita administrar diferentes perfiles de clientes, asegurando la integridad de la información mediante validaciones avanzadas y persistencia de datos.
Funcionalidades Clave:

    Gestión Multiperfil: Diferenciación lógica entre Clientes Regulares, Premium y Corporativos mediante herencia y polimorfismo.

    Validaciones Avanzadas: Control estricto de formatos para emails, teléfonos y direcciones.

    Integración de APIs: Conexión con servicios externos para validación de identidad y envío automatizado de correos de bienvenida.

    Persistencia Híbrida: Almacenamiento seguro en base de datos SQLite y soporte para exportación/manejo de archivos JSON y CSV.

    Registro de Actividad (Logs): Sistema de auditoría para guardar un historial de todas las operaciones realizadas.

🛠️ Stack Tecnológico

    Lenguaje: Python 3.

    Paradigma: Programación Orientada a Objetos (Clases, Herencia, Encapsulamiento, Polimorfismo).

    Base de Datos: SQLite.

    Formatos de Datos: JSON, CSV.

    Interfaz: GUI desarrollada en Tkinter.

    Testing: Implementación de Pruebas Unitarias para asegurar la calidad del código.

📂 Estructura del Código

Basado en las mejores prácticas de modularidad:

    modelos.py: Definición de clases y lógica de negocio (POO).

    validaciones.py: Funciones de limpieza y verificación de datos.

    base_datos.py: Gestión de la persistencia con SQLite.

    apis.py: Lógica de integración con servicios externos.

    interfaz.py: Manejo de la capa visual (GUI).

    test.py: Suite de pruebas unitarias.

⚙️ Instalación y Ejecución

    Clona el repositorio:
    Bash

    git clone https://github.com/Bercc7/Gestor-de-Clientes-Inteligente.git

    Instala las dependencias necesarias:
    Bash

    pip install -r requirements.txt

    Ejecuta la aplicación principal:
    Bash

    python main.py
