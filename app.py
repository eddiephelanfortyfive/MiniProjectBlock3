from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
        return render_template("home.html")

@app.route("/home")
def home():
        return render_template("home.html")
@app.route("/login")
def login():
        return render_template("login.html")

@app.route("/clubs")
def clubs():
        return render_template("clubs.html")