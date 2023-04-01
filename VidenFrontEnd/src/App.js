import React from 'react';
import './App.css';

// import Navbar from './components/Navbar';
import { BrowserRouter, Routes, Route, Switch, Link }
    from 'react-router-dom';
import Home from './pages/home';
import About from './pages/about';
import Blogs from './pages/blogs';
import Contact from './pages/contact';


function App() {
  return (
    <BrowserRouter>
      <div className="App">
          <header className="App-header">
          <nav>
            <li><Link className="App-link" to="/">Home</Link>{" "}</li>
            <li><Link className="App-link" to="/about">About</Link>{" "}</li>
            <li> <Link className="App-link" to="/blogs">Blogs</Link>{" "}</li>
            <li><Link className="App-link" to="/contact">Contact</Link>{" "}</li>
          </nav>
        
        </header>
        
        <body>   
        <div className="container"> {/* add the container class here */} 
          <img src= "https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca9d90d7-99fe-427d-b218-7b2662615eee_500x500.png" alt="test text" />
        </div>
        </body>
        {/* Define your routes inside Routes */}
        <Routes>
          {/* Each Route has a path and an element prop */}
          {/* The path / matches the home page */}
          {/* The element prop specifies what component to render */}
          <Route exact path="/" element={<Home />} />
          {/* The path /about matches the about page */}
          {/* The element prop specifies what component to render */}
          <Route path="/about" element={<About />} />
          {/* The path /blogs matches the blogs page */}
          {/* The element prop specifies what component to render */}
          <Route path="/blogs" element={<Blogs />} />
           {/* The path /signup matches the signup page */}
           {/* The element prop specifies what component to render */}
           <Route path="/contact" element={<Contact />} />
        </Routes>

      </div>
    </BrowserRouter>
  );
}

export default App;