
cursor = db.cursor()
try:
    cursor = cursor.execute("")
    records = cursor.fetchall()
    for rec in records:
        print(rec)
except pymysql.Error as e:
    print(e)

db.close()
