from flask import Flask, render_template, request
import random

app = Flask(__name__, static_folder="static", static_url_path="/asset")

@app.route("/",methods=["GET", "POST"])
def index():
    email = ""
    password = ""
    numbers = []
    x = None
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        print(f"email is {email} and password is {password}")
    numbers = [ random.randint(1,10) for _ in range(10)]
    x = '<p>welcome</p>'
    return render_template("index.html", email = email, password= password, num = numbers, x=x)





app.run(debug=True)