-- OPBJETIVOS DEL PROYECTO --
  Desarrollar una aplicación de consola en Python que permita realizar cuestionarios tipo test.
  El usuario podrá responder a una serie de preguntas, y el programa corregirá automáticamente las respuestas, mostrando la puntuación obtenida al finalizar.

-- REQUISITOS MINIMOS --
  1. Implementar un menu que se ejecute indefinidamente hasta que el usuario finalice (while), que permitirá las siguientes opciones:

     _### MENÚ ###_
     _1- Empezar Cuestionario_
     _2- Ranking_
     _3- Salir_
  3. Mostrar una serie de preguntas una a una al usuario.
  4. Cada pregunta debe tener:
     * Enunciado de la pregunta.
     * Cuatro opciones de respuesta
     * Una única opción correcta
  5. El usuario debe poder introducir su respuesta (por ejemplo: A, B, C o D).
  6. El programa debe indicar si la respuesta es correcta o incorrecta.
  7. Al finalizar el test, debe mostrar:
     * Número total de preguntas.
     * Número de aciertos.
     * Porcentaje de aciertos.
     * Una valoración final (por ejemplo: “¡Muy bien!”, “Necesitas practicar”, etc.).
    
-- CONTENIDOS A APLICAR --
  * Tipos de datos primitivos y estructuras complejas (listas, diccionarios).
  * Control de flujo (if, elif, else).
  * Bucles (for, while).
  * Funciones con parámetros y retorno.
  * Entrada/salida de datos por consola.

-- SUGERENCIA ESTRUCTURA --
* cargar_preguntas() → Devuelve una lista de preguntas (pueden estar "hardcodeadas" al principio).
* mostrar_pregunta(pregunta) → Muestra la pregunta y sus opciones.
* obtener_respuesta() → Pide al usuario su respuesta y la valida.
* corregir_respuesta(respuesta, correcta) → Comprueba si es correcta.
* mostrar_resultados(aciertos, total) → Muestra el resumen final.
