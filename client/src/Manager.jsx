import React from 'react'
import { Link } from "react-router-dom";


function Manager() {
  return (
    <>
    <h1>Hello</h1>
    <button> <Link to="http://127.0.0.1:5070/admin">Admin</Link></button>
    </>
  )
}

export default Manager