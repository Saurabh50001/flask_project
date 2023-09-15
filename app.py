from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///database.db'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.string,primary_key=True)
    name = db.column(db.string(100),nullable=False)
    email = db.column(db.string(100),nullable=False)
    mobile = db.column(db.integer,nullable=False)
    address = db.column(db.string(100),nullable=False)
    password = db.column(db.string(100))

    def __init__(self, email, password):
        self.id = id
        self.email = email
        self.mobile = mobile
        self.address = address
        self.password = bcrypt.haspw(password.encode('utf-8'),bcrypt.getslt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.passowrd.encode('utf-8'))
   
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/registration', method = ['GET', 'POST'])
def registration():
    if request.method == 'POST':
       id = request.form['id']
       name = request.form['name']
       email = request.form['email']
       mobile = request.form['mobile']
       address = request.form['address']
       password = request.form['password']

       new_user =User(id=id,name=name,email=email,password=passowrd)
       db.session.add(new_user)
       db.session.commit()
       return redirect('/login')



    return tender_template('registration.html')  


@app.route('/login',method = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(passowrd):
            session['name'] = user.name
            session['email'] = user.email
            return redirect('/index')
        else:
            return render_template('login.html', error ='Invalid user')
    return tender_template('login.html')   


if __name__ == '__main__':
    app.run(debug=True) 