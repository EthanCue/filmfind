Para garantizar que el sistema FilmFind funcione correctamente después de transferir el proyecto, el
destinatario debe seguir una serie de pasos que van desde la configuración del entorno hasta la
ejecución del servidor y la interfaz frontend. Este ensayo desglosa detalladamente estos pasos
esenciales.
1. Clonación y Configuración del Entorno de Desarrollo
El primer paso para correr FilmFind es clonar el repositorio en la máquina local. Esto se realiza
mediante el comando git clone https://github.com/EthanCue/filmfind, o descargar el zip directamente.
Una vez clonado, es fundamental moverse al directorio del proyecto principal (cd filmfind) para poder
trabajar en él. El siguiente paso crucial es configurar un entorno virtual, lo cual encapsula todas las
dependencias del proyecto, previniendo conflictos con otras aplicaciones. Esto se logra mediante el
comando python -m venv venv, creando un entorno virtual llamado "venv" dentro del directorio del
proyecto. Luego, se activa con source venv/bin/activate en sistemas Unix o venv\Scripts\activate en
Windows.
2. Instalación de Dependencias
Una vez activado el entorno virtual, el siguiente paso es instalar todas las dependencias necesarias.
Esto se hace con pip install -r requirements.txt, utilizando el archivo de requerimientos que se ha
generado previamente en el proyecto original. Este archivo asegura que todas las bibliotecas,
incluyendo Django, Pandas, Scikit-learn y NLTK, se instalen con las versiones correctas. Además,
algunos recursos de NLTK (como punkt, wordnet, y stopwords) pueden necesitar descargarse
manualmente. El destinatario puede hacerlo ejecutando el script ensure_nltk_resources() o añadiendo
manualmente las descargas para que el sistema de procesamiento de lenguaje natural funcione
correctamente.
3. Cargar los Datos de Películas y Entrenar el Modelo
El sistema FilmFind utiliza un modelo de K-Nearest Neighbors (KNN) basado en los datos de las
películas, que se encuentran en un archivo Excel en el directorio film_dataset. Este archivo debe estar
disponible en el sistema y es cargado automáticamente cuando se ejecuta el servidor. Si el archivo de
datos no se encuentra o está dañado, el destinatario debe reponerlo para evitar errores. La carga de
datos y el entrenamiento del modelo KNN se gestionan en el método ready de NlpConfig dentro de
apps.py. Esta configuración asegura que, al iniciar el servidor, el modelo y los datos estén disponibles
para procesar las descripciones enviadas desde el frontend.
4. Iniciar el Servidor de Desarrollo de Django
Con todos los preparativos listos, el siguiente paso es ejecutar el servidor backend de Django. Esto se
hace con python manage.py runserver, lo que inicia el servidor en http://127.0.0.1:8000. Si todos los
pasos anteriores se han completado correctamente, el servidor cargará los datos de las películas,
inicializará el modelo KNN, y estará listo para recibir peticiones.
5. Configuración del Frontend y Ejecución de Vite
FilmFind también cuenta con una interfaz frontend creada con React y gestionada por Vite. Para
correr el frontend, es necesario instalar las dependencias de Node.js. En una terminal diferente (aun en
el entorno virtual venv), mientras el servidor se encuentra operando, el usuario debe navegar al
directorio client (cd client) y ejecutar npm install para instalar las bibliotecas de frontend
especificadas en package.json. Una vez instaladas, el frontend se lanza con npm run dev, iniciando un
servidor de desarrollo en http://localhost:3000. Esto permite al usuario interactuar con la interfaz
gráfica y enviar peticiones al backend para obtener recomendaciones de películas.
