from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "secret123"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'role_based'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT * FROM account WHERE username=%s AND password=%s",
            (request.form['username'], request.form['password'])
        )
        user = cursor.fetchone()

        if user:
            session['acctno'] = user['acctno']
            session['username'] = user['username']
            session['role'] = user['role']
            flash('Login successful!', 'success')
            return redirect('/home')
        else:
            flash('Invalid username or password', 'error')
            return redirect('/')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO account (name, sex, dob, username, password) VALUES (%s,%s,%s,%s,%s)",
            (
                request.form['name'],
                request.form['sex'],
                request.form['dob'],
                request.form['username'],
                request.form['password']
            )
        )
        mysql.connection.commit()

        flash('Account created successfully!', 'success')
        return redirect('/')

    return render_template('register.html')

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect('/')

    cursor = mysql.connection.cursor()

    if session['role'] == 'admin':
        cursor.execute("SELECT * FROM account")
        users = cursor.fetchall()
        return render_template('admin.html', users=users)

    cursor.execute(
        "SELECT * FROM account WHERE acctno=%s",
        (session['acctno'],)
    )
    user = cursor.fetchone()
    return render_template('home.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
