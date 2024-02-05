from app import *

#Loads the user_loader
@login_manager.user_loader
def load_user(id):
   return User.query.get(id)

#Route for logging in as an Admin
@app.route('/')
def index():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

#Logic for Admin after logging in
@app.route('/manager_login', methods=['GET', 'POST'])
def manager_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))  

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check user credentials
        user = User.query.filter_by(username=username, password=password).first()

        if user and user.role == 'admin':
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('admin.index'))  # Redirect to admin dashboard after successful login

        flash('Login failed. Please check your username and password.', 'danger')

    return render_template('admin_access_denied.html')

#Logout function for the admin
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
