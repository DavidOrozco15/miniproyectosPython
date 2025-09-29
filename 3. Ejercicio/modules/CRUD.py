import modules.messages as m
import modules.utils as u
estudiantes = {}
materiasDisponibles = set()

def registrarEstudiantes():
    print("----REGISTRO DE ESTUDIANTES----")
    IDestudiante = input("Ingrese el ID del Estudiante: ")
    if not IDestudiante:
        print("ID no puede estar vacio")
        u.pausar()
        return
    
    if IDestudiante in estudiantes:
        print(f"El ID: {IDestudiante} ya esta registrado")
        u.pausar()
        return
    
    nombre = input("Ingrese el nombre completo del estudiante: ")
    estudiantes[IDestudiante] = {
        "Nombre": nombre,
        "Materias": set(),
        "Calificaciones": {}
    }

    print(f"El Estudiante {nombre} fue registrado con ID: {IDestudiante}")
    u.pausar()


def agregarMateria():
    print("----AGREGAR MATERIA----")
    materia = input("Nombre de la materia: ")
    if not materia:
        print("Nombre de la materia esta vacio")
        u.pausar()
        return
    
    if materia in materiasDisponibles:
        print(f"La materia {materia} ya existe en el sistema")
        u.pausar()

    materiasDisponibles.add(materia)
    print(f"La materia {materia} fue agregada a las materias disponibles")
    u.pausar()


def inscribirEstudiante():
    print("----INSCRIPCION DE ESTUDIANTES----")
    IDestudiante = input("Ingrese el ID del estudiante que desea inscribir: ")
    alumno = estudiantes.get(IDestudiante)
    if alumno is None:
        print(f"No existe un estudiante con ID: {IDestudiante}")
        u.pausar()
        return
    
    if not materiasDisponibles:
        print("No hay materias disponibles para inscribir")
        u.pausar()
        return
    
    materia = input("Ingrese el nombre de la materia que desea inscribir").lower()
    if materia not in materiasDisponibles:
        print(f"La materia {materia} no esta entre las materias disponibles")
        u.pausar()
        return
    
    alumno["Materias"].add(materia)
    alumno["Calificaciones"].setdefault(materia, [])
    print(f"El estudiante {IDestudiante} esta inscrito en {materia}")
    u.pausar()

def registrarCalificacion():
    print("----REGISTRO DE CALIFICACIONES----")
    IDestudiante = input("Ingresa el ID del estudiante: ")
    alumno = estudiantes.get(IDestudiante)
    if alumno is None:
        print(f"No existe un estudiante con ID: {IDestudiante}")
        u.pausar()
        return
    
    materia = input("Ingrese el nombre de la materia: ")
    if materia not in alumno["Materias"]:
        print(f"El estudiante {IDestudiante} no esta inscrito en {materia}.")
        u.pausar()
        return
    
    try:
        nota = float(input("Ingrese la nota(numero)"))
    except ValueError:
        print("Nota Invalida. Intentelo de nuevo")
        u.pausar()
        return
    
    alumno["Calificaciones"].setdefault(materia, []).append(nota)
    print(f"La nota {nota} registrada para {IDestudiante} en {materia}")
    u.pausar()

def materiasComunes():
    print("----MATERIAS COMUNES----")
    id1 = input("ID del primer estudiante: ")
    id2 = input("ID del primer estudiante: ")
    a = estudiantes.get(id1)
    b = estudiantes.get(id2)
    if a is None or b is None:
        print("Alguno de los IDs no existe")
        u.pausar()
        return
    
    materiasA = a["Materias"]
    materiasB = b["Materias"]

    inter = materiasA & materiasB
    union = materiasA | materiasB
    diferencia = materiasA - materiasB

    print(f"Materias de {id1}: {materiasA}")
    print(f"Materias de {id2}: {materiasB}")
    print(f"Intersección: {inter}")
    print(f"Unión: {union}")
    print(f"En {id1} pero no en {id2}: {diferencia}")
    u.pausar()

def mostrarCalificaciones(calificaciones):
    totalSuma = 0.0
    totalContador = 0

    for materia, notas in calificaciones.items():
        if notas: 
            promedio = sum(notas)/ len(notas)
            print(f"-{materia}-: Notas: {notas} = Promedio = {promedio:.2f}")
            totalSuma += sum(notas)
            totalContador += len(notas)
        else:
            print(f"-{materia}- : Sin notas")
            u.pausar()
    
    if totalContador > 0:
        promedioGlobal = totalSuma / totalContador
        print(f"Promedio global (Todas las notas): {promedioGlobal:.2f}")
        u.pausar()
    else:
        print("Promedio global: Sin notas registradas")
        u.pausar()

def generarReporte():
    print("----REPORTE ACADEMICO----")
    IDestudiante = input("Ingrese el ID del estudiante para generar el reporte: ")
    alumno = estudiantes.get(IDestudiante)
    if alumno is None:
        print(f"No existe un estudiante con el ID: {IDestudiante}")
        u.pausar()
        return
    
    print(f"\n --- REPORTE DEL ESTUDIANTE: {alumno["Nombre"]}(ID: {IDestudiante})---")
    materias = alumno["Materias"]
    print(f"Las materias inscritas son: {materias}")

    mostrarCalificaciones(alumno["Calificaciones"])
    u.pausar()

def listarEstudiantes():
    print("---LISTA DE ESTUDIANTES---")
    if not estudiantes:
        print("No hay estudiantes registrados")
        u.pausar()
        return
    else:
        print("IDs registrados: ", estudiantes.keys())
        print("Datos registrados: ", estudiantes.values())
        print("\nInformacion de los Estudiantes")
        for IDestudiante, info in estudiantes.items():
            print(f"\nID: {IDestudiante} | Nombre: {info["Nombre"]} | Materias: {info["Materias"]} |")
            u.pausar()

def listarMaterias():
    print("----LISTAR MATERIAS----")
    if not materiasDisponibles:
        print("No hay materias disponibles")
        u.pausar()
        return
    print("Materias Disponibles:")
    for materi in sorted(materiasDisponibles):
        print(" -", materi)
        u.pausar()

def mostrarLista():
    opcion = m.menuLista()
    match opcion:
        case 1:
            listarEstudiantes()
        case 2:
            listarMaterias()
        case _:
            print("Opción inválida. Intente nuevamente.")
            u.pausar()
            u.limpiar()