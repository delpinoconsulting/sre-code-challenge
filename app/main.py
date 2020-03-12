from flask import Flask
from flaskext.mysql import MySQL 
from os import environ

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = environ.get('MYSQL_DATABASE_USER') 
app.config['MYSQL_DATABASE_PASSWORD'] = environ.get('MYSQL_DATABASE_PASSWORD') 
app.config['MYSQL_DATABASE_DB'] = environ.get('MYSQL_DATABASE_DB') 
app.config['MYSQL_DATABASE_HOST'] = environ.get('MYSQL_DATABASE_HOST') 
app.config['MYSQL_DATABASE_PORT'] = environ.get('MYSQL_DATABASE_PORT') 
mysql.init_app(app)

@app.route("/message")
def message():
    cursor = mysql.connect.connect().cursor()
    cursor.execute("SELECT message from mytable where 1")
    return cursor.fetchone()


if __name__ == "__main__":
    app.run(debug=True)
