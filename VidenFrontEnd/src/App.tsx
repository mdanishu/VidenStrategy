import React from 'react';
import './App.css';

import { Switch, Route, Link } from 'react-router-dom';
import Home from './pages/home';
import About from './pages/about';
import Blogs from './pages/blogs';
import Contact from './pages/contact';
import ReactGA from 'react-ga';

//for google analytics
const trackingId = "G-X9TQKJ8Q0J"; // Replace with your Google Analytics tracking ID
ReactGA.initialize(trackingId);

import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';



const App: React.FC = () => {
  let location = useLocation();

  //for google analytics
  useEffect(() => {
    // To not send hits during development
    if (process.env.NODE_ENV === 'production') {
      ReactGA.pageview(location.pathname + location.search);
    }
  }, [location]);
//for google analytics above

  return (
    <div className="App">
      <header className="App-header">
        <nav>
          <li>
            <Link className="App-link" to="/">
              <button className="nav-button">Home</button>
            </Link>{" "}
          </li>
          <li>
            <Link className="App-link" to="/about">
            <button className="nav-button">About</button>
            </Link>{" "}
          </li>
          <li>
            {" "}
            <Link className="App-link" to="/blogs">
              <button className="nav-button">Blogs</button>
            </Link>{" "}
          </li>
          <li>
            <Link className="App-link" to="/contact">
              <button className="nav-button">Contact</button>
            </Link>{" "}
          </li>
        </nav>
      </header>

      <div className="content">
        <div className="container">
          {/* add the container class here */}
          <img
            src="Viden Strategy.png"
            alt="test text"
          />
        </div>
      </div>

      {/* Define your routes inside Switch */}
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
        <Route path="/blogs" component={Blogs} />
        <Route path="/contact" component={Contact} />
      </Switch>
    </div>
  );
};

export default App;