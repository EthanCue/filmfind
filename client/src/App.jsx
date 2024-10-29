import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { MoviesPage } from "./pages/MoviesPage";
import { UserDesc } from "./components/UserDesc";
import { UserWelcome } from "./pages/UserWelcome";
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <BrowserRouter>
      <div className="container mx-auto">
        <Routes>
          <Route path="/" element={<Navigate to="/user-welcome" />} />
          <Route path="/user-desc" element={<UserDesc />} />
          <Route path="/user-welcome" element={<UserWelcome />} />
          <Route path="/movies-recomendations" element={<MoviesPage />} />
        </Routes>
        <Toaster />
      </div>
    </BrowserRouter>
  );
}

export default App;
