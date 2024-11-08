from ..apps import NlpConfig

# Función para recomendar películas basadas en la descripción del usuario
def recommend_movies(user_description, start_index=0, batch_size=3):
    # Asegurarse de que el vectorizador y el modelo estén disponibles
    if NlpConfig.vectorizer is None or NlpConfig.knn_model is None:
        return {"error": "El vectorizador o el modelo KNN no están disponibles. Inténtalo de nuevo más tarde."}

    # Acceder a los datos y al modelo precargados
    movies_df = NlpConfig.moviesData
    vectorizer = NlpConfig.vectorizer
    knn_model = NlpConfig.knn_model

    if NlpConfig.moviesData is None or NlpConfig.moviesData.empty:
        print("Error: Los datos de las películas no se han cargado correctamente.")
    else:
        print(f"Datos de películas cargados correctamente: {len(NlpConfig.moviesData)} películas.")

    if movies_df is None or movies_df.empty:
        return {"error": "No se encontraron datos de películas. Intenta de nuevo más tarde."}


    # Vectorizar solo la descripción del usuario
    user_vector = vectorizer.transform([user_description])

    try:
        # Buscar los vecinos más cercanos a la descripción del usuario
        distances, indices = knn_model.kneighbors(user_vector, n_neighbors=start_index + batch_size + 1)

        # Seleccionar las películas recomendadas según el índice de inicio y el tamaño del lote
        recommended_movies = movies_df.iloc[indices[0][start_index + 1 : start_index + batch_size + 1]]  # Excluye el índice 0

        return recommended_movies[['id', 'title', 'overview', 'poster_path']].to_dict(orient='records')  # Convertir a dict para un fácil manejo
    except Exception as e:
        # Manejo de errores si la recomendación falla
        return {"error": f"Ocurrió un error al generar las recomendaciones: {str(e)}"}