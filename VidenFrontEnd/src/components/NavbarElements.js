// import React and the styled components from NavbarElements.js
import React from 'react';
import { Nav, NavLink, Bars, NavMenu } from './Navbar';

// create a Navbar component
const Navbar = () => {
  return (
    // use the Nav styled component as the container
    <Nav>
      // use the Bars styled component to display a menu icon for smaller screens
      <Bars />
      // use the NavMenu styled component to wrap the navigation links
      <NavMenu>
        // use the NavLink styled component to create the navigation links
        // use the exact attribute to match the exact path
        // use the activeClassName attribute to apply a different style for the active link
        <NavLink to="/" exact activeClassName="active">
          Home
        </NavLink>
        <NavLink to="/about" activeClassName="active">
          About
        </NavLink>
        <NavLink to="/blogs" activeClassName="active">
          Blogs
        </NavLink>
        <NavLink to="/signup" activeClassName="active">
          Sign Up
        </NavLink>
        <NavLink to="/contact" activeClassName="active">
          Contact
        </NavLink>
      </NavMenu>
    </Nav>
  );
};

// export the Navbar component
export default Navbar;