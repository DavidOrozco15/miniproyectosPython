
usuarios = {}
libros = {}
generos = set()

def registrarUsuario():
    cedula = input("Ingrese la cedula: ")
    if cedula in usuarios:
        print("\nEsta cedula ya existe")
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

    print("Usuario regustrado con exito.")

def agregarLibro():
    try:
        codigo = int(input("Ingrese el codigo del libro: "))
    except ValueError:
        print("El código debe ser un número entero.")
        return
    if codigo in libros:
        print("Este codigo de libro ya existe")
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
    generos.update({genero})

def prestarLibro():
    cedula = input("Ingrese la cedula del usuario: ")
    if cedula not in usuarios:
        print("Su cedula no existe en la base de datos. Registrese primero")
        return
    
    try:
        codigo = int(input("Ingrese el codigo del libro: "))
    except ValueError:
        print("\nEl codigo debe ser un numero entero.")
        return
    
    if codigo not in libros:
        print(f"\nNo existe un libro con el codigo {codigo}.")
        return
    
    if not libros[codigo]["Disponible"]:
        print("\nEl libro no esta Disponible")
        return
    
    libros[codigo]["Disponible"] = False
    usuarios[cedula]["Historial"].append(
        {
            "Codigo": codigo,
            "Titulo": libros[codigo]["Titulo"],
            "Estado": "Prestado"
        }
    )
    print(f"El Libro {libros[codigo]["Titulo"]} fue prestado a {usuarios[cedula]["Nombre"]}")

def devolverLibro():
    cedula = input("Ingrese la cedula del usuario: ")
    if cedula not in usuarios:
        print("Su cedula no existe en la base de datos. Registrese primero")
        return
    
    try:
        codigo = int(input("Ingrese el codigo del libro: "))
    except ValueError:
        print("\nEl codigo debe ser un numero entero.")
        return
    
    if codigo not in libros:
        print(f"\nNo existe un libro con el codigo {codigo}.")
        return
    
    if libros[codigo]["Disponible"]:
        print("El libro ya está marcado como disponible.")
        return
    
    libros[codigo]["Disponible"] = True
    usuarios[cedula]["Historial"].append(
        {
            "Codigo": codigo,
            "Titulo": libros[codigo]["Titulo"],
            "Estado": "Devuelto"
        }
    )
    print(f"El Libro {libros[codigo]["Titulo"]} fue devuelto por {usuarios[cedula]["Nombre"]}")

def recomendarLibros():
    cedula = input("Ingrese la cedula del usuario: ")
    if cedula not in usuarios:
        print("Su cedula no existe en la base de datos. Registrese primero")
        return
    
    favoritos = usuarios[cedula]["GenerosFavoritos"]
    recomendados = []

    for libro in libros.values():
        if libro["Disponible"] and libro["Genero"] in favoritos:
            recomendados.append(libro)

    if recomendados:
        print("---RECOMENDACIONES BASADAS EN TUS GENEROS FAVORITOS---")
        for libro in recomendados:
            print(f"-{libro["Titulo"]}- ({libro["Genero"]}) de {libro["Autor"]}")
    else:
        print("No hay libros de generos disponibles en tus generos favoritos")

def analisisUsuarios():
    print("---ANALISIS DE USUARIOS---")
    ced1 = input("Ingrese la cedula del primer usuario: ")
    ced2 = input("Ingrese la cedula del segundo usuario: ")

    if ced1 not in usuarios or ced2 not in usuarios:
        print("Uno de los usuarios no esta registrado.")
        return
    
    g1 = usuarios[ced1]["GenerosFavoritos"]
    g2 = usuarios[ced2]["GenerosFavoritos"]

    print(f"Géneros en común: {g1 & g2}")
    print(f"Géneros únicos entre ambos: {g1 ^ g2}")
    print(f"¿Géneros de {usuarios[ced1]['Nombre']} ⊆ géneros de biblioteca?: {g1 <= generos}")
    print(f"¿Géneros de {usuarios[ced2]['Nombre']} ⊆ géneros de biblioteca?: {g2 <= generos}")