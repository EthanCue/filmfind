from ..apps import NlpConfig
from .loadData import generate_embeddings_in_batches

def recommend_movies(user_description, start_index=0, batch_size=3):
    # Asegurarse de que el vectorizador y el modelo estén disponibles
    if NlpConfig.tokenizer is None or NlpConfig.model is None or NlpConfig.knn_model is None:
        return {"error": "El modelo BERT o el modelo KNN no están disponibles. Inténtalo de nuevo más tarde."}

    # Acceder a los datos y al modelo precargados
    movies_df = NlpConfig.moviesData
    tokenizer = NlpConfig.tokenizer
    model = NlpConfig.model
    knn_model = NlpConfig.knn_model

    if movies_df is None or movies_df.empty:
        return {"error": "No se encontraron datos de películas. Intenta de nuevo más tarde."}

    # Vectorizar solo la descripción del usuario
    user_vector = generate_embeddings_in_batches([user_description], model, tokenizer, batch_size=1)[0]

    try:
        # Buscar los vecinos más cercanos a la descripción del usuario
        _, indices = knn_model.kneighbors([user_vector], n_neighbors=start_index + batch_size + 1)

        # Seleccionar las películas recomendadas según el índice de inicio y el tamaño del lote
        recommended_movies = movies_df.iloc[indices[0][start_index + 1 : start_index + batch_size + 1]]  # Excluye el índice 0

        return recommended_movies[['id', 'title', 'overview', 'poster_path']].to_dict(orient='records')  # Convertir a dict para un fácil manejo
    except Exception as e:
        # Manejo de errores si la recomendación falla
        return {"error": f"Ocurrió un error al generar las recomendaciones: {str(e)}"}