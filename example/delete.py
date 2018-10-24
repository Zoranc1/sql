import os
import pymysql

connection = pymysql.connect(host='localhost',
                             user=os.getenv('C9_USER'),
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'bob')
        connection.commit()
finally:
    connection.close()