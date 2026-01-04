from flask import Flask, render_template

from words import Words

app = Flask(__name__)

@app.route("/")
def dictionary():
    return render_template("index.html")


@app.route("/lookup_word", methods=["POST"])
def lookup_word():
    ## lookup_word = request.form["word"]
    ## words = Words(lookup_word)
    ## word = words.retrieve_word
    ## return render_template("index.html", word=word)
    return "Abracadabra"


@app.route("/add_word", methods=["POST"])
def add_word(word):
    word = Words(word)
    word.create_word


@app.route("/delete_word", methods=["POST"])
def delete_word(word):
    word = Words(word)
    word.delete_word


@app.route("/add_relationship", methods=["POST"])
def add_relationship(word_1, word_2, relationship):
    word = Words(word_1)
    word.add_word_relationship(word_2, relationship)


if __name__ == "__main__":
    app.run(debug=True)
