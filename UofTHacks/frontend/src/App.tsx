
import fire from "./fire.jpeg";
import "animate.css";

function App() {
  return (
    <div className="relative min-h-screen bg-gradient-to-r from-orange-600 via-red-600 to-yellow-500 flex items-center justify-center overflow-hidden">
      <div
        className="absolute inset-0 bg-cover bg-center opacity-40"
        style={{
          backgroundImage:
            'url("https://source.unsplash.com/1600x900/?wildfire,fire")',
        }}
      ></div>
      <div className="relative z-10 text-center text-white px-8 py-12 max-w-4xl w-full">
        <center>
          <img src={fire} className="ml-5 h-52" />
        </center>
        <h1 className="text-black text-6xl font-extrabold bg-clip-text bg-gradient-to-r mb-6 animate__animated animate__fadeIn animate__delay-1s">
          Project Wildfire
        </h1>
        <p className="text-xl mb-8 opacity-90 animate__animated animate__fadeIn animate__delay-2s">
          Ignite your passion. Join the wildfire of collaboration, where ideas
          spark and innovation blazes. Let’s create something extraordinary.
        </p>

        <div className="flex justify-center gap-8 animate__animated animate__fadeIn animate__delay-3s">
          <a
            href="https://www.youtube.com/watch?v=xvFZjo5PgG0"
            className="bg-transparent border-4 border-white text-white py-3 px-10 rounded-full text-2xl transition duration-300 transform hover:bg-white hover:text-red-600 hover:scale-110"
          >
            View Map
          </a>
        </div>
      </div>
    </div>
  );
}

export default App;
