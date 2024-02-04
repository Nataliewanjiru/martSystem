from models import *
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask,  render_template, request, jsonify,flash
from sqlalchemy import or_
import datetime,os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required,get_jwt_identity
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate

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



app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to a secure key
# Initialize the JWTManager
jwt = JWTManager(app)



##deals with the login routes
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'login'
#
@app.route('/')
def index():
    return "Welcome to our API"


if __name__ == '__main__':
    app.run(debug=True, port=5070)
