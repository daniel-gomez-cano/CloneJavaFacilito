#app.py
from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re
import os
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
 
app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'cairocoders-ednalan'

# FUNCIÓN PARA SUBIR ARCHIVOS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'profile_pics')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ✅ Crear carpeta si no existe (para evitar el error)
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

 
DB_HOST = "dpg-d11hun8gjchc7381sprg-a.oregon-postgres.render.com"
DB_NAME = "javafacilito_db"
DB_USER = "admin"
DB_PASS = "gVgbaGYJb6C0Z9GPjnw39Xf26PkfhTXK"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/comments', methods=['GET', 'POST'])
def comments():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if 'loggedin' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        content = request.form['content']
        if content.strip():  # Validación simple
            cursor.execute(
                "INSERT INTO comments (user_id, content) VALUES (%s, %s)",
                (session['id'], content)
            )
            conn.commit()
            flash('Comentario enviado!')

    # Cargar todos los comentarios
    cursor.execute('''
        SELECT c.content, c.created_at, u.username, u.profile_image
        FROM comments c
        JOIN users u ON c.user_id = u.id
        ORDER BY c.created_at DESC
    ''')
    comments = cursor.fetchall()

    return render_template('comments.html', comments=comments)

@app.route('/data', methods=['GET', 'POST'])
def data():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if 'loggedin' not in session:
        return redirect(url_for('login'))

    module_name = 'data'  # << este es el nombre que se guarda en el campo 'module'

    if request.method == 'POST':
        content = request.form['content']
        if content.strip():
            cursor.execute(
                "INSERT INTO comments (user_id, content, module) VALUES (%s, %s, %s)",
                (session['id'], content, module_name)
            )
            conn.commit()
            flash('Comentario enviado!')

    # Cargar comentarios SOLO para este módulo
    cursor.execute('''
        SELECT c.content, c.created_at, u.username, u.profile_image
        FROM comments c
        JOIN users u ON c.user_id = u.id
        WHERE c.module = %s
        ORDER BY c.created_at DESC
    ''', (module_name,))
    comments = cursor.fetchall()

    return render_template('data.html', comments=comments)

# Conditionals
@app.route('/conditionals', methods=['GET', 'POST'])
def conditionals():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if 'loggedin' not in session:
        return redirect(url_for('login'))

    module_name = 'conditionals'

    if request.method == 'POST':
        content = request.form['content']
        if content.strip():
            cursor.execute(
                "INSERT INTO comments (user_id, content, module) VALUES (%s, %s, %s)",
                (session['id'], content, module_name)
            )
            conn.commit()
            flash('Comentario enviado!')

    cursor.execute('''
        SELECT c.content, c.created_at, u.username, u.profile_image
        FROM comments c
        JOIN users u ON c.user_id = u.id
        WHERE c.module = %s
        ORDER BY c.created_at DESC
    ''', (module_name,))
    comments = cursor.fetchall()

    return render_template('conditionals.html', comments=comments)

# Cicles
@app.route('/cicles', methods=['GET', 'POST'])
def cicles():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if 'loggedin' not in session:
        return redirect(url_for('login'))

    module_name = 'cicles'

    if request.method == 'POST':
        content = request.form['content']
        if content.strip():
            cursor.execute(
                "INSERT INTO comments (user_id, content, module) VALUES (%s, %s, %s)",
                (session['id'], content, module_name)
            )
            conn.commit()
            flash('Comentario enviado!')

    cursor.execute('''
        SELECT c.content, c.created_at, u.username, u.profile_image
        FROM comments c
        JOIN users u ON c.user_id = u.id
        WHERE c.module = %s
        ORDER BY c.created_at DESC
    ''', (module_name,))
    comments = cursor.fetchall()

    return render_template('cicles.html', comments=comments)

# Arrays
@app.route('/arrays', methods=['GET', 'POST'])
def arrays():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if 'loggedin' not in session:
        return redirect(url_for('login'))

    module_name = 'arrays'

    if request.method == 'POST':
        content = request.form['content']
        if content.strip():
            cursor.execute(
                "INSERT INTO comments (user_id, content, module) VALUES (%s, %s, %s)",
                (session['id'], content, module_name)
            )
            conn.commit()
            flash('Comentario enviado!')

    cursor.execute('''
        SELECT c.content, c.created_at, u.username, u.profile_image
        FROM comments c
        JOIN users u ON c.user_id = u.id
        WHERE c.module = %s
        ORDER BY c.created_at DESC
    ''', (module_name,))
    comments = cursor.fetchall()

    return render_template('arrays.html', comments=comments)

# Functions
@app.route('/functions', methods=['GET', 'POST'])
def functions():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if 'loggedin' not in session:
        return redirect(url_for('login'))

    module_name = 'functions'

    if request.method == 'POST':
        content = request.form['content']
        if content.strip():
            cursor.execute(
                "INSERT INTO comments (user_id, content, module) VALUES (%s, %s, %s)",
                (session['id'], content, module_name)
            )
            conn.commit()
            flash('Comentario enviado!')

    cursor.execute('''
        SELECT c.content, c.created_at, u.username, u.profile_image
        FROM comments c
        JOIN users u ON c.user_id = u.id
        WHERE c.module = %s
        ORDER BY c.created_at DESC
    ''', (module_name,))
    comments = cursor.fetchall()

    return render_template('functions.html', comments=comments)

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
  
@app.route('/profile', methods=['GET', 'POST'])
def profile(): 
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if 'loggedin' not in session:
        return redirect(url_for('login'))

    try:
        # Manejar subida de imagen si es POST
        if request.method == 'POST':
            if 'profile_pic' not in request.files:
                flash('No file part')
                return redirect(request.url)

            file = request.files['profile_pic']
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = f"{app.config['UPLOAD_FOLDER']}/{filename}"
                file.save(file_path)

                # Actualizar en la base de datos
                cursor.execute("UPDATE users SET profile_image = %s WHERE id = %s", (filename, session['id']))
                conn.commit()
                flash('Profile picture updated!')

        # Obtener info del usuario y mostrar
        cursor.execute('SELECT * FROM users WHERE id = %s', [session['id']])
        account = cursor.fetchone()
        return render_template('profile.html', account=account)

    except Exception as e:
        conn.rollback()
        flash("Error: " + str(e))  # Muestra el error real en pantalla (para desarrollo)
        print(f"[Profile error]: {e}")  # También lo imprime en consola
        return redirect(url_for('login'))  # Mejor redirigir a profile para debug



if __name__ == "__main__":
    app.run(debug=True)