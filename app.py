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

if __name__ == '__main__':
    app.run(debug=True)
    