import modules.utils as u

def menu():
    u.limpiar()
    print("--- Gestion de Estudiantes ---")
    print()
    print("1. Registrar estudiante")
    print("2. Agregar Materias Disponibles")
    print("3. Inscribir estudiante a materia")
    print("4. Registrar calificacion")
    print("5. Ver materias comunes")
    print("6. Generar Reporte")
    print("7. Mostrar Lista")
    print("0. Salir")
    print()
    
    opcion = int(input("Seleccione una opción: "))
    return opcion
        
def menuLista():
    print("\n---MOSTRAR LISTA---")
    print("1. Lista de Estudiantes")
    print("2. Lista de Materias")
    print("0. Volver")

    opcion = int(input("Seleccione una opcion: "))
    return opcion