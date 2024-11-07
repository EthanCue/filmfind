# apps.py
from django.apps import AppConfig 
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import nltk

class NlpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nlp'
    movies_data = None
    vectorizer = None
    knn_model = None

    def ready(self):
        # Verificar y descargar paquetes de NLTK solo si faltan
        nltk_packages = [
            ('tokenizers/punkt', 'punkt'),
            ('corpora/stopwords', 'stopwords'),
            ('corpora/wordnet', 'wordnet'),
            ('corpora/omw-1.4', 'omw-1.4')
        ]

        for resource, package in nltk_packages:
            try:
                nltk.data.find(resource)
            except LookupError:
                nltk.download(package)

        # Verificar si los datos de películas ya están cargados
        if NlpConfig.movies_data is None or NlpConfig.vectorizer is None or NlpConfig.knn_model is None:
            try:
                # Cargar el archivo de datos solo si no está en memoria
                file_path = './film_dataset/moviesClean.xlsx'
                if os.path.exists(file_path):
                    movies_df = pd.read_excel(file_path)

                    # Asegurarse de que 'normalizedOverview' esté presente y no tenga valores NaN
                    if 'normalizedOverview' in movies_df.columns:
                        movies_df['normalizedOverview'] = movies_df['normalizedOverview'].fillna('').astype(str)
                    else:
                        raise KeyError("La columna 'normalizedOverview' no se encontró en el archivo de datos.")

                    # Guardar los datos en la configuración de la aplicación
                    NlpConfig.movies_data = movies_df

                    # Inicializar el vectorizador y el modelo KNN
                    vectorizer = TfidfVectorizer()
                    tfidf_matrix = vectorizer.fit_transform(movies_df['normalizedOverview'])

                    knn_model = NearestNeighbors(n_neighbors=7, metric='cosine')
                    knn_model.fit(tfidf_matrix)

                    # Asignar el vectorizador y el modelo entrenado a la configuración de la aplicación
                    NlpConfig.vectorizer = vectorizer
                    NlpConfig.knn_model = knn_model

                    print("Datos de películas y modelo KNN cargados con éxito al iniciar el servidor.")
                else:
                    print(f"Archivo de datos no encontrado en la ruta: {file_path}")
            except Exception as e:
                print(f"Error al cargar los datos de películas o al inicializar el modelo: {e}")