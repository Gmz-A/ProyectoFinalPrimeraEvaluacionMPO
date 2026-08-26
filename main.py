import os
import random

opcion_menu = 0
errores = 0
ranking = [1, 0] #Nº de preguntas | Nº de aciertos | Porcen. de aciertos

while opcion_menu != 3:

    #os.system('cls' if os.name == 'nt' else 'clear')

    print ("""
    MENÚ
        1. Empezar Cuestionario
        2. Ranking
        3. Salir
    """)
    opcion_menu = int(input("-> "))

    match opcion_menu:
        case 1: 
            opcion_preguntas = 0
            historial_preguntas = []
            while opcion_preguntas != 2:
                numero_aleatorio = random.randint(1, 10)
                if numero_aleatorio in historial_preguntas:
                    pass
                else:
                    respuesta = 0
                    match numero_aleatorio:
                        case 1:
                            print("""
                            ¿Qué país tiene el mayor número de islas en el mundo?
                                A) Filipinas
                                B) Indonesia
                                C) Suecia C
                                D) Canadá
                            """)
                            respuesta = input("-> ").lower()
                            if respuesta == "c":
                                print("Respuesta Correcta, enhorabuena :)")
                                historial_preguntas.append(1)
                                ranking[1] += 1
                            else:
                                print("respuesta incorrecta, intentalo de nuevo mas adelante")
                                errores += 1
                            pass
                        case 2:
                            print("""
                            ¿En qué país se inventó originalmente el cruasán (croissant)?
                                A) Francia
                                B) Italia
                                C) Suiza
                                D) Austria C
                            """)
                            respuesta = input("-> ").lower()
                            if respuesta == "d":
                                print("Respuesta Correcta, enhorabuena :)")
                                ranking[1] += 1
                                historial_preguntas.append(2)
                            else:
                                print("respuesta incorrecta, intentalo de nuevo mas adelante")
                                errores += 1
                            pass
                        case 3:
                            print("""
                            ¿Cuál es el único mamífero capaz de volar de forma activa (no planear)?
                                A) Ardilla voladora
                                B) Murciélago C
                                C) Petauro del azúcar
                                D) Lémur volador
                            """)
                            respuesta = input("-> ").lower()
                            if respuesta == "b":
                                print("Respuesta Correcta, enhorabuena :)")
                                ranking[1] += 1
                                historial_preguntas.append(3)
                            else:
                                errores += 1
                                print("respuesta incorrecta, intentalo de nuevo mas adelante")
                            pass
                        case 4:
                            print("""
                            ¿Cuál es el planeta más caliente de nuestro sistema solar?
                                A) Mercurio
                                B) Júpiter
                                C) Marte
                                D) Venus C
                            """)
                            respuesta = input("-> ").lower()
                            if respuesta == "d":
                                print("Respuesta Correcta, enhorabuena :)")
                                ranking[1] += 1
                                historial_preguntas.append(4)
                            else:
                                errores += 1
                                print("respuesta incorrecta, intentalo de nuevo mas adelante")
                            pass
                        case 5:
                            print("""
                            ¿De qué color es la piel de un oso polar bajo su pelaje?
                                A) Blanca
                                B) Rosa
                                C) Negra C
                                D) Azulada
                            """)
                            respuesta = input("-> ").lower()
                            if respuesta == "c":
                                print("Respuesta Correcta, enhorabuena :)")
                                ranking[1] += 1
                                historial_preguntas.append(5)
                            else:
                                errores += 1
                                print("respuesta incorrecta, intentalo de nuevo mas adelante")
                            pass
                        case 6:
                            print("""
                            ¿Qué significa la sigla "HTTP" que vemos al inicio de las direcciones web?
                                A) HyperText Transfer Protocol C
                                B) Hyperlink Transfer Technology Platform
                                C) Host To Text Protocol
                                D) HyperText Terminal Processor
                            """)
                            respuesta = input("-> ").lower()
                            if respuesta == "a":
                                print("Respuesta Correcta, enhorabuena :)")
                                ranking[1] += 1
                                historial_preguntas.append(6)
                            else:
                                errores += 1
                                print("respuesta incorrecta, intentalo de nuevo mas adelante")
                            pass
                        case 7:
                            print("""
                            ¿Cuál fue la ciudad considerada como la capital del Imperio Inca?
                                A) Machu Picchu
                                B) Cusco C
                                C) Quito
                                D) Lima
                            """)
                            respuesta = input("-> ").lower()
                            if respuesta == "b":
                                print("Respuesta Correcta, enhorabuena :)")
                                ranking[1] += 1
                                historial_preguntas.append(7)
                            else:
                                errores += 1
                                print("respuesta incorrecta, intentalo de nuevo mas adelante")
                            pass
                        case 8:
                            print("""
                            ¿Cuál es el hueso más largo del cuerpo humano?
                                A) Tibia
                                B) Húmero
                                C) Peroné
                                D) Fémur C
                            """)
                            respuesta = input("-> ").lower()
                            if respuesta == "d":
                                print("Respuesta Correcta, enhorabuena :)")
                                ranking[1] += 1
                                historial_preguntas.append(8)
                            else:
                                errores += 1
                                print("respuesta incorrecta, intentalo de nuevo mas adelante")
                            pass
                        case 9:
                            print("""
                            ¿Cuántas teclas tiene un piano clásico estándar?
                                A) 76 
                                B) 88 C
                                C) 92
                                D) 64
                            """)
                            respuesta = input("-> ").lower()
                            if respuesta == "b":
                                print("Respuesta Correcta, enhorabuena :)")
                                ranking[1] += 1
                                historial_preguntas.append(9)
                            else:
                                errores += 1
                                print("respuesta incorrecta, intentalo de nuevo mas adelante")
                            pass
                        case 10:
                            print("""
                            ¿Quién pintó la famosa obra "La joven de la perla"?
                                A) Johannes Vermeer C
                                B) Rembrandt
                                C) Vincent van Gogh
                                D) Leonardo da Vinci
                            """)
                            respuesta = input("-> ").lower()
                            if respuesta == "a":
                                print("Respuesta Correcta, enhorabuena :)")
                                ranking[1] += 1
                                historial_preguntas.append(10)
                            else:
                                errores += 1
                                print("respuesta incorrecta, intentalo de nuevo mas adelante")
                            pass
                    if len(historial_preguntas) == 10:
                        print("Se han acabado las preguntas :)")
                        opcion_preguntas = 2
                        porcentaje_acierto = ((ranking[0]/ranking[1])*100)
                        print(f"Has realizado {ranking[0]} preguntas de las cuales has acertado {ranking[1]} por lo qeu tienes un porcentaje de acierto del {porcentaje_acierto}%")
                    else:
                        opcion_preguntas = int(input("Quiere seguir realizando preguntas (1. Si | 2. No) -> "))
                        if opcion_preguntas == 1: (ranking[0])+=1
                pass
        case 2: 
            print("ranking")
            pass
        case 3:
            print("Hasta lueo, muchas gracias :)")
            pass


#def preguntas_aleatorias():