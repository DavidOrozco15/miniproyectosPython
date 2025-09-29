inventario = {}           
clientes = {}             
empleados = {}            
configuracion = {"IVA": 0.19, "DescuentoVIP": 0.10}

historialVentas = []      
empleadosActivos = []     

plataformas = set()       
generos = set()           
clientesVIP = set()       

def registrarCliente():
    cedula = input("Ingrese la cédula del cliente: ")
    if cedula in clientes:
        print("El cliente ya existe.")
        return
    nombre = input("Ingrese el nombre del cliente: ")
    clientes[cedula] = {"Nombre": nombre, "Compras": []}
    print(f"Cliente {nombre} registrado con éxito.")

def buscarCliente():
    cedula = input("Ingrese la cédula a buscar: ")
    if cedula in clientes:
        c = clientes[cedula]
        print(f"Cliente encontrado: {cedula} - {c['Nombre']}. Compras: {len(c['Compras'])}")
    else:
        print("🔍 Cliente no encontrado.")

def mostrarClientes():
    print("\n--- LISTA DE CLIENTES ---")
    for cedula, datos in clientes.items():
        print(f"Cédula: {cedula} | Nombre: {datos['Nombre']}")

def registrarEmpleado():
    IDempleado = input("Ingrese el ID del empleado: ")
    if IDempleado in empleados:
        print("El empleado ya existe")
        return
    nombre = input("Ingrese el enombre del empleado: ")
    empleados[IDempleado]={"Nombre": nombre}
    empleadosActivos.append(IDempleado)
    print(f"Empleado {nombre} registrado y activo con exito.")

def mostrarEmpleadosActivos():
    print("\n--- EMPLEADOS ACTIVOS ---")
    if not empleadosActivos:  
        print("No hay empleados activos registrados.")
    else:
        for i, IDempleado in enumerate(empleadosActivos, start=1):
            nombre = empleados[IDempleado]["Nombre"]  
            print(f"{i}. ID: {IDempleado} | Nombre: {nombre}")


def agregarVideojuego():
    codigo = input("Ingrese el código del videojuego: ")
    if codigo in inventario:
        print("Ese videojuego ya existe en el inventario.")
        return
    titulo = input("Ingrese el titulo del videojuego: ")
    genero = input("Ingrese el genero del juego: ").lower()
    plataforma = input("Ingrese la plataforma (consola): ").lower()
    try:
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock disponible: "))
    except ValueError:
        print("Precio y stock deben ser números.")
        return
    
    inventario[codigo] = (titulo, genero, plataforma, precio, stock)
    generos.add(genero)
    plataformas.add(plataforma)
    print(f"\nEl Videojuego {titulo} fue agregado al inventario")

def mostrarInventario():
    print("\n----INVENTARIO----")
    for i, (codigo, informacion) in enumerate(inventario.items(), start=1):
        titulo, genero, plataforma, precio, stock = informacion
        print(f"-{codigo}- {titulo} | {genero} | {plataforma} | ${precio} | Stock: {stock}")

def registrarVenta():
    cedula = input("Ingrese la cédula del cliente: ")
    if cedula not in clientes:
        print("El cliente no está registrado.")
        return
    codigo = input("Ingrese el código del videojuego: ")
    if codigo not in inventario:
        print("El videojuego no existe.")
        return
    titulo, genero, plataforma, precio, stock = inventario[codigo]
    if stock <= 0:
        print("No hay stock disponible.")
        return
    
    subtotal = precio
    total = subtotal * (1 + configuracion["IVA"])
    if cedula in clientesVIP:
        total *= (1 - configuracion["DescuentoVIP"])
    
    inventario[codigo] = (titulo, genero, plataforma, precio, stock - 1)# -1 es para restarle al stock del videojuego
    transaccion = (cedula, codigo, total)
    historialVentas.append(transaccion)
    clientes[cedula]["Compras"].append(transaccion)
    print(f"Venta registrada de: {titulo} por ${total:.2f}")

def mostrarHistorialVentas():
    print("\n--- HISTORIAL DE VENTAS ---")
    for i, venta in enumerate(historialVentas, start=1):
        cedula, codigo, total = venta
        titulo = inventario[codigo][0] if codigo in inventario else "Desconocido"
        print(f"[{i}]. CLiente {cedula} Compro: {titulo} por ${total:.2f}")

def marcarClienteVIP():
    cedula = input("Ingrese la cédula del cliente: ")
    if cedula not in clientes:
        print("El cliente no está registrado.")
        return
    clientesVIP.add(cedula)
    print(f"Cliente {clientes[cedula]['Nombre']} marcado como VIP.")

def reporteStock():
    print("\n--- REPORTE: ---")
    for codigo, informacion in inventario.items():
        titulo, _, _, _, stock = informacion
        if stock <= 3:
            print("\n---STOCK BAJO----")
            print(f"{titulo} (Stock: {stock})")
        if stock >= 4:
            print("\n---STOCK SUFICIENTE----")
            print(f"{titulo} (Stock: {stock})")

def reporteVentasPorGenero():
    print("\n--- REPORTE: VENTAS POR GÉNERO ---")
    contador = {}
    for _, codigo, _ in historialVentas:
        if codigo in inventario:
            genero = inventario[codigo][1]
            contador[genero] = contador.get(genero, 0) + 1
    for genero, cantidad in contador.items():
        print(f"{genero}: {cantidad} ventas")

def reporteVentasPorPlataforma():
    print("\n--- REPORTE: VENTAS POR PLATAFORMA ---")
    contador = {}
    for _, codigo, _ in historialVentas:
        if codigo in inventario:
            plataforma = inventario[codigo][2]
            contador[plataforma] = contador.get(plataforma, 0) + 1
    for plataforma, cantidad in contador.items():
        print(f"{plataforma}: {cantidad} ventas")

def analisisClientesVIP():
    print("\n--- ANÁLISIS CLIENTES VIP ---")
    print(f"Clientes VIP: {clientesVIP}")
    print(f"Total VIP: {len(clientesVIP)}")

def analisisGenerosPopulares():
    print("\n--- ANÁLISIS: GÉNEROS POPULARES ---")
    vendidos = set()
    for _, codigo, _ in historialVentas:
        if codigo in inventario:
            vendidos.add(inventario[codigo][1])
    print(f"Géneros vendidos: {vendidos}")
    print(f"Géneros no vendidos: {generos - vendidos}")

def analisisPlataformas():
    print("\n--- ANÁLISIS: PLATAFORMAS ---")
    consolas = set()
    for _, codigo, _ in historialVentas:
        if codigo in inventario:
            consolas.add(inventario[codigo][2])
    print(f"Plataformas activas: {consolas}")
    print(f"Plataformas sin ventas: {plataformas - consolas}")

def configurarParametros():
    try:
        iva = float(input("Ingrese nuevo IVA (ej: 0.19): "))
        desc = float(input("Ingrese descuento VIP (ej: 0.10): "))
        configuracion["IVA"] = iva
        configuracion["DescuentoVIP"] = desc
        print("Parámetros configurados con éxito.")
    except ValueError:
        print("Valores inválidos.")