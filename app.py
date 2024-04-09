from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Here, insert code to handle the sign-up form submission.
        # This could involve validating the form data, checking if the
        # username is already taken, and storing the new user's information
        # in the database.
        return redirect(url_for('login'))
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
    