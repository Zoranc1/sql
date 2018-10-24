from flask import Flask, render_template, request
import pymysql
import os

app = Flask(__name__)

@app.route("/")
def show_hi():
    return render_template("index.html")
    
@app.route('/search') 
def search():
    connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password='',
                             db='Chinook')

    try:
        query='%' + request.args['q'] +'%'
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM Artist WHERE Name like %s"
            cursor.execute(sql,query)
            rows = cursor.fetchall()
        return render_template("artist_list.html", artists=rows,)
    
    finally:
        connection.close()
@app.route('/artist/<int:id>')
def artist_detail(id):
    connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password='',
                             db='Chinook')

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM Artist WHERE ArtistId = %s"
            cursor.execute(sql,id)
            artist = cursor.fetchone()
        
            sql = "SELECT * FROM Album WHERE ArtistId = %s"
            cursor.execute(sql,id)
            rows = cursor.fetchall()
        return render_template("artist_detail.html", albums=rows, artist=artist)
    
    finally:
        connection.close()
        
@app.route('/album/<int:id>')
def album_detail(id):
    connection = pymysql.connect(host='localhost',
                             user=os.environ.get("C9_USER"),
                             password='',
                             db='Chinook')

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM Album WHERE AlbumId = %s"
            cursor.execute(sql,id)
            album = cursor.fetchone()
        
            sql = "SELECT * FROM Track WHERE AlbumId = %s"
            cursor.execute(sql,id)
            rows = cursor.fetchall()
        return render_template("songs.html", albums=rows,album=album)
    
    finally:
        connection.close()
       
    

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)