function App() {
  return (
    <div style={{ maxWidth: "800px", margin: "40px auto", fontFamily: "Arial, sans-serif" }}>
      <h1>Healthcare Analytics Portfolio</h1>

      <p>
        Welcome to my first React application.
      </p>

      <h2>Skills</h2>
      <ul>
        <li>Python</li>
        <li>Pandas</li>
        <li>SQL</li>
        <li>React</li>
      </ul>

      <button onClick={() => alert("Welcome to my React portfolio!")}>
        Click Me
      </button>
    </div>
  );
}

export default App;