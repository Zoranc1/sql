import os
import pymysql

connection = pymysql.connect(host='localhost',
                             user=os.getenv('C9_USER'),
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                       (63, 'jim'))
        connection.commit()
finally:
    connection.close()