from flask import Flask

from words import Words

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/dictionary")
def dictionary():
    pass


@app.route("/add_word")
def add_word(word):
    word = Words(word)
    word.create_word


@app.route("/delete_word")
def delete_word(word):
    pass