from app import *
from datetime import timedelta,datetime

#Routes for login
@app.route('/userlogin', methods=['POST'])
def userlogin():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not (username or email) or not password:
     return jsonify({'error': 'Invalid JSON data'}), 400

    if username:
      user = User.query.filter(User.username.ilike(username)).first()
    elif email:
      user = User.query.filter(User.email.ilike(email)).first()


    if user and user.is_active and check_password_hash(user.password, password):
        login_user(user)
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=24))

        # Set the access_token as a cookie
        response = make_response(jsonify({'access_token': access_token, 'userid': current_user.id}))
        response.set_cookie('access_token_cookie', access_token, expires=datetime.utcnow() + timedelta(hours=24), httponly=True)
        return response
    else:
        return jsonify({'message': 'Invalid username,email or password'}), 401


# Route for profile
@app.route('/userprofile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()  
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    user_schema = User.LoginSchema()

    # Serialize the user's information
    serialized_user, _ = user_schema.dump(user)

    return jsonify(serialized_user), 200


# Route for logout
@app.route('/userlogout', methods=['GET'])
@jwt_required()
def userlogout():
    logout_user()
    return 'Logged out successfully'