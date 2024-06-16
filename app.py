from flask import (
    Flask,
    redirect,
    render_template,
    request
)

from support_model import Support

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.get("/support")
def support_get():
    return render_template("support.html", support=Support())

@app.post("/support")
def support_post():
    first_name =  request.form.get("first_name")
    last_name =  request.form.get("last_name")
    country =  request.form.get("country")
    gender =  request.form.get("gender")
    subjects = 0
    if request.form.get("repair"):
        subjects += 4
    if request.form.get("order"):
        subjects += 2
    if request.form.get("others") or subjects == 0:
        subjects += 1
    message = request.form.get("message")
    support = Support(first_name, last_name, country, gender, subjects, message)
    if support.validate():
        return redirect("/")
    else:
        return render_template("support.html", support=support)



if __name__ == "__main__":
    app.run()
