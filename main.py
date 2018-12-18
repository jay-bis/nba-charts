# beginner/mess around stuff with flask - may update to actual
# main code file at some point

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/route")
def route():
    return render_template("route.html")

if __name__ == "__main__":
    app.run(debug=True)