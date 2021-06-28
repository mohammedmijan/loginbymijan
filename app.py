from flask import Flask , render_template , redirect , request
import urllib
from flask_pymongo import PyMongo
import time
import bcrypt
from dotenv import dotenv_values
import jwt
from bson.json_util import dumps
from bson.json_util import loads



config = dotenv_values(".env")
password = urllib.parse.quote_plus(config["password"])



app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/mijandb"
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mydb"
app.config["MONGO_URI"] = f'mongodb+srv://{config["user"]}:{password}@cluster0.1ce4z.mongodb.net/e-mart'

db = PyMongo(app)
@app.route("/" , methods= ["GET" , 'POST'])
def main():
    if request.method == "POST":
        password = request.form.get("password").encode("utf-8")
        hashed = bcrypt.hashpw(password , bcrypt.gensalt(16))
        username = request.form.get("name")
        db.db.mart.insert_one({"username":username , "password" : hashed , "date": time.time()} )
    return render_template("test.html" )

@app.route("/main" , methods=[ "GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password").encode("utf-8")
        username = request.form.get("name")
        cursor = db.db.mart.find({"username":username})
        data = loads(dumps(cursor))
        for da in data:
            if bcrypt.hashpw(password , da['password']) == da["password"]:
                return da["username"]

    return render_template("main.html")



if __name__ == "__main__":
    app.run(port=9000 , debug=True)
    