from flask import Flask,render_template,request
import pymysql
from Bank import Bank

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        paswd = request.form['paswd']
        #Bank.check_password(name,paswd)
        return render_template('login.html',name=name,msg="Successfully Logged In")
    return render_template('register.html')

@app.route('/login',methods=['POST','GET'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)
