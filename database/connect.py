import pymysql

def db_connect(db):
    db = pymysql.connect("localhost","root","admin@123","xplore")
    return db

def db_create(db):
    pass

def db_update(db):
    pass

def db_delete(db):
    pass

def db_view(db):
    cursor = db.cursor()
    try:
        cursor = cursor.execute("")
        records = cursor.fetchall()
        for rec in records:
            print(rec)
    except pymysql.Error as e:
        print(e)

    db.close()
