from flask import Flask, flash, redirect, render_template, request
from sqlite3 import connect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'aerovision'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

conn = connect('data.db', check_same_thread=False)
cur = conn.cursor()

@app.route("/", methods=["POST", "GET"])
def login():
    """Log user in"""

    if request.method == "POST":

        # Ensure username was submitted.
        if not request.form.get("username"):
            flash("Enter username!")
            return render_template("login.html")

        # Ensure password was submitted.
        elif not request.form.get("password"):
            flash("Enter password!")
            return render_template("login.html")

        # Query database for username
        cur.execute("SELECT * FROM Register WHERE Password LIKE ?", [request.form.get("password")])
        rows = cur.fetchall()
        print(rows)
        flash(rows,"is incorrect")
        return render_template("login.html")

    # User reached route via GET.
    else:
        return render_template("login.html")