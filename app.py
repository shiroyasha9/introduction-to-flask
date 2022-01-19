from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello Cat!</h1>"


@app.route("/information")
def information():
    return "<h1>Cats are awesome!</h1>"


@app.route("/cat/<name>")
def greet(name):
    return f"<h1>This is a page for {name} with all caps is {name.upper()}!</h1>"


if __name__ == "__main__":
    app.run()

