# Documentación del Sistema Experto (Clasificador de Temas)

## ¿Qué se agregó?
Se implementó una funcionalidad de **Sistema Experto basado en Reglas** dentro del analizador de textos. Su objetivo es identificar automáticamente el tema principal del texto analizado.

## ¿Cómo funciona?
El sistema utiliza un enfoque lógico simple pero efectivo:

1.  **Base de Conocimiento**: Contiene listas de palabras clave asociadas a categorías específicas.
    *   **Tecnología**: *computadora, software, inteligencia artificial, internet...*
    *   **Ciencia**: *física, química, biología, teoría, experimento...*
    *   **Deportes**: *fútbol, gol, partido, equipo, jugador...*
    *   **Política**: *gobierno, ley, elecciones, presidente, democracia...*
    *   **Arte/Cultura**: *música, pintura, literatura, cine, obra...*

2.  **Motor de Inferencia**:
    *   El sistema recorre las palabras del texto (tokens).
    *   Cuenta cuántas palabras coinciden con cada categoría.
    *   La categoría con mayor número de coincidencias es seleccionada como el tema del texto.

3.  **Reglas de Decisión**:
    *   Si no hay coincidencias suficientes (0 puntos), el sistema clasifica el texto como **"General / No identificado"**.

## Archivos Modificados
*   `analizadortext.py`: Se agregó la función `sistema_experto_clasificacion` y se integró en el flujo principal.
*   `testapp.py`: Se actualizaron las pruebas para verificar que el sistema clasifique correctamente los textos de ejemplo.
