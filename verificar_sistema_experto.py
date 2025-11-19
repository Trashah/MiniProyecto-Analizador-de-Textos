from analizadortext import analizar_texto

test_cases = [
    ("La inteligencia artificial está cambiando el mundo del software.", "Tecnología"),
    ("El delantero metió un gol impresionante en el partido de ayer.", "Deportes"),
    ("El presidente firmó una nueva ley en el parlamento.", "Política"),
    ("La teoría de la relatividad fue propuesta por Einstein.", "Ciencia"),
    ("Este es un texto sin mucho sentido sobre caminar por la calle.", "General / No identificado")
]

print("--- Verificación del Sistema Experto ---\n")

for texto, esperado in test_cases:
    resultado = analizar_texto(texto)
    print(f"Texto: {texto[:50]}...")
    
    # Buscar la línea de clasificación
    lines = resultado.split('\n')
    clasificacion = "No encontrada"
    for line in lines:
        if "Clasificación de Tema (Sistema Experto):" in line:
            clasificacion = line.split(": ")[1].split(" (")[0]
            break
            
    print(f"  Esperado: {esperado}")
    print(f"  Obtenido: {clasificacion}")
    
    if esperado in clasificacion:
        print("  ✅ CORRECTO")
    else:
        print("  ❌ INCORRECTO")
    print("-" * 30)
