from flask import Flask
from flaskext.mysql import MySQL 
import config

mysql = MySQL()
app = Flask(__name__)   

mysql.init_app(app)

@app.route("/message")
def message():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT message from mytable where 1")
    return cursor.fetchone()


if __name__ == "__main__":
    app.run(host="app", debug=True)
