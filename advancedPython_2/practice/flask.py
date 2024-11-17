import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def printHello():
    return "<h1>hello world </h1>"

app.run()