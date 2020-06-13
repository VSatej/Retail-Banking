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

    


