import modules.utils as u

def menu():
    u.limpiar()
    print("--- Menú de Biblioteca ---")
    print()
    print("1. Agregar libro")
    print("2. Ver biblioteca completa")
    print("3. Buscar libros")
    print("4. Cambiar estado de lectura")
    print("5. Ver estadísticas")
    print("6. Eliminar libro")
    print("7. Salir")
    print()
    
    opcion = input("Seleccione una opción: ")
    return opcion
        