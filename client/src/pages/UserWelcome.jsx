import { UserDesc } from "../components/UserDesc";

export function UserWelcome() {
  return (
    <div>
      <header className="pt-24 px-12">
        <div className="container mx-auto px-4">
          <h1 className="text-5xl text-center font-semibold">
            Comó funciona <em className="text-ffpink">FilmFind</em>
          </h1>
          <div className="container mx-auto py-12 px-4">
            <div className="text-lg text-center">
              <p>
                ¿Sabías que, en promedio, una persona tarda <span className="text-ffpink">24</span> minutos en
                escoger una película?
              </p>
              <p>
                Solo descríbenos lo que se te antoja ver, un estado de ánimo o
                una película cuyo nombre no recuerdes.
              </p>
              <p>Nosotros encontraremos la película <span className="text-ffpink">ideal</span>.</p>
            </div>
          </div>
        </div>
      </header>
      <UserDesc />
    </div>
  );
}
