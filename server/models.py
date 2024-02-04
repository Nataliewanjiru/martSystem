from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask import render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from marshmallow import Schema, fields, ValidationError
from marshmallow.decorators import  pre_load
from uuid import uuid4
import hashlib
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64


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
        first_letter = email[0].upper()
        # Create an image with a white background
        image_size = (100, 100)
        background_color = (255, 255, 255)
        image = Image.new("RGB", image_size, background_color)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        # Calculate text position to center it in the image
        text_bbox = draw.textbbox((0, 0), first_letter, font=font)
        text_position = (
            (image_size[0] - text_bbox[2] - text_bbox[0]) // 2,
            (image_size[1] - text_bbox[3] - text_bbox[1]) // 2
        )
        # Draw the first letter on the image
        draw.text(text_position, first_letter, font=font, fill=(0, 0, 0))
        # Convert image to base64 string
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        # Return the data URL
        return f"data:image/png;base64,{image_base64}"

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

