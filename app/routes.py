from app import app
from flask import render_template


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/route")
def route():
    user = {"username": "Jack"}
    return render_template("route.html", user=user, title="New")

@app.route("/harden")
def harden():
    player = {"name": "James Harden"}
    return render_template("harden.html", user=player)