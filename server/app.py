from models import *
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask,  render_template, request, jsonify, redirect, url_for
from sqlalchemy import or_
import os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required,get_jwt_identity
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from datetime import timedelta

app = Flask(__name__)
CORS(app)

#Load environment variables from .env
load_dotenv()

SECRET_KEY = os.environ.get("secretkey")
DATABASE_URL = os.environ.get("dburl")

# Access environment variables using config()
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#initialize and configure the Flask-Admin extension
admin.init_app(app)

migrate = Migrate(app, db)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.init_app(app)



app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to a secure key
# Initialize the JWTManager
jwt = JWTManager(app)




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('login.html')

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
   
       response = {'message': 'Registration successful!'}
       return jsonify(response)
  except Exception as e:
    print(e)
    response = {"status": False,"msg": str(e)}
    return jsonify(response), 500


@app.route('/login',methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not ((username or email) and password):
      return jsonify({'error': 'Invalid JSON data'}), 400  

    user = User.query.filter(or_(User.username == username, User.email == email)).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=24))
        return jsonify({'access_token': access_token,
                        "userid":current_user.id}), 200
    else:
        return jsonify({'message': 'Invalid username,email or password'}), 401



@app.route('/manager_login', methods=['GET', 'POST'])
def manager_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check user credentials
        user = User.query.filter_by(username=username, password=password).first()

        if user and user.role == 'admin':
            # Login successful for manager
            # Redirect to the manager dashboard or AdminView
            return redirect(url_for('admin.index'))

    return render_template('admin_access_denied.html')

@app.route('/admin/')
def admin_dashboard():
    return "Hello"


@app.route('/profile')
def userProfile():
    return LoginSchema




if __name__ == '__main__':
    app.run(debug=True, port=5070)
