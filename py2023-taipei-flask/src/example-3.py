from flask import Flask
from flask import render_template, request
import xlrd
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", name="Jay")


@app.route("/jay")
def jaySayHi():
    return render_template("jay.html", longName="阿傑", shortName="傑哥")


@app.route("/adult")
def adult():
    age = 0
    try:
        age = int(request.args.get("age"))
    except Exception as e:
        print(e)
    return render_template("adult.html", age=age)


@app.route("/store")
def store():
    cart = {"酒": 10, "麵包": 20, "南瓜": 887414}
    return render_template("store.html", cart=cart)


if __name__ == "__main__":
    app.run(debug=True)
