import React from 'react';
import './App.css';

import { Switch, Route, Link } from 'react-router-dom';
import Home from './pages/home';
import About from './pages/about';
import Blogs from './pages/blogs';
import Contact from './pages/contact';

const App: React.FC = () => {
  return (
    <div className="App">
      <header className="App-header">
        <nav>
          <li>
            <Link className="App-link" to="/">
              Home
            </Link>{" "}
          </li>
          <li>
            <Link className="App-link" to="/about">
              About
            </Link>{" "}
          </li>
          <li>
            {" "}
            <Link className="App-link" to="/blogs">
              Blogs
            </Link>{" "}
          </li>
          <li>
            <Link className="App-link" to="/contact">
              Contact
            </Link>{" "}
          </li>
        </nav>
      </header>

      <div className="content">
        <div className="container">
          {/* add the container class here */}
          <img
            src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca9d90d7-99fe-427d-b218-7b2662615eee_500x500.png"
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
