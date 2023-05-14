from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_sprout():
    return "Hello, Sprout!"


if __name__ == "__main__":
    app.run()
