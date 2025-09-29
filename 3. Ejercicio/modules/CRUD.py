import modules.messages as m
import modules.utils as u

estudiantes = {}
materiasDisponibles = set()

def registrarEstudiantes():
    u.limpiar()
    print("\n---- REGISTRO DE ESTUDIANTES ----")
    IDestudiante = input("Ingrese el ID del Estudiante: ")
    if not IDestudiante:
        print("\nID no puede estar vacío.")
        u.pausar()
        return

    if IDestudiante in estudiantes:
        print(f"\nEl ID: {IDestudiante} ya está registrado.")
        u.pausar()
        return

    nombre = input("Ingrese el nombre completo del estudiante: ")
    if not nombre:
        print("\nEl nombre no puede estar vacío.")
        u.pausar()
        return

    estudiantes[IDestudiante] = {
        "Nombre": nombre,
        "Materias": set(),
        "Calificaciones": {}
    }

    print(f"\nEl Estudiante {nombre} fue registrado con ID: {IDestudiante}")
    u.pausar()

def agregarMateria():
    u.limpiar()
    print("\n---- AGREGAR MATERIA ----")
    materia = input("Nombre de la materia: ").lower()
    if not materia:
        print("\nNombre de la materia está vacío.")
        u.pausar()
        return

    if materia in materiasDisponibles:
        print(f"\nLa materia '{materia}' ya existe en el sistema.")
        u.pausar()
        return

    materiasDisponibles.add(materia)
    print(f"\nLa materia '{materia}' fue agregada a las materias disponibles.")
    u.pausar()

def inscribirEstudiante():
    u.limpiar()
    print("\n---- INSCRIPCIÓN DE ESTUDIANTES ----")
    IDestudiante = input("Ingrese el ID del estudiante que desea inscribir: ")
    alumno = estudiantes.get(IDestudiante)
    if alumno is None:
        print(f"\nNo existe un estudiante con ID: {IDestudiante}")
        u.pausar()
        return

    if not materiasDisponibles:
        print("\nNo hay materias disponibles para inscribir.")
        u.pausar()
        return

    materia = input("Ingrese el nombre de la materia que desea inscribir: ").lower()
    if materia not in materiasDisponibles:
        print(f"\nLa materia '{materia}' no está entre las materias disponibles.")
        u.pausar()
        return

    if materia in alumno["Materias"]:
        print(f"\nEl estudiante ya está inscrito en la materia '{materia}'.")
        u.pausar()
        return

    alumno["Materias"].add(materia)
    alumno["Calificaciones"].setdefault(materia, [])
    print(f"\nEl estudiante {IDestudiante} está inscrito en {materia}.")
    u.pausar()

def registrarCalificacion():
    u.limpiar()
    print("\n---- REGISTRO DE CALIFICACIONES ----")
    IDestudiante = input("Ingresa el ID del estudiante: ")
    alumno = estudiantes.get(IDestudiante)
    if alumno is None:
        print(f"\nNo existe un estudiante con ID: {IDestudiante}")
        u.pausar()
        return

    materia = input("Ingrese el nombre de la materia: ").lower()
    if materia not in alumno["Materias"]:
        print(f"\nEl estudiante {IDestudiante} no está inscrito en {materia}.")
        u.pausar()
        return

    try:
        nota = float(input("Ingrese la nota (número): "))
    except ValueError:
        print("\nNota inválida. Inténtelo de nuevo.")
        u.pausar()
        return

    alumno["Calificaciones"].setdefault(materia, []).append(nota)
    print(f"\nLa nota {nota} fue registrada para {IDestudiante} en {materia}.")
    u.pausar()

def materiasComunes():
    u.limpiar()
    print("\n---- MATERIAS COMUNES ----")
    id1 = input("ID del primer estudiante: ")
    id2 = input("ID del segundo estudiante: ")

    a = estudiantes.get(id1)
    b = estudiantes.get(id2)
    if a is None or b is None:
        print("\nAlguno de los IDs no existe.")
        u.pausar()
        return

    materiasA = a["Materias"]
    materiasB = b["Materias"]

    inter = materiasA & materiasB
    union = materiasA | materiasB
    diferencia = materiasA - materiasB

    print(f"\nMaterias de {id1}: {materiasA}")
    print(f"Materias de {id2}: {materiasB}")
    print(f"Intersección: {inter}")
    print(f"Unión: {union}")
    print(f"En {id1} pero no en {id2}: {diferencia}")
    u.pausar()

def mostrarCalificaciones(calificaciones):
    totalSuma = 0.0
    totalContador = 0

    print("\n--- CALIFICACIONES ---\n")
    for materia, notas in calificaciones.items():
        if notas:
            promedio = sum(notas) / len(notas)
            print(f"- {materia} - Notas: {notas} | Promedio: {promedio:.2f}")
            totalSuma += sum(notas)
            totalContador += len(notas)
        else:
            print(f"- {materia} - Sin notas")

    if totalContador > 0:
        promedioGlobal = totalSuma / totalContador
        print(f"\nPromedio global (todas las notas): {promedioGlobal:.2f}")
    else:
        print("\nPromedio global: Sin notas registradas")
    u.pausar()

def generarReporte():
    u.limpiar()
    print("\n---- REPORTE ACADÉMICO ----")
    IDestudiante = input("Ingrese el ID del estudiante para generar el reporte: ")
    alumno = estudiantes.get(IDestudiante)
    if alumno is None:
        print(f"\nNo existe un estudiante con el ID: {IDestudiante}")
        u.pausar()
        return

    print(f"\n--- REPORTE DEL ESTUDIANTE: {alumno['Nombre']} (ID: {IDestudiante}) ---")
    materias = alumno["Materias"]
    print(f"Materias inscritas: {materias}")

    mostrarCalificaciones(alumno["Calificaciones"])

def listarEstudiantes():
    u.limpiar()
    print("\n--- LISTA DE ESTUDIANTES ---\n")
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("IDs registrados:", list(estudiantes.keys()))
        print("Datos registrados:", list(estudiantes.values()))
        print("\nInformación de los Estudiantes:")
        for IDestudiante, info in estudiantes.items():
            print(f"\nID: {IDestudiante} | Nombre: {info['Nombre']} | Materias: {info['Materias']}")
    u.pausar()

def listarMaterias():
    u.limpiar()
    print("\n---- LISTAR MATERIAS ----")
    if not materiasDisponibles:
        print("No hay materias disponibles.")
    else:
        print("Materias disponibles:")
        for materi in sorted(materiasDisponibles):
            print(" -", materi)
    u.pausar()

def mostrarLista():
    u.limpiar()
    opcion = m.menuLista()
    match opcion:
        case 1:
            listarEstudiantes()
        case 2:
            listarMaterias()
        case _:
            print("\nOpción inválida. Intente nuevamente.")
            u.pausar()
            u.limpiar()
