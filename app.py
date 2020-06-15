from flask import Flask,render_template,request,flash,redirect,url_for,session
# from flask.ext.session import Session
from database.db_handler import DBHandler
# from Bank import Bank

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


@app.route('/login',methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        login = request.form["username"]
        password = request.form["password"]
        db = DBHandler()
        server_pass = db.get_password(login)
        if len(server_pass) is not 0 and server_pass[0][0] == password:
            flash('Logged In Successfully')
            return render_template("createAccount.html")
        else:
            error = "Invalid Credentials"
    return render_template('login.html', error=error)



@app.route("/createAccount")
def createAccount():
	return render_template("createAccount.html")

@app.route("/deleteAccount")
def deleteAccount():
	return render_template("deleteAccount.html")

@app.route("/updateCustomer")
def updateCustomer():
	return render_template("updateCustomer.html")

@app.route("/deleteCustomer")
def deleteCustomer():
	return render_template("deleteCustomer.html")

@app.route("/cashier_deposit")
def cashier_deposit():
	return render_template("cashier_deposit.html")

@app.route("/cashier_withdraw")
def cashier_withdraw():
	return render_template("cashier_withdraw.html")

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
    
