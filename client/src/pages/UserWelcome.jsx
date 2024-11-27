import { UserDesc } from "../components/UserDesc";

export function UserWelcome() {
  return (
    <div>
      <header className="pt-24 px-12">
        <div className="container mx-auto px-4">
          <h1 className="text-5xl text-center font-semibold">
            How does <em className="text-ffpink">FilmFind</em> works?
          </h1>
          <div className="container mx-auto py-12 px-4">
            <div className="text-lg text-center">
              <p>
                Did you known, on average, a person takes about <span className="text-ffpink">24</span> minutes chosing a movie?
              </p>
              <br />
              <p>
                Just describe us what you'd like to see, a movie you don't remember or a topic.
              </p>
              <p>Don´t be afraid of exploring unusual movies!</p>
              <p>
                We will find the <span className="text-ffpink">ideal</span> movie.
              </p>
            </div>
          </div>
        </div>
      </header>
      <UserDesc />
    </div>
  );
}
