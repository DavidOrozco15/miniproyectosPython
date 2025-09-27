import modules.utils as u
import modules.messages as m
import modules.CRUD as c

def main():
    while True:
        opcion = m.menu()
        match opcion:
            case '1':
                c.agregar_libro()
            case '2':
                c.ver_biblioteca()
            case '3':
                c.buscar_libros()
            case '4':
                c.cambiar_estado()
            case '5':
                c.estadisticas()
            case '6':
                c.eliminar_libro()
            case '7':
                print("¡Hasta luego! 👋")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")
                u.pausar()
                u.limpiar()