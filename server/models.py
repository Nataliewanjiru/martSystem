from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin

#Initiates the database
db = SQLAlchemy()
#Initiates the admin side
admin = Admin()

Base = declarative_base()
metadata = Base.metadata
