"""Sample Hello World application."""

import datetime
import importlib
import sys

from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static",
)


@app.route("/", defaults={"path": "home"})
@app.route("/<path:path>")
def root(path: str) -> str:
    context = {
        "path": path,
        "python_version": sys.version,
        "flask_version": importlib.metadata.version("flask"),
        "datetime": datetime.datetime.now(),
    }
    return render_template("index.html", **context)


def create_app() -> Flask:
    return app
