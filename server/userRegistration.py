from app import*
from flask_mail import Mail, Message

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'b3655f12d7fcf1'
app.config['MAIL_PASSWORD'] = 'bd0e3e3d02a4ff'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

users = {}

# Function to generate a verification token (JWT)
def generate_verification_token(email):
     token = secrets.token_urlsafe(32)
     return token


def send_verification_email(email, token):
    msg = Message('Verify Your Email', sender='your_email@example.com', recipients=[email])
    verification_url = f'http://localhost:5173/verification?token={token}'
    msg.body = f'Click the following link to verify your email: {verification_url}'
    mail.send(msg)


@app.route('/register' ,methods=['POST'])
def register_user():
  try:
       data = request.get_json() 
       if not data:
           return jsonify({'error': 'Invalid JSON data'}), 400
       
       username = data.get('username')
       first_name = data.get('first_name')
       last_name = data.get('last_name')
       email = data.get('email')
       password = data.get('password')
       phoneNumber=data.get("phoneNumber")
   
       # Check if the username is already taken
       existing_user = User.query.filter_by(username=username).first()
       if existing_user:
           response = {'message': 'Username is already taken. Please choose another one.'}
           return jsonify(response), 400
      
       userProfile=User.generate_profile_picture(email)

       # Create a new user
       hashed_password = generate_password_hash(password, method='sha256')
       new_user = User(first_name=first_name,last_name=last_name,username=username,email=email, password=hashed_password,phone_number=phoneNumber,profile_picture_url=userProfile)
   
       # Add the new user to the database
       db.session.add(new_user)
       db.session.commit()
       
        # For simplicity, consider the email as the user identity
       token = generate_verification_token(email)
       users[email] = {'token': token, 'verified': False}
       send_verification_email(email, token)

        # Create a JWT token for the user
       access_token = create_access_token(identity=email)
       return jsonify(access_token=access_token, message='Verification email sent. Please check your email for instructions.')
  
  except Exception as e:
       print(e)
       response = {"status": False,"msg": str(e)}
       return jsonify(response), 500

@app.route('/verify', methods=['POST'])
@jwt_required()
def verify_email():
    try:
        data = request.get_json()
        token = data.get('token')
        email = get_jwt_identity()
        print("Received JSON Payload:", data)

        if email in users and 'token' in users[email] and users[email]['token'] == token:
            users[email]['verified'] = True
            return jsonify(message=f'Thank you! Your email ({email}) has been verified.')
        else:
            return jsonify(message='Invalid verification token.'), 400
    except KeyError:
        return jsonify(message='Email not found in users.'), 400
    except Exception as e:
        return jsonify(message=f'Error during verification: {str(e)}'), 500