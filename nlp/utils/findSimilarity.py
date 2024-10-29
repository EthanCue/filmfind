from ..apps import NlpConfig

# Función para recomendar películas basadas en la descripción del usuario
def recommend_movies(user_description, start_index=0, batch_size=3):
    # Acceder a los datos y al modelo precargados
    movies_df = NlpConfig.movies_data
    vectorizer = NlpConfig.vectorizer
    knn_model = NlpConfig.knn_model
        
    # Vectorizar solo la descripción del usuario
    user_vector = vectorizer.transform([user_description])
    
    # Buscar los vecinos más cercanos a la descripción del usuario
    distances, indices = knn_model.kneighbors(user_vector, n_neighbors=start_index + batch_size + 1)

    # Seleccionar las películas recomendadas según el índice de inicio y el tamaño del lote
    recommended_movies = movies_df.iloc[indices[0][start_index + 1 : start_index + batch_size + 1]]  # Excluye el índice 0

    return recommended_movies[['id', 'title', 'overview', 'poster_path']].to_dict(orient='records')  # Convertir a dict para un fácil manejo
