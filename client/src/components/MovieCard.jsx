import PropTypes from 'prop-types';

export function MovieCard({ movie }) {
  return (
    <div className="max-w-sm bg-neutral-800 rounded-xl hover:bg-neutral-700 hover:cursor-pointer">
      <div className="flex justify-center">
        <img
          className="rounded-t-lg"
          src={
            movie.poster_path
              ? `https://image.tmdb.org/t/p/w300_and_h450_bestv2/${movie.poster_path}`
              : "https://via.placeholder.com/300"
          }
          alt={movie.title}
        />
      </div>
      <div className="p-5">
        <h5 className="mb-2 text-2xl font-semibold uppercase tracking-tight">
          {movie.title}
        </h5>
        <p className="mb-3 text-stone-300 max-h-32 overflow-y-auto">
          {movie.overview}
        </p>
      </div>
    </div>
  );
}

MovieCard.propTypes = {
  movie: PropTypes.shape({
    poster_path: PropTypes.string,
    title: PropTypes.string.isRequired,
    overview: PropTypes.string,
  }).isRequired,
};