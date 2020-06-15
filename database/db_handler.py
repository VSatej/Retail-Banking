# DatabaseHandler class :
# For interfacing python with mysql database. 
# 
# Tables :
#   -   Customer
#   -   Account
#   -   userstore
#   -   CustomerStatus
#   -   AccountStatus
#   -   Transactions
#
# Functions :
#   -   __init__(self)
#   -   add_customer_status(self, SSN_ID, Customer_ID, Status, Message, Last_Updated)
#   -   get_customer_status_from_Customer_ID(self, Customer_ID)
#   -   get_all_customer_status(self)
#   -   add_account_status(self, Customer_ID, Account_ID, Account_Type, Status, Message, Last_Updated)
#   -   get_all_account_status(self)
#   -   get_account_status_from_Account_ID(self, Account_ID)
#   -   get_password(self, login)
#   -   add_user(self, login, password)
#   -   get_users(self)



import mysql.connector
import yaml

class DBHandler:
    def __init__(self):
        config_file = open("database/config.yaml")
        config = yaml.load(config_file,Loader=yaml.FullLoader)

        self.db = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )


    # Customer status and account status management :
    
    # CustomerStatus Table :
    # +--------------+--------------+------+-----+-------------------+-------------------+
    # | Field        | Type         | Null | Key | Default           | Extra             |
    # +--------------+--------------+------+-----+-------------------+-------------------+
    # | SSN_ID       | int          | NO   |     | NULL              |                   |
    # | Customer_ID  | int          | NO   |     | NULL              |                   |
    # | Status       | varchar(20)  | NO   |     | NULL              |                   |
    # | Message      | varchar(100) | YES  |     | NULL              |                   |
    # | Last_Updated | datetime     | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
    # +--------------+--------------+------+-----+-------------------+-------------------+


    def add_customer_status(self, SSN_ID, Customer_ID, Status, Message):
        mycursor = self.db.cursor()

        sql = "INSERT INTO CustomerStatus (SSN_ID, Customer_ID, Status, Message) VALUES (%s, %s, %s, %s)"
        val = (SSN_ID, Customer_ID, Status, Message)
        mycursor.execute(sql, val)

        self.db.commit()

        print(mycursor.rowcount, "record inserted.")

    
    def get_customer_status_from_Customer_ID(self, Customer_ID):
        mycursor = self.db.cursor(self)

        mycursor.execute("SELECT * FROM CustomerStatus where Customer_ID={}".format(Customer_ID))
        result = mycursor.fetchall()
        
        return result


    def get_all_customer_status(self):
        mycursor = self.db.cursor(self)

        mycursor.execute("SELECT * FROM CustomerStatus")
        result = mycursor.fetchall()
        
        return result


    # AccountStatus Table:
    # +--------------+-------------+------+-----+---------+-------+
    # | Field        | Type        | Null | Key | Default | Extra |
    # +--------------+-------------+------+-----+---------+-------+
    # | Customer_ID  | int         | NO   |     | NULL    |       |
    # | Account_ID   | int         | NO   |     | NULL    |       |
    # | Account_Type | varchar(20) | NO   |     | NULL    |       |
    # | Status       | varchar(20) | NO   |     | NULL    |       |
    # | Message      | varchar(20) | NO   |     | NULL    |       |
    # | Last_Updated | varchar(20) | NO   |     | NULL    |       |
    # +--------------+-------------+------+-----+---------+-------+


    def add_account_status(self, Customer_ID, Account_ID, Account_Type, Status, Message):
        mycursor = self.db.cursor()

        sql = "INSERT INTO AccountStatus(Customer_ID, Account_ID, Account_Type, Status, Message) VALUES (%s, %s, %s, %s, %s)"
        val = (Customer_ID, Account_ID, Account_Type, Status, Message)
        mycursor.execute(sql, val)

        self.db.commit()

        print(mycursor.rowcount, "record inserted.")


    def get_all_account_status(self):
        mycursor = self.db.cursor(self)

        mycursor.execute("SELECT * FROM AccountStatus")
        result = mycursor.fetchall()
        
        return result

    def get_account_status_from_Account_ID(self, Account_ID):
        mycursor = self.db.cursor(self)

        mycursor.execute("SELECT * FROM AccountStatus where Account_ID={}".format(Account_ID))
        result = mycursor.fetchall()
        
        return result


    # UserStore Table :
    # +----------+-------------+------+-----+-------------------+-------------------+
    # | Field    | Type        | Null | Key | Default           | Extra             |
    # +----------+-------------+------+-----+-------------------+-------------------+
    # | login    | varchar(50) | NO   | PRI | NULL              |                   |
    # | password | varchar(20) | NO   |     | NULL              |                   |
    # | time     | timestamp   | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
    # +----------+-------------+------+-----+-------------------+-------------------+


    def get_password(self, login):
        mycursor = self.db.cursor(self)

        mycursor.execute("SELECT password FROM userstore WHERE login='{}'".format(login))
        result = mycursor.fetchall()
        
        return result

    
    def add_user(self, login, password):
        mycursor = self.db.cursor(self)
        sql = "INSERT into userstore(login, password) VALUES(%s, %s)"
        val = (login, password)
        mycursor.execute(sql, val)
        self.db.commit()


    def get_users(self):
        mycursor = self.db.cursor(self)

        mycursor.execute("SELECT login FROM userstore")
        result = mycursor.fetchall()
        
        return result


    # Customer Table :
    # +-------------+--------------+------+-----+---------+-------+
    # | Field       | Type         | Null | Key | Default | Extra |
    # +-------------+--------------+------+-----+---------+-------+
    # | SSN_ID      | int          | NO   | PRI | NULL    |       |
    # | Customer_ID | int          | NO   | UNI | NULL    |       |
    # | Name        | varchar(40)  | NO   |     | NULL    |       |
    # | Address     | varchar(100) | NO   |     | NULL    |       |
    # | Age         | int          | NO   |     | NULL    |       |
    # +-------------+--------------+------+-----+---------+-------+

    def get_customer_from_Customer_ID(self, Customer_ID):
        mycursor = self.db.cursor(self)

        mycursor.execute("SELECT * FROM Customer WHERE Customer_ID={}".format(Customer_ID))
        result = mycursor.fetchall()
        
        return result


    def add_customer(self, SSN_ID, Customer_ID, Name, Address, Age):
        mycursor = self.db.cursor()

        sql = "INSERT INTO Customer VALUES (%s, %s, %s, %s, %s)"
        val = (SSN_ID, Customer_ID, Name, Address, Age)
        mycursor.execute(sql, val)

        self.db.commit()

        status = "Active"
        message = "Customer Created Successfully"
        self.add_customer_status(SSN_ID, Customer_ID, status, message)

        print(mycursor.rowcount, "record inserted.")


    def get_customer_from_SSN_ID(self, SSN_ID):
        mycursor = self.db.cursor(self)

        mycursor.execute("SELECT * FROM Customer WHERE SSN_ID={}".format(SSN_ID))
        result = mycursor.fetchall()
        
        return result

    
    def remove_customer(self, Customer_ID):
        mycursor = self.db.cursor(self)

        status = "Removed"
        message = "Customer Removed Successfully"
        SSN_ID = self.get_customer_from_Customer_ID(Customer_ID)[0][0]
        self.add_customer_status(SSN_ID, Customer_ID, status, message)

        mycursor.execute("DELETE from Customer WHERE Customer_ID={}".format(Customer_ID))
        self.db.commit()

        print(mycursor.rowcount, "record(s) deleted")


    def update_customer_from_Customer_ID(self, Customer_ID, name, address, age):
        mycursor = self.db.cursor(self)

        mycursor.execute("UPDATE Customer SET name='{}',address='{}', age={} WHERE Customer_ID={}".format(name, address, age, Customer_ID))
        self.db.commit()

        status = "Active"
        message = "Customer Update Complete"
        SSN_ID = self.get_customer_from_Customer_ID(Customer_ID)[0][0]
        self.add_customer_status(SSN_ID, Customer_ID, status, message)

        print(mycursor.rowcount, "record(s) affected")

    
    def update_customer_from_SSN_ID(self, SSN_ID, name, address, age):
        mycursor = self.db.cursor(self)

        mycursor.execute("UPDATE Customer SET name='{}',address='{}', age={} WHERE SSN_ID={}".format(name, address, age, SSN_ID))
        self.db.commit()

        status = "Active"
        message = "Customer Update Complete"
        Customer_ID = self.get_customer_from_SSN_ID(SSN_ID)[0][1]
        self.add_customer_status(SSN_ID, Customer_ID, status, message)

        print(mycursor.rowcount, "record(s) affected")


    # Account Table:
    # +--------------+------------+------+-----+-------------------+-------------------+
    # | Field        | Type       | Null | Key | Default           | Extra             |
    # +--------------+------------+------+-----+-------------------+-------------------+
    # | Customer_ID  | int        | NO   | UNI | NULL              |                   |
    # | Account_ID   | int        | NO   | PRI | NULL              |                   |
    # | Balance      | int        | NO   |     | NULL              |                   |
    # | CR_Data      | datetime   | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
    # | CR_LDate     | datetime   | YES  |     | NULL              |                   |
    # | Duration     | int        | NO   |     | 10                |                   |
    # | Account_Type | varchar(1) | NO   |     | NULL              |                   |
    # +--------------+------------+------+-----+-------------------+-------------------+

    def add_Account(self, Customer_ID, Account_ID, Account_Type, Balance):
        mycursor = self.db.cursor()

        sql = "INSERT INTO Account(Customer_ID, Account_ID, Balance, Account_Type, CR_LDate) VALUES (%s, %s, %s, %s, DATE_ADD(CURDATE(),INTERVAL 10 YEAR))"
        val = (Customer_ID, Account_ID, Balance, Account_Type)
        mycursor.execute(sql, val)

        self.db.commit()

        status = "Active"
        message = "Account Created Successfully"
        self.add_account_status(Customer_ID, Account_ID, Account_Type,status, message)

        print(mycursor.rowcount, "record inserted.")

    
    def get_account(self, Account_ID):
        mycursor = self.db.cursor(self)

        mycursor.execute("SELECT * FROM Account WHERE Account_ID={}".format(Account_ID))
        result = mycursor.fetchall()
        
        return result

    



# mysqldump -u root -p xplore > database/data.sql

# db = DBHandler()
# db.add_customer(345, 345, "Viren", "Pune", 21)
# print(db.get_customer_from_Customer_ID(345))
# db.update_customer_from_Customer_ID(345,"Viren Pasalkar","Pune", 21)
# print(db.get_customer_from_Customer_ID(345))
# db.update_customer_from_SSN_ID(345, "Viren", "Pune", 21)
# print(db.get_customer_from_Customer_ID(345))
# db.remove_customer(345)
# print(db.get_customer_from_Customer_ID(345))
# [print(x) for x in db.get_all_customer_status()]