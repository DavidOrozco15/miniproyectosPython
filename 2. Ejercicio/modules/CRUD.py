import modules.utils as u

biblioteca = {}
contadorId = 1

def agregar_libro():
    global contadorId
    u.limpiar()
    print("\n---- AGREGAR LIBRO ----")
    
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")

    try:
        año = int(input("Ingrese el año de publicación: "))
    except ValueError:
        print("\nError: El año debe ser un número entero.")
        u.pausar()
        return
    
    estado = input("¿Ya lo leíste? (s/n): ").lower()
    if estado == 's':
        estado = "✅"
    elif estado == 'n':
        estado = "❌"
    else:
        print("\nError: Debe responder 's' para sí o 'n' para no.")
        u.pausar()
        return
    
    libro = (titulo, autor, genero, año, estado)
    biblioteca[contadorId] = libro
    print(f"\nLibro agregado con ID: {contadorId}")
    contadorId += 1
    u.pausar()


def ver_biblioteca():
    u.limpiar()
    print("\n---- CONTENIDO DE LA BIBLIOTECA ----")

    if not biblioteca:
        print("La biblioteca está vacía.")
        u.pausar()
        return

    print("\n---------------------------------------- Biblioteca Completa --------------------------------------------")
    for id_libro, info in biblioteca.items():
        titulo, autor, genero, año, estado = info
        print(f"\nID: {id_libro} | Título: {titulo} | Autor: {autor} | Género: {genero} | Año: {año} | Estado: {estado}")
    print("----------------------------------------------------------------------------------------------------------")
    u.pausar()


def buscar_libros():
    u.limpiar()
    if not biblioteca:
        print("\nLa biblioteca está vacía.")
        u.pausar()
        return

    print("\n---- BUSCAR LIBRO ----")
    buscarPor = input("Buscar por | 1: Título | 2: Autor | 3: Género |: ")
    termino = input("Ingrese el término de búsqueda: ").lower()

    encontrados = False

    for id_libro, info in biblioteca.items():
        titulo, autor, genero, año, estado = info
        siEncontro = False

        if buscarPor == '1' and termino in titulo.lower():
            siEncontro = True
        elif buscarPor == '2' and termino in autor.lower():
            siEncontro = True
        elif buscarPor == '3' and termino in genero.lower():
            siEncontro = True
        elif buscarPor not in {'1', '2', '3'}:
            print("\nÍndice inválido.")
            u.pausar()
            return

        if siEncontro:
            print(f"\nID: {id_libro} | Título: {titulo} | Autor: {autor} | Género: {genero} | Año: {año} | Estado: {estado}")
            encontrados = True

    if not encontrados:
        print("\nNo se encontraron libros que coincidan con la búsqueda.")
    u.pausar()


def cambiar_estado():
    u.limpiar()
    if not biblioteca:
        print("La biblioteca está vacía.")
        u.pausar()
        return

    try:
        print("\n---------------------------------------- Biblioteca Completa --------------------------------------------")
        for id_libro, info in biblioteca.items():
            titulo, autor, genero, año, estado = info
            print(f"\nID: {id_libro} | Título: {titulo} | Autor: {autor} | Género: {genero} | Año: {año} | Estado: {estado}")
        print("----------------------------------------------------------------------------------------------------------")
        id_libro = int(input("Ingrese el ID del libro: "))
    except ValueError:
        print("\nError: El ID debe ser un número entero.")
        u.pausar()
        return

    if id_libro not in biblioteca:
        print("\nID no encontrado.")
        u.pausar()
        return

    entrada = input("¿Ya lo leíste? (s/n): ").lower()
    if entrada == 's':
        nuevoEstado = "✅"
    elif entrada == 'n':
        nuevoEstado = "❌"
    else:
        print("\nError: Debe responder 's' o 'n'.")
        u.pausar()
        return

    titulo, autor, genero, año, _ = biblioteca[id_libro]
    biblioteca[id_libro] = (titulo, autor, genero, año, nuevoEstado)
    print("\nEstado actualizado correctamente.")
    u.pausar()


def estadisticas():
    u.limpiar()
    if not biblioteca:
        print("La biblioteca está vacía.")
        u.pausar()
        return

    totalLibros = len(biblioteca)
    leidos = 0
    noLeidos = 0
    generos = {}

    for info in biblioteca.values():
        _, _, genero, _, estado = info
        if estado == "✅":
            leidos += 1
        else:
            noLeidos += 1

        generos[genero] = generos.get(genero, 0) + 1

    print("\n--- ESTADÍSTICAS ---")
    print(f"Total de libros: {totalLibros}")
    print(f"Libros leídos (✅): {leidos}")
    print(f"Libros por leer (❌): {noLeidos}")

    if generos:
        print("\nGéneros más frecuentes:")
        genero_max = max(generos, key=generos.get)
        print(f"Género más frecuente: {genero_max} ({generos[genero_max]} libros)")
    print("--------------------------------------------------")
    u.pausar()


def eliminar_libro():
    u.limpiar()
    if not biblioteca:
        print("La biblioteca está vacía.")
        u.pausar()
        return

    try:
        print("\n---------------------------------------- Biblioteca Completa --------------------------------------------")
        for id_libro, info in biblioteca.items():
            titulo, autor, genero, año, estado = info
            print(f"\nID: {id_libro} | Título: {titulo} | Autor: {autor} | Género: {genero} | Año: {año} | Estado: {estado}")
        print("----------------------------------------------------------------------------------------------------------")
        id_libro = int(input("Ingrese el ID del libro a eliminar: "))
    except ValueError:
        print("\nError: El ID debe ser un número entero.")
        u.pausar()
        return

    if id_libro not in biblioteca:
        print("\nID no encontrado.")
        u.pausar()
        return

    titulo, autor, _, _, _ = biblioteca[id_libro]
    confirm = input(f"¿Eliminar '{titulo}' de {autor}? (s/n): ").lower()
    if confirm == 's':
        del biblioteca[id_libro]
        print("\nLibro eliminado correctamente.")
    else:
        print("\nEliminación cancelada.")
    u.pausar()

