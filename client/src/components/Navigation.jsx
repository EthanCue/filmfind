import { Link } from "react-router-dom";

export function Navigation() {
  return (
    <div className="flex justify-between py-3">
      <Link to="/tasks">
        <h1 className="font-bold text-3xl mb-4">Task App</h1>
      </Link>
      <Link to="/tasks-create">
        <button className="bg-ffpink px-3 py-2 rounded-lg">CreateTask</button>
      </Link>
      <Link to="/user-welcome">
        <button className="bg-ffpink px-3 py-2 rounded-lg">UserWelcome</button>
      </Link>
      <Link to="/movies-recomendations">
        <button className="bg-ffpink px-3 py-2 rounded-lg">MoviesPage</button>
      </Link>
    </div>
  );
}
