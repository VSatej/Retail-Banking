from flask import Flask,render_template,request,flash,redirect,url_for,session
import functools
# from flask.ext.session import Session
from database.db_handler import DBHandler
#from Bank import Bank
from numpy.random import randint

app = Flask(__name__)

def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if "username" not in session:
            return render_template('login.html', name="")
        return func()

    return secure_function 

"delete this comment later"

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


@app.route('/login',methods=['POST',"GET"])
def login():
    error = None
    if request.method == 'POST':
        login = request.form["username"]
        password = request.form["password"]
        db = DBHandler()
        server_pass = db.get_password(login)
        if len(server_pass) != 0 and server_pass[0][0] == password:
            flash('Logged In Successfully')
            session["username"] = login
            acc_type = db.get_type(login)
            if acc_type[0][0] == "Cashier":
                return render_template("accountDetails.html")
            else:
                return render_template('createAccount.html')
        else:
            error = "Invalid Credentials"
            return render_template("login.html")
    return render_template('login.html', error=error)



@app.route("/createAccount",methods=['POST','GET'])
@login_required
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
                print(db.get_account(customer_id))
                if account_type == "Savings":
                    account_id = int(int(customer_id)/10000)*10000 + randint(1000,9999)
                    db.add_Account(customer_id,account_id,"S",deposit)
                else:
                    account_id = int(int(customer_id)/10000)*10000 + randint(1000,9999)
                    db.add_Account(customer_id,account_id,"C",deposit)
                message = "Account Added Successfully"
                return render_template("createAccount.html", message=message)


        #Bank.createAccount()
    return render_template("createAccount.html")



@app.route("/deleteAccount",methods=['POST','GET'])
@login_required
def deleteAccount():
    if request.method == 'POST':
        error = None
        di = request.form.to_dict()
        if "delete_ssn_id" in di.keys():
            SSN_ID = request.form["delete_ssn_id"]
            Customer_ID = request.form["delete_acc_id"]
            if not SSN_ID and not Customer_ID:
                error = "Enter either Customer ID or SSN ID to fetch acount"
                return render_template("deleteAccount.html",ssn_id="",cust_id="",name="",address="",age="", error=error,accounts=[])
            elif SSN_ID:
                db = DBHandler()
                customer = db.get_all_accounts(SSN_ID)
                print(customer)
                if len(customer) == 0:
                    error = "Invalid SSN ID/Account doesn't exit"
                    return render_template("deleteAccount.html",ssn_id="",cust_id="",name="",address="",age="", error=error,accounts=[])
                else:
                    accounts = []
                    for account in customer:
                        if account[6] == "S":
                            acc_type = "Savings"
                        else:
                            acc_type = "Current"
                        accounts.append([account[1],acc_type])
                    return render_template("deleteAccount.html",ssn_id="",cust_id="",name="",address="",age="", error="",accounts=accounts)
            elif Customer_ID:
                db = DBHandler()
                customer = db.get_all_accounts(Customer_ID)
                if len(customer) == 0:
                    error = "Invalid customer ID/Account doesn't exist"
                    return render_template("deleteAccount.html",ssn_id="",cust_id="",name="",address="",age="", error=error,accounts=[])
                else:
                    accounts = []
                    for account in customer:
                        if account[6] == "S":
                            acc_type = "Savings"
                        else:
                            acc_type = "Current"
                        accounts.append(account[1],acc_type)
                    return render_template("deleteAccount.html",ssn_id="",cust_id="",name="",address="",age="", error="",accounts=accounts)

        if "account_list" in di.keys():
            db = DBHandler()
            customer = db.get_account(di["account_list"])
            db.remove_account(di["account_list"])
            message = "Account Removed Successfully!"
            return render_template("deleteAccount.html",ssn_id=customer[0][1],cust_id="",name="",address="",age="", message=message)
    return render_template("deleteAccount.html")



@app.route("/updateCustomer",methods=['POST','GET'])
@login_required
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
@login_required
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



@app.route("/accountSearch",methods=['POST','GET'])
@login_required
def accountSearch():
    if request.method == 'POST':
        account_id = request.form['']
        customer_id = request.form['']
        #Bank.accountSearch()
        return redirect(request.url) 
    return render_template("accountSearch.html")



@app.route("/customerSearch",methods=['POST','GET'])
@login_required
def customerSearch():
    if request.method == 'POST':
        ssn_id = request.form['']
        customer_id = request.form['']
        #Bank.customerSearch()
        return redirect(request.url) 
    return render_template("customerSearch.html")



@app.route("/createCustomer",methods=['POST','GET'])
@login_required
def createCustomer():
    if request.method == "POST":
        ssn_id = request.form["cust_ssn_id"]
        name = request.form['cust_name']
        age = request.form['cust_age']
        address = request.form['cust_address']
        state = request.form["stt"]
        city = request.form["city"]

        address = address + ", " + city + ", " + state

        db = DBHandler()
        if len(str(ssn_id)) != 9:
            error="Invalid SSN ID"
            return render_template("createCustomer.html",error=error)
        elif len(db.get_customer_from_SSN_ID(ssn_id)) != 0:
            error="Customer Already Exists"
            return render_template("createCustomer.html",error=error)
        else:
            db.add_customer(ssn_id, ssn_id, name, address, age)
            message="Customer Added Successfully"
            return render_template("createCustomer.html",message=message)
    return render_template("createCustomer.html")



@app.route("/customerStatus",methods=['POST','GET'])
@login_required
def customerStatus():
    db = DBHandler()
    status = db.get_all_customer_status()
    return render_template("customerStatus.html", data=status)



@app.route("/accountStatus",methods=['POST','GET'])
@login_required
def accountStatus():
    db = DBHandler()
    status = db.get_all_account_status()
    return render_template("accountStatus.html",data=status)



@app.route("/cashier_withdraw",methods=['POST','GET'])
@login_required
def cashier_withdraw():
    if request.method == 'POST':
        cust_id = request.form['']
        account_id = request.form['']
        account_type = request.form['']
        balance = request.form['']
        #Bank.withdraw()
        return redirect(request.url) 
    return render_template("cashier_withdraw.html")



@app.route("/accountDetails",methods=['POST','GET'])
@login_required
def accountDetails():
    if request.method == 'POST':
        error = None
        di = request.form.to_dict()
        if "cust_ssn_id" in di.keys():
            SSN_ID = request.form["cust_ssn_id"]
            Customer_ID = request.form["cust_id"]
            if not SSN_ID and not Customer_ID:
                error = "Enter either Customer ID or SSN ID to fetch acount"
                return render_template("accountDetails.html",error=error)
            elif SSN_ID:
                db = DBHandler()
                customer = db.get_customer_from_SSN_ID(SSN_ID)
                print(customer)
                if len(customer) == 0:
                    error = "Invalid SSN ID"
                    return render_template("accountDetails.html",error=error)
                else:
                    db = DBHandler()
                    accounts = db.get_all_accounts(SSN_ID)
                    return render_template("accountDetails.html",accounts=accounts)
            elif Customer_ID:
                db = DBHandler()
                customer = db.get_customer_from_Customer_ID(Customer_ID)
                if len(customer) == 0:
                    error = "Invalid Customer ID"
                    return render_template("accountDetails.html",error=error)
                else:
                    db = DBHandler()
                    accounts = db.get_all_accounts(Customer_ID)
                    return render_template("accountDetails.html",accounts=accounts)

        elif "account_list" in di.keys():
            account_id = request.form["account_list"]
            db = DBHandler()
            account = db.get_account(account_id)
            return render_template("accountDetails.html", account=account[0])

    # elif request.method == "GET":
        # di = request.form.to_dict()
        # print(di.keys())
        if "cust_id" in di.keys():
            cust = request.form["cust_id"]
            acc = request.form["acc_id"]
            typ = request.form["acc_type"]
            bal = request.form["acc_bal"]
            account = [cust,acc,typ,bal]
            if request.form["action"] == 'Deposit':
                return render_template("cashier_deposit.html",account=account)
            elif request.form['action'] == 'Transfer':
                db = DBHandler()
                accounts = db.get_all_accounts(cust)
                return render_template("cashier_transfer.html",account=account,  accounts=accounts)
            elif request.form['action'] == 'Withdraw':
                return render_template("cashier_withdraw.html",account=account)

        if "deposit_amount" in di.keys():
            cust = request.form["customer_id"]
            acc = request.form["acc_id"]
            typ = request.form["acc_type"]
            bal = request.form["acc_bal"]
            amount = request.form["deposit_amount"]
            db = DBHandler()
            db.set_balance(acc,int(int(bal)+int(amount)))
            db.add_transaction(acc, "Deposit", amount)
            return render_template("accountDetails.html",message="Deposit Successful")

        if "withdraw_amount" in di.keys():
            cust = request.form["customer_id"]
            acc = request.form["acc_id"]
            typ = request.form["acc_type"]
            bal = request.form["acc_bal"]
            amount = request.form["withdraw_amount"]
            if int(bal) >= int(amount):
                db = DBHandler()
                db.set_balance(acc,int(int(bal)-int(amount)))
                db.add_transaction(acc, "Withdraw", amount)
                return render_template("accountDetails.html",message="Withdraw Successful")
            else:
                return render_template("accountDetails.html",error="Insufficient Balance")

        
        if "transfer_amount" in di.keys():
            cust = request.form["customer_id"]
            acc = request.form["source_account_list"]
            dest = request.form["target_account_list"]
            amount = request.form["transfer_amount"]
            db = DBHandler()
            bal = db.get_balance(acc)[0][0]
            if int(bal) >= int(amount):
                db.set_balance(acc,int(int(bal)-int(amount)))
                bal = db.get_balance(acc)[0][0]
                db.set_balance(dest,int(int(bal)+int(amount)))
                db.add_transaction(acc, "Transfer", amount)
                db.add_transaction(dest, "Transfer", amount)
                new_bal = db.get_balance(acc)[0][0]
                return render_template("accountDetails.html",message="Transfer Successful, New Balance : {}".format(new_bal))
            else:
                return render_template("accountDetails.html",error="Insufficient Balance")

    return render_template("accountDetails.html")



@app.route("/cashier_deposit",methods=['POST','GET'])
@login_required
def cashier_deposit():
    if request.method == 'POST':
        cust_id = request.form['']
        account_id = request.form['']
        account_type = request.form['']
        balance = request.form['']
        #Bank.withdraw()
        return redirect(request.url) 
    return render_template("cashier_deposit.html")



@app.route("/cashier_transfer",methods=['POST','GET'])
@login_required
def cashier_transfer():
    if request.method == 'POST':
        cust_id = request.form['']
        account_id = request.form['']
        account_type = request.form['']
        balance = request.form['']
        #Bank.withdraw()
        return redirect(request.url) 
    return render_template("cashier_transfer.html")

@app.route("/accountStatement",methods=['POST','GET'])
def accountStatement():
    if request.method == 'POST':
        acc = request.form["acc_id"]
        print(acc)
        db = DBHandler()
        transactions = db.get_transactions(acc)
        # transactions = []
        print(transactions)
        return render_template("accountStatement.html", transactions=transactions)
    return render_template("accountStatement.html")

@app.route("/home_cashier",methods=['POST','GET'])
def home_cashier():
    return render_template("home_cashier.html")

@app.route("/home",methods=['POST','GET'])
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
    
