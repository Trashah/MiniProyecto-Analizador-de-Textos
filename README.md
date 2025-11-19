# MiniProyecto-Analizador-de-Textos
Este proyecto es una aplicación en Python con interfaz gráfica que permite analizar textos académicos, literarios o generales.
El analizador muestra:

Número de palabras.
Frecuencia de términos clave.
Sinónimos de los términos clave.
Entidades nombradas (personas, lugares, organizaciones).

Además, permite escribir directamente un texto o importar un archivo .txt para ser analizado.

## Requisitos
Tener instalado [Python] en su versión 3.13.17 
Tener instalado [Visual Studio Code]
Pip (este ya debería venir incluido en la instalación de Python)

## Instalación
Para empezar a usar este documento, necesitarás clonar el repositorio a tu sistema de archivos. Todas las instrucciones están escritas para usuarios de Windows solamente.

Entra a la carpeta en la que quieras tener el proyecto usando el Explorador de Archivos; por ejemplo en tu carpeta de `Documentos\Proyectos` o algo por el estilo.

Haz clic derecho sobre algún espacio en blanco dentro del Explorador y selecciona la opción `Abrir en Terminal`. Si no aparece, puede ser que diga `Abrir en Símbolo del Sistema`, `Abrir en PowerShell` `Abrir en CMD` o algo así. Si no aparece ninguna de estas opciones, prueba manteniendo la tecla `Shift` pulsada en tu teclado mientras haces clic derecho.

Una vez abierta la terminal, ingresa el siguiente comando:

```bash
git clone https://github.com/skym0ds/MiniProyecto-Analizador-de-Textos
```

Es posible que te aparezca una ventana pidiendo que ingreses tu nombre de usuario o correo electrónico que tienes en GitHub y la contraseña de tu cuenta. Ingrésalas para poder continuar.

Una vez clonado el repositorio, podrás acceder a la carpeta usando.

```bash
cd MiniProyecto-Analizador-deTextos
```

Si ya tienes abierto VS CODE o algún otro editor o IDE, abre una terminal integrada para continuar; si no continua en la misma terminal de hace rato.

### Paso 1: Instalar librerías
Ejecuta el siguiente comando para instalar todas las dependencias necesarias (NLTK, Scikit-learn, Numpy, etc.):

```bash
pip install -r requerimientos.txt
```

### Paso 2: Descargar datos de NLTK
Hemos creado un script para facilitar la descarga de los diccionarios y modelos necesarios. Ejecuta:

```bash
python instalar_datos_nltk.py
```

Esto descargará automáticamente todo lo necesario para que el analizador funcione correctamente.

## USO DEL TEST
Como ya instalaste las dependencias en el paso anterior (incluyendo `scikit-learn`), para ejecutar las pruebas solo necesitas correr:

```bash
python testapp.py
```

## Ejecución

Para ejecutar el proyecto bastaría con poner el siguiente comando en la consola desde visual studio:

```bash
python analizadortext.py
```





















[Python]: https://www.python.org/downloads/
[Visual Studio Code]: https://code.visualstudio.com/
