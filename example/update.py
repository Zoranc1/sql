import os
import pymysql

connection = pymysql.connect(host='localhost',
                             user=os.getenv('C9_USER'),
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = 28 WHERE name = 'bob';")
        connection.commit()
finally:
    connection.close()