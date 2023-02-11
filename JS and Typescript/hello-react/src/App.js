import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          This is Viden Strategy's first app!
        </p>
        <a
          className="App-link"
          href="videnstrategy.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          Go to Viden Blog
        </a>
      </header>
    </div>
  );
}

export default App;
