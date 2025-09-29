import modules.utils as u

def menu():
    while True:
        u.limpiar()
        print("\n--- MENÚ ---")
        print("\n1. Registrar Usuario")
        print("2. Agregar Libro")
        print("3. Prestar Libro")
        print("4. Devolver Libro")
        print("5. Recomendar Libros")
        print("6. Análisis de Usuarios")
        print("0. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if 0 <= opcion <= 6:
                return opcion
            else:
                print("Por favor, ingrese un número entre 0 y 6.")
                u.pausar()
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
            u.pausar()
