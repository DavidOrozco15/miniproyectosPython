import modules.utils as u
import modules.messages as m
import modules.CRUD as c

def main():
    while True:
        opcion = m.menu()
        match opcion:
            case 1:
                c.registrarUsuario()
            case 2:
                c.agregarLibro()
            case 3:
                c.prestarLibro()
            case 4:
                c.devolverLibro()
            case 5:
                c.recomendarLibros()
            case 6:
                c.analisisUsuarios()
            case 0:
                print("¡Hasta luego! 👋")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")
                u.pausar()
                u.limpiar()