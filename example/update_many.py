import os
import pymysql

connection = pymysql.connect(host='localhost',
                             user=os.getenv('C9_USER'),
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        rows = [(29, 'bob'),
                (63, 'jim'),
                (107, 'fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                           rows)
        connection.commit()
finally:
    connection.close()