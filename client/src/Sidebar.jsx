import React from 'react'
import { Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom'
import './index.css'

function Sidebar() {
    return (
        <Nav className="flex-column">
          <Link to='findMart' className="nav-link">Find Mart</Link>
          <Link to='activities' className="nav-link">Activities</Link>
          <Link to='payments' className="nav-link">Payments</Link>
          <Link to='profile' className="nav-link">Profile</Link>
          <Link to='helpCenter' className="nav-link">Help Center</Link>
        </Nav>
      );
}

export default Sidebar