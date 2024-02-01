from models import *
from app import app

def create_admin_account():
    # Define a valid admin email address
    admin_email = 'admin@example.com'

    # Use the static method to generate a dynamic profile picture URL
    profile_picture_url = User.generate_profile_picture_url(admin_email)

    # Create the admin user
    admin = User(
        first_name="ad",
        last_name="min",
        username='admin',
        email=admin_email,
        password='admin_password',
        phone_number="0547654",
        role="admin", 
        profile_picture_url=profile_picture_url
    )

    # Add the admin user to the session and commit changes
    db.session.add(admin)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        create_admin_account()