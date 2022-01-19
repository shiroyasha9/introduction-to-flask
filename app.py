from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    name = "Ginger"
    letters = list(name)
    cat_dictionary = {"cat_name": "Ginger"}
    return render_template(
        "index.html", name=name, letters=letters, cat_dictionary=cat_dictionary
    )


if __name__ == "__main__":
    app.run(debug=True)
