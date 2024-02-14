import React, { useState, useEffect } from 'react';
import {Link, useNavigate } from "react-router-dom";

function VerificationPage() {
  const [tokenInUrl, setTokenInUrl] = useState(false);
  const [loading, setLoading] = useState(true);
  const[message,setMessage] =useState(<div><h2>Please check your email</h2></div>)

  useEffect(() => {
    // Extract token from URL
    const urlParams = new URLSearchParams(window.location.search);
    const token = urlParams.get('token');
   if (token) {
    fetch('http://127.0.0.1:5070/verify', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ token: token }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.message === 'Invalid verification token.') {
          setMessage(<div><h2>Token verification failed</h2></div>)
          console.log('Token verification failed');
        } else if(data.message === 'Invalid request. Token is required.') {
          setMessage(<div><h2>Token verification failed</h2></div>)
          console.log('Token verification failed');
        }else{
          setMessage(<div><h2>Email verification complete.</h2><p><Link to="/login">Proceed to login</Link></p></div>)
        }
      })
      .catch(error => {
        console.error('Error:', error);
      })
      .finally(() => {
        setLoading(false);
      });
  } else {
    setLoading(false);
  }
  
  }, []);
 
 
  return (
    <>
      {loading && <p>Loading...</p>}
      {!loading && message}
    </>
  );
}

export default VerificationPage;
