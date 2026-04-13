import sqlite3
import csv
import json

def inicializar_bd():
    conexion = sqlite3.connect('clientes.db')
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            dni TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')
    conexion.commit() 
    conexion.close()  


def guardar_cliente(cliente):
    try:
        conexion = sqlite3.connect('clientes.db')
        cursor = conexion.cursor()
        
        tipo_cliente = cliente.obtener_tipo()
        
        cursor.execute('''
            INSERT INTO clientes (dni, nombre, email, telefono, tipo)
            VALUES (?, ?, ?, ?, ?)
        ''', (cliente.dni, cliente.nombre, cliente.email, cliente.telefono, tipo_cliente))
        
        conexion.commit()
        conexion.close()
        return True

    except sqlite3.IntegrityError:
        raise ValueError("El DNI ya está registrado en el sistema.")
    except Exception as e:
        raise Exception(f"Error inesperado al guardar en la base de datos: {e}")


def exportar_a_csv():
    conexion = sqlite3.connect('clientes.db')
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM clientes")
    clientes_db = cursor.fetchall() 
    conexion.close()
    
    with open('clientes_exportados.csv', mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['DNI', 'Nombre', 'Email', 'Teléfono', 'Tipo'])
        escritor.writerows(clientes_db)
    
    return "Datos exportados a CSV correctamente."