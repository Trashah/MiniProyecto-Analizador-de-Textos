
#Importación de librerías
import nltk #Libería principal para el procesamiento del lenguaje natural
from nltk.corpus import wordnet as wn, stopwords
from nltk import word_tokenize, pos_tag, ne_chunk, FreqDist
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox


def analizar_texto(texto):
    resultado = ""

    if not texto.strip():
        return "⚠️ No se ha ingresado texto"

#Tokenización
#Se divide el texto en una lista de palabras (tokens) y se convierten a minúsculas.
    tokens = word_tokenize(texto.lower(), language="spanish")

#Liempieza, solo se tomarán las palabras (sin signos ni números) y se eliminarán las stopwords (palabras vacías)
    tokens_limpios = [t for t in tokens if t.isalpha()]

# Se carga el conjunto de "stopwords" (palabras comunes sin valor semántico) en español.

    stop_words = set(stopwords.words("spanish"))
    tokens_filtrados = [t for t in tokens_limpios if t not in stop_words]

#Número de palabras reales
    num_palabras = len(tokens_filtrados)  #Se corrigió y se agregó la filtración para contar palabras "reales"
    resultado += f"📌 Número total de palabras: {num_palabras}\n\n"

#Frecuencia de términos
    fdist = FreqDist(tokens_filtrados)
    top_terminos = fdist.most_common(5)
    resultado += "📌 Términos clave más comunes:\n"
    for palabra, frecuencia in top_terminos:
        resultado += f"{palabra}: {frecuencia}\n"
    resultado += "\n"

#Sinónimos para los términos clave
    resultado += "📌 Sinónimos de los términos clave:\n"
    for palabra, _ in top_terminos:
        synsets = wn.synsets(palabra, lang="spa") #Se busca la palabra en wordnet
        sinonimos = set() #Evitamos sinónimos duplicados
        for syn in synsets:
            for lemma in syn.lemmas("spa"):
                sinonimos.add(lemma.name())
        if sinonimos:
            resultado += f"- {palabra}: {', '.join(list(sinonimos)[:5])}\n" #Se proporcionan los primeros 5 resultados
        else:
            resultado += f"- {palabra}: (no se encontraron sinónimos)\n"
    resultado += "\n"

    # ... (previous code)

    #Reconocimiento de Entidades Nombradas (NER)
    tokens_origen = word_tokenize(texto, language="spanish") #se agregó el idioma a español
    etiquetas = pos_tag(tokens_origen)     # Primero, se etiqueta cada palabra con su categoría gramatical (nombre, verbo, adjetivo, etc.)
    arbol_entidades = ne_chunk(etiquetas) #agrupa las palabras con su categoría gramatical
    resultado += "📌 Entidades reconocidas en el texto:\n"
    for subtree in arbol_entidades:
        if hasattr(subtree, "label"):
            entidad = " ".join(c[0] for c in subtree.leaves())
            resultado += f"{subtree.label()}: {entidad}\n"
    resultado += "\n"

    # --- SISTEMA EXPERTO: Clasificación de Tema ---
    resultado += sistema_experto_clasificacion(tokens_limpios)
    
    return resultado


def sistema_experto_clasificacion(tokens):
    """
    Sistema experto simple basado en reglas para clasificar el tema del texto.
    Base de conocimiento: Diccionario de palabras clave.
    Motor de inferencia: Conteo de coincidencias y selección de máximo.
    """
    # Base de conocimiento
    base_conocimiento = {
        "Tecnología": ["computadora", "software", "hardware", "inteligencia", "artificial", "internet", "redes", "algoritmo", "datos", "programación", "código", "app", "digital", "robot", "cibernético"],
        "Ciencia": ["física", "química", "biología", "espacio", "teoría", "experimento", "científico", "átomo", "molécula", "energía", "célula", "astronomía", "genética"],
        "Deportes": ["fútbol", "baloncesto", "tenis", "gol", "partido", "jugador", "equipo", "torneo", "campeonato", "medalla", "olímpico", "entrenador", "atleta", "carrera"],
        "Política": ["gobierno", "ley", "elecciones", "presidente", "ministro", "democracia", "voto", "parlamento", "política", "nación", "naciones", "estado", "candidato", "partido", "organización", "unidas"],
        "Arte/Cultura": ["música", "pintura", "cine", "literatura", "poesía", "escultura", "artista", "obra", "museo", "concierto", "teatro", "novela", "autor", "escritor", "libro", "escribió"]
    }

    # Motor de inferencia
    puntuaciones = {tema: 0 for tema in base_conocimiento}
    
    for token in tokens:
        for tema, palabras_clave in base_conocimiento.items():
            if token in palabras_clave:
                puntuaciones[tema] += 1

    # Reglas de decisión
    tema_detectado = "General / No identificado"
    max_puntos = 0
    
    for tema, puntos in puntuaciones.items():
        if puntos > max_puntos:
            max_puntos = puntos
            tema_detectado = tema
            
    # Umbral mínimo
    if max_puntos < 1:
        tema_detectado = "General / No identificado"

    return f"📌 Clasificación de Tema (Sistema Experto): {tema_detectado} (Coincidencias: {max_puntos})\n"


#Función para botón "Analizar"
def ejecutar_analisis():
    texto = entrada_texto.get("1.0", tk.END)
    try:
        resultado = analizar_texto(texto)
        salida_texto.delete("1.0", tk.END)
        salida_texto.insert(tk.END, resultado)
    except Exception as e:
        messagebox.showerror("Error en análisis", str(e))


#Función para cargar archivo txt
def cargar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                contenido = f.read()
                entrada_texto.delete("1.0", tk.END)
                entrada_texto.insert(tk.END, contenido)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")

#Función para limpiar o borrar el texto introducido
def limpiar_texto():
    entrada_texto.delete("1.0", tk.END)
    salida_texto.delete("1.0", tk.END)



#Interfaz gráfica (Tkinter)
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Analizador de Textos Academicos Equipo 11")
    ventana.geometry("850x650")

#Etiqueta
    tk.Label(ventana, text="Introduce un texto académico o carga un archivo .txt:",
            font=("Arial", 12)).pack(pady=5)

#Cuadro de texto para entrada
    entrada_texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=95, height=10)
    entrada_texto.pack(padx=10, pady=10)

#Botones
    frame_botones = tk.Frame(ventana)
    frame_botones.pack()

    btn_analizar = tk.Button(frame_botones, text="Analizar", command=ejecutar_analisis, bg="lightgreen")
    btn_analizar.grid(row=0, column=0, padx=5)

    btn_cargar = tk.Button(frame_botones, text="Cargar archivo .txt", command=cargar_archivo, bg="lightblue")
    btn_cargar.grid(row=0, column=1, padx=5)

    btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_texto, bg="salmon")
    btn_limpiar.grid(row=0, column=2, padx=5)

#Cuadro de texto para salida
    tk.Label(ventana, text="Resultados del análisis:",
            font=("Arial", 12)).pack(pady=5)

    salida_texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=95, height=20, state="normal")
    salida_texto.pack(padx=10, pady=10)

    ventana.mainloop()
