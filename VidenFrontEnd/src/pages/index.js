// import React from 'react';

// const Home = () => {
// return (
// 	<div>
// 	<h1>Welcome to Danish's first website</h1>
// 	</div>
// );
// };

// export default Home;

import React from 'react';
import ReactDOM from 'react-dom';
import './Pages.css';
import App from './App';
import { BrowserRouter } from "react-router-dom";

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);