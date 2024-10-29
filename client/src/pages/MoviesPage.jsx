import { Link, useLocation, useNavigate } from "react-router-dom";
import { useState } from "react";
import { MoviesList } from "../components/MoviesList";
import { recommendMovies } from "../api/Task.api";

export function MoviesPage() {
  const location = useLocation();
  const navigate = useNavigate();
  const initialRecommendations = location.state?.recommendations || [];
  const normalizedDesc = location.state?.normalizedDesc;
  
  const batchSize = 3;
  const [recommendations, setRecommendations] = useState(initialRecommendations);
  const [startIndex, setStartIndex] = useState(location.state?.startIndex || 0);

  // Función para cargar el siguiente lote de recomendaciones
  const loadNextBatch = async () => {
    try {
      const newRecommendations = await recommendMovies(normalizedDesc, startIndex + batchSize, batchSize);
      setRecommendations(newRecommendations);
      setStartIndex(startIndex + batchSize);
    } catch (error) {
      console.error("Error al cargar más recomendaciones:", error);
    }
  };

  return (
    <div>
      <header className="pt-24 px-12">
        <div className="container mx-auto px-4">
          <h1 className="text-5xl text-center font-semibold">
            Te recomendamos estas películas
          </h1>
          <div className="container mx-auto pt-4 pb-5 px-4 text-lg text-center">
            <p>
              Esperamos que las disfrutes, si no te sientes satisfecho con las
              recomendaciones prueba otras peliculas similares o intenta de
              nuevo.
            </p>
          </div>
        </div>
      </header>
      <MoviesList recommendations={recommendations} />
      <div className="flex justify-center items-center max-w-xl mx-auto pt-5">
        <button
          onClick={loadNextBatch}
          className="bg-ffpink px-3 py-2 rounded-l-lg mr-0.5 w-52"
        >
          Dame otras opciones
        </button>
        <Link to="/user-welcome">
          <button className="bg-white text-black px-3 py-2 rounded-r-lg w-52">
            Ingresar otra descripción
          </button>
        </Link>
      </div>
    </div>
  );
}
