import { useEffect, useState } from "react";
import { getAllMovies, recommendMovies } from "../api/Task.api";
import { MovieCard } from "./MovieCard";

export function MoviesList({ recommendations }) {
  return (
    <div className="grid grid-cols-3 gap-4 pb-5">
      {recommendations.map((movie) => (
        <MovieCard key={movie.id} movie={movie} />
      ))}
    </div>
  );
}
