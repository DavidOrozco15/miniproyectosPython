import modules.utils as u

def menuPrincipal():
    while True:
        u.limpiar()
        print("\n==== MENÚ PRINCIPAL ====")
        print("1. Clientes")
        print("2. Empleados")
        print("3. Inventario / Ventas")
        print("4. Reportes")
        print("5. Análisis")
        print("6. Configuración")
        print("0. Salir")
        opcion = input("Seleccione: ")
        return opcion

def menuClientes():
    while True:
        u.limpiar()
        print("\n--- MENÚ CLIENTES ---")
        print("1. Registrar cliente")
        print("2. Buscar cliente")
        print("3. Mostrar clientes")
        print("4. Marcar cliente VIP")
        print("0. Volver")
        opcion = input("Seleccione: ")
        return opcion

def menuEmpleados():
    while True:
        u.limpiar()
        print("\n--- MENÚ EMPLEADOS ---")
        print("1. Registrar empleado")
        print("2. Mostrar empleados activos")
        print("0. Volver")
        opcion = input("Seleccione: ")
        return opcion

def menuInventarioVentas():
    while True:
        u.limpiar()
        print("\n--- MENÚ INVENTARIO Y VENTAS ---")
        print("1. Agregar videojuego")
        print("2. Mostrar inventario")
        print("3. Registrar venta")
        print("4. Mostrar historial de ventas")
        print("0. Volver")
        opcion = input("Seleccione: ")
        return opcion

def menuReportes():
    while True:
        u.limpiar()
        print("\n--- MENÚ REPORTES ---")
        print("1. Reporte stock")
        print("2. Ventas por género")
        print("3. Ventas por plataforma")
        print("0. Volver")
        opcion = input("Seleccione: ")
        return opcion

def menuAnalisis():
    while True:
        u.limpiar()
        print("\n--- MENÚ ANÁLISIS ---")
        print("1. Análisis clientes VIP")
        print("2. Análisis géneros populares")
        print("3. Análisis plataformas")
        print("0. Volver")
        opcion = input("Seleccione: ")
        return opcion

def menuConfiguracion():
    while True:
        u.limpiar()
        print("\n--- MENÚ CONFIGURACIÓN ---")
        print("1. Configurar IVA y Descuento")
        print("0. Volver")
        opcion = input("Seleccione: ")
        return opcion
        