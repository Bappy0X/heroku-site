from flask import Flask, render_template, Blueprint

def create_app():
    app = Flask(__name__)

    from views import main
    app.register_blueprint(main)

    return(app)

"""errors = Blueprint("errors", __name__)

@errors.errorhandler(403)
def not_found(error):
    return render_template("pages/error.html", code=403, error=error), 403

@errors.errorhandler(404)
def forbidden(error):
    return render_template("pages/error.html", code=404, error=error), 404

@errors.errorhandler(500)
def internal_server_error(error):
    return render_template("pages/error.html", code=500, error=error), 500

app.register_blueprint(errors)"""

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=3000, debug=True)