from database import db_handler

class Bank:
    def __init__(self):
        self.db = db_handler.get_instance()

    
        

bank = Bank()


# class Bank:
#     def check_password(self,name,paswd):
#         db = connect.db_connect()

#     def createAccount(self):
#         db = connect.db_connect()
#         connect.db_create(db)

#     def updateAccount(self):
#         db = connect.db_connect()
#         connect.db_update(db)
#         pass

#     def deleteAccount(self):
#         db = connect.db_connect()
#         connect.db_delete(db)
#         pass

#     def createCustomer(self):
#         db = connect.db_connect()
#         connect.db_create(db)

#     def updateCustomer(self):
#         db = connect.db_connect()
#         connect.db_update(db)
#         pass

#     def deleteCustomer(self):
#         db = connect.db_connect()
#         connect.db_delete(db)
#         pass

#     def view(self):
#         db = connect.db_connect(db)
#         connect.db_view(db)
#         pass

#     def status(self):
#         pass

#     def deposit(self):
#         pass

#     def withdraw(self):
#         pass

#     def transfer(self):
#         pass


