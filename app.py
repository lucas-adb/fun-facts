from flask import Flask


app = Flask(__name__)


@app.route("/", methods=["GET"])
def check_app():
    return "<p>flask is working!</p>"


if __name__ == "main":
    app.run(debug=True)
