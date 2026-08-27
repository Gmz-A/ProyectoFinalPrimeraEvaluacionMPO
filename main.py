import os
import random
import json

opcion_menu = 0
errores = 0
ranking = [1, 0]  # Nº de preguntas | Nº de aciertos | Porcen. de aciertos
with open("preguntas.json", "r", encoding="utf-8") as archivo:
    datos_json = json.load(archivo)
banco_preguntas = {int(clave): valor for clave, valor in datos_json.items()}

while opcion_menu != 3:

    print("""
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
                pregunta = banco_preguntas[numero_aleatorio]
                if numero_aleatorio in historial_preguntas:
                    pass
                else:
                    print(pregunta["pregunta"])
                    print(pregunta["opciones"])
                    
                    respuesta = input("-> ").lower()
                    os.system("cls" if os.name == "nt" else "clear")

                    if respuesta == pregunta["respuesta_correcta"]:
                        print("Respuesta Correcta, enhorabuena :)")
                        historial_preguntas.append(numero_aleatorio)
                        ranking[1] += 1
                    else:
                        print(
                            "Respuesta Incorrecta, intentalo de nuevo mas adelante\n"
                        )
                        errores += 1
                    pass
                
                    if len(historial_preguntas) == 10:
                        print("Se han acabado las preguntas :)\n")
                        opcion_preguntas = 2
                        porcentaje_acierto = (ranking[1] / ranking[0]) * 100
                        print(f"Has realizado {ranking[0]} preguntas de las cuales has acertado {ranking[1]} por lo qeu tienes un porcentaje de acierto del {porcentaje_acierto:.2f}%")
                    else:
                        ranking[0] += 1
                pass
        case 2:
            print("ranking")
            pass
        case 3:
            print("Hasta lueo, muchas gracias :)")
            pass