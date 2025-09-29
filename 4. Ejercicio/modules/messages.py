import modules.utils as u

def menu():
    u.limpiar()
    print("\n--- MENÚ ---")
    print("1. Registrar Usuario")
    print("2. Agregar Libro")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Recomendar Libros")
    print("6. Análisis de Usuarios")
    print("0. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    return opcion