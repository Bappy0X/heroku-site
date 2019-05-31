#from os import environ
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sql/db.sqlite3" #environ["DATABASE_URI"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.errorhandler(403)
    def invalid(error):
        return render_template("pages/error.html", parallax=False, code=403, flask_error=error), 403

    @app.errorhandler(404)
    def not_found(error):
        return render_template("pages/error.html", parallax=False, code=404, flask_error=error), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("pages/error.html", parallax=False, code=500, flask_error=error), 500

    from views import main
    app.register_blueprint(main)

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=3000, debug=True)