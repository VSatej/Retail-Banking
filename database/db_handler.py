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


    def add_customer_status(self, SSN_ID, Customer_ID, Status, Message, Last_Updated):
        mycursor = self.db.cursor()

        sql = "INSERT INTO CustomerStatus (SSN_ID, Customer_ID, Status, Message, Last_Updated) VALUES (%s, %s, %s, %s, %s)"
        val = (SSN_ID, Customer_ID, Status, Message, Last_Updated)
        mycursor.execute(sql, val)

        self.db.commit()

        print(mycursor.rowcount, "record inserted.")


    def add_account_status(self, Customer_ID, Account_ID, Account_Type, Status, Message, Last_Updated):
        mycursor = self.db.cursor()

        sql = "INSERT INTO AccountStatus(Customer_ID, Account_ID, Account_Type, Status, Message, Last_Updated) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (Customer_ID, Account_ID, Account_Type, Status, Message, Last_Updated)
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


    def get_all_account_status(self):
        mycursor = self.db.cursor(self)

        mycursor.execute("SELECT * FROM AccountStatus")
        result = mycursor.fetchall()
        
        return result


    def get_customer_status_from_Account_ID(self, Account_ID):
        mycursor = self.db.cursor(self)

        mycursor.execute("SELECT * FROM AccountStatus where Account_ID={}".format(Account_ID))
        result = mycursor.fetchall()
        
        return result

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

    


dbh = DBHandler()
dbh.add_user("User01","qwerty")
print(dbh.get_password("Rohan"))
[print(x) for x in dbh.get_users()]