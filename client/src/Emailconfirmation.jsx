import React, { useEffect } from 'react';

async function Emailconfirmation({ email }) {
    const url = 'https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send';

    const options = {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-RapidAPI-Key': 'dd91de6d20mshc3665b7aac50046p1b5f16jsncfbcdb2c653f',
            'X-RapidAPI-Host': 'rapidprod-sendgrid-v1.p.rapidapi.com'
        },
        body: JSON.stringify({
            personalizations: [
                {
                    to: [
                        {
                            email: email
                        }
                    ],
                    subject: 'Email Verification'
                }
            ],
            from: {
                email: 'natalieamazon16@example.com' // Replace with your sender email address
            },
            content: [
                {
                    type: 'text/plain',
                    value: 'Hello, please verify your email!' // Customize the email body
                }
            ]
        })
    };

    try {
        const response = await fetch(url, options);
        const result = await response.text();
        console.log(result);
    } catch (error) {
        console.error(error);
    }

    return <div>Hello</div>;
}

export default Emailconfirmation;
