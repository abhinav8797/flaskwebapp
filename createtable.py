import psycopg2

'''conn = psycopg2.connect(" dbname='STUDENT' user='postgres' password='04051998abhinav' host='localhost' port='5433' ")
cur= conn.cursor()
cur.execute(" CREATE TABLE IF NOT EXISTS REGISTER10 (ID SERIAL AUTO INCREMENT,USERNAME VARCHAR NOT NULL,EMAIL VARCHAR UNIQUE NOT NULL,PASSWORD1 VARCHAR NOT NULL)" )
conn.commit()
conn.close()
print("table created again")


    '''

 
#EMAIL1="piyushsharma24@gmail.com"

pass=piyush0405 
conn = psycopg2.connect(" dbname='STUDENT' user='postgres' password='04051998abhinav' host='localhost' port='5433' ")
   
cur = conn.cursor()
cur.execute("SELECT password1 FROM register9 WHERE register9.email='piyushsharma24@gmail.com' ")
    #cur.execute("SELECT password1,CASE WHEN password1~E'^\\d+$' THEN CAST (password1 AS INTEGER) ELSE 0 END as password1 FROM register9 WHERE password1=%d",(password1,))
rows = cur.fetchall()
print(rows)
conn.commit()
conn.close()

if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("bull.reports"))



if pass == rows:
    return "succes"
        #in select their is no commit
else:
    return "failure"



