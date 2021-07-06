from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_minify import minify
from flask_bcrypt import Bcrypt
from models import db, User
from datetime import timedelta


login_manager = LoginManager()

app = Flask(__name__)

app.config["SECRET_KEY"] = "-WLXT8jMzB6;d#[nSHQq''vQ`X|^KQ?KtcXR(.wm^(DRAYK~,|p- b`FxzTwYEl+"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuarios.db"

minify(app=app, html=True, js=True, cssless=True)
db.init_app(app)
login_manager.init_app(app)

bcrypt = Bcrypt(app)

@app.teardown_request
def teardown_request(e):
    db.session.close()


def register_user(email, user, password, superuser=False):
    found_email = User.query.filter_by(email=email).first()
    if found_email is None:
        password = bcrypt.generate_password_hash(password)
        newUser = User(email=email, username=user, password=password, is_superuser=superuser)
        db.session.add(newUser)
        db.session.commit()

        return True

    else:
        return False


@login_manager.user_loader
def get_user(user_id: int):
    found_user = User.query.filter_by(uid=user_id).first()
    return found_user


@app.route("/", methods=["GET"])
def home():
    if current_user.is_authenticated:
        return render_template("index.html")

    else:
        return redirect(url_for("login_page"))


@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "GET":
        if "error" in request.args:
            return render_template("login.html", error=request.args["error"])

        else:
            return render_template("login.html")

    else:
        username = request.form["usuario"]
        password = request.form["contraseña"]
        user = User.query.filter_by(username=username).first()

        if user is not None and bcrypt.check_password_hash(user.password, password):
            if user.is_superuser:
                login_user(user, remember=True, duration=timedelta(days=2))

            else:
                login_user(user)

            return redirect(url_for("home"))

        return redirect(url_for("login_page", error="Usuario o contraseña incorrectos."))


@app.get("/registrarse")
def register():
    if "error" in request.args:
        return render_template("registrarse.html", error=request.args["error"])

    else:
        return render_template("registrarse.html")


@app.post("/registrarse")
def register_post():
    if any((value == "") for value in request.form.values()):
        return redirect(url_for("register", error="Complete los campos requeridos."))

    email = request.form["email"]

    # Oh dios sagrado del utf-8, que la ñ funcione. funcionó. Gracias.
    password = request.form["contraseña"]
    username = request.form["usuario"]

    pudo_registrarse = register_user(email, username, password)
    if pudo_registrarse:
       return redirect(url_for("login_page"))

    else:
        return redirect(url_for("register", error="El nombre de usuario o el email existen."))


@app.get("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login_page"))


if __name__ == "__main__":
    app.run(debug=True)
