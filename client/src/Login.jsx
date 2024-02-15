import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import swal from 'sweetalert';



function Login({ onLogin }) {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const signIn = async (e) => {
    e.preventDefault();
    try {
      if (email && username && password) {
        // Perform your authentication logic here...
        const response = await axios.post("http://127.0.0.1:5070/userlogin", {
          email,
          username,
          password
        });



        // Clear form fields after successful login
        setEmail("");
        setUsername("");
        setPassword("");


        swal({
          title: 'Success',
          text: 'Logged in successfully',
          icon: 'success',
        });

        // Navigate to the desired page after successful login
        navigate("/");
      } else {
        swal({
          title: 'Error',
          text: 'Please fill in all the inputs',
          icon: 'error',
        });
      }
    } catch (error) {
      swal({
        title: 'Error',
        text: 'User not found',
        icon: 'error',
      });
    }
  };

  return (
    <div className="signInBody">
      <div className="sign-in-parent">
        <div className="sign-in-container">
          <h1>Log In</h1>
          <p>Login.Please fill in all the inputs.</p>
          <form onSubmit={signIn}>
            <input type="email" placeholder="Enter your email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <input type="text" placeholder="Enter your username" value={username} onChange={(e) => setUsername(e.target.value)} />
            <input type="password" placeholder="Enter your password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button type="submit">Log In</button>
          </form>
          <button><Link to="/signup">Don't have an account</Link></button>
        </div>
      </div>
    </div>
  );
}

export default Login;