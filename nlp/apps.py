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

        self.load_model()

    def load_model(self, **kwargs):
        print("Cargando el modelo...")
        tokenizer, model, knn_model, movies_df = load_data_and_initialize_model()
        
        if knn_model and movies_df is not None and not movies_df.empty:
            NlpConfig.tokenizer = tokenizer  # Si necesitas el tokenizer
            NlpConfig.model = model          # Si necesitas el modelo BERT
            NlpConfig.knn_model = knn_model
            NlpConfig.moviesData = movies_df
            print("Modelo BERT, vectorizador, modelo KNN y datos de películas cargados correctamente.")
        else:
            print("Error al cargar el modelo y los datos de películas.")
