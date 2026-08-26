import os

opcion_menu = 0

while opcion_menu != 3:

    os.system('cls' if os.name == 'nt' else 'clear')

    print ("""
    MENÚ
        1. Empezar Cuestionario
        2. Ranking
        3. Salir
    """)
    opcion_menu = int(input("->"))

    match opcion_menu:
        case 1: 
            print("preguntas")
            pass
        case 2: 
            print("ranking")
            pass
        case 3:
            print("Hasta lueo, muchas gracias :)")
            pass