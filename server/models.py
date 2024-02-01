from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin
from marshmallow import Schema, fields, ValidationError

#Initiates the database
db = SQLAlchemy()
#Initiates the admin side
admin = Admin()

Base = declarative_base()
metadata = Base.metadata

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String())
    
    def is_authenticated(self):
        return True
        
    def is_active(self):
        """True if user account is active."""
        return True

    def is_anonymous(self):
        """False for users. True for anonymous users."""
        return False

    def get_id(self):
        """Returns the email field to satisfy Flask-Login's requirements."""
        # `get_id` typically returns a unicode string representing the user ID.
        return self.username


class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    @postprocessor
    def process_data(schema, data):
        if not data['password']:
            raise ValidationError('Password cannot be empty')


login_schema = LoginSchema()

@admin.register(User)
class UsersAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ['username',]
    list_display = ('username', 'is_staff', 'date_joined')  

