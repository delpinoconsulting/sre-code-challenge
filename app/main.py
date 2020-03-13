from flask import Flask
from flaskext.mysql import MySQL 
from mysql import connector
import config

mysql = MySQL()
app = Flask(__name__)   

mysql.init_app(app)

@app.route("/message")
def message():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute("SELECT message from mytable where 1")
    cursor.close()
    connection.close()
    return cursor.fetchone()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
