from urllib import request
import urllib.request
from flask import Flask, render_template, request

import functools

from flask import Flask, g, current_app, redirect, render_template, request, url_for, flash
import sqlite3
import click
from werkzeug.security import generate_password_hash




# import statements omitted

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['ClubHub.db'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        # your config here
    )

    # Database initialization
    @app.teardown_appcontext
    def close_db(e=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()

    def init_db():
        with app.app_context():
            db = get_db()
            with current_app.open_resource('schema.sql') as f:
                db.executescript(f.read().decode('utf8'))

    # Register init_db_command with the CLI
    @app.cli.command('init-db')
    def init_db_command():
        """Clear the existing data and create new tables."""
        init_db()
        click.echo('Initialized the database.')

    # Authentication routes
    @app.route('/auth/register', methods=('GET', 'POST'))
    def register():
        if request.method == 'POST':
            user_id = request.form['user_id']
            username = request.form['username']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            user_type = request.form['user_type']


            db = get_db()
            error = None

            if not username:
                error = 'Username is required.'
            elif not password:
                error = 'Password is required.'

            if error is None:
                try:
                    db.execute(
                        "INSERT INTO users (user_id, username, first_name, last_name, email, password, user_type ) VALUES (?, ?, ?, ? ,?, ?, ?)",
                        (user_id,username,first_name,last_name,email, generate_password_hash(password), user_type),
                    )
                    db.commit()
                except db.IntegrityError:
                    error = f"User {username} is already registered."
                else:
                    return redirect(url_for("login"))

            flash(error)

        return render_template('auth/register.html')

    # Add other authentication routes (login, logout, etc.) here

    # Return the Flask application instance
    return app





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

