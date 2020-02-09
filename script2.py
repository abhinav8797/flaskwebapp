import psycopg2
from flask import *
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_user,login_required, login_required, logout_user, current_user
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from flask_login import login_user, logout_user, login_required
from sqlalchemy.dialects.postgresql import JSON

app = Flask(__name__)

app.config['SECRET_KEY']='THISISmysupersecretKEY'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:04051998abhinav@localhost:5433/USERSS'

Bootstrap(app)

#app.config['SQLALCHEMY_TRACK_MODIFICATION']=True

db = SQLAlchemy(app)

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

class Users(UserMixin, db.Model):
    __tablename__="user1"
    id=db.Column(db.Integer, primary_key=True )
    name=db.Column(db.String(15),unique=False, nullable = False)
    email=db.Column(db.String(30),unique=True, nullable = False)
    password=db.Column(db.String(80), nullable=False)
    print("database connected")

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signupme', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = Users.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    if user:
        flash('Email address already exists') # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = Users(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    print("users added succesfully")
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    print("users commited succesfully")
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logmein', methods=['GET','POST'])
def logmein():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Users.query.filter_by(email = email).first()
    print("email checked")
    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    #if not user or not check_password_hash(user.password, password):
    
    if login_user(user):
        print("user excepted")
        if check_password_hash(user.password, password):
            flash('successfully loged in')
            return redirect(url_for('profile'))
            print("password matched")
            #return redirect(url_for('login')) # if user doesn't exist or password is wrong, reload the page
    flash('Please check your login details and try again.')
    return redirect(url_for('login'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@app.route('/return_file')
@login_required
def return_file():
    #This is just for checking
    return send_file()
    
    #below this line is the correct line
    #the pdf will be inside static folder
    #return send_file('static/Abhinav_Resume.pdf', attachment_filename='Abhinav_Resume.pdf')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__== '__main__':
    app.run(debug= True)