from models import *
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask,  render_template, request, jsonify, redirect, url_for,flash
from sqlalchemy import or_
import os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required,get_jwt_identity
from flask_login import LoginManager, login_user, login_required, logout_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from datetime import timedelta
from form import *

import secrets

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


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200




@app.route('/user_login',methods=['POST'])
def user_login():
    data = request.get_json()
    user_username = data.get('username')
    user_email = data.get('email')
    user_password = data.get('password')

    if not ((user_username or user_email) and user_password):
      return jsonify({'error': 'Invalid JSON data'}), 400  

    user_info = User.query.filter(or_(User.username == user_username, User.email == user_email)).first()

    if user_info and check_password_hash(user_info.password, user_password):
        login_user(user_info)
        access_token = create_access_token(identity=user_info.id, expires_delta=timedelta(hours=24))
        return jsonify({'access_token': access_token,
                        "userid":current_user.id}), 200
    else:
        return jsonify({'message': 'Invalid username,email or password'}), 401




@app.route('/profile')
def userProfile():
    return "Hello"


from Adminroutes import *
from userRegistration import *

if __name__ == '__main__':
    app.run(debug=True, port=5070)
