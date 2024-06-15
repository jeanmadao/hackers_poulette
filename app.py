from flask import (
    Flask,
    render_template,
    request
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/support", methods=["GET", "POST"])
def support():
    if request.method == 'POST':
        first_name =  request.form.get("first_name")
        last_name =  request.form.get("last_name")
        gender =  request.form.get("gender")
        subjects = 0
        if request.form.get("repair"):
            subjects += 4
        if request.form.get("order"):
            subjects += 2
        if request.form.get("others") or subjects == 0:
            subjects += 1
        message = request.form.get("gender")
        return render_template("support.html")
    else:
        return render_template("support.html")

if __name__ == "__main__":
    app.run()
