from database import connect

class Bank:
    def check_password(self,name,paswd):
        db = connect.db_connect()

    def create(self):
        db = connect.db_connect()
        connect.db_create(db)

    def update(self):
        db = connect.db_connect()
        connect.db_update(db)
        pass

    def delete(self):
        db = connect.db_connect()
        connect.db_delete(db)
        pass

    def view(self):
        db = connect.db_connect(db)
        connect.db_view(db)
        pass

    def status(self):
        pass

    def deposit(self):
        pass

    def withdraw(self):
        pass

    def transfer(self):
        pass


