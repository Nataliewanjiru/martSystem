import React from 'react'
import { createUserWithEmailAndPassword, sendEmailVerification, signInWithPopup, updateProfile } from "firebase/auth";


function Emailconfirmation({email}) {

    const url = 'https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send';
const options = {
	method: 'POST',
	headers: {
		'content-type': 'application/json',
		'X-RapidAPI-Key': 'dd91de6d20mshc3665b7aac50046p1b5f16jsncfbcdb2c653f',
		'X-RapidAPI-Host': 'rapidprod-sendgrid-v1.p.rapidapi.com'
	},
	body: {
		personalizations: [
			{
				to: [
					{
						email: email
					}
				],
				subject: 'Registration successful!'
			}
		],
		from: {
			email: 'martsystem@example.com'
		},
		content: [
			{
				type: 'text/plain',
				value: "You're registration was successful login to explore the services.!"
			}
		]
	}
};

try {
	const response = fetch(url, options);
	const result =  response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}
  return (
    <div>Emailconfirmation</div>
  )
}

export default Emailconfirmation