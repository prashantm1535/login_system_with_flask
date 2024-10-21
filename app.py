from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Wel-Come to Flask Project.</h1>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5656, debug=True)