import modules.utils as u

def menu():
    u.limpiar()
    print("--- Gestión de Estudiantes ---\n")
    print("1. Registrar estudiante")
    print("2. Agregar Materias Disponibles")
    print("3. Inscribir estudiante a materia")
    print("4. Registrar calificación")
    print("5. Ver materias comunes")
    print("6. Generar Reporte")
    print("7. Mostrar Lista")
    print("0. Salir\n")
    
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 0 <= opcion <= 7:
                return opcion
            else:
                print("Por favor, ingrese un número entre 0 y 7.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def menuLista():
    u.limpiar()
    print("\n--- MOSTRAR LISTA ---")
    print("1. Lista de Estudiantes")
    print("2. Lista de Materias")
    print("0. Volver\n")
    
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 0 <= opcion <= 2:
                return opcion
            else:
                print("Por favor, ingrese un número entre 0 y 2.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
