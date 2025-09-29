import modules.utils as u

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
    u.limpiar()
    cedula = input("Ingrese la cédula del cliente: ")
    if cedula in clientes:
        print("\nEl cliente ya existe.")
        u.pausar()
        return
    nombre = input("Ingrese el nombre del cliente: ")
    clientes[cedula] = {"Nombre": nombre, "Compras": []}
    print(f"\nCliente {nombre} registrado con éxito.")
    u.pausar()

def buscarCliente():
    u.limpiar()
    cedula = input("Ingrese la cédula a buscar: ")
    if cedula in clientes:
        c = clientes[cedula]
        print(f"\nCliente encontrado: {cedula} - {c['Nombre']}. Compras: {len(c['Compras'])}")
    else:
        print("\n🔍 Cliente no encontrado.")
    u.pausar()

def mostrarClientes():
    u.limpiar()
    print("\n--- LISTA DE CLIENTES ---\n")
    for cedula, datos in clientes.items():
        print(f"Cédula: {cedula} | Nombre: {datos['Nombre']}")
    u.pausar()

def registrarEmpleado():
    u.limpiar()
    IDempleado = input("Ingrese el ID del empleado: ")
    if IDempleado in empleados:
        print("\nEl empleado ya existe.")
        u.pausar()
        return
    nombre = input("Ingrese el nombre del empleado: ")
    empleados[IDempleado] = {"Nombre": nombre}
    empleadosActivos.append(IDempleado)
    print(f"\nEmpleado {nombre} registrado y activo con éxito.")
    u.pausar()

def mostrarEmpleadosActivos():
    u.limpiar()
    print("\n--- EMPLEADOS ACTIVOS ---\n")
    if not empleadosActivos:
        print("No hay empleados activos registrados.")
    else:
        for i, IDempleado in enumerate(empleadosActivos, start=1):
            nombre = empleados[IDempleado]["Nombre"]
            print(f"{i}. ID: {IDempleado} | Nombre: {nombre}")
    u.pausar()

def agregarVideojuego():
    u.limpiar()
    codigo = input("Ingrese el código del videojuego: ")
    if codigo in inventario:
        print("\nEse videojuego ya existe en el inventario.")
        u.pausar()
        return
    titulo = input("Ingrese el título del videojuego: ")
    genero = input("Ingrese el género del juego: ").lower()
    plataforma = input("Ingrese la plataforma (consola): ").lower()
    try:
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock disponible: "))
    except ValueError:
        print("\nPrecio y stock deben ser números.")
        u.pausar()
        return
    
    inventario[codigo] = (titulo, genero, plataforma, precio, stock)
    generos.add(genero)
    plataformas.add(plataforma)
    print(f"\nEl videojuego '{titulo}' fue agregado al inventario.")
    u.pausar()

def mostrarInventario():
    u.limpiar()
    print("\n---- INVENTARIO ----\n")
    for i, (codigo, info) in enumerate(inventario.items(), start=1):
        titulo, genero, plataforma, precio, stock = info
        print(f"-{codigo}- {titulo} | {genero} | {plataforma} | ${precio} | Stock: {stock}")
    u.pausar()

def registrarVenta():
    u.limpiar()
    cedula = input("Ingrese la cédula del cliente: ")
    if cedula not in clientes:
        print("\nEl cliente no está registrado.")
        u.pausar()
        return
    codigo = input("Ingrese el código del videojuego: ")
    if codigo not in inventario:
        print("\nEl videojuego no existe.")
        u.pausar()
        return
    titulo, genero, plataforma, precio, stock = inventario[codigo]
    if stock <= 0:
        print("\nNo hay stock disponible.")
        u.pausar()
        return
    
    subtotal = precio
    total = subtotal * (1 + configuracion["IVA"])
    if cedula in clientesVIP:
        total *= (1 - configuracion["DescuentoVIP"])
    
    inventario[codigo] = (titulo, genero, plataforma, precio, stock - 1)
    transaccion = (cedula, codigo, total)
    historialVentas.append(transaccion)
    clientes[cedula]["Compras"].append(transaccion)

    print(f"\nVenta registrada de: {titulo} por ${total:.2f}")
    u.pausar()

def mostrarHistorialVentas():
    u.limpiar()
    print("\n--- HISTORIAL DE VENTAS ---\n")
    for i, venta in enumerate(historialVentas, start=1):
        cedula, codigo, total = venta
        titulo = inventario[codigo][0] if codigo in inventario else "Desconocido"
        print(f"[{i}]. Cliente {cedula} compró: {titulo} por ${total:.2f}")
    u.pausar()

def marcarClienteVIP():
    u.limpiar()
    cedula = input("Ingrese la cédula del cliente: ")
    if cedula not in clientes:
        print("\nEl cliente no está registrado.")
        u.pausar()
        return
    clientesVIP.add(cedula)
    print(f"\nCliente {clientes[cedula]['Nombre']} marcado como VIP.")
    u.pausar()

def reporteStock():
    u.limpiar()
    print("\n--- REPORTE DE STOCK ---\n")
    for codigo, info in inventario.items():
        titulo, _, _, _, stock = info
        if stock <= 3:
            print("\n--- STOCK BAJO ---")
            print(f"{titulo} (Stock: {stock})")
        else:
            print("\n--- STOCK SUFICIENTE ---")
            print(f"{titulo} (Stock: {stock})")
    u.pausar()

def reporteVentasPorGenero():
    u.limpiar()
    print("\n--- REPORTE: VENTAS POR GÉNERO ---\n")
    contador = {}
    for _, codigo, _ in historialVentas:
        if codigo in inventario:
            genero = inventario[codigo][1]
            contador[genero] = contador.get(genero, 0) + 1
    for genero, cantidad in contador.items():
        print(f"{genero}: {cantidad} ventas")
    u.pausar()

def reporteVentasPorPlataforma():
    u.limpiar()
    print("\n--- REPORTE: VENTAS POR PLATAFORMA ---\n")
    contador = {}
    for _, codigo, _ in historialVentas:
        if codigo in inventario:
            plataforma = inventario[codigo][2]
            contador[plataforma] = contador.get(plataforma, 0) + 1
    for plataforma, cantidad in contador.items():
        print(f"{plataforma}: {cantidad} ventas")
    u.pausar()

def analisisClientesVIP():
    u.limpiar()
    print("\n--- ANÁLISIS CLIENTES VIP ---\n")
    print(f"Clientes VIP: {clientesVIP}")
    print(f"Total VIP: {len(clientesVIP)}")
    u.pausar()

def analisisGenerosPopulares():
    u.limpiar()
    print("\n--- ANÁLISIS: GÉNEROS POPULARES ---\n")
    vendidos = set()
    for _, codigo, _ in historialVentas:
        if codigo in inventario:
            vendidos.add(inventario[codigo][1])
    print(f"Géneros vendidos: {vendidos}")
    print(f"Géneros no vendidos: {generos - vendidos}")
    u.pausar()

def analisisPlataformas():
    u.limpiar()
    print("\n--- ANÁLISIS: PLATAFORMAS ---\n")
    consolas = set()
    for _, codigo, _ in historialVentas:
        if codigo in inventario:
            consolas.add(inventario[codigo][2])
    print(f"Plataformas activas: {consolas}")
    print(f"Plataformas sin ventas: {plataformas - consolas}")
    u.pausar()

def configurarParametros():
    u.limpiar()
    try:
        iva = float(input("Ingrese nuevo IVA (ej: 0.19): "))
        desc = float(input("Ingrese descuento VIP (ej: 0.10): "))
    except ValueError:
        print("\nValores inválidos.")
        u.pausar()
        return
    configuracion["IVA"] = iva
    configuracion["DescuentoVIP"] = desc
    print("\nParámetros configurados con éxito.")
    u.pausar()

