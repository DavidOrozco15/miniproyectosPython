import modules.utils as u
import modules.messages as m
import modules.CRUD as c

def main():
    while True:
        opcion = m.menu()
        match opcion:
            case 1:
                c.registrarEstudiantes()
            case 2:
                c.agregarMateria()
            case 3:
                c.inscribirEstudiante()
            case 4:
                c.registrarCalificacion()
            case 5:
                c.materiasComunes()
            case 6:
                c.generarReporte()
            case 7:
                m.menuLista()
                c.mostrarLista()
            case 0:
                print("¡Hasta luego! 👋")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")
                u.pausar()
                u.limpiar()