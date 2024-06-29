from flask import (
    Flask,
    redirect,
    render_template,
    request
)
from support_model import Support
from pymongo import MongoClient


# import mariadb
from dotenv import dotenv_values
config = dotenv_values(".env")

client = MongoClient(config["HOST"])
db = client["hackers_poulette"]
support_collection = db["support"]
#
# # connection parameters
# conn_params= {
#     "user" : config["USER"],
#     "password" : config["PASSWORD"],
#     "host" : config["HOST"],
#     "database" : config["DATABASE"]
# }


app = Flask(__name__)

@app.template_filter("bitwise_and")
def bitwise_and(x, y):
    return x & y

@app.route("/")
def index():
    return render_template("index.html")

@app.get("/support")
def support_get():
    return render_template("support.html", support=Support())

@app.post("/support")
def support_post():

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    country = request.form.get("country")
    gender = request.form.get("gender")
    subjects = 0
    if request.form.get("repair"):
        subjects += 4
    if request.form.get("order"):
        subjects += 2
    if request.form.get("others") or subjects == 0:
        subjects += 1
    message = request.form.get("message")
    support = Support(first_name, last_name, email, country, gender, subjects, message)
    if support.validate():
        post = support.to_json()
        support_collection.insert_one(post)
        return render_template("form_confirmation.html", support=support)
    else:
        return render_template("support.html", support=support)

if __name__ == "__main__":
    app.run()

