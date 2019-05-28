from os import environ
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return("Hello, World!")

if __name__ == "__main__":
    print("test")
    app.run(host="0.0.0.0", port=environ.get("PORT", 3000))