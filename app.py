from urllib import request
import urllib.request
from flask import Flask, render_template, request

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash



bp = Blueprint('auth', __name__, url_prefix='/auth')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
        if request.method == 'POST':
                print(request.form)

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

