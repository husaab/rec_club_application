from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyz'

db = SQLAlchemy(app)
admin = Admin(app, name='MicroAdmin', template_mode='bootstrap3')

# Models
class Profiles(db.Model):

    username = db.Column(db.String(20), primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(30), nullable=False)
    balance = db.Column(db.String(30), nullable=False, unique=False)
    attendance = db.Column(db.String(30), nullable=False, unique=False)

    def __init__(self, username, first_name, last_name, password, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.attendance = 0
        self.balance = 10
        self.settings = UserSettings()

    def check_password(self, password):
        return self.password == password
    
    def getBalance(self):
        return self.balance
    
  
    def getUsername(self):
        return self.usernaame
    
class UserSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('profiles.username'), nullable=False)
    user = db.relationship('Profiles', back_populates='settings')
    notifications = db.Column(db.Boolean, default=True)
    theme = db.Column(db.String(20), default='light')

Profiles.settings = db.relationship('UserSettings', back_populates='user', uselist=False, cascade="all, delete-orphan")


admin.add_view(ModelView(Profiles, db.session))

@app.route('/')
def welcome():
    return render_template('login.html', Profiles = Profiles.query.all() )

@app.route('/home')
def home():
    username= session.get('username')
    email = session.get('email')
    balance = session.get('balance')
    return render_template('home.html', username=username, email=email, balance=balance)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = Profiles.query.filter_by(username=request.form['username']).first()
        if user is None or not user.check_password(request.form['password']):
            flash('Invalid Credentials. Please try again.')
        else:
            session['username'] = user.username  
            session['email'] = user.email 
            session['balance'] = user.balance
            session['attendance'] = user.attendance
            flash('You were successfully logged in')
            return redirect(url_for('home'))
    return render_template('login.html')


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
                profile.settings = UserSettings()
                db.session.add(profile)
                db.session.commit()
                return redirect(url_for('login'))
            
    return render_template('signup.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    username = session.get('username')
    if username:
        user = Profiles.query.filter_by(username=username).first()
        if request.method == 'POST':
            # Example: Update theme
            user.settings.theme = request.form['theme']
            db.session.commit()
            flash('Settings updated successfully.')
            return redirect(url_for('settings'))
        return render_template('settings.html', username=username, theme=user.settings.theme)
    else:
        return redirect(url_for('login'))

    
   
@app.route('/balance', methods=['GET', 'POST'])
def balance():
    username= session.get('username')
    email = session.get('email')
    balance = session.get('balance')
    
    if request.method == 'POST':
        request.form['balance']
    
        if username:
            return render_template('balance.html', balance=balance)
        else:
            print("hi")
    
    return redirect(url_for('login'))

"""
@app.route('/attendance')
def attendance():
   def attendance():
    if 'username' not in session:
        flash('Please log in to view attendance.')
        return redirect(url_for('login'))
    
    user = Profiles.query.filter_by(username=session['username']).first()
    if user:
        return render_template('attendance.html', attendance=user.attendance)
    else:
        flash('User not found.')
        return redirect(url_for('login'))
"""



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    