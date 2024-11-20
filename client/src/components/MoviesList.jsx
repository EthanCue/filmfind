import PropTypes from 'prop-types';
import { MovieCard } from "./MovieCard";

export function MoviesList({ recommendations }) {
  console.log(recommendations);
  return (
    <div className="grid grid-cols-3 gap-4 pb-5">
      {recommendations.map((movie) => (
        <MovieCard key={movie.id} movie={movie} />
      ))}
    </div>
  );
}

MoviesList.propTypes = {
  recommendations: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
      poster_path: PropTypes.string,
      title: PropTypes.string.isRequired,
      overview: PropTypes.string,
    })
  ).isRequired,
};
