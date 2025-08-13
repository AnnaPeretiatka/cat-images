import random
from flask import Flask, render_template
import os

app = Flask(__name__)

images = [
    "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg",
    "https://cdn2.thecatapi.com/images/MTg0Njg5OQ.jpg",
    "https://cdn2.thecatapi.com/images/MTY3ODIyMg.jpg",
    "https://cdn2.thecatapi.com/images/2oo.gif",
    "https://cdn2.thecatapi.com/images/4e6.gif"
]

@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))