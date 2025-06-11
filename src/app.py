#app.py
from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from werkzeug.security import generate_password_hash, check_password_hash
 
app = Flask(__name__)
app.secret_key = 'cairocoders-ednalan'
 
DB_HOST = "dpg-d11hun8gjchc7381sprg-a.oregon-postgres.render.com"
DB_NAME = "javafacilito_db"
DB_USER = "admin"
DB_PASS = "gVgbaGYJb6C0Z9GPjnw39Xf26PkfhTXK"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/conditionals')
def conditionals():
    return render_template('conditionals.html')

@app.route('/cicles')
def cicles():
    return render_template('cicles.html')

@app.route('/arrays')
def arrays():
    return render_template('arrays.html')

@app.route('/functions')
def functions():
    return render_template('functions.html')

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print(password)
        try:
            # Check if account exists using MySQL
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            # Fetch one record and return result
            account = cursor.fetchone()
        except Exception as e:
            conn.rollback()
            flash('Error while checking credentials. Please try again.')
            print(f"Login error: {e}")
            return render_template('login.html')
 
        if account:
            password_rs = account['password']
            print(password_rs)
            # If account exists in users table in out database
            if check_password_hash(password_rs, password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                # Redirect to home page
                return redirect(url_for('home'))
            else:
                # Account doesnt exist or username/password incorrect
                flash('Incorrect username/password')
        else:
            # Account doesnt exist or username/password incorrect
            flash('Incorrect username/password')
 
    return render_template('login.html')
  
@app.route('/register', methods=['GET', 'POST'])
def register():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
 
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
    
        _hashed_password = generate_password_hash(password)
    
        try:
            #Check if account exists using MySQL
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            account = cursor.fetchone()
            print(account)
            # If account exists show error and validation checks
        except Exception as e:
            conn.rollback()
            flash('Error while checking credentials. Please try again.')
            print(f"Login error: {e}")
            return render_template('login.html')
        
        if account:
            flash('Account already exists!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!')
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('Username must contain only characters and numbers!')
        elif not username or not password or not email:
            flash('Please fill out the form!')
        else:
            try:
                # Account doesnt exists and the form data is valid, now insert new account into users table
                cursor.execute("INSERT INTO users (fullname, username, password, email) VALUES (%s,%s,%s,%s)", (fullname, username, _hashed_password, email))
                conn.commit()
                flash('You have successfully registered!')
            except Exception as e:
                conn.rollback()
                flash('Error during registration.')
                print(f"Register INSERT error: {e}")
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        flash('Please fill out the form!')
    # Show registration form with message (if any)
    return render_template('register.html')
   
   
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))
  
@app.route('/profile')
def profile(): 
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    # Check if user is loggedin
    if 'loggedin' in session:
        try:
            cursor.execute('SELECT * FROM users WHERE id = %s', [session['id']])
            account = cursor.fetchone()
            # Show the profile page with account info
            return render_template('profile.html', account=account)
        except Exception as e:
            conn.rollback()
            flash("Couldn't load profile.")
            print(f"Profile error: {e}")
            return redirect(url_for('login'))
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))
 
if __name__ == "__main__":
    app.run(debug=True)