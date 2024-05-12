from flask import Flask
from flask import render_template , request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ship")
def ship():
    return render_template("ship.html", system="太陽系", planet="地球")


@app.route("/passenger")
def passenger():
    passenger_data = {"超級貓貓男": "1A", "豬大哥": "1B", "勒布朗-詹姆斯": "2A"}
    return render_template("passenger.html", data=passenger_data)

@app.route("/board")
def board():
    age = 0
    try:
        age = int( request.args.get("age"))
    except Exception as e:
        print(e)
    return render_template("board.html" , age = age )

if __name__ == "__main__":
    app.run(debug=True)
