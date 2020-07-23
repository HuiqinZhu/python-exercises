from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/")
def index():
    number = random.randint(1, 100)
    return render_template("index.html", name="Emma", number=number)


@app.route("/age")
def age():
    age1 = request.args.get("age")
    if not age1:
        return render_template("failure.html")
    return render_template("age.html", day=int(age1)*365)


@app.route("/goodbye")
def bye():
    return "Goodbye!"
