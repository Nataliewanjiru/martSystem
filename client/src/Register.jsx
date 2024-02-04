import React, { useState } from "react";
import axios from "axios";
import {Link, useNavigate } from "react-router-dom";
import swal from 'sweetalert';




const Register = () => {
    const [formData, setFormData] = useState({
        first_name: "",
        last_name: "",
        username:"",
        email: "",
        password: "",
        phoneNumber:"",
    });

    const { first_name, last_name,username, email, password, phoneNumber} = formData;
    
    let navigate = useNavigate()

    const signUp = async (e) => {
        e.preventDefault();
        
        try {
            if(first_name,last_name,username,email,password,phoneNumber){
            const response = await axios.post("http://127.0.0.1:5070/register", formData);
            swal({
                title: 'Success',
                text: 'User created successfully',
                icon: 'success',
              });
                    
                    
            // Clear the form inputs after submission
            setFormData({
                first_name: "",
                last_name: "",
                username:"",
                email: "",
                password: "",
            });
            navigate("/login")
        }
        else{
            swal({
                title: 'Error',
                text: 'Please fill in all the inputs',
                icon: 'error',
              });
             }

        } catch (error) {
            console.error(error.response.data);
        }   
};

    return (
        <div className="signUpBody">
       
        <div className="sign-up-parent">
        <div className="sign-up-container">
        <h1>Create Account</h1>
            <form onSubmit={signUp}>
                <input type="text" placeholder="Enter your first name.." value={first_name} onChange={(e) =>setFormData({ ...formData, first_name: e.target.value })}/>
                <input type="text" placeholder="Enter your last name.." value={last_name} onChange={(e) =>setFormData({ ...formData, last_name: e.target.value })}/>
                 <input type="text" placeholder="Enter your username.." value={username} onChange={(e) =>setFormData({ ...formData, username: e.target.value })}/>
                 <input type="text" placeholder="Enter your phoneNumber" value={phoneNumber} onChange={(e) =>setFormData({ ...formData, phoneNumber: e.target.value })}/>
                <input type="email" placeholder="Enter your email.." value={email} onChange={(e) => setFormData({ ...formData, email: e.target.value }) }/>
                <input type="password" placeholder="Enter your password" value={password} onChange={(e) =>setFormData({ ...formData, password: e.target.value })}/>
                <button type="submit">Sign Up</button>
            </form>
            <button>
            <Link to="/login">Already have an account</Link>
            </button>
        </div>
        </div>
        </div>
    );
};

export default Register;