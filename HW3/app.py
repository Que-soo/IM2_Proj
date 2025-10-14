from flask import *

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    lastname = request.form['lastname']
    firstname = request.form['firstname']
    sex = request.form['sex']
    institution = request.form['institution']
    email = request.form['email']
    return render_template(
        'output.html',
        lastname=lastname,
        firstname=firstname,
        sex=sex,
        institution=institution,
        email=email
    )

if __name__ == '__main__':
    app.run(debug=True)