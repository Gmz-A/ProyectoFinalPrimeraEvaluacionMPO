-- OPBJETIVOS DEL PROYECTO --
  Desarrollar una aplicación de consola en Python que permita realizar cuestionarios tipo test.
  El usuario podrá responder a una serie de preguntas, y el programa corregirá automáticamente las respuestas, mostrando la puntuación obtenida al finalizar.

-- REQUISITOS MINIMOS --
  1. Implementar un menu que se ejecute indefinidamente hasta que el usuario finalice (while), que permitirá las siguientes opciones:
     MENÚ
     1. Empezar Cuestionario
     2. Ranking
     3. Salir
      
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

-- RESPUESTAS CORRECTAS --
**Respuestas correctas:**

1. 1. ¿Qué país tiene el mayor número de islas en el mundo?
A) Indonesia
B) Filipinas
C) Suecia
D) Canadá
c. Suecia (Tiene más de 260,000 islas).

2. ¿En qué país se inventó originalmente el cruasán (croissant)?
A) Francia
B) Italia
C) Suiza
D) Austria
D. Austria (Se originó a partir de un panecillo llamado *kipferl*).


3. ¿Cuál es el único mamífero capaz de volar de forma activa (no planear)?
A) Ardilla voladora
B) Murciélago
C) Petauro del azúcar
D) Lémur volador
B. Murciélago

4. ¿Cuál es el planeta más caliente de nuestro sistema solar?
A) Mercurio
B) Júpiter
C) Marte
D) Venus
D. Venus (Su densa atmósfera crea un efecto invernadero que atrapa el calor, superando a Mercurio).

5. ¿De qué color es la piel de un oso polar bajo su pelaje?
A) Blanca
B) Rosa
C) Negra
D) Azulada
C. Negra (Le ayuda a absorber el calor del sol, mientras que los pelos son en realidad translúcidos y huecos).


6. ¿Qué significa la sigla "HTTP" que vemos al inicio de las direcciones web?
A) HyperText Transfer Protocol
B) Hyperlink Transfer Technology Platform
C) Host To Text Protocol
D) HyperText Terminal Processor
A. HyperText Transfer Protocol

7. ¿Cuál fue la ciudad considerada como la capital del Imperio Inca?
A) Machu Picchu
B) Cusco
C) Quito
D) Lima
B, Cusco

8. ¿Cuál es el hueso más largo del cuerpo humano?
A) Tibia
B) Húmero
C) Peroné
D) Fémur
D, Fémur

9. ¿Cuántas teclas tiene un piano clásico estándar?
A) 76
B) 88
C) 92
D) 64
B. 88 (52 teclas blancas y 36 teclas negras).

10. ¿Quién pintó la famosa obra "La joven de la perla"?
A) Johannes Vermeer
B) Rembrandt
C) Vincent van Gogh
D) Leonardo da Vinci
A. Johannes Vermeer**