from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyz'

db = SQLAlchemy(app)

# Models
class Profiles(db.Model):

    username = db.Column(db.String(20), primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(30), nullable=False)
 
    # repr method represents how one object of this datatable
    # will look like
    #def __repr__(self):
    #    return f"Username: {self.username} Name : {self.first_name, self.last_name}, Email: {self.email}"

    def __init__(self, username, first_name, last_name, password, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def check_password(self, password):
        return self.password == password

@app.route('/')
def home():
    return render_template('home.html', Profiles = Profiles.query.all() )

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = Profiles.query.filter_by(username=request.form['username']).first()
        if username is None or not username.check_password(request.form['password']):
            error = 'Invalid Credentials. Please try again.'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if not request.form['new_username'] or not request.form['new_password'] or not request.form['confirm_password'] or not request.form['email']:
            flash("Please fill out all the required fields", "error")
        else:
            existing_profile = Profiles.query.filter_by(username=request.form['new_username']).first()
            if existing_profile:
                flash("User already exists.")
            else:
                profile = Profiles(request.form['new_username'], request.form['first_name'], request.form['last_name'], request.form['new_password'], request.form['email'])
                db.session.add(profile)
                db.session.commit()
        # Here, insert code to handle the sign-up form submission.
        # This could involve validating the form data, checking if the
        # username is already taken, and storing the new user's information
        # in the database.
                return redirect(url_for('login'))
    return render_template('signup.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    