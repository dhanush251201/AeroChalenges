from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def html1():
    return render_template("html1.html")

@app.route("/html2")
def html2():
    return render_template("html2.html")

@app.route("/html3")
def html3():
    return render_template("html3.html")

@app.route("/html4")
def html4():
    return render_template("html4.html")

if __name__ == "__main__":
    app.run()
