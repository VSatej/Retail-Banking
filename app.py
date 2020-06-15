from flask import Flask,render_template,request,flash,redirect,url_for,session
# from flask.ext.session import Session
from database.db_handler import DBHandler
#from Bank import Bank

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

@app.route("/createAccount",methods=['POST','GET'])
def createAccount():
    if request.method == 'POST':
        customer_id = request.form['']
        account_type = request.form['']
        deposit = request.form['']
        #Bank.createAccount()
        return redirect(request.url)
	return render_template("createAccount.html",name)

@app.route("/deleteAccount",methods=['POST','GET'])
def deleteAccount():
    if request.method == 'POST':
        account_id = request.form['']
        account_type = request.form['']
        #Bank.deleteAccount()
        return redirect(request.url)
	return render_template("deleteAccount.html")

@app.route("/updateCustomer",methods=['POST','GET'])
def updateCustomer():
    if request.method == 'POST':
        new_name = request.form['']
        new_age = request.form['']
        new_address = request.form['']
        #Bank.createAccount(new_name.new_age,new_address)
        return redirect(request.url)
    #Bank.accountDetails()
	return render_template("updateCustomer.html",ssn_id,cust_id,name,address,age)

@app.route("/deleteCustomer",methods=['POST','GET'])
def deleteCustomer():
    if request.method == 'POST':
        ssn_id = request.form['']
        cust_id = request.form['']
        name = request.form['']
        age = request.form['']
        address = request.form['']
        #Bank.deleteCustomer(ssn_id,cust_id,name,age,address)
        return redirect(request.url) 
	return render_template("deleteCustomer.html")

@app.route("/deleteAccount",methods=['POST','GET'])
def deleteCustomer():
    if request.method == 'POST':
        account_id = request.form['']
        account_type = request.form['']
        #Bank.deleteAccount(account_id,account_type)
        return redirect(request.url) 
	return render_template("deleteAccount.html")

@app.route("/accountSearch",methods=['POST','GET'])
def search():
    if request.method == 'POST':
        account_id = request.form['']
        customer_id = request.form['']
        #Bank.accountSearch()
        return redirect(request.url) 
	return render_template("accountSearch.html")

@app.route("/customerSearch",methods=['POST','GET'])
def search():
    if request.method == 'POST':
        ssn_id = request.form['']
        customer_id = request.form['']
        #Bank.customerSearch()
        return redirect(request.url) 
	return render_template("customerSearch.html")

@app.route("/cashier_deposit",methods=['POST','GET'])
def cashier_deposit():
    if request.method == 'POST':
        cust_id = request.form['']
        account_id = request.form['']
        account_type = request.form['']
        balance = request.form['']
        #Bank.deposit()
        return redirect(request.url) 
	return render_template("cashier_deposit.html")

@app.route("/cashier_withdraw",methods=['POST','GET'])
def cashier_withdraw():
    if request.method == 'POST':
        cust_id = request.form['']
        account_id = request.form['']
        account_type = request.form['']
        balance = request.form['']
        #Bank.withdraw()
        return redirect(request.url) 
	return render_template("cashier_withdraw.html")

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
    
