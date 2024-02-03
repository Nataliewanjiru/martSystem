from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask import render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from marshmallow import Schema, fields, ValidationError
from marshmallow.decorators import  pre_load
from uuid import uuid4
import hashlib
from pydenticon import generate_identicon



#Initiates the database
db = SQLAlchemy()
#Initiates the admin side
admin = Admin()

Base = declarative_base()
metadata = Base.metadata

def get_uuid():
    return uuid4().hex


#User info
class User(db.Model,Base):
    __tablename__ = 'users'
    id = db.Column(db.String(36), primary_key=True, unique=True, default=lambda: str(uuid4()))
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(345), unique=True, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    profile_picture_url = db.Column(db.String, nullable=True, default="")  
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='user')


    def __repr__(self):
        return f"<User {self.username}>"
    
    @staticmethod
    def generate_profile_picture(email):
        # Take only the first character of the email
        email_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()

        # Construct the Gravatar URL
        gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}"
    
        return gravatar_url
     

    def is_authenticated(self):
        return True
        
    def is_active(self):
        """True if user account is active."""
        return True

    def is_anonymous(self):
        """True for users. False for anonymous users."""
        return False

    def get_id(self):
        """Returns the email field to satisfy Flask-Login's requirements."""
        # `get_id` typically returns a unicode string representing the user ID.
        return self.username


class LoginSchema(Schema):
    id = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    username = fields.Str(required=True)
    phone_number=fields.Str(required=True)
    profile_picture_url = fields.Str(required=True)

  
    @pre_load
    def process_data(self, data, **kwargs):
        required_fields = ['first_name', 'last_name', 'email', 'username', 'password']
        missing_fields = [field for field in required_fields if field not in data or not data[field]]

        if missing_fields:
            raise ValidationError(f"Missing required fields: {', '.join(missing_fields)}")

        if not data['password']:
            raise ValidationError('Password cannot be empty')

        if not data['email']:
            raise ValidationError('Email cannot be empty')


login_schema = LoginSchema()


# Add User model to the admin panel
admin.add_view(ModelView(User,db.session))

