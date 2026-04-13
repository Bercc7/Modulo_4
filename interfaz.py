import tkinter as tk
from tkinter import messagebox, ttk

from modelos import ClienteRegular, ClientePremium, ClienteCorporativo
from validaciones import validar_email, validar_telefono, ErrorValidacion
from base_datos import guardar_cliente, exportar_a_csv

def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Gestor Inteligente de Clientes (GIC)")
    ventana.geometry("400x500")
    ventana.configure(padx=20, pady=20)

    tk.Label(ventana, text="DNI:").pack(anchor="w")
    entry_dni = tk.Entry(ventana, width=40)
    entry_dni.pack(pady=5)

    tk.Label(ventana, text="Nombre:").pack(anchor="w")
    entry_nombre = tk.Entry(ventana, width=40)
    entry_nombre.pack(pady=5)

    tk.Label(ventana, text="Email:").pack(anchor="w")
    entry_email = tk.Entry(ventana, width=40)
    entry_email.pack(pady=5)

    tk.Label(ventana, text="Teléfono:").pack(anchor="w")
    entry_telefono = tk.Entry(ventana, width=40)
    entry_telefono.pack(pady=5)

    tk.Label(ventana, text="Tipo de Cliente:").pack(anchor="w")
    combo_tipo = ttk.Combobox(ventana, values=["Regular", "Premium", "Corporativo"], state="readonly", width=37)
    combo_tipo.set("Regular")
    combo_tipo.pack(pady=5)

    def accion_guardar():
        dni = entry_dni.get()
        nombre = entry_nombre.get()
        email = entry_email.get()
        telefono = entry_telefono.get()
        tipo = combo_tipo.get()

        if not dni or not nombre or not email or not telefono:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        try:
            validar_email(email)
            validar_telefono(telefono)

            if tipo == "Regular":
                nuevo_cliente = ClienteRegular(dni, nombre, email, telefono)
            elif tipo == "Premium":
                nuevo_cliente = ClientePremium(dni, nombre, email, telefono, puntos=100)
            else:
                nuevo_cliente = ClienteCorporativo(dni, nombre, email, telefono, nombre_empresa="Empresa S.A.")

            guardar_cliente(nuevo_cliente)
            
            messagebox.showinfo("Éxito", f"Cliente {nombre} guardado correctamente.")
            entry_dni.delete(0, tk.END)
            entry_nombre.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_telefono.delete(0, tk.END)

        except ErrorValidacion as e:
            messagebox.showerror("Error de Validación", str(e))
        except ValueError as e:
            messagebox.showerror("Error de Base de Datos", str(e))
        except Exception as e:
            messagebox.showerror("Error Inesperado", f"Ocurrió un error: {e}")

    def accion_exportar():
        try:
            mensaje = exportar_a_csv()
            messagebox.showinfo("Exportar", mensaje)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar: {e}")

    tk.Button(ventana, text="Guardar Cliente", command=accion_guardar, bg="lightblue").pack(pady=15)
    tk.Button(ventana, text="Exportar a CSV", command=accion_exportar).pack(pady=5)

    ventana.mainloop()