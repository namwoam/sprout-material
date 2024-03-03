from flask import Flask
from flask import redirect, request

app = Flask(__name__)
password = "CHIPI-CHIPI-CHAPA-CHAPA"


@app.route("/")
def hello_maowman():
    return "<h1>Hello, Maowman!</h1>"


@app.route("/dancing")
def dancing():
    return '<div class="tenor-gif-embed" data-postid="8301814479124957525" data-share-method="host" data-aspect-ratio="0.618834" data-width="100%"><a href="https://tenor.com/view/catdancing-cat-dance-cat-busting-it-down-cat-dance-girlfriend-tiktokcatdance-gif-8301814479124957525">Catdancing Cat Dance GIF</a>from <a href="https://tenor.com/search/catdancing-gifs">Catdancing GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>'


@app.route("/who")
def price():
    return "<p>我是超級貓貓男<\p>"


@app.route("/student/<studentName>")
def hello_student(studentName):
    return f"<h1>Hello, {studentName}!</h1>"


@app.route("/secret")
def getSecret():
    try:
        inputPassword = request.args.get("password")
        if password != inputPassword:
            raise Exception("Password incorrect")
        return "<h1>超級貓貓男高中的時候體育跟美術都被當:P</h1>"
    except Exception as e:
        return f"403 Forbidden : {e}", 403


@app.route("/chipi")
def rickroll():
    return redirect("https://www.youtube.com/watch?v=wh9QLjk3M2k")


if __name__ == "__main__":
    app.run(debug=True)
