import React from 'react';
import PropTypes from 'prop-types';
import Auth from '../Auth/Auth';
import { Link } from 'react-router';
import './Base.css';

const Base = ({ children }) => (
  <div>
    <nav className="nav-bar indigo lighten-1">
      <div className="nav-wrapper">
        <a href="/" className="brand-logo"> &nbsp; Stock Board &nbsp; Author: Huiqing Dai</a>
        <ul id="nav-mobile" className="right">
          {Auth.isUserAuthenticated() ?
            (<div>
               <li>{Auth.getEmail()}</li>
               <li><Link to="/logout">Log out</Link></li>
             </div>)
             :
            (<div>
               <li><Link to="/login">Log in</Link></li>
               <li><Link to="/signup">Sign up</Link></li>
             </div>)
          }
        </ul>
      </div>
    </nav>
    <br/>
    {children}
  </div>
);

Base.propTypes = {
  children: PropTypes.object.isRequired
};

export default Base;