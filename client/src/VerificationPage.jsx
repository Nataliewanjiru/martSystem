import React, { useState, useEffect } from 'react';

function VerificationPage() {
  const [tokenInUrl, setTokenInUrl] = useState(false);
  const [loading, setLoading] = useState(true);
  const[message,setMessage] =useState("")

  useEffect(() => {
    // Extract token from URL
    const urlParams = new URLSearchParams(window.location.search);
    const token = urlParams.get('token');
   console.log(token);
    if (token) {
      fetch('http://127.0.0.1:5070/verify', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ token: token }),
      })
        .then(response => response.json())
        .then(data => {
          if (data.message === 'Invalid token.') {
            console.log('Token verification failed');
        }else {
            console.log(data.message);
            setTokenInUrl(true);
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
      {!loading && tokenInUrl ? <p>Hello</p> : <p>Bye</p>}
    </>
  );
}

export default VerificationPage;
