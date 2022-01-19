from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    mylist = [1, 2, 3, 4, 5, 6]
    cats = ["Ginger", "Tom", "Leo"]
    return render_template("index.html", mylist=mylist, cats=cats)


@app.route("/secret")
def secret():
    user_logged_in = False
    return render_template("secret.html", user_logged_in=user_logged_in)


if __name__ == "__main__":
    app.run(debug=True)
