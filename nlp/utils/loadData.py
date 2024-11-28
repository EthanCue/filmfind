import os
import joblib
import pandas as pd
from transformers import BertTokenizer, BertModel
import torch
from sklearn.neighbors import NearestNeighbors
from django.conf import settings
import nltk
from tqdm import tqdm  # Para mostrar progreso

# Configuración de rutas de archivo
BERT_EMBEDDINGS_PATH = os.path.join(settings.BASE_DIR, 'film_dataset', 'bert_embeddings.joblib')
KNN_MODEL_PATH = os.path.join(settings.BASE_DIR, 'film_dataset', 'knn_model.joblib')

# Carga de recursos NLTK
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

# Generación de embeddings en lotes
def generate_embeddings_in_batches(overviews, model, tokenizer, batch_size=64):
    embeddings = []
    for i in tqdm(range(0, len(overviews), batch_size)):
        try:
            batch = overviews[i:i+batch_size]
            encoded = tokenizer(batch, padding=True, truncation=True, return_tensors='pt', max_length=512)
            with torch.no_grad():
                batch_embeddings = model(**encoded).last_hidden_state.mean(dim=1)
            embeddings.extend(batch_embeddings.cpu().numpy())
        except Exception as e:
            print(f"Error al procesar el lote {i}: {e}")
    return embeddings

# Función principal para cargar datos y modelo
def load_data_and_initialize_model():
    print("Cargando datos y modelo...")
    try:
        from ..models import Movie

        # Cargar datos desde la base de datos
        movies = Movie.objects.all().values_list('normalizedOverview', 'id', 'title', 'overview', 'poster_path')
        if not movies:
            print("No se encontraron películas en la base de datos.")
            return None, None, None, None

        # Preprocesar descripciones
        moviesData = [{
            'id': movie[1],
            'title': movie[2],
            'overview': movie[3],
            'poster_path': movie[4]
        } for movie in movies]

        # Convertir a DataFrame
        movies_df = pd.DataFrame(moviesData)

        # Cargar BERT
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        model = BertModel.from_pretrained('bert-base-uncased').to('cuda' if torch.cuda.is_available() else 'cpu')

        # Generar o cargar embeddings
        if os.path.exists(BERT_EMBEDDINGS_PATH):
            embeddings = joblib.load(BERT_EMBEDDINGS_PATH)
            print("Embeddings de BERT cargados desde disco.")
        else:
            print("Generando embeddings de BERT...")
            movies_overviews = [movie[0] for movie in movies if isinstance(movie[0], str) and len(movie[0]) > 0]
            embeddings = generate_embeddings_in_batches(movies_overviews, model, tokenizer, batch_size=16)
            joblib.dump(embeddings, BERT_EMBEDDINGS_PATH)

        # Configurar modelo KNN
        if os.path.exists(KNN_MODEL_PATH):
            knn_model = joblib.load(KNN_MODEL_PATH)
            print("Modelo KNN cargado desde disco.")
        else:
            knn_model = NearestNeighbors(n_neighbors=7, metric='cosine', algorithm='auto')
            knn_model.fit(embeddings)
            joblib.dump(knn_model, KNN_MODEL_PATH)
            print("Modelo KNN guardado en disco.")

        print("Datos de películas y modelo KNN cargados y configurados con éxito.")
        return tokenizer, model, knn_model, movies_df
    except Exception as e:
        print(f"Error al cargar los datos de películas o al inicializar el modelo: {e}")
        return None, None, None, None
