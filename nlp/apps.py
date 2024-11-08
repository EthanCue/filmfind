from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .utils.loadData import load_nltk_resources, load_data_and_initialize_model

class NlpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nlp'
    vectorizer = None
    knn_model = None
    moviesData = None  # Agregar atributo para los datos de las películas

    def ready(self):
        # Cargar recursos de NLTK
        load_nltk_resources()
        print("Recursos de NLTK cargados correctamente.")

        # Registrar una señal para cargar el modelo después de que se hayan migrado las bases de datos
        self.load_model()

    def load_model(self, **kwargs):
        print("load_model")
        vectorizer, knn_model, moviesData = load_data_and_initialize_model()
        if vectorizer and knn_model and not moviesData.empty:
            NlpConfig.vectorizer = vectorizer
            NlpConfig.knn_model = knn_model
            NlpConfig.moviesData = moviesData
            print("Vectorizador, modelo KNN y datos de películas cargados correctamente en NlpConfig.")
        else:
            print("Error al cargar el modelo y los datos de películas.")
