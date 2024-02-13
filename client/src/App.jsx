import { useState } from 'react'
import './App.css'
import { Route, Routes,Navigate } from 'react-router-dom';
import Register from './Register';
import VerificationPage from './VerificationPage';
import Login from './Login';

function App() {

  return (
    <>
    <Routes>
    <Route path="/verification" exact="true" element={<VerificationPage/>}/>
    <Route path="/register" exact="true" element={<Register/>}/>
    <Route path="/login" exact="true" element={<Login/>}/>
    </Routes>
    </>
  )
}

export default App
