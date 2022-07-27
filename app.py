from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

posts = [
    {
        "title": "O primeiro Post",
        "body": "Aqui é o texto do post",
        "author": "Marcos Novais",
        "created": datetime(2022,7,25),
    },
    {
        "title": "O segundo Post",
        "body": "Aqui é o texto do post",
        "author": "Jamile",
        "created": datetime(2022,7,26),
    },
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/login")
def login():
    return render_template("index.html", posts=posts)