import modules.utils as u
usuarios = {}
libros = {}
generos = set()

def registrarUsuario():
    u.limpiar()
    cedula = input("Ingrese la cedula: ")
    if cedula in usuarios:
        print("\nEsta cedula ya existe")
        u.pausar()
        return
    nombre = input("Ingrese el nombre: ")
    generosFav = set()

    while True:
        genero = input("Ingrese un genero favorito o varios (Escriba 'fin' para terminar): ")
        if genero.lower() == "fin":
            break
        generosFav.add(genero)

    usuarios[cedula] = {
        "Nombre": nombre,
        "GenerosFavoritos": generosFav,
        "Historial": []
    }
    generos.update(generosFav)

    print("\nUsuario registrado con exito.")
    u.pausar()

def agregarLibro():
    u.limpiar()
    try:
        codigo = int(input("Ingrese el codigo del libro: "))
    except ValueError:
        print("El código debe ser un número entero.")
        u.pausar()
        return
    if codigo in libros:
        print("Este codigo de libro ya existe")
        u.pausar()
        return
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el genero del libro: ").lower()
    libros[codigo] = {
        "Titulo": titulo,
        "Autor": autor,
        "Genero": genero,
        "Disponible": True
    }
    generos.add(genero)
    print("\nLibro registrado con exito.")
    u.pausar()

def prestarLibro():
    u.limpiar()
    cedula = input("Ingrese la cedula del usuario: ")
    if cedula not in usuarios:
        print("\nSu cedula no existe en la base de datos. Registrese primero")
        u.pausar()
        return
    
    try:
        codigo = int(input("Ingrese el codigo del libro: "))
    except ValueError:
        print("\nEl codigo debe ser un numero entero.")
        u.pausar()
        return
    
    if codigo not in libros:
        print(f"\nNo existe un libro con el codigo {codigo}.")
        u.pausar()
        return
    
    if not libros[codigo]["Disponible"]:
        print("\nEl libro no esta Disponible")
        u.pausar()
        return
    
    libros[codigo]["Disponible"] = False
    usuarios[cedula]["Historial"].append(
        {
            "Codigo": codigo,
            "Titulo": libros[codigo]["Titulo"],
            "Estado": "Prestado"
        }
    )
    print(f"\nEl Libro {libros[codigo]['Titulo']} fue prestado a {usuarios[cedula]['Nombre']}")
    u.pausar()

def devolverLibro():
    u.limpiar()
    cedula = input("Ingrese la cedula del usuario: ")
    if cedula not in usuarios:
        print("\nSu cedula no existe en la base de datos. Registrese primero")
        u.pausar()
        return
    
    try:
        codigo = int(input("\nIngrese el codigo del libro: "))
    except ValueError:
        print("\nEl codigo debe ser un numero entero.")
        u.pausar()
        return
    
    if codigo not in libros:
        print(f"\nNo existe un libro con el codigo {codigo}.")
        u.pausar()
        return
    
    if libros[codigo]["Disponible"]:
        print("\nEl libro ya está marcado como disponible.")
        u.pausar()
        return
    
    libros[codigo]["Disponible"] = True
    usuarios[cedula]["Historial"].append(
        {
            "Codigo": codigo,
            "Titulo": libros[codigo]["Titulo"],
            "Estado": "Devuelto"
        }
    )
    print(f"\nEl Libro {libros[codigo]['Titulo']} fue devuelto por {usuarios[cedula]['Nombre']}")
    u.pausar()

def recomendarLibros():
    u.limpiar()
    cedula = input("Ingrese la cedula del usuario: ")
    if cedula not in usuarios:
        print("\nSu cedula no existe en la base de datos. Registrese primero")
        u.pausar()
        return
    
    favoritos = usuarios[cedula]["GenerosFavoritos"]
    recomendados = []

    for libro in libros.values():
        if libro["Disponible"] and libro["Genero"] in favoritos:
            recomendados.append(libro)

    if recomendados:
        print("---RECOMENDACIONES BASADAS EN TUS GENEROS FAVORITOS---")
        for libro in recomendados:
            print(f"\n-{libro['Titulo']}- ({libro['Genero']}) de {libro['Autor']}")
            u.pausar()
    else:
        print("\nNo hay libros de generos disponibles en tus generos favoritos")
        u.pausar()

def analisisUsuarios():
    u.limpiar()
    print("---ANALISIS DE USUARIOS---")
    ced1 = input("\nIngrese la cedula del primer usuario: ")
    ced2 = input("\nIngrese la cedula del segundo usuario: ")

    if ced1 not in usuarios or ced2 not in usuarios:
        print("\nUno de los usuarios no esta registrado.")
        u.pausar()
        return
    
    g1 = usuarios[ced1]["GenerosFavoritos"]
    g2 = usuarios[ced2]["GenerosFavoritos"]

    print(f"Géneros en común: {g1 & g2}")
    print(f"Géneros únicos entre ambos: {g1 ^ g2}")
    print(f"¿Géneros de {usuarios[ced1]['Nombre']} ⊆ géneros de biblioteca?: {g1 <= generos}")
    print(f"¿Géneros de {usuarios[ced2]['Nombre']} ⊆ géneros de biblioteca?: {g2 <= generos}")
    u.pausar()
