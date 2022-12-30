from flask import Flask,render_template, request, url_for, redirect, flash
from forms import SignupForm, LoginForm
import sqlite3


app=Flask(__name__)
app.config['SECRET_KEY']='fjwieivjovlwe'


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route("/signup",methods=['POST','GET'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        connection=sqlite3.connect("users_data.db")
        cursor=connection.cursor()
        sqlite_insert="""INSERT INTO users(name,email,password) VALUES(?,?,?);"""
        username=form.username.data
        email=form.email.data
        password=form.password.data
        print(username,email,password)
        data_tuple=(username,email,password)
        cursor.execute(sqlite_insert,data_tuple)
        connection.commit()
        flash(f'Account created successfully for {form.username.data}')
        return redirect(url_for('index'))
    return render_template('signup.html',title='Signup',form=form)



@app.route('/index',methods=['GET','POST'])
def index():
    if request.method=='POST':
        connection=sqlite3.connect('users_data.db')
        cursor=connection.cursor()

        name=request.form['name']
        password=request.form['password']

        # print(name,password)

        query="SELECT name,password FROM users where name='"+name+"' and password='"+password+"'" 
        cursor.execute(query)

        results=cursor.fetchall() 

        if len(results)==0:
            print("Incorrect Credentials provided.Try Again!")  
        else:
            # return render_template('login.html',name=name)
            return redirect(url_for('login',name=name))
         
   

    return render_template('index.html')
    # return redirect(url_for('index'))

@app.route("/login/<name>",methods=['POST','GET'])
def login(name):
     if request.method=='POST':
        EventName=request.form['EventName']
        link1=request.form['link1']
        link2=request.form['link2']
        connection=sqlite3.connect('users_data.db')
        cursor=connection.cursor()
        sqlite_insert="""INSERT INTO events(EventName,link1,link2) VALUES(?,?,?);"""
        data_tuple=(EventName,link1,link2)
        cursor.execute(sqlite_insert,data_tuple)
        connection.commit()
     return render_template('login.html',name=name)
    
if __name__=="__main__":
    app.run(debug=True)