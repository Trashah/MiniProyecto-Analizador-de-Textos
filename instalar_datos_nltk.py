import nltk

def download_nltk_data():
    print("Descargando datos necesarios de NLTK...")
    
    packages = [
        'punkt',
        'stopwords',
        'averaged_perceptron_tagger',
        'maxent_ne_chunker',
        'words',
        'wordnet',
        'omw-1.4'
    ]
    
    for package in packages:
        try:
            print(f"Verificando/Descargando: {package}")
            nltk.download(package, quiet=True)
            print(f"  ✅ {package} listo.")
        except Exception as e:
            print(f"  ❌ Error descargando {package}: {e}")

    print("\n¡Descarga completa! Ahora puedes ejecutar la aplicación.")

if __name__ == "__main__":
    download_nltk_data()
