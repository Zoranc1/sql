import pymysql
import os



connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password='',
                             db='Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Album"
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
finally:
    connection.close()