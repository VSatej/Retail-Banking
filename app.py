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
        if len(server_pass) != 0 and server_pass[0][0] == password:
            flash('Logged In Successfully')
            return render_template('client.html',name=login)
        else:
            error = "Invalid Credentials"
            return redirect(request.url)
        if login == 'admin' and password=='admin@123':
            render_template('admin.html')
    return render_template('login.html', error=error)



@app.route("/createAccount",methods=['POST','GET'])
def createAccount():
    if request.method == 'POST':
        error = None
        customer_id = request.form['customer_ssn_id']
        account_type = request.form['acc_type']
        deposit = request.form['amount']
        if len(str(customer_id)) != 9:
            error = "Customer ID Incorrect"
            return render_template("createAccount.html", error=error)
        else:
            db = DBHandler()
            customer = db.get_customer_from_Customer_ID(customer_id)
            if len(customer) == 0:
                error = "Customer ID Incorrect"
                return render_template("createAccount.html", error=error)
            else:
                if len(db.get_account(customer_id)) == 0:
                    print(db.get_account(customer_id))
                    if account_type == "Savings":
                        db.add_Account(customer_id,customer_id,"S",deposit)
                    else:
                        db.add_Account(customer_id,customer_id,"C",deposit)
                    message = "Account Added Successfully"
                    return render_template("createAccount.html", message=message)
                else:
                    error = "Account Already Exists!"
                    return render_template("createAccount.html", error=error)

        #Bank.createAccount()
    return render_template("createAccount.html")



@app.route("/deleteAccount",methods=['POST','GET'])
def deleteAccount():
    if request.method == 'POST':
        error = None
        di = request.form.to_dict()
        if "delete_ssn_id" in di.keys():
            SSN_ID = request.form["delete_ssn_id"]
            Customer_ID = request.form["delete_acc_id"]
            if not SSN_ID and not Customer_ID:
                error = "Enter either Customer ID or SSN ID to fetch acount"
                return render_template("deleteAccount.html",ssn_id="",cust_id="",name="",address="",age="", error=error)
            elif SSN_ID:
                db = DBHandler()
                customer = db.get_account(SSN_ID)
                print(customer)
                if len(customer) == 0:
                    error = "Invalid SSN ID/Account doesn't exit"
                    return render_template("deleteAccount.html",ssn_id="",cust_id="",name="",address="",age="", error=error)
                else:
                    print(customer[0][6])
                    if customer[0][6] == "S":
                        acc_type = "Savings"
                    else:
                        acc_type = "Current"
                    return render_template("deleteAccount.html",ssn_id=customer[0][1],cust_id="",name="",address="",age="", type=acc_type)
            elif Customer_ID:
                db = DBHandler()
                customer = db.get_account(Customer_ID)
                if len(customer) == 0:
                    error = "Invalid customer ID/Account doesn't exist"
                    return render_template("deleteAccount.html",ssn_id="",cust_id="",name="",address="",age="", error=error)
                else:
                    if customer[0][6] == "S":
                        acc_type = "Savings"
                    else:
                        acc_type = "Current"
                    return render_template("deleteAccount.html",ssn_id=customer[0][1],cust_id="",name="",address="",age="", type=acc_type)

        if "account_list" in di.keys():
            db = DBHandler()
            customer = db.get_account(di["account_list"])
            db.remove_account(di["account_list"])
            message = "Account Removed Successfully!"
            return render_template("deleteAccount.html",ssn_id=customer[0][1],cust_id="",name="",address="",age="", message=message)
    return render_template("deleteAccount.html")



@app.route("/updateCustomer",methods=['POST','GET'])
def updateCustomer():
    error = None
    if request.method == 'POST':
        di = request.form.to_dict()
        if "update_ssn_id" in di.keys():
            SSN_ID = request.form["update_ssn_id"]
            Customer_ID = request.form["update_acc_id"]
            if not SSN_ID and not Customer_ID:
                error = "Enter either Customer ID or SSN ID to fetch acount"
                return render_template("updateCustomer.html",ssn_id="",cust_id="",name="",address="",age="", error=error)
            elif SSN_ID:
                db = DBHandler()
                customer = db.get_customer_from_SSN_ID(SSN_ID)
                if len(customer) == 0:
                    error = "Invalid SSN ID"
                    return render_template("updateCustomer.html",ssn_id="",cust_id="",name="",address="",age="", error=error)
                else:
                    return render_template("updateCustomer.html",ssn_id=SSN_ID,cust_id=customer[0][1],name=customer[0][2],address=customer[0][3],age=customer[0][4])
            elif Customer_ID:
                db = DBHandler()
                customer = db.get_customer_from_Customer_ID(Customer_ID)
                if len(customer) == 0:
                    error = "Invalid Customer ID"
                    return render_template("updateCustomer.html",ssn_id="",cust_id="",name="",address="",age="", error=error)
                else:
                    return render_template("updateCustomer.html",ssn_id=customer[0][0],cust_id=customer[0][1],name=customer[0][2],address=customer[0][3],age=customer[0][4])

        elif "cust_new_name" in di.keys():
            new_name = request.form['cust_new_name']
            new_age = request.form['cust_new_age']
            new_address = request.form['cust_new_address']
            Customer_ID = request.form["cust_id"]
            if new_name and new_age and new_address:
                db = DBHandler()
                db.update_customer_from_Customer_ID(Customer_ID, new_name, new_address, new_age)
                return render_template("updateCustomer.html",ssn_id="",cust_id="",name="",address="",age="", error="", message="Updated Successfully!")

    #Bank.accountDetails()
    return render_template("updateCustomer.html",ssn_id="",cust_id="",name="",address="",age="")


@app.route("/deleteCustomer",methods=['POST','GET'])
def deleteCustomer():
    if request.method == 'POST':
        error = None
        di = request.form.to_dict()
        if "delete_ssn_id" in di.keys():
            SSN_ID = request.form["delete_ssn_id"]
            Customer_ID = request.form["delete_acc_id"]
            if not SSN_ID and not Customer_ID:
                error = "Enter either Customer ID or SSN ID to fetch acount"
                return render_template("deleteCustomer.html",ssn_id="",cust_id="",name="",address="",age="", error=error)
            elif SSN_ID:
                db = DBHandler()
                customer = db.get_customer_from_SSN_ID(SSN_ID)
                print(customer)
                if len(customer) == 0:
                    error = "Invalid SSN ID"
                    return render_template("deleteCustomer.html",ssn_id="",cust_id="",name="",address="",age="", error=error)
                else:
                    return render_template("deleteCustomer.html",ssn_id=SSN_ID,cust_id=customer[0][1],name=customer[0][2],address=customer[0][3],age=customer[0][4])
            elif Customer_ID:
                db = DBHandler()
                customer = db.get_customer_from_Customer_ID(Customer_ID)
                if len(customer) == 0:
                    error = "Invalid Customer ID"
                    return render_template("deleteCustomer.html",ssn_id="",cust_id="",name="",address="",age="", error=error)
                else:
                    return render_template("deleteCustomer.html",ssn_id=customer[0][0],cust_id=customer[0][1],name=customer[0][2],address=customer[0][3],age=customer[0][4])

        elif "cust_id" in di.keys():
            cust_id = request.form['cust_id']
            db = DBHandler()
            db.remove_customer(cust_id)
            message="Customer Deleted Successfully!"
            return render_template("deleteCustomer.html",message=message)
    return render_template("deleteCustomer.html")
"""
@app.route("/deleteAccount",methods=['POST','GET'])
def deleteAccount():
    if request.method == 'POST':
        account_id = request.form['']
        account_type = request.form['']
        #Bank.deleteAccount(account_id,account_type)
        return redirect(request.url) 
    return render_template("deleteAccount.html")
"""
@app.route("/accountSearch",methods=['POST','GET'])
def accountSearch():
    if request.method == 'POST':
        account_id = request.form['']
        customer_id = request.form['']
        #Bank.accountSearch()
        return redirect(request.url) 
    return render_template("accountSearch.html")

@app.route("/customerSearch",methods=['POST','GET'])
def customerSearch():
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

@app.route("/createCustomer",methods=['POST','GET'])
def createCustomer():
    return render_template("createCustomer.html")

@app.route("/customerStatus",methods=['POST','GET'])
def customerStatus():
    db = DBHandler()
    status = db.get_all_customer_status()
    return render_template("customerStatus.html", data=status)

@app.route("/accountStatus",methods=['POST','GET'])
def accountStatus():
    db = DBHandler()
    status = db.get_all_account_status()
    return render_template("accountStatus.html",data=status)

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
    
