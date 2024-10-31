# apps.py
from django.apps import AppConfig 
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
        nltk_packages = [
            'stopwords',
            'punkt',
            'wordnet',
            'omw-1.4'
        ]

        for package in nltk_packages:
            try:
                nltk.data.find(f"tokenizers/{package}") if package == 'punkt' else nltk.data.find(f"corpora/{package}")
            except LookupError:
                nltk.download(package)        
        try:
            movies_df = pd.read_excel('./film_dataset/moviesShortClean.xlsx')

            #dataset completo:
            #movies_df = pd.read_excel('C:/Users/ethan/OneDrive/Desktop/ESCOM/ESCOM_6/Ingenieria_de_Software/FilmFind/film_dataset/moviesClean.xlsx')
            #movies_df['overview'] = movies_df['normalizedOverview']

            #movies_df['overview'] = movies_df['overview'].fillna('').astype(str)

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
        except Exception as e:
            print(f"Error al cargar los datos de películas o al inicializar el modelo: {e}")
