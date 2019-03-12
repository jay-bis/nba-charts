# beginner/mess around stuff with flask - may update to actual
# main code file at some point

from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)