from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder="templates", )

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

# NOTE: to run this, all you have to do is write
# python app.py into command line. Was having too
# much trouble setting flask environment variables
# just to test, so doing this for now.
if __name__ == '__main__':
    app.run(debug=True)