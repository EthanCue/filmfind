import { useForm } from "react-hook-form";
import { useNavigate, useParams } from "react-router-dom";
import { createUserDesc, recommendMovies } from "../api/Task.api";
import { toast } from "react-hot-toast";

export function UserDesc() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const navigate = useNavigate();
  const batchSize = 3;

  const onSubmit = handleSubmit(async (data) => {
    try {
      const response = await createUserDesc(data);
      const normalizedDesc = response.normalized_description;
      toast.success("Descripcion creada", {
        position: "bottom-right",
        style: { background: "#101010", color: "#fff" },
      });
      try {
        const recommendations = await recommendMovies(
          normalizedDesc,
          0,
          batchSize
        );
        toast.success("Recomendaciones creadas", {
          position: "bottom-right",
          style: { background: "#101010", color: "#fff" },
        });
        console.log(recommendations);
        navigate("/movies-recomendations", {
          state: { recommendations, normalizedDesc, startIndex: 0 },
        });
      } catch (error) {
        toast.error("Error al buscar recomendaciones");
      }
    } catch (error) {
      toast.error("Error al procesar la descripción");
    }
  });

  return (
    <div className="max-w-xl mx-auto pt-5">
      <form onSubmit={onSubmit}>
        <textarea
          rows="7"
          placeholder="Escribe aqui..."
          {...register("description", { required: true })}
          className="bg-gray-50 p-3 rounded-lg block w-full mb-3 text-neutral-700"
        ></textarea>
        {errors.description && <span>Ingresa una descrición</span>}
        <div className="flex justify-center">
          <button className="bg-ffpink p-3 rounded-full w-1/2">Buscar</button>
        </div>
      </form>
    </div>
  );
}
