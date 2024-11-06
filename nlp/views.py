from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer, MovieSerializer
from .models import Movie
from .utils.descProcessing import normalize
from .utils.findSimilarity import recommend_movies
from django.http import JsonResponse

@api_view(['GET'])
def getMovies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# Vista para procesar la descripción del usuario
@api_view(['POST'])
def process_description(request):
    data = request.data  # Accede al JSON enviado en el request
    description = data.get("description", "")
    
    # Verifica si la descripción es válida
    if not description:
        return JsonResponse({"error": "La descripción no debe estar vacía."}, status=400)
    #print("Descripción recibida:", description)

    try:
        # Normalizar el texto
        normalized_description = normalize(description)
        #print("Descripción normalizada:", normalized_description)
    except Exception as e:
        return JsonResponse({"error": f"Ocurrió un error al normalizar la descripción: {str(e)}"}, status=500)

    # Ejemplo de respuesta con la descripción normalizada
    return JsonResponse({"normalized_description": normalized_description})

# Vista para encontrar recomendaciones de películas
@api_view(['POST'])
def find_similarity(request):
    data = request.data
    description = data.get("description", "")
    start_index = data.get("start_index", 0)
    batch_size = data.get("batch_size", 3)

    if not description:
        return JsonResponse({"error": "La descripción no debe estar vacía."}, status=400)

    try:
        recommendations = recommend_movies(description, start_index, batch_size)
    except Exception as e:
        return JsonResponse({"error": f"Ocurrió un error al buscar recomendaciones: {str(e)}"}, status=500)

    return JsonResponse({"recommendations": recommendations})