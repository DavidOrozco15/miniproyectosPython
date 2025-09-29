import modules.utils as u
import modules.messages as m
import modules.CRUD as c

def main():
    while True:
        opcion = m.menuPrincipal()
        match opcion:
            case "1":
                m.menuClientes()
            case "2":
                m.menuEmpleados()
            case "3":
                m.menuInventarioVentas()
            case "4":
                m.menuReportes()
            case "5":
                m.menuAnalisis()
            case "6":
                m.menuConfiguracion()
            case "0":
                print("¡Hasta luego! 👋")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")
                u.pausar()
                u.limpiar()

def mainClientes():
    while True:
        opcion = m.menuClientes()
        match opcion:
            case "1":
                c.registrarCliente()
            case "2":
                c.buscarCliente()
            case "3":
                c.mostrarClientes()
            case "4":
                c.marcarClienteVIP()
            case "0":
                break
            case _:
                print("Opción inválida.")
                u.pausar()
                u.limpiar()

def mainEmpleados():
    while True:
        opcion = m.menuEmpleados()
        match opcion:
            case "1":
                c.registrarEmpleado()
            case "2":
                c.mostrarEmpleadosActivos()
            case "0":
                break
            case _:
                print("Opción inválida.")
                u.pausar()
                u.limpiar()

def mainInventario():
    while True:
        opcion = m.menuInventarioVentas()
        match opcion:
            case "1":
                c.agregarVideojuego()
            case "2":
                c.mostrarInventario()
            case "3":
                c.registrarVenta()
            case "4":
                c.mostrarHistorialVentas()
            case "0":
                break
            case _:
                print("Opción inválida.")
                u.pausar()
                u.limpiar()

def mainReportes():
    while True:
        opcion = m.menuReportes()
        match opcion:
            case "1":
                c.reporteStock()
            case "2":
                c.reporteVentasPorGenero()
            case "3":
                c.reporteVentasPorPlataforma()
            case "0":
                break
            case _:
                print("Opción inválida.")

def mainAnalisis():
    while True:
        opcion = m.menuAnalisis()
        match opcion:
            case "1":
                c.analisisClientesVIP()
            case "2":
                c.analisisGenerosPopulares()
            case "3":
                c.analisisPlataformas()
            case "0":
                break
            case _:
                print("Opción inválida.")

def mainConfig():
    while True:
        opcion = m.menuConfiguracion()
        match opcion:
            case "1":
                c.configurarParametros()
            case "0":
                break
            case _:
                print("Opción inválida.")