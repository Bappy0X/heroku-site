from os import environ
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<user>")
def index(user):
    return render_template("index.html", name=user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)