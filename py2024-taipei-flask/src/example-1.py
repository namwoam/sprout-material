from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_sprout():
    return '<h1 style="color:blue;">Andre</h1><iframe src="https://giphy.com/embed/Ac0fCix8D3oN7DwCEB" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/justin-meme-raccoon-pedro-Ac0fCix8D3oN7DwCEB">via GIPHY</a></p>'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
