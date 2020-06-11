import pymysql

def db_connect():
    db = pymysql.connect("localhost","root","admin@123","xplore")
    return db

def db_insert():
    pass

def db_get():
    pass
