import axios from "axios";

const taskApi = axios.create({
  baseURL: "http://127.0.0.1:8000/tasks/api/v1/",
});

export const getAllMovies = () => taskApi.get("http://127.0.0.1:8000/tasks/api/v1/getMovies/");

export const createUserDesc = async (description) => {
  try {
    const response = await taskApi.post(
      "http://127.0.0.1:8000/tasks/api/v1/process-description/",
      description
    );
    return response.data;
  } catch (error) {
    console.error("Error al enviar la descripción:", error);
    throw error;
  }
};

export const recommendMovies = async (description, startIndex = 0, batchSize = 3) => {
  try {
    const response = await axios.post("http://127.0.0.1:8000/tasks/api/v1/recommend-movies/", {
      description,
      start_index: startIndex,
      batch_size: batchSize,
    });
    return response.data.recommendations;
  } catch (error) {
    console.error("Error al obtener recomendaciones:", error);
    throw error;
  }
};
