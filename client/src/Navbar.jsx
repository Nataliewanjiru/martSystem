import React from 'react'
import { Navbar, Container, Row, Col, Dropdown } from 'react-bootstrap';
import "./index.css"

function Appnavbar() {
    return (
        <Navbar bg="light" expand="lg" className='nav'>
          <Container className='nav-container'>
            <Row className="w-100">
              <Col xs={6} md={10} className="d-flex align-items-center">
                <Navbar.Brand className="ml-auto">WashyWonders</Navbar.Brand>
              </Col>
              <Col xs={6} md={2} className="d-flex justify-content-end align-items-center">
                <img src="" alt="User image" className="mr-2" />
                <Dropdown>
                  <Dropdown.Toggle variant="success" id="dropdown-basic" drop="start">
                    <span className="dash-container">
                      <span className="dash"></span>
                      <span className="dash"></span>
                      <span className="dash"></span>
                    </span>
                  </Dropdown.Toggle>
                  <Dropdown.Menu>
                    <Dropdown.Item href="#/action-1">Manage Account</Dropdown.Item>
                    <Dropdown.Item href="#/action-2">Settings</Dropdown.Item>
                  </Dropdown.Menu>
                </Dropdown>
              </Col>
            </Row>
          </Container>
        </Navbar>
      );
}

export default Appnavbar