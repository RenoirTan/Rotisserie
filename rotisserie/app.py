import typing as t
import uuid
from flask import Flask, request, render_template
from .info import NAME, PROJECT_ROOT


__all__: t.Iterable[str] = ["app", "SECRET_KEY"]


app = Flask(
    NAME,
    static_url_path="/cdn/static",
    static_folder=PROJECT_ROOT / "static",
    template_folder=PROJECT_ROOT / "templates",
)

SECRET_KEY: str = uuid.uuid4().hex
app.secret_key = SECRET_KEY


@app.route("/", methods=["GET"])
def root():
    return render_template("base.html")


@app.route("/portion/root", methods=["GET"])
def portion_root():
    return render_template("root.html")


@app.route("/portion/rot13/crypt", methods=["GET"])
def portion_rot13_crypt():
    return render_template("portion_rot13_crypt.html")
