import modules.utils as u
import modules.messages as m
import modules.CRUD as c

def main():
    running = True
    
    while running:
        u.clear_screen()
        option = m.menu()
        
        if option == '1':
            u.clear_screen()
            c.add_game()
            u.pause()
        elif option == '2':
            u.clear_screen()
            c.view_games()
            u.pause()
        elif option == '3':
            u.clear_screen()
            c.complete_game()
            u.pause()
        elif option == '4':
            u.clear_screen()
            c.show_stats()
            u.pause()
        elif option == '5':
            print("¡Hasta luego!")
            running = False
        else:
            print("Opción inválida.")
            u.pause()