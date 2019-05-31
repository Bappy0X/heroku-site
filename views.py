from flask import Blueprint, render_template, request, redirect, url_for
from sql.models import *

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("pages/index.html", parallax=True)

@main.route("/about")
def about():
    return render_template("pages/about.html", parallax=True)

@main.route("/contact")
def contact():
    return render_template("pages/contact.html", parallax=True, contacts=comment.query.all())

@main.route("/contact", methods=["POST"])
def contact_post():
    name = request.form["name"]
    text = request.form["text"]
    if not name or not text:
        return("Please fill in the form correctly!")
    new_comment = comment(name, text)
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for("main.index"))