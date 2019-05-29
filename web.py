from os import environ
from flask import Flask, Blueprint, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3" #environ["DATABASE_URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

# MAIN
main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("pages/index.html")

@main.route("/about")
def about():
    return render_template("pages/about.html")

@main.route("/contact")
def contact():
    return render_template("pages/contact.html", contacts=comment.query.all())

@main.route("/contact", methods=["POST"])
def contact_post():
    firstname = request.form.get("firstname")
    new_comment = comment(name=firstname)
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for("main.index"))

app.register_blueprint(main)

# ERRORS
errors = Blueprint("errors", __name__)

@errors.errorhandler(403)
def not_found(error):
    return render_template("pages/error.html", code=403, error=error), 403

@errors.errorhandler(404)
def forbidden(error):
    return render_template("pages/error.html", code=404, error=error), 404

@errors.errorhandler(500)
def internal_server_error(error):
    return render_template("pages/error.html", code=500, error=error), 500

app.register_blueprint(errors)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)