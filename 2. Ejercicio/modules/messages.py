import modules.utils as u

def menu():
    u.limpiar()
    print("--- Menú de Biblioteca ---\n")
    print("1. Agregar libro")
    print("2. Ver biblioteca completa")
    print("3. Buscar libros")
    print("4. Cambiar estado de lectura")
    print("5. Ver estadísticas")
    print("6. Eliminar libro")
    print("7. Salir\n")
    
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Por favor, ingrese un número entre 1 y 7.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

        