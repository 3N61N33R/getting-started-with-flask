# your views go here

from app import app


@app.route("/")
def hello_world():
    return "Hello, World"
