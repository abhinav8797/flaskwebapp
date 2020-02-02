import psycopg2
from flask import *
from flask_mail import Mail,Message  
from random import * 

app = Flask(__name__)
app.secrect_key ="yoursuperstrongkey" 

'''app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://localhost/DATABASE_NAME'
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)'''

#mail=Mail(app)

#just after constructer of flask it will be mail=Mail(app)
#we have to start (mail) with  all its configuration and then 
#end with same (mail) after app.configure


'''app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465     
app.config["MAIL_USERNAME"] = 'youremail@gmail.com'  
app.config['MAIL_PASSWORD'] = '*****yourpass******'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True'''  
#mail = Mail(app) 

#here mail will have space

#otp = randint(000000,999999)  
 

@app.route("/")
def home():
    return render_template('registration.html')


@app.route("/regis",methods = ["POST","GET"])
def regis():
    if request.method == "POST":
        USERNAME = request.form["name"]
        EMAIL = request.form["email"]
        PASSWORD = request.form["password"]
        print("name")
        print("hello")  
        conn = psycopg2.connect(" dbname='STUDENT' user='postgres' password='04051998abhinav' host='localhost' port='5433' ")
        cur= conn.cursor()
        cur.execute("INSERT INTO register9 (USERNAME,EMAIL,PASSWORD1) VALUES(%s,%s,%s)", (USERNAME,EMAIL,PASSWORD) )
        conn.commit()
        conn.close()
        print("data inserted")

    return render_template("login1.html")
        
    
    
    
'''conn= sqlite3.connect("register.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE NAME OR REGISTER (NAME TEXT NOT NULL,EMAIL EMAIL UNIQUE NOT NULL,PASSWORD STRINGVAR NOT NULL) VALUES (?,?,?)",(NAME,EMAIL,PASSWORD) )
    conn.commit()
    conn.close()
    print("yable created")
    return render_template("login1.html")'''



@app.route("/login")
def login():
    return render_template("login1.html")



'''
#make sure you have install flask,flask-mail in the current directory or in the directory 
#in which these scripts are
##or activate your environment an install flask,flask-mail in  it'''


@app.route("/verify",methods = ["POST","GET"])
def verify():
    if request.method == "POST":
        EMAIL = request.form["email"]
        PASS = request.form["pass"]

        conn = psycopg2.connect("dbname='STUDENT' user='postgres' password='04051998abhinav' host='localhost' port='5433' ")
        cur = conn.cursor()
        #cur.execute("SELECT CAST (password1 AS INTEGER) FROM register9 WHERE email=%s",(EMAIL,))
        cur.execute(" SELECT password1 FROM register9 WHERE email = EMAIL ")  
        row = cur.fetchone()
        print(row)
        #in select their is no commit
        #conn.commit()
        cur.close()
        conn.close()
        #repass = rows)

        if PASS == row:
            flash("successfully Loged_in")
            return redirect(url_for("validate1"))
           
        else:
            error = "please enter valid username or password"
    else:
        return render_template("login1.html",error = error)
    #return render_template("verify.html")


'''
@app.route('/validate1',methods=["POST"])  
def validate1():
    if request.method == "POST":        
        session["email"] = request.form["email"]
        email = session["email"]    
        msg = Message('OTP',sender = 'youremail@gmail.com', recipients =[email])  
        msg.body = str(otp)  
        mail.send(msg) 
    return render_template("verify.html")



'
#@app.route('/validate1',methods=["POST"])  
#def validate(): 
    #email = request.form["email"]    
    msg = Message('OTP',sender = 'youremail@gmail.com', recipients =[email])  
    msg.body = str(otp)  
    mail.send(msg)  
    return render_template("verify.html")  
 '''

'''@app.route('/validate2',methods=["POST"])  
def validate2():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        return render_template('peoples.html') 
    return "<h3>failure</h3>"  


@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email',None)
        return render_template('logout.html')
    else:
        return "<p>user already logged out</p>"

'''
if __name__ == '__main__':
    app.run(debug = True)