from flask import Flask
from flask import redirect, request

app = Flask(__name__)
password = "bingchilling"


@app.route("/")
def hello_sprout():
    return "<h1>Hello, Sprout!</h1>"


@app.route("/location")
def location():
    return '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.4313908491335!2d121.53896767367566!3d25.01943013888124!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aa2669686ea5%3A0x23428906fb6d9683!2z5Y-w5aSn6LOH6KiK5bel56iL6aSo77yI5b6355Sw6aSo77yJ!5e0!3m2!1sen!2stw!4v1684048829466!5m2!1sen!2stw" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'


@app.route("/price")
def price():
    return "<p>兩個階段都1700</p>"


@app.route("/student/<studentName>")
def hello_student(studentName):
    return f"<h1>Hello, {studentName}!</h1>"


@app.route("/secret")
def getSecret():
    try:
        inputPassword = request.args.get("password")
        if password != inputPassword:
            raise Exception("Password incorrect")
        return "<h1>我的房子還蠻大的</h1>"
    except Exception as e:
        return f"403 Forbidden : {e}", 403


@app.route("/rick")
def rickroll():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


if __name__ == "__main__":
    app.run(debug=True)
