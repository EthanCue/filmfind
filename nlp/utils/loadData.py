import joblib
import nltk
import os
from django.conf import settings
from django.db import connection
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd

# Configuración de rutas de archivo
VECTOR_PATH = os.path.join(settings.BASE_DIR, 'film_dataset', 'vectorizer.joblib')
KNN_MODEL_PATH = os.path.join(settings.BASE_DIR, 'film_dataset', 'knn_model.joblib')

def load_nltk_resources():
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

def load_data_and_initialize_model():
    print("Cargando datos y modelo...")
    try:
        from ..models import Movie  # Mover la importación aquí
        
        # Verificar si los modelos ya están en disco
        vectorizer = joblib.load(VECTOR_PATH)
        knn_model = joblib.load(KNN_MODEL_PATH)
        print("Modelo y vectorizador cargados desde archivos.")
        
        # Cargar datos desde la base de datos
        movies = Movie.objects.all().values_list('normalizedOverview', 'id', 'title', 'overview', 'poster_path')
        if not movies:
            print("No se encontraron películas en la base de datos.")
            return None, None, None

        # Extraer los resúmenes normalizados de las películas
        moviesOverviews = [movie[0] for movie in movies]
        moviesData = [{
            'id': movie[1],
            'title': movie[2],
            'overview': movie[3],
            'poster_path': movie[4]
        } for movie in movies]

        # Convertir moviesData a un DataFrame
        movies_df = pd.DataFrame(moviesData)

        # Configurar vectorización y modelo KNN
        vectorizer = TfidfVectorizer(
            max_features=10000,
            max_df=0.8,
            min_df=2,
            sublinear_tf=True,
            ngram_range=(1, 2)
        )
        tfidf_matrix = vectorizer.fit_transform(moviesOverviews)

        knn_model = NearestNeighbors(n_neighbors=7, metric='cosine', algorithm='auto')
        knn_model.fit(tfidf_matrix)

        # Guardar los modelos en disco
        joblib.dump(vectorizer, VECTOR_PATH)
        joblib.dump(knn_model, KNN_MODEL_PATH)
        print("Datos de películas y modelo KNN cargados y guardados con éxito.")
            
        return vectorizer, knn_model, movies_df
    except Exception as e:
        print(f"Error al cargar los datos de películas o al inicializar el modelo: {e}")
        return None, None, None
