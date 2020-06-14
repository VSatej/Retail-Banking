from flask import Flask,render_template,request
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

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        ssn_id = request.form['ssd-id']
        cust_id = request.form['cust-id']
        name = request.form['name']
        date = request.form['date']
        address = request.form['address']
        age = request.form['age']
        #Bank.create(ssn_id,cust_id,name,date,address,age)
    return render_template('login.html')

@app.route("/createAccount")
def createAccount():
	return render_template("createAccount.html")

@app.route("/deleteAccount")
def deleteAccount():
	return render_template("deleteAccount.html")

@app.route("/updateCustomer")
def updateCustomer():
	return render_template("updateCustomer.html")
    
if __name__ == '__main__':
    app.run(port=5000,debug=True)
