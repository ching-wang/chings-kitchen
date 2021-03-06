import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/recipe")
def recipe():
    return render_template("recipe.html")


@app.route("/popular")
def popular():
    return render_template("popular.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
