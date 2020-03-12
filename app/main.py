from flask import Flask
from flaskext.mysql import MySQL 
from configparser import ConfigParser 

# config = ConfigParser()  
# config.read('database.ini')  

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'MYPASSWORD'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_PORT'] = '3306'
mysql.init_app(app)

@app.route("/message")
def message():
    cursor = mysql.connect.connect().cursor()
    cursor.execute("SELECT message from mytable where 1")
    return cursor.fetchone()


if __name__ == "__main__":
    app.run(debug=True)
